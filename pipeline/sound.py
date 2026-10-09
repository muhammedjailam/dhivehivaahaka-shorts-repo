"""Procedural sound design + mix. No music: ambience beds, non-melodic drones, SFX only.
Usage: python sound.py <episode_dir> <episode_number>
Writes audio/narration_48k.wav, audio/ambience.wav, audio/sfx.wav, audio/drone.wav, audio/final_mix.wav
"""
import json, os, subprocess, sys
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
ep_dir, n = sys.argv[1], sys.argv[2]
A = os.path.join(ep_dir, "audio"); os.makedirs(A, exist_ok=True)
rng = np.random.default_rng(int(n))
doc = json.load(open(os.path.join(ep_dir, "scenes.json"), encoding="utf-8"))
# flatten beats -> shots (ambience is per beat, SFX and hums per shot)
scenes = [dict(sh, ambience=b["ambience"]) for b in doc["beats"] for sh in b["shots"]] if isinstance(doc, dict) else doc

# ---------------------------------------------------------------- narration
narr_path = os.path.join(A, "narration_48k.wav")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(ep_dir, "work", f"episode-{n}.wav"),
                "-af", "aresample=48000:resampler=soxr", "-ac", "2", "-c:a", "pcm_s16le", narr_path], check=True)
_, nar = wavfile.read(narr_path)
nar = nar[:, 0].astype(np.float32) / 32768
N = len(nar)
# speech RMS over active 50 ms frames
fr = nar[: N // 2400 * 2400].reshape(-1, 2400)
frms = np.sqrt((fr ** 2).mean(1) + 1e-12)
speech_rms = float(np.sqrt(np.mean(frms[frms > np.percentile(frms, 60) * 0.5] ** 2)))
print(f"narration {N / SR:.2f}s, speech RMS {20 * np.log10(speech_rms):.1f} dBFS")


def db(x): return 10 ** (x / 20)
def t_(sec): return np.arange(int(round(sec * SR))) / SR


def bp(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, hi], "bandpass", fs=SR, output="sos"); return signal.sosfilt(sos, x)
def lp(x, f, order=2):
    sos = signal.butter(order, f, "lowpass", fs=SR, output="sos"); return signal.sosfilt(sos, x)
def hp(x, f, order=2):
    sos = signal.butter(order, f, "highpass", fs=SR, output="sos"); return signal.sosfilt(sos, x)


def noise(sec): return rng.standard_normal(int(round(sec * SR))).astype(np.float64)
def brown(sec):
    b = np.cumsum(noise(sec)); b = hp(b, 20); return b / (np.abs(b).max() + 1e-9)
def smooth_rand(sec, rate, lo=0.0, hi=1.0):
    """Slowly varying random envelope (rate = changes per second)."""
    k = max(2, int(sec * rate) + 2)
    pts = rng.uniform(lo, hi, k)
    return np.interp(np.linspace(0, k - 1, int(round(sec * SR))), np.arange(k), pts)
def rmsnorm(x):
    a = np.abs(x); m = a > a.max() * 0.05
    r = np.sqrt(np.mean(x[m] ** 2)) if m.any() else 1
    return x / (r + 1e-9)
def fade(x, fi=0.01, fo=0.02):
    x = x.copy(); a = int(fi * SR); b = int(fo * SR)
    if a: x[:a] *= np.linspace(0, 1, a)
    if b: x[-b:] *= np.linspace(1, 0, b)
    return x
def stereo(x, pan=0.0):
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    return np.stack([x * l, x * r], 1) * 1.4142


# ---------------------------------------------------------------- ambience generators (stereo)
def crickets(sec, density=1.0):
    out = np.zeros((int(round(sec * SR)), 2))
    for _ in range(3):
        f = rng.uniform(4200, 5600); rate = rng.uniform(14, 22); pan = rng.uniform(-0.8, 0.8)
        t = t_(sec)
        carrier = np.sin(2 * np.pi * f * t)
        pulse = (np.sin(2 * np.pi * rate * t) > 0.3).astype(float)
        chirp_gate = (smooth_rand(sec, 0.6) > 0.45).astype(float)
        chirp_gate = lp(chirp_gate, 8)
        x = carrier * lp(pulse, 120) * chirp_gate * rng.uniform(0.4, 1.0) * density
        out += stereo(x, pan)
    return out * 0.25
def wind(sec, strength=1.0):
    x = brown(sec); y = bp(noise(sec), 300, 1200) * 0.15
    env = smooth_rand(sec, 0.15, 0.3, 1.0)
    l = (x * 0.8 + y) * env; r = (np.roll(x, 2400) * 0.8 + np.roll(y, 1800)) * env
    return np.stack([l, r], 1) * 0.5 * strength
def waves(sec):
    out = np.zeros((int(round(sec * SR)), 2)); pos = 0
    base = lp(noise(sec), 600) * 0.6 + bp(noise(sec), 600, 3000) * 0.25
    env = np.zeros(int(round(sec * SR)))
    while pos < len(env):
        period = rng.uniform(6, 10); L = int(period * SR)
        e = np.concatenate([np.linspace(0.15, 1, int(L * 0.35)) ** 2, np.linspace(1, 0.15, L - int(L * 0.35)) ** 1.5])
        env[pos:pos + L] += e[: len(env[pos:pos + L])]; pos += L
    x = base * env
    return np.stack([x, np.roll(x, 3000)], 1) * 0.7
def room_tone(sec):
    x = lp(brown(sec), 300) * 0.8
    fan = 1 + 0.15 * np.sin(2 * np.pi * 3.1 * t_(sec))  # fan blade swoosh
    y = bp(noise(sec), 200, 900) * 0.12 * fan
    m = x + y
    return np.stack([m, np.roll(m, 1200)], 1) * 0.6
def traffic(sec, busy=False):
    out = np.stack([lp(brown(sec), 200)] * 2, 1) * 0.5
    t = 0.5
    while t < sec - 3:
        out_pass = pass_by(rng.uniform(2.5, 4), rng.choice([-1, 1]), engine=rng.random() < 0.6)
        s = int(t * SR); e = min(len(out), s + len(out_pass))
        out[s:e] += out_pass[: e - s] * (1.0 if busy else 0.25)
        t += rng.uniform(2, 5) if busy else rng.uniform(8, 16)
    return out
def rain(sec):
    x = hp(noise(sec), 1500) * 0.3 + bp(noise(sec), 300, 1500) * 0.2
    drops = (rng.random(int(round(sec * SR))) > 0.9993).astype(float)
    d = signal.lfilter([1], [1, -0.995], drops) * bp(noise(sec), 2000, 6000)
    m = x + d * 0.5
    return np.stack([m, np.roll(m, 2000)], 1) * 0.6


def pass_by(sec, direction=1, engine=True):
    t = t_(sec); u = t / sec
    env = np.exp(-((u - 0.5) ** 2) / 0.03)
    whoosh = bp(noise(sec), 200, 3000) * env
    x = whoosh
    if engine:
        f0 = 95 * (1.08 - 0.16 * (u > 0.5) * np.minimum(1, (u - 0.5) * 8))  # doppler drop
        ph = 2 * np.cumsum(np.pi * f0 / SR)
        eng = signal.sawtooth(ph) * 0.4 + signal.sawtooth(ph * 2) * 0.2
        x = x + lp(eng, 1200) * env * 0.8
    pan = np.clip((u - 0.5) * 2.2 * direction, -1, 1)
    l = x * np.cos((pan + 1) * np.pi / 4); r = x * np.sin((pan + 1) * np.pi / 4)
    return np.stack([l, r], 1)


def birds(sec, density=1.0):
    """Sparse dawn bird chirps: short enveloped frequency sweeps at random times and pans."""
    out = np.zeros((int(round(sec * SR)), 2)); t = 0.2
    while t < sec - 1:
        n_ = rng.integers(2, 6); f0 = rng.uniform(2500, 5000); pan = rng.uniform(-0.9, 0.9)
        for k in range(n_):
            L = rng.uniform(0.05, 0.14); tt = t_(L)
            f = f0 * (1 + rng.uniform(-0.25, 0.25) * tt / L) + 300 * np.sin(2 * np.pi * rng.uniform(20, 60) * tt)
            x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * tt / L) ** 2 * rng.uniform(0.3, 1)
            s0 = int((t + k * rng.uniform(0.12, 0.2)) * SR); e0 = min(len(out), s0 + len(x))
            out[s0:e0] += stereo(x[: e0 - s0], pan)
        t += rng.uniform(0.8, 3.5) / density
    return out * 0.3
def ac_hum(sec):
    """Air-conditioner / fluorescent room tone for the hospital (filtered noise + very low steady hum)."""
    x = lp(brown(sec), 400) * 0.6 + bp(noise(sec), 150, 600) * 0.15 + np.sin(2 * np.pi * 100 * t_(sec)) * 0.03
    return np.stack([x, np.roll(x, 900)], 1) * 0.6
def distant_boats(sec):
    out = np.zeros((int(round(sec * SR)), 2)); t = 0.0
    while t < sec - 6:
        L = rng.uniform(8, 14); x = lp(sfx_boat_engine(L), 500)
        e = min(len(out), int(t * SR) + len(x)); out[int(t * SR):e] += stereo(x[: e - int(t * SR)], rng.uniform(-0.8, 0.8))
        t += rng.uniform(6, 12)
    return out * 0.5
def car_cabin(sec):
    """Inside a moving car at night: low engine/tyre rumble with slow variation, muffled passing cars."""
    t = t_(sec)
    eng = lp(brown(sec), 140) * (0.8 + 0.2 * smooth_rand(sec, 0.1)) + np.sin(2 * np.pi * 42 * t) * 0.04
    road = lp(bp(noise(sec), 120, 700), 500) * 0.25 * smooth_rand(sec, 0.3, 0.6, 1.0)
    m = eng + road
    out = np.stack([m, np.roll(m, 600)], 1) * 0.7
    tt = 1.0
    while tt < sec - 4:
        x = pass_by(rng.uniform(2.5, 4), rng.choice([-1, 1]), engine=True)
        x = np.stack([lp(x[:, 0], 600), lp(x[:, 1], 600)], 1) * 0.35
        s0 = int(tt * SR); e0 = min(len(out), s0 + len(x)); out[s0:e0] += x[: e0 - s0]
        tt += rng.uniform(9, 18)
    return out


AMB = {
    "sea_search": lambda s: waves(s) + wind(s, 0.9) * 0.8 + distant_boats(s) * 0.6,
    "hospital_night": lambda s: ac_hum(s) + crickets(s, 0.2) * 0.25,
    "hospital_room": lambda s: ac_hum(s) * 0.9 + crickets(s, 0.2) * 0.2,
    "hospital_day": lambda s: ac_hum(s) + birds(s, 0.3) * 0.3,
    "memory": lambda s: lp(room_tone(s), 500) * 0.8,
    "dawn_exterior": lambda s: birds(s, 1.0) + wind(s, 0.4) + waves(s) * 0.25,
    "room_day": lambda s: room_tone(s) + birds(s, 0.4) * 0.35,
    "fazaal_room": lambda s: room_tone(s) * 0.8 + wind(s, 0.3) + birds(s, 0.3) * 0.3,
    "airport": lambda s: wind(s, 1.0) + waves(s) * 0.3,
    "night_exterior": lambda s: crickets(s) * 1.0 + wind(s, 0.6),
    "room_night": lambda s: room_tone(s) + crickets(s, 0.3) * 0.5,
    "living_night": lambda s: room_tone(s) * 0.9 + crickets(s, 0.3) * 0.4,
    "street_night": lambda s: crickets(s, 0.8) + traffic(s, False) * 0.6 + wind(s, 0.3),
    "road_busy": lambda s: traffic(s, True) * 0.8 + crickets(s, 0.4) * 0.5,
    "memory_rain": lambda s: rain(s),
    "beach_night": lambda s: waves(s) + wind(s, 0.8) * 0.8 + crickets(s, 0.4) * 0.4,
    "beach_dusk": lambda s: waves(s) + wind(s, 0.6) * 0.7 + birds(s, 0.25) * 0.4 + crickets(s, 0.15) * 0.25,
    "car_night": lambda s: car_cabin(s),
}
AMB_LEVEL = -31  # dB relative to narration speech RMS


def murmur(sec, voices=6):
    """Distant unintelligible crowd/office chatter: band-passed noise with syllable-rate amplitude modulation."""
    out = np.zeros((int(round(sec * SR)), 2))
    for _ in range(voices):
        x = bp(noise(sec), rng.uniform(250, 400), rng.uniform(1800, 2800))
        syl = lp(np.abs(noise(sec)), rng.uniform(3, 6)); syl /= syl.max() + 1e-9
        x = x * syl * (smooth_rand(sec, 0.3) > 0.4) * rng.uniform(0.4, 1)
        out += stereo(x, rng.uniform(-0.8, 0.8))
    return lp(out.T, 3000).T * 0.4
def keyboard_bed(sec, density=0.5):
    out = np.zeros(int(round(sec * SR))); t = 0.3
    while t < sec - 1:
        if rng.random() < density:
            for k in range(rng.integers(4, 14)):
                s0 = int((t + k * rng.uniform(0.08, 0.16)) * SR); L = int(0.015 * SR)
                if s0 + L < len(out): out[s0:s0 + L] += hp(noise(0.015), 1500) * np.exp(-np.arange(L) / 90) * rng.uniform(0.3, 1)
        t += rng.uniform(1.5, 4)
    return stereo(out, rng.uniform(-0.5, 0.5)) * 0.5


AMB.update({
    "office_day": lambda s: ac_hum(s) * 0.9 + murmur(s, 5) * 0.35 + keyboard_bed(s, 0.5) * 0.25,
    "office_quiet": lambda s: ac_hum(s) + keyboard_bed(s, 0.2) * 0.15,
    "office_night": lambda s: ac_hum(s) * 0.9 + traffic(s, False) * 0.15,
    "cafe": lambda s: murmur(s, 8) * 0.6 + room_tone(s) * 0.5,
    "car_interior": lambda s: np.stack([lp(brown(s), 160)] * 2, 1) * 0.8 + traffic(s, False) * 0.2,
    "city_day": lambda s: traffic(s, True) * 0.7 + murmur(s, 4) * 0.25 + birds(s, 0.2) * 0.2,
    "home_day": lambda s: room_tone(s) + birds(s, 0.4) * 0.3 + traffic(s, False) * 0.15,
    "home_night": lambda s: room_tone(s) + crickets(s, 0.3) * 0.4 + traffic(s, False) * 0.1,
    "mansion_day": lambda s: ac_hum(s) * 0.7 + birds(s, 0.3) * 0.25,
    "mansion_night": lambda s: ac_hum(s) * 0.7 + crickets(s, 0.3) * 0.3,
    "balcony_night": lambda s: wind(s, 0.5) + traffic(s, False) * 0.4 + crickets(s, 0.3) * 0.3,
    "hospital_corridor": lambda s: ac_hum(s) + murmur(s, 3) * 0.2,
    "hall_crowd": lambda s: murmur(s, 12) * 0.8 + room_tone(s) * 0.3,
    "resort_evening": lambda s: waves(s) * 0.8 + wind(s, 0.5) * 0.6 + murmur(s, 4) * 0.1,
    "beach_evening": lambda s: waves(s) + wind(s, 0.6) * 0.6 + birds(s, 0.2) * 0.2,
    "garden_day": lambda s: birds(s, 0.8) + wind(s, 0.3) + traffic(s, False) * 0.1,
    "bank_night": lambda s: ac_hum(s) * 0.8,
    "prison_exterior": lambda s: wind(s, 0.8) + waves(s) * 0.4 + birds(s, 0.2) * 0.2,
    # Taubaa (stories set in Saudi Arabia / abroad)
    "mosque_interior": lambda s: lp(room_tone(s), 900) * 0.8 + ac_hum(s) * 0.4,
    "plane_cabin": lambda s: np.stack([lp(brown(s), 300)] * 2, 1) * 0.9 + ac_hum(s) * 0.3,
    "desert_night": lambda s: wind(s, 0.9) + crickets(s, 0.3) * 0.3,
    "city_night_far": lambda s: traffic(s, False) * 0.5 + wind(s, 0.4) + murmur(s, 3) * 0.15,
    "makkah_crowd": lambda s: murmur(s, 16) * 0.7 + wind(s, 0.3) * 0.4,
    "clinic_room": lambda s: ac_hum(s) * 0.9 + room_tone(s) * 0.3,
})


# ---------------------------------------------------------------- SFX generators (mono unless stated)
def sfx_door_open():
    sec = 0.9; t = t_(sec)
    f = 520 + 140 * np.sin(2 * np.pi * 1.3 * t) + 40 * smooth_rand(sec, 20, -1, 1)
    creak = np.sin(2 * np.pi * np.cumsum(f) / SR) * (np.abs(signal.sawtooth(2 * np.pi * 38 * t)) ** 4)
    creak = bp(creak, 300, 3000) * np.linspace(1, 0.3, len(t))
    click = np.zeros_like(t); click[:300] = noise(300 / SR) * np.exp(-np.arange(300) / 40)
    return fade(creak * 0.6 + click * 1.5, 0.005, 0.1)
def sfx_door_close():
    sec = 0.6; t = t_(sec)
    thud = np.sin(2 * np.pi * 75 * t) * np.exp(-t * 18) + lp(noise(sec), 400) * np.exp(-t * 25) * 0.6
    click = np.zeros_like(t); s = int(0.04 * SR); click[s:s + 400] = hp(noise(400 / SR), 2000) * np.exp(-np.arange(400) / 60)
    return fade(thud + click * 0.5, 0.002, 0.1)
def sfx_wheelchair_roll():
    sec = 2.2; t = t_(sec)
    rumble = lp(noise(sec), 250) * (1 + 0.3 * np.sin(2 * np.pi * 2.5 * t))
    ticks = (rng.random(len(t)) > 0.9996).astype(float); ticks = signal.lfilter([1], [1, -0.97], ticks) * bp(noise(sec), 1500, 5000)
    env = np.minimum(1, t / 0.3) * np.minimum(1, (sec - t) / 0.6)
    return (rumble + ticks * 0.4) * env
def sfx_breath(sec=0.9, lo=400, hi=2500, inhale=False):
    t = t_(sec)
    env = np.sin(np.pi * np.minimum(1, t / sec)) ** (0.6 if inhale else 1.5)
    return bp(noise(sec), lo, hi) * env
def sfx_sob_breath():
    parts = []
    for k in range(3):
        parts.append(sfx_breath(rng.uniform(0.25, 0.4), 500, 2200, True) * rng.uniform(0.6, 1))
        parts.append(np.zeros(int(rng.uniform(0.08, 0.2) * SR)))
    parts.append(sfx_breath(1.0, 300, 1600) * 0.8)
    return fade(np.concatenate(parts), 0.01, 0.1)
def sfx_cloth_rustle():
    sec = 0.7; x = bp(noise(sec), 1500, 7000) * smooth_rand(sec, 25, 0, 1) ** 2
    return fade(x, 0.02, 0.15)
def sfx_phone_game_taps():
    out = np.zeros(int(1.6 * SR))
    for k in range(5):
        s = int((0.1 + k * 0.28 + rng.uniform(-0.05, 0.05)) * SR)
        c = hp(noise(0.012), 2500) * np.exp(-np.arange(int(0.012 * SR)) / 80)
        out[s:s + len(c)] += c
    return out
def steps(n_steps, interval, soft=False):
    out = np.zeros(int((n_steps * interval + 0.5) * SR))
    for k in range(n_steps):
        s = max(0, int((k * interval + rng.uniform(-0.03, 0.03)) * SR)); L = int(0.18 * SR); tt = np.arange(L) / SR
        if soft:
            st = lp(noise(0.18), 1800) * np.exp(-tt * 18) + bp(noise(0.18), 2000, 6000) * np.exp(-tt * 30) * 0.4
        else:
            st = np.sin(2 * np.pi * 90 * tt) * np.exp(-tt * 40) * 0.8 + bp(noise(0.18), 800, 5000) * np.exp(-tt * 35) * 0.6
        out[s:s + L] += st * rng.uniform(0.7, 1)
    return out
def sfx_footsteps_pavement(): return steps(5, 0.55)
def sfx_footsteps_sand(): return steps(5, 0.6, soft=True)
def sfx_motorbike_pass(): return pass_by(3.0, 1, True)
def sfx_car_pass(): return pass_by(3.5, -1, True)
def sfx_car_approach():
    sec = 2.0; t = t_(sec); u = t / sec
    f0 = 80 + 30 * u; ph = 2 * np.pi * np.cumsum(f0) / SR
    eng = lp(signal.sawtooth(ph) * 0.5 + signal.sawtooth(ph * 2) * 0.25, 1500)
    x = (eng + bp(noise(sec), 200, 2500) * 0.5) * u ** 2
    return stereo(fade(x, 0.05, 0.05), 0.2)
def sfx_brake_screech():
    sec = 1.5; t = t_(sec)
    f = 2400 + 300 * np.sin(2 * np.pi * 7 * t) + 200 * smooth_rand(sec, 30, -1, 1) - 500 * t / sec
    squeal = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.5 + bp(noise(sec), 1800, 3500) * 0.6
    env = np.minimum(1, t / 0.05) * np.exp(-np.maximum(0, t - 0.9) * 6)
    rumble = lp(noise(sec), 300) * env * 0.8
    return fade((squeal * env + rumble), 0.005, 0.1)
def sfx_gasp(): return fade(sfx_breath(0.45, 700, 3500, True), 0.005, 0.05)
def sfx_heartbeat():
    bpm = 88; beat = 60 / bpm; n_ = 6; out = np.zeros(int((n_ * beat + 0.4) * SR))
    for k in range(n_):
        for off, a in ((0, 1.0), (0.22, 0.7)):
            s = int((k * beat + off) * SR); L = int(0.16 * SR); tt = np.arange(L) / SR
            out[s:s + L] += np.sin(2 * np.pi * 52 * tt) * np.exp(-tt * 28) * a * (0.6 + 0.4 * k / n_)
    return lp(out, 160)
def sfx_breath_heavy():
    return np.concatenate([sfx_breath(0.35, 500, 2500, True), sfx_breath(0.5, 300, 1500)] * 3)
def sfx_car_door():
    sec = 1.2; t = t_(sec)
    latch = np.zeros_like(t); latch[:500] = hp(noise(500 / SR), 1500) * np.exp(-np.arange(500) / 70)
    s = int(0.65 * SR); L = int(0.4 * SR); tt = np.arange(L) / SR
    slam = np.zeros_like(t); slam[s:s + L] = np.sin(2 * np.pi * 65 * tt) * np.exp(-tt * 14) + lp(noise(0.4), 700) * np.exp(-tt * 20) * 0.7
    return latch * 0.4 + slam
def sfx_car_drive_off():
    sec = 4.0; t = t_(sec); u = t / sec
    f0 = 70 + 70 * u; ph = 2 * np.pi * np.cumsum(f0) / SR
    eng = lp(signal.sawtooth(ph) * 0.5 + signal.sawtooth(ph * 2) * 0.2, 1400)
    env = np.minimum(1, t / 0.4) * (1 - u) ** 1.5
    x = (eng + bp(noise(sec), 150, 2000) * 0.4) * env
    return fade(x, 0.05, 0.3)
def sfx_phone_buzz():
    out = []
    for k in range(2):
        tt = t_(0.35); b = signal.square(2 * np.pi * 170 * tt) * 0.5 + bp(noise(0.35), 150, 600) * 0.3
        out += [lp(b, 900) * np.minimum(1, tt / 0.01), np.zeros(int(0.18 * SR))]
    return fade(np.concatenate(out), 0.005, 0.02)
def sfx_wind_gust():
    sec = 3.0; t = t_(sec)
    x = bp(noise(sec), 250, 1400) * np.sin(np.pi * t / sec) ** 2 + lp(brown(sec), 300) * np.sin(np.pi * t / sec) * 0.6
    return np.stack([x, np.roll(x, 2400)], 1)
def sfx_page_turn():
    sec = 0.5; t = t_(sec)
    return fade(bp(noise(sec), 1200, 8000) * np.sin(np.pi * t / sec) ** 3 * smooth_rand(sec, 40, 0.3, 1), 0.01, 0.05)
def sfx_cup_clatter():
    sec = 1.0; t = t_(sec); out = np.zeros_like(t)
    for k, (st, a) in enumerate(((0, 1), (0.09, 0.6), (0.2, 0.4), (0.33, 0.25))):
        s = int(st * SR); L = len(t) - s; tt = np.arange(L) / SR
        ping = sum(np.sin(2 * np.pi * f * tt) * np.exp(-tt * d) for f, d in ((2350, 14), (3980, 22), (5710, 30)))
        out[s:] += ping * a * 0.4 + np.concatenate([hp(noise(0.01), 2000), np.zeros(L - int(0.01 * SR))]) * a
    return fade(out, 0.001, 0.2)
def sfx_sigh(): return fade(sfx_breath(1.4, 250, 1400) * 1.0, 0.05, 0.2)
def sfx_wave_crash():
    sec = 3.5; t = t_(sec)
    env = np.minimum(1, t / 0.4) * np.exp(-np.maximum(0, t - 0.4) * 1.2)
    x = (lp(noise(sec), 900) + bp(noise(sec), 900, 5000) * 0.5) * env
    return np.stack([x, np.roll(x, 3000)], 1)
def sfx_splash():
    sec = 2.5; t = t_(sec)
    body = (lp(noise(sec), 1500) * 0.9 + bp(noise(sec), 1500, 7000) * 0.6) * np.exp(-t * 4) * np.minimum(1, t / 0.008)
    thump = np.sin(2 * np.pi * 60 * t) * np.exp(-t * 12) * 0.8
    drops = np.zeros_like(t)
    for _ in range(25):
        s = int(rng.uniform(0.15, 1.8) * SR); L = int(0.05 * SR); tt = np.arange(L) / SR
        f = rng.uniform(700, 2200)
        drops[s:s + L] += np.sin(2 * np.pi * f * (1 + tt * 8) * tt) * np.exp(-tt * 70) * rng.uniform(0.1, 0.35)
    return fade(body + thump + drops, 0.002, 0.3)


def sfx_boat_engine(sec=6.0):
    t = t_(sec); f0 = 42 + 3 * np.sin(2 * np.pi * 0.3 * t); ph = 2 * np.pi * np.cumsum(f0) / SR
    thump = (np.maximum(0, np.sin(ph)) ** 6) * 0.9 + lp(noise(sec), 300) * 0.3
    env = np.minimum(1, t / 1.5) * np.minimum(1, (sec - t) / 1.5)
    return lp(thump, 600) * env
def sfx_glass_break():
    sec = 1.2; t = t_(sec); out = lp(noise(sec), 400) * np.exp(-t * 30) * 0.6
    for _ in range(40):
        s0 = int(rng.uniform(0, 0.5) ** 2 * SR); L = int(0.08 * SR); tt = np.arange(L) / SR
        f = rng.uniform(3000, 9000)
        out[s0:s0 + L] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * rng.uniform(40, 90)) * rng.uniform(0.2, 0.7)
    out[:600] += hp(noise(600 / SR), 2000) * np.exp(-np.arange(600) / 120) * 1.5
    return fade(out, 0.001, 0.2)
def sfx_knock():
    out = np.zeros(int(1.0 * SR))
    for k in range(3):
        s0 = max(0, int((k * 0.22 + rng.uniform(-0.02, 0.02)) * SR)); L = int(0.12 * SR); tt = np.arange(L) / SR
        hit = np.sin(2 * np.pi * 180 * tt) * np.exp(-tt * 45) + bp(noise(0.12), 300, 2500) * np.exp(-tt * 70) * 0.8
        out[s0:s0 + L] += hit * rng.uniform(0.8, 1)
    return out
def sfx_lock_click():
    sec = 0.4; out = np.zeros(int(sec * SR))
    for st, a in ((0, 0.6), (0.12, 1.0)):
        s0 = int(st * SR); L = int(0.03 * SR)
        out[s0:s0 + L] += hp(noise(0.03), 1500) * np.exp(-np.arange(L) / 120) * a
    return out
def sfx_soft_thud():
    sec = 0.4; t = t_(sec)
    return fade(np.sin(2 * np.pi * 90 * t) * np.exp(-t * 25) + lp(noise(sec), 600) * np.exp(-t * 35) * 0.5, 0.002, 0.05)
def sfx_plane_pass():
    sec = 6.0; t = t_(sec); u = t / sec
    env = np.exp(-((u - 0.45) ** 2) / 0.05)
    x = (lp(brown(sec), 500) + bp(noise(sec), 400, 3000) * 0.4 * env) * env
    pan = np.clip((u - 0.45) * 2, -1, 1)
    return np.stack([x * np.cos((pan + 1) * np.pi / 4), x * np.sin((pan + 1) * np.pi / 4)], 1)


def sfx_keyboard_typing():
    out = np.zeros(int(2.0 * SR))
    for k in range(16):
        s0 = int((k * 0.11 + rng.uniform(-0.02, 0.02) + 0.02) * SR); L = int(0.015 * SR)
        out[s0:s0 + L] += hp(noise(0.015), 1500) * np.exp(-np.arange(L) / 90) * rng.uniform(0.5, 1)
    return out
def sfx_applause():
    sec = 4.0; out = np.zeros(int(sec * SR))
    for _ in range(900):
        s0 = int(rng.uniform(0, sec - 0.05) * SR); L = int(0.012 * SR)
        out[s0:s0 + L] += bp(noise(0.012), 800, 5000) * np.exp(-np.arange(L) / 60) * rng.uniform(0.2, 1)
    env = np.minimum(1, t_(sec) / 0.4) * np.minimum(1, (sec - t_(sec)) / 1.2)
    return stereo(out * env, 0)
def sfx_doorbell_buzz():
    tt = t_(0.6); b = signal.square(2 * np.pi * 120 * tt) * 0.4 + bp(noise(0.6), 200, 900) * 0.2
    return fade(lp(b, 1200), 0.01, 0.05)
def sfx_pen_scribble():
    sec = 1.2; x = bp(noise(sec), 2000, 7000) * smooth_rand(sec, 12, 0, 1) ** 2
    return fade(x, 0.02, 0.1)
def sfx_paper_shuffle():
    return np.concatenate([sfx_page_turn(), sfx_page_turn() * 0.7])
def sfx_crowd_gasp():
    return sum(fade(sfx_breath(rng.uniform(0.4, 0.6), 500, 3000, True), 0.01, 0.05)[:int(0.4 * SR)] * rng.uniform(0.5, 1) for _ in range(6))
def sfx_fire_crackle():
    sec = 3.0; out = lp(noise(sec), 500) * 0.3
    for _ in range(80):
        s0 = int(rng.uniform(0, sec - 0.02) * SR); L = int(0.008 * SR)
        out[s0:s0 + L] += hp(noise(0.008), 1500) * rng.uniform(0.3, 1)
    return fade(out, 0.2, 0.5)


# ---- Milahanduvaru (island village, night/moonlight, supernatural): extra beds and effects
def sfx_thunder():
    sec = 4.0; t = t_(sec)
    crack = hp(noise(sec), 800) * np.exp(-t * 6) * 0.5
    roll = lp(brown(sec), 120) * (np.exp(-((t - 0.6) ** 2) / 0.5) + 0.6 * np.exp(-((t - 1.8) ** 2) / 0.8))
    return fade(crack + roll * 1.6, 0.01, 0.8)
def sfx_rain_start():
    sec = 5.0; x = rain(sec)[:, 0]; t = t_(sec)
    return fade(x * np.minimum(1, t / 2.5), 0.3, 0.6)
def sfx_wind_howl():
    sec = 3.5; t = t_(sec)
    x = bp(noise(sec), 300, 900) * (0.5 + 0.5 * np.sin(np.pi * t / sec)) * smooth_rand(sec, 1.5, 0.5, 1)
    return fade(x, 0.4, 0.8)
def sfx_dhoni_engine(): return sfx_boat_engine(6.0)
def sfx_leaves_rustle():
    sec = 2.0; x = hp(bp(noise(sec), 1500, 7000), 1200) * smooth_rand(sec, 4, 0.2, 1)
    return fade(x, 0.2, 0.5)
def thunder_bed(sec):
    out = np.zeros((int(round(sec * SR)), 2)); t = rng.uniform(4, 12)
    while t < sec - 5:
        x = lp(sfx_thunder(), 900) * rng.uniform(0.4, 0.9)
        s0 = int(t * SR); e0 = min(len(out), s0 + len(x)); out[s0:e0] += stereo(x[: e0 - s0], rng.uniform(-0.6, 0.6))
        t += rng.uniform(15, 35)
    return out


AMB.update({
    "island_day": lambda s: birds(s, 0.7) + wind(s, 0.5) + waves(s) * 0.3,
    "island_night": lambda s: crickets(s) * 1.0 + wind(s, 0.5) + waves(s) * 0.3,
    "island_house_day": lambda s: room_tone(s) + birds(s, 0.4) * 0.35 + waves(s) * 0.12,
    "island_house_night": lambda s: room_tone(s) + crickets(s, 0.4) * 0.45 + waves(s) * 0.12,
    "jungle_night": lambda s: crickets(s, 1.3) * 1.1 + wind(s, 0.7),
    "beach_day": lambda s: waves(s) + wind(s, 0.6) * 0.6 + birds(s, 0.3) * 0.3,
    "jetty_day": lambda s: waves(s) * 0.7 + wind(s, 0.5) * 0.6 + distant_boats(s) * 0.5 + birds(s, 0.2) * 0.2,
    "sea_boat": lambda s: waves(s) * 0.8 + wind(s, 0.8) * 0.6 + np.stack([lp(sfx_boat_engine(s), 500)] * 2, 1) * 0.5,
    "rain_night": lambda s: rain(s) + crickets(s, 0.1) * 0.1 + thunder_bed(s) * 0.5,
    "rain_day": lambda s: rain(s) + birds(s, 0.1) * 0.1,
    "storm_night": lambda s: rain(s) * 1.2 + wind(s, 1.2) + thunder_bed(s),
    "village_day": lambda s: birds(s, 0.5) + wind(s, 0.4) + murmur(s, 3) * 0.2 + waves(s) * 0.15,
    "village_night": lambda s: crickets(s, 0.9) + wind(s, 0.4) + murmur(s, 3) * 0.1 + waves(s) * 0.15,
})


# ---- Sector 7 (underground bunker city, sci-fi dystopia): industrial beds and effects (non-melodic)
def machinery(sec, heavy=1.0):
    """Deep bunker machinery: low rumble with slow swell, periodic hydraulic thumps, faint metal creaks."""
    out = np.zeros(int(round(sec * SR)))
    out += lp(brown(sec), 90) * (0.8 + 0.25 * smooth_rand(sec, 0.08)) * 1.2 * heavy
    out += bp(noise(sec), 60, 220) * 0.25 * heavy
    p = rng.uniform(0.5, 2.0)
    while p < sec - 1:
        L = int(0.5 * SR); tt = np.arange(L) / SR; s0 = int(p * SR)
        out[s0:s0 + L] += (np.sin(2 * np.pi * 48 * tt) * np.exp(-tt * 9) + lp(noise(0.5), 300)[:L] * np.exp(-tt * 12) * 0.5) * 0.5 * heavy
        p += rng.uniform(1.6, 3.2)
    p = rng.uniform(3, 8)
    while p < sec - 2:
        L = int(1.2 * SR); s0 = int(p * SR); f = rng.uniform(500, 900)
        cr = bp(noise(1.2), f, f * 1.6)[:L] * np.sin(np.pi * np.arange(L) / L) ** 2 * smooth_rand(1.2, 18, 0.2, 1)[:L]
        out[s0:s0 + L] += cr * 0.12
        p += rng.uniform(7, 16)
    return np.stack([out, np.roll(out, 1500)], 1) * 0.6
def drips(sec, density=1.0):
    out = np.zeros((int(round(sec * SR)), 2)); p = rng.uniform(0.2, 1.0)
    while p < sec - 0.3:
        L = int(0.12 * SR); tt = np.arange(L) / SR; f = rng.uniform(900, 1800)
        d = np.sin(2 * np.pi * (f + 600 * np.exp(-tt * 60)) * tt) * np.exp(-tt * 45)
        s0 = int(p * SR); out[s0:s0 + L] += stereo(d * rng.uniform(0.2, 0.6), rng.uniform(-0.9, 0.9))
        p += rng.uniform(0.6, 2.8) / density
    return out * 0.5
def steam(sec, level=1.0):
    x = hp(bp(noise(sec), 2500, 9000), 2000) * smooth_rand(sec, 0.12, 0.2, 1.0)
    return np.stack([x, np.roll(x, 900)], 1) * 0.18 * level
def electric_hum(sec):
    t = t_(sec)
    x = (np.sin(2 * np.pi * 50 * t) * 0.5 + np.sin(2 * np.pi * 100 * t) * 0.25 + np.sin(2 * np.pi * 150 * t) * 0.08) * (0.9 + 0.1 * smooth_rand(sec, 2))
    x += bp(noise(sec), 3000, 8000) * 0.03 * (smooth_rand(sec, 6) > 0.85)
    return stereo(x, 0) * 0.12
def siren_bed(sec):
    """Low slow two-tone alarm whoop, far away and filtered (an alarm signal, not music)."""
    t = t_(sec); f = 380 + 170 * (0.5 + 0.5 * np.sin(2 * np.pi * t / 2.4))
    x = signal.sawtooth(2 * np.pi * np.cumsum(f) / SR) * 0.5
    return stereo(lp(bp(x, 250, 1400), 1100), 0) * 0.35
def hollow_wind(sec):
    x = bp(brown(sec), 80, 500) * smooth_rand(sec, 0.25, 0.3, 1.0) + bp(noise(sec), 200, 700) * 0.15 * smooth_rand(sec, 0.4, 0, 1)
    return np.stack([x, np.roll(x, 2600)], 1) * 0.7
def sfx_siren():
    sec = 5.0; t = t_(sec); f = 420 + 220 * (0.5 + 0.5 * np.sin(2 * np.pi * t / 1.6 - np.pi / 2))
    x = signal.sawtooth(2 * np.pi * np.cumsum(f) / SR) * 0.6
    return fade(lp(bp(x, 300, 2500), 2000), 0.15, 0.8)
def sfx_alarm_beep():
    out = np.zeros(int(2.4 * SR))
    for k in range(4):
        tt = t_(0.22); b = signal.square(2 * np.pi * 880 * tt) * 0.3
        s0 = int(k * 0.6 * SR); out[s0:s0 + len(tt)] += fade(lp(b, 3000), 0.005, 0.02)
    return out
def sfx_computer_beep():
    out = np.zeros(int(0.5 * SR))
    for k, f in enumerate((1200, 1600)):
        tt = t_(0.08); s0 = int(k * 0.12 * SR); out[s0:s0 + len(tt)] += fade(np.sin(2 * np.pi * f * tt), 0.004, 0.02) * 0.4
    return out
def sfx_metal_clang():
    sec = 1.8; t = t_(sec); x = np.zeros(len(t))
    for f in (310, 523, 811, 1187, 1730):
        x += np.sin(2 * np.pi * f * rng.uniform(0.97, 1.03) * t) * np.exp(-t * rng.uniform(3, 7)) * rng.uniform(0.3, 1)
    x += bp(noise(sec), 1000, 6000) * np.exp(-t * 60) * 0.8
    return fade(x, 0.002, 0.3)
def sfx_steam_hiss():
    sec = 2.5; t = t_(sec)
    return fade(hp(noise(sec), 2500) * np.minimum(1, t / 0.08) * np.exp(-t * 0.8) * 0.6, 0.01, 0.5)
def sfx_drone_pass():
    sec = 4.0; t = t_(sec); u = t / sec
    env = np.exp(-((u - 0.5) ** 2) / 0.06)
    f = 190 * (1 + 0.04 * np.tanh((0.5 - u) * 6))
    x = (signal.sawtooth(2 * np.pi * np.cumsum(f) / SR) * 0.3 + bp(noise(sec), 300, 2500) * 0.6) * env
    x = lp(x, 2500); pan = np.clip((u - 0.5) * 2.2, -1, 1)
    return np.stack([x * np.cos((pan + 1) * np.pi / 4), x * np.sin((pan + 1) * np.pi / 4)], 1)
def sfx_boots_march():
    a = steps(8, 0.42); b = steps(8, 0.42)
    s = int(0.21 * SR); out = np.zeros(len(a) + s); out[:len(a)] += a; out[s:s + len(b)] += b * 0.8
    return lp(out, 2500) * 0.9
def sfx_electric_spark():
    sec = 1.2; out = np.zeros(int(sec * SR))
    for _ in range(25):
        L = int(rng.uniform(0.005, 0.025) * SR); s0 = int(rng.uniform(0, sec - 0.03) * SR)
        out[s0:s0 + L] += hp(noise(L / SR), 2500)[:L] * rng.uniform(0.3, 1)
    return fade(out + hp(noise(sec), 4000)[:len(out)] * 0.05, 0.01, 0.1)
def sfx_weld_hiss():
    sec = 3.0; x = bp(noise(sec), 1500, 7000) * (0.6 + 0.4 * smooth_rand(sec, 8))
    return fade(x * 0.5, 0.05, 0.3)
def sfx_power_down():
    sec = 1.6; t = t_(sec); f = 220 * np.exp(-t * 1.8) + 30
    return fade(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.2) * 0.6 + lp(noise(sec), 200) * np.exp(-t * 3) * 0.3, 0.005, 0.2)
def sfx_power_up():
    sec = 1.6; t = t_(sec); f = 40 + 200 * (1 - np.exp(-t * 2))
    return fade(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / 0.3) * 0.5 + bp(noise(sec), 2000, 6000) * 0.05, 0.05, 0.3)
def sfx_metal_door():
    x = sfx_soft_thud() * 1.4; c = lp(sfx_metal_clang()[:int(1.0 * SR)], 1500) * 0.35
    out = np.zeros(max(len(x), len(c))); out[:len(x)] += x; out[:len(c)] += c
    return out
def sfx_vent_knock():
    out = np.zeros(int(2.6 * SR))
    for k in range(5):
        L = int(0.25 * SR); tt = np.arange(L) / SR
        h = np.sin(2 * np.pi * rng.uniform(140, 220) * tt) * np.exp(-tt * 18) + bp(noise(0.25), 400, 2000)[:L] * np.exp(-tt * 30) * 0.3
        s0 = int((k * 0.48 + rng.uniform(0, 0.04) + 0.05) * SR); out[s0:s0 + L] += h * rng.uniform(0.5, 1)
    return out
def sfx_engine_rev():
    sec = 3.5; t = t_(sec); f = 45 + 35 * np.minimum(1, t / 1.2)
    x = signal.sawtooth(2 * np.pi * np.cumsum(f) / SR) * 0.4 + lp(brown(sec), 200)[:len(t)] * 0.6
    return fade(lp(x, 600) * np.minimum(1, t / 0.3), 0.05, 0.8)
def sfx_distant_boom():
    sec = 3.5; t = t_(sec)
    x = lp(brown(sec), 140)[:len(t)] * np.exp(-t * 1.5) * 2.0 + lp(noise(sec), 500) * np.exp(-t * 8) * 0.6
    return fade(x, 0.003, 1.0)
def sfx_energy_zaps():
    """Muffled, distant volley of energy bursts (never shown on screen)."""
    out = np.zeros(int(2.5 * SR))
    for k in range(6):
        tt = t_(0.18); f = 1800 * np.exp(-tt * 18) + 300
        z = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 14)
        s0 = int((k * 0.33 + rng.uniform(0, 0.08)) * SR); out[s0:s0 + len(tt)] += z * rng.uniform(0.5, 1)
    return lp(out, 1600) * 0.8
def sfx_crowd_roar():
    sec = 4.0; t = t_(sec)
    return murmur(sec, 24) * 2.2 * (np.minimum(1, t / 0.6) * np.minimum(1, (sec - t) / 1.5))[:, None]
def sfx_crowd_panic():
    sec = 4.0; t = t_(sec)
    x = murmur(sec, 30) * 2.0 + stereo(bp(noise(sec), 800, 3000) * smooth_rand(sec, 3, 0, 1) * 0.2, 0)
    return x * (np.minimum(1, t / 0.3) * np.minimum(1, (sec - t) / 1.5))[:, None]
def sfx_cuffs_click():
    return np.concatenate([sfx_lock_click(), np.zeros(int(0.12 * SR)), sfx_lock_click() * 0.8])
def sfx_box_unlock():
    return np.concatenate([sfx_lock_click() * 0.8, np.zeros(int(0.1 * SR)), fade(lp(noise(0.6), 900) * 0.3, 0.05, 0.3)])

AMB.update({
    "wasteland": lambda s: hollow_wind(s) * 1.1 + wind(s, 0.8) * 0.5 + thunder_bed(s) * 0.4,
    "bunker_machinery": lambda s: machinery(s) + steam(s, 0.6) + drips(s, 0.5),
    "engine_room": lambda s: machinery(s, 1.5) + steam(s, 1.2) + electric_hum(s),
    "corridor_drip": lambda s: machinery(s, 0.5) * 0.6 + drips(s, 1.5) + hollow_wind(s) * 0.3,
    "alarm_corridor": lambda s: machinery(s, 0.7) + siren_bed(s) + drips(s, 0.6),
    "workshop": lambda s: electric_hum(s) * 1.4 + machinery(s, 0.35) * 0.5 + hollow_wind(s) * 0.25 + drips(s, 0.3),
    "warehouse_crowd": lambda s: murmur(s, 16) * 0.8 + machinery(s, 0.5) * 0.6 + hollow_wind(s) * 0.3,
    "rebel_workshop": lambda s: murmur(s, 10) * 0.5 + machinery(s, 0.6) * 0.6 + steam(s, 0.4) + electric_hum(s) * 0.5,
    "vent_shaft": lambda s: hollow_wind(s) * 1.2 + drips(s, 0.6) + machinery(s, 0.4) * 0.4,
    "storage_hall": lambda s: ac_hum(s) * 0.8 + hollow_wind(s) * 0.3 + murmur(s, 8) * 0.3,
    "chaos_hall": lambda s: murmur(s, 24) * 0.9 + siren_bed(s) * 0.6 + ac_hum(s) * 0.4,
    "command_center": lambda s: ac_hum(s) + electric_hum(s) * 0.4,
    "detention_room": lambda s: ac_hum(s) * 0.9,
    "upper_balcony": lambda s: hollow_wind(s) * 0.5 + ac_hum(s) * 0.4 + machinery(s, 0.25) * 0.4,
    "surface_green": lambda s: birds(s, 0.8) + wind(s, 0.5),
})

# Isq (island romance): festive street, busy kitchen, courtyard dinner; phone camera, pouring, colour-bag splat
AMB.update({
    "eid_street": lambda s: murmur(s, 10) * 0.55 + birds(s, 0.5) * 0.4 + wind(s, 0.3) + waves(s) * 0.1,
    "kitchen_busy": lambda s: room_tone(s) * 0.8 + murmur(s, 4) * 0.35 + birds(s, 0.3) * 0.2,
    "courtyard_dinner": lambda s: crickets(s, 0.5) * 0.5 + murmur(s, 8) * 0.4 + room_tone(s) * 0.3,
})
def sfx_camera_shutter():
    sec = 0.35; t = t_(sec); out = np.zeros_like(t)
    for st, a in ((0.0, 1.0), (0.11, 0.7)):
        s = int(st * SR); L = int(0.03 * SR); tt = np.arange(L) / SR
        out[s:s + L] += bp(noise(0.03), 1500, 9000) * np.exp(-tt * 160) * a
    return fade(out, 0.001, 0.05)
def sfx_pour():
    sec = 2.2; t = t_(sec)
    x = bp(noise(sec), 500, 3500) * smooth_rand(sec, 25, 0.5, 1.0) * np.minimum(1, t / 0.15) * np.minimum(1, (sec - t) / 0.4)
    bub = np.zeros_like(t)
    for _ in range(30):
        s = int(rng.uniform(0.1, sec - 0.2) * SR); L = int(0.04 * SR); tt = np.arange(L) / SR
        f = rng.uniform(400, 1200)
        bub[s:s + L] += np.sin(2 * np.pi * f * (1 + tt * 10) * tt) * np.exp(-tt * 90) * rng.uniform(0.05, 0.2)
    return fade(x * 0.5 + bub, 0.02, 0.2)
def sfx_splat():
    sec = 0.8; t = t_(sec)
    body = (lp(noise(sec), 1800) + bp(noise(sec), 1500, 6000) * 0.5) * np.exp(-t * 9) * np.minimum(1, t / 0.004)
    return fade(body + np.sin(2 * np.pi * 90 * t) * np.exp(-t * 25) * 0.6, 0.001, 0.1)


# ---------------------------------------------------------------- horror additions (Marufas)
def monitor_bed(sec):
    """ICU: soft periodic patient-monitor blip (a signal tone, not music) + ventilator breath cycle."""
    t = t_(sec); out = np.zeros(len(t)); p = 0.3
    while p < sec - 0.2:
        L = int(0.07 * SR); tt = np.arange(L) / SR; s0 = int(p * SR)
        out[s0:s0 + L] += np.sin(2 * np.pi * 980 * tt) * np.sin(np.pi * tt / 0.07) * 0.25
        p += 0.85
    vent = bp(noise(sec), 300, 1800) * (0.5 + 0.5 * np.sin(2 * np.pi * t / 4.0)) ** 3 * 0.25
    return stereo(out + vent, 0.1)
def dread(sec):
    """Very low, slowly breathing sub-rumble (filtered noise, non-tonal) for possessed-room nights."""
    x = lp(brown(sec), 70) * smooth_rand(sec, 0.12, 0.4, 1.0)
    return np.stack([x, np.roll(x, 3100)], 1) * 0.8
def sfx_bulb_flicker():
    sec = 1.6; t = t_(sec)
    gate = (smooth_rand(sec, 14) > 0.45).astype(float); gate = lp(gate, 60)
    buzz = (np.sin(2 * np.pi * 100 * t) * 0.5 + bp(noise(sec), 2000, 7000) * 0.4) * gate
    for _ in range(5):
        s0 = int(rng.uniform(0, sec - 0.05) * SR); L = int(0.01 * SR)
        buzz[s0:s0 + L] += hp(noise(0.01), 2500)[:L] * np.exp(-np.arange(L) / 60) * 1.5
    return fade(buzz, 0.005, 0.2)
def sfx_door_slam():
    sec = 1.2; t = t_(sec)
    boom = np.sin(2 * np.pi * 55 * t) * np.exp(-t * 7) + lp(noise(sec), 500) * np.exp(-t * 14) * 0.9
    rattle = bp(noise(sec), 900, 4000) * np.exp(-t * 9) * smooth_rand(sec, 30, 0.2, 1) * 0.3
    return fade(boom + rattle, 0.001, 0.25)
def sfx_low_growl():
    sec = 2.6; t = t_(sec)
    x = bp(brown(sec), 35, 160) * (0.5 + 0.5 * np.abs(np.sin(2 * np.pi * 7 * t))) * smooth_rand(sec, 3, 0.4, 1)
    x += bp(noise(sec), 120, 400) * 0.15 * smooth_rand(sec, 9, 0, 1)
    return fade(x * np.sin(np.pi * t / sec) ** 0.6, 0.1, 0.4)
def sfx_whisper_recite():
    """Low indistinct murmured recitation (one voice, unintelligible, filtered noise with syllable rhythm)."""
    sec = 5.0
    x = lp(murmur(sec, 1).mean(1), 1400)
    return fade(x, 0.4, 0.8)
def sfx_creak():
    sec = 1.4; t = t_(sec)
    f = 260 + 90 * np.sin(2 * np.pi * 0.7 * t)
    c = np.sin(2 * np.pi * np.cumsum(f) / SR) * (np.abs(signal.sawtooth(2 * np.pi * 24 * t)) ** 6)
    return fade(bp(c, 200, 2200) * np.sin(np.pi * t / sec), 0.02, 0.2)
def sfx_monitor_alarm():
    out = np.zeros(int(2.0 * SR))
    for k in range(3):
        s = int(k * 0.55 * SR); L = int(0.25 * SR); tt = np.arange(L) / SR
        out[s:s + L] += np.sin(2 * np.pi * 880 * tt) * np.sin(np.pi * tt / 0.25) * 0.6
    return fade(out, 0.005, 0.05)
def sfx_flashlight_click():
    sec = 0.2; out = np.zeros(int(sec * SR)); L = int(0.02 * SR)
    out[:L] = hp(noise(0.02), 1800) * np.exp(-np.arange(L) / 70)
    return out
def sfx_crash_clatter():
    """Things knocked over: several thuds + small clatters (vases, cushions, a table edge)."""
    sec = 1.8; out = np.zeros(int(sec * SR))
    for _ in range(6):
        s0 = int(rng.uniform(0, 1.2) * SR); L = int(0.35 * SR); tt = np.arange(L) / SR
        out[s0:s0 + L] += (np.sin(2 * np.pi * rng.uniform(70, 160) * tt) * np.exp(-tt * 20)
                           + bp(noise(0.35), 600, 4000)[:L] * np.exp(-tt * 30) * 0.6) * rng.uniform(0.4, 1)
    return fade(out, 0.002, 0.2)


AMB.update({
    "haunted_room": lambda s: room_tone(s) * 0.6 + dread(s) * 0.9 + hollow_wind(s) * 0.35 + crickets(s, 0.15) * 0.15,
    "haunted_living": lambda s: room_tone(s) * 0.7 + dread(s) * 0.6 + crickets(s, 0.3) * 0.3,
    "abandoned_house": lambda s: hollow_wind(s) * 0.9 + drips(s, 0.4) + crickets(s, 0.6) * 0.5 + wind(s, 0.4) * 0.5,
    "icu_room": lambda s: ac_hum(s) * 0.8 + monitor_bed(s),
    "night_lane": lambda s: crickets(s, 0.9) + wind(s, 0.6) + waves(s) * 0.2 + dread(s) * 0.3,
})

AMB.update({
    "hacker_room": lambda s: room_tone(s) * 0.7 + electric_hum(s) * 0.45 + ac_hum(s) * 0.3 + traffic(s, False) * 0.08,
    "server_room": lambda s: electric_hum(s) * 1.0 + ac_hum(s) * 0.8,
    "gallery": lambda s: lp(room_tone(s), 900) * 0.8 + ac_hum(s) * 0.4 + murmur(s, 3) * 0.12,
    "storeroom": lambda s: lp(room_tone(s), 600) * 0.9 + hollow_wind(s) * 0.15,
    "lounge_private": lambda s: ac_hum(s) * 0.8 + room_tone(s) * 0.4,
    "harbour_cafe": lambda s: murmur(s, 8) * 0.45 + waves(s) * 0.5 + wind(s, 0.4) * 0.4 + distant_boats(s) * 0.35,
})


# Emme Fahu Message (rainy-monsoon apartment grief drama): rain on windows, car in rain, clinic, kettle, wipers, clock
def window_rain(sec):
    """Rain heard through a closed window: muffled wash + sparse taps on the glass."""
    x = lp(rain(sec)[:, 0], 2500) * 0.8
    taps = (rng.random(int(round(sec * SR))) > 0.9996).astype(float)
    taps = signal.lfilter([1], [1, -0.97], taps) * bp(noise(sec), 1500, 4500) * 0.4
    m = x + taps
    return np.stack([m, np.roll(m, 1700)], 1)
def wiper_bed(sec):
    """Windscreen wipers: a soft rubbery swish every ~1.3 s."""
    t = t_(sec); out = np.zeros(len(t)); p = 0.2
    while p < sec - 0.6:
        L = int(0.45 * SR); tt = np.arange(L) / SR; s0 = int(p * SR)
        out[s0:s0 + L] += bp(noise(0.45), 300, 2200)[:L] * np.sin(np.pi * tt / 0.45) ** 2 * 0.5
        p += 1.3
    return stereo(out, 0.0)
def clock_bed(sec):
    t = t_(sec); out = np.zeros(len(t)); p = 0.1
    while p < sec - 0.05:
        L = int(0.012 * SR); s0 = int(p * SR)
        out[s0:s0 + L] += hp(noise(0.012), 2500)[:L] * np.exp(-np.arange(L) / 50) * 0.5
        p += 1.0
    return stereo(out, -0.3)
AMB.update({
    "apartment_morning": lambda s: room_tone(s) + birds(s, 0.3) * 0.25 + traffic(s, False) * 0.25,
    "apartment_rain_day": lambda s: room_tone(s) * 0.8 + window_rain(s) * 0.9 + traffic(s, False) * 0.12,
    "apartment_rain_night": lambda s: room_tone(s) * 0.7 + window_rain(s) + thunder_bed(s) * 0.35,
    "apartment_quiet_night": lambda s: room_tone(s) * 0.9 + clock_bed(s) * 0.6 + window_rain(s) * 0.4,
    "car_rain": lambda s: car_cabin(s) * 0.8 + window_rain(s) * 0.7 + wiper_bed(s) * 0.6,
    "clinic_waiting": lambda s: ac_hum(s) * 0.9 + murmur(s, 4) * 0.25,
    "nursery_evening": lambda s: room_tone(s) * 0.7 + birds(s, 0.25) * 0.25 + wind(s, 0.2) * 0.3,
    # Nindheveethimeymathee (Malé TV studio, school, penthouse terraces, a Vietnam hotel)
    "tv_studio": lambda s: ac_hum(s) * 0.8 + room_tone(s) * 0.4 + murmur(s, 4) * 0.12,
    "classroom": lambda s: room_tone(s) + ac_hum(s) * 0.3 + murmur(s, 6) * 0.25 + birds(s, 0.2) * 0.15,
    "hotel_hall": lambda s: murmur(s, 14) * 0.7 + ac_hum(s) * 0.4,
    "hotel_room": lambda s: ac_hum(s) * 0.9 + traffic(s, False) * 0.1,
    "rooftop_day": lambda s: wind(s, 0.7) + traffic(s, False) * 0.35 + birds(s, 0.3) * 0.25,
    "rooftop_night": lambda s: wind(s, 0.6) + traffic(s, False) * 0.3 + crickets(s, 0.3) * 0.25,
    "seawall_dusk": lambda s: waves(s) + traffic(s, False) * 0.35 + wind(s, 0.5) * 0.5 + birds(s, 0.2) * 0.2,
    "cemetery_dawn": lambda s: birds(s, 0.6) + wind(s, 0.5) + traffic(s, False) * 0.1,
})
AMB.update({
    # 16February (island night road / unfinished guesthouses, resort office + shop, staff launch)
    "office_storm_night": lambda s: ac_hum(s) * 0.7 + window_rain(s) * 0.8 + thunder_bed(s) * 0.45,
    "resort_day": lambda s: waves(s) * 0.6 + birds(s, 0.5) * 0.5 + wind(s, 0.4) * 0.5 + murmur(s, 3) * 0.08,
    "building_site_rain": lambda s: rain(s) * 0.9 + wind(s, 0.8) + dread(s) * 0.3,
    "shop_day": lambda s: ac_hum(s) * 0.8 + murmur(s, 2) * 0.15 + waves(s) * 0.12,
    "staff_room": lambda s: ac_hum(s) + room_tone(s) * 0.5 + birds(s, 0.15) * 0.1,
})
AMB.update({
    # SuratulFaatihaa (reflective tafsir: cosmos, the plain of the hereafter, old Madinah, libraries, mosques)
    "cosmos": lambda s: np.stack([lp(brown(s), 120)] * 2, 1) * 0.5 + wind(s, 0.15) * 0.4,
    "vast_plain": lambda s: wind(s, 0.8) + dread(s) * 0.25,
    "old_madinah_day": lambda s: wind(s, 0.5) + birds(s, 0.4) * 0.4,
    "library_night": lambda s: room_tone(s) + clock_bed(s) * 0.35,
    "mosque_dawn": lambda s: lp(room_tone(s), 900) * 0.8 + birds(s, 0.5) * 0.3,
    "exam_hall": lambda s: room_tone(s) + ac_hum(s) * 0.4 + clock_bed(s) * 0.5,
    "ruins_dust": lambda s: wind(s, 0.8) + dread(s) * 0.3,
    "battlefield_far": lambda s: wind(s, 0.9) + lp(murmur(s, 10).T, 600).T * 0.5,
})
def sfx_lift_ding():
    """A single soft elevator arrival chime (one decaying tone, not a melody)."""
    sec = 1.2; t = t_(sec)
    return fade((np.sin(2 * np.pi * 1320 * t) + 0.3 * np.sin(2 * np.pi * 2640 * t)) * np.exp(-t * 4) * 0.4, 0.003, 0.2)
def sfx_kettle_whistle():
    """A kettle coming to the boil: rising breathy hiss into a steady high whistle (a signal tone, not music)."""
    sec = 2.4; t = t_(sec)
    rise = np.minimum(1, t / 1.0)
    hiss = bp(noise(sec), 2500, 7000) * 0.3 * rise
    f = 1900 + 300 * rise + 15 * np.sin(2 * np.pi * 5 * t)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.clip((t - 0.4) / 0.8, 0, 1) * 0.35
    return fade(hiss + tone, 0.05, 0.4)
def sfx_pan_sizzle():
    sec = 2.5; t = t_(sec)
    x = bp(noise(sec), 2000, 9000) * smooth_rand(sec, 30, 0.4, 1.0) * 0.6
    pops = (rng.random(int(sec * SR)) > 0.9995).astype(float)
    x += signal.lfilter([1], [1, -0.9], pops) * hp(noise(sec), 3000) * 0.6
    return fade(x, 0.2, 0.5)
def sfx_wipers(): return fade(wiper_bed(3.0)[:, 0], 0.05, 0.3)
def sfx_clock_tick(): return fade(clock_bed(4.0)[:, 0], 0.01, 0.2)
def sfx_keys_jingle():
    sec = 0.7; out = np.zeros(int(sec * SR))
    for _ in range(9):
        s0 = int(rng.uniform(0, 0.45) * SR); L = int(0.12 * SR); tt = np.arange(L) / SR
        out[s0:s0 + L] += np.sin(2 * np.pi * rng.uniform(3000, 6500) * tt) * np.exp(-tt * 45) * rng.uniform(0.2, 0.6)
    return fade(out, 0.002, 0.1)

# Sahar (Palestine 1948: stone village, burning hills, cave, army truck, Haifa port, ship to France, road to Jordan)
def fire_bed(sec):
    """Distant fire: low roar + sparse crackles (heard far off, never close)."""
    x = lp(brown(sec), 250) * smooth_rand(sec, 0.3, 0.6, 1.0) * 0.6
    cr = np.zeros(int(round(sec * SR)))
    for _ in range(int(sec * 6)):
        s0 = int(rng.uniform(0, sec - 0.02) * SR); L = int(0.008 * SR)
        cr[s0:s0 + L] += hp(noise(0.008), 1500) * rng.uniform(0.1, 0.5)
    m = x + lp(cr, 4000) * 0.5
    return np.stack([m, np.roll(m, 2100)], 1)
def far_booms(sec):
    out = np.zeros((int(round(sec * SR)), 2)); t = rng.uniform(5, 14)
    while t < sec - 4:
        x = lp(sfx_distant_boom(), 400) * rng.uniform(0.3, 0.7)
        s0 = int(t * SR); e0 = min(len(out), s0 + len(x)); out[s0:e0] += stereo(x[: e0 - s0], rng.uniform(-0.7, 0.7))
        t += rng.uniform(18, 40)
    return out
def truck_cabin(sec):
    """Old 1940s truck on a rough road: low diesel rumble, body rattle, tyre on gravel."""
    t = t_(sec)
    f0 = 38 + 4 * smooth_rand(sec, 0.2); ph = 2 * np.pi * np.cumsum(f0) / SR
    eng = lp(signal.sawtooth(ph) * 0.4 + lp(brown(sec), 120) * 0.8, 400)
    rattle = bp(noise(sec), 900, 3500) * (smooth_rand(sec, 6, 0, 1) > 0.7) * 0.12
    gravel = bp(noise(sec), 200, 1200) * 0.15 * smooth_rand(sec, 0.5, 0.5, 1)
    m = eng + rattle + gravel
    return np.stack([m, np.roll(m, 700)], 1) * 0.7
def ship_hull(sec):
    """Inside a steamship: deep engine throb, slow hull creaks, muffled sea wash."""
    t = t_(sec)
    throb = lp(brown(sec), 90) * (0.8 + 0.2 * np.sin(2 * np.pi * 1.6 * t)) * 0.9
    wash = lp(waves(sec)[:, 0], 500) * 0.4
    m = throb + wash
    out = np.stack([m, np.roll(m, 1300)], 1)
    p = rng.uniform(3, 8)
    while p < sec - 2:
        c = sfx_creak() * 0.25; s0 = int(p * SR); e0 = min(len(out), s0 + len(c))
        out[s0:e0] += stereo(c[: e0 - s0], rng.uniform(-0.6, 0.6)); p += rng.uniform(8, 18)
    return out * 0.7
def sfx_distant_shots():
    """A far-off, heavily muffled volley of cracks heard across the hills (offscreen; never shown)."""
    sec = 2.6; out = np.zeros(int(sec * SR))
    for k in range(rng.integers(4, 8)):
        s0 = int(rng.uniform(0, 2.0) * SR); L = int(0.25 * SR); tt = np.arange(L) / SR
        out[s0:s0 + L] += (lp(noise(0.25), 1200)[:L] * np.exp(-tt * 30) + np.sin(2 * np.pi * 70 * tt) * np.exp(-tt * 18) * 0.5) * rng.uniform(0.4, 1)
    return fade(lp(out, 1500), 0.002, 0.3)
def sfx_chain_rattle():
    sec = 1.4; out = np.zeros(int(sec * SR))
    for _ in range(22):
        s0 = int(rng.uniform(0, 1.1) * SR); L = int(0.06 * SR); tt = np.arange(L) / SR
        out[s0:s0 + L] += np.sin(2 * np.pi * rng.uniform(1800, 4200) * tt) * np.exp(-tt * 60) * rng.uniform(0.2, 0.6)
    return fade(out + bp(noise(sec), 2000, 6000) * 0.05, 0.005, 0.1)
def sfx_ship_horn():
    """One long, low steamship horn blast (a signal tone, not music)."""
    sec = 3.5; t = t_(sec)
    x = signal.sawtooth(2 * np.pi * 110 * t) * 0.4 + signal.sawtooth(2 * np.pi * 165 * t) * 0.15
    return fade(lp(x, 700) * np.minimum(1, t / 0.3) * np.minimum(1, (sec - t) / 0.8), 0.05, 0.4)
def sfx_truck_start():
    sec = 3.5; t = t_(sec); f = 30 + 25 * np.minimum(1, t / 1.5)
    x = signal.sawtooth(2 * np.pi * np.cumsum(f) / SR) * 0.4 + lp(brown(sec), 180) * 0.6
    return fade(lp(x, 500) * np.minimum(1, t / 0.2), 0.02, 0.8)
def sfx_metal_gate(): return sfx_metal_door()
def sfx_water_splash_small(): return sfx_pour()
def sfx_stone_scrape():
    sec = 0.9; t = t_(sec)
    return fade(bp(noise(sec), 300, 2500) * smooth_rand(sec, 20, 0.3, 1) * np.sin(np.pi * t / sec), 0.01, 0.1)
AMB.update({
    "village_spring_day": lambda s: birds(s, 0.8) + wind(s, 0.4) + murmur(s, 3) * 0.15,
    "village_evening": lambda s: birds(s, 0.25) * 0.5 + crickets(s, 0.4) * 0.5 + wind(s, 0.4),
    "wedding_crowd": lambda s: murmur(s, 14) * 0.7 + birds(s, 0.4) * 0.3 + wind(s, 0.3) * 0.5,
    "stone_house_day": lambda s: lp(room_tone(s), 500) * 0.7 + birds(s, 0.5) * 0.35,
    "stone_house_dawn": lambda s: lp(room_tone(s), 500) * 0.6 + birds(s, 0.9) * 0.4 + wind(s, 0.2),
    "stone_house_night": lambda s: lp(room_tone(s), 500) * 0.7 + crickets(s, 0.5) * 0.45,
    "village_burning": lambda s: fire_bed(s) * 0.9 + wind(s, 0.7) + far_booms(s) * 0.8 + lp(murmur(s, 10).T, 900).T * 0.3,
    "hillside_smoke": lambda s: wind(s, 0.8) + fire_bed(s) * 0.35 + far_booms(s) * 0.5 + birds(s, 0.15) * 0.15,
    "olive_hill_day": lambda s: wind(s, 0.6) + birds(s, 0.5) * 0.4 + crickets(s, 0.2) * 0.15,
    "forest_night": lambda s: crickets(s, 1.0) + wind(s, 0.6) + hollow_wind(s) * 0.2,
    "cave": lambda s: hollow_wind(s) * 0.9 + drips(s, 0.6) + lp(room_tone(s), 300) * 0.4,
    "cave_night": lambda s: hollow_wind(s) * 0.8 + drips(s, 0.4) + crickets(s, 0.3) * 0.25,
    "truck_back": lambda s: truck_cabin(s) + wind(s, 0.5) * 0.6,
    "truck_night": lambda s: truck_cabin(s) * 0.9 + wind(s, 0.4) * 0.5 + crickets(s, 0.4) * 0.3,
    "army_camp_night": lambda s: crickets(s, 0.6) + wind(s, 0.5) + lp(murmur(s, 6).T, 1200).T * 0.3 + fire_bed(s) * 0.15,
    "army_camp_dawn": lambda s: birds(s, 0.4) * 0.5 + wind(s, 0.5) + lp(murmur(s, 5).T, 1200).T * 0.25,
    "old_city_crowd": lambda s: murmur(s, 16) * 0.6 + wind(s, 0.4) + truck_cabin(s) * 0.25,
    "port_day": lambda s: waves(s) * 0.7 + wind(s, 0.6) + murmur(s, 6) * 0.25 + birds(s, 0.3) * 0.3 + distant_boats(s) * 0.4,
    "ship_cabin": lambda s: ship_hull(s),
    "ship_deck": lambda s: waves(s) + wind(s, 0.9) + lp(brown(s), 90)[:, None].repeat(2, 1) * 0.4,
    "ship_storm": lambda s: ship_hull(s) * 0.7 + rain(s) * 0.9 + wind(s, 1.2) + thunder_bed(s) * 0.8,
    "checkpoint_night": lambda s: crickets(s, 0.6) + wind(s, 0.5) + truck_cabin(s) * 0.3 + lp(murmur(s, 3).T, 1000).T * 0.2,
    "desert_dawn": lambda s: wind(s, 0.7) + birds(s, 0.5) * 0.4,
    "border_post_day": lambda s: wind(s, 0.6) + murmur(s, 5) * 0.25 + birds(s, 0.3) * 0.25,
    "dream_glow": lambda s: lp(room_tone(s), 400) * 0.6 + wind(s, 0.15) * 0.3,
})

SFX ={k[4:]: v for k, v in globals().items() if k.startswith("sfx_") and callable(v)}


def to_st(x): return x if x.ndim == 2 else stereo(x, 0)


# ---------------------------------------------------------------- build stems
def build():
    amb = np.zeros((N, 2)); sfx = np.zeros((N, 2)); drone = np.zeros((N, 2))
    amb_lvl = speech_rms * db(AMB_LEVEL)
    XF = int(1.5 * SR)
    # ambience: group consecutive shots with the same bed
    runs = []
    for s in scenes:
        a, b = int(s["startMs"] * SR / 1000), int(s["endMs"] * SR / 1000)
        if runs and runs[-1][0] == s["ambience"]: runs[-1][2] = b
        else: runs.append([s["ambience"], a, b])
    for k, (name, a, b) in enumerate(runs):
        a0 = max(0, a - XF // 2); b0 = min(N, b + XF // 2)
        bed = rmsnorm(AMB[name]((b0 - a0) / SR + 0.01)[: b0 - a0]) * amb_lvl
        env = np.ones(b0 - a0)
        fi = XF if k else int(2.5 * SR); fo = XF if k < len(runs) - 1 else int(2.0 * SR)
        env[:fi] *= np.linspace(0, 1, fi); env[-fo:] *= np.linspace(1, 0, fo)
        amb[a0:b0] += bed * env[:, None]
    # sfx at word times, never longer than the shot
    cues = []
    for s in scenes:
        end = int(s["endMs"] * SR / 1000)
        for c in s["sfx"]:
            x = to_st(SFX[c["name"]]())
            x = x / (np.sqrt(np.mean(x[np.abs(x).max(1) > np.abs(x).max() * 0.05] ** 2)) + 1e-9)
            pos = int(c["atMs"] * SR / 1000)
            L = min(len(x), end - pos, N - pos)
            if L <= 0: continue
            seg = x[:L].copy()
            f = min(int(0.015 * SR), L // 4) if L == len(x) else min(int(0.25 * SR), L // 3)  # longer fade if cut at shot end
            seg[:int(0.005 * SR)] *= np.linspace(0, 1, int(0.005 * SR))[:, None]
            seg[-f:] *= np.linspace(1, 0, f)[:, None]
            sfx[pos:pos + L] += seg * speech_rms * db(c["gainDb"])
            cues.append((s["id"], c["name"], c["atMs"]))
    # drones: soft, low, non-melodic beds under emotional peaks (merged runs, 3 s fades)
    runs = []
    for s in scenes:
        if not s.get("hum"): continue
        a, b = int(s["startMs"] * SR / 1000), int(s["endMs"] * SR / 1000)
        if runs and a - runs[-1][1] < 2 * SR: runs[-1][1] = b
        else: runs.append([a, b])
    for a, b in runs:
        L = b - a; t = np.arange(L) / SR
        x = np.sin(2 * np.pi * 58 * t + 0.3 * np.sin(2 * np.pi * 0.07 * t)) * 0.7
        x += lp(bp(noise(L / SR), 80, 400), 300) * 0.5 * smooth_rand(L / SR, 0.2, 0.5, 1)
        x = rmsnorm(x)
        env = np.ones(L); f = min(int(3 * SR), L // 3)
        env[:f] = np.linspace(0, 1, f); env[-f:] = np.linspace(1, 0, f)
        drone[a:b] += stereo(x * env, 0) * speech_rms * db(-32)
    return amb, sfx, drone, cues


amb, sfx, drone, cues = build()
def wr(path, x): wavfile.write(path, SR, np.clip(x, -1, 1).astype(np.float32))
wr(os.path.join(A, "ambience.wav"), amb); wr(os.path.join(A, "sfx.wav"), sfx); wr(os.path.join(A, "drone.wav"), drone)
wr(os.path.join(A, "fx_bed.wav"), amb + sfx + drone)
json.dump(cues, open(os.path.join(A, "sfx_cues.json"), "w"), indent=0)
print(f"{len(cues)} sfx cues placed")

# ---------------------------------------------------------------- mix: duck fx under narration, loudnorm -14 LUFS / -1.5 dBTP
pre = os.path.join(A, "premix.wav")
graph = ("[0:a]asplit=2[n1][n2];"
         "[1:a][n2]sidechaincompress=threshold=0.03:ratio=4:attack=30:release=500:makeup=1[fxd];"
         "[n1][fxd]amix=inputs=2:normalize=0:duration=first[m]")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", narr_path, "-i", os.path.join(A, "fx_bed.wav"),
                "-filter_complex", graph, "-map", "[m]", "-c:a", "pcm_f32le", pre], check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", pre, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                    "-f", "null", "-"], capture_output=True, text=True)
js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
m = json.loads(js)
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
      f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", pre, "-af", ln + ",aresample=48000", "-ar", "48000",
                "-c:a", "pcm_s16le", os.path.join(A, "final_mix.wav")], check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", os.path.join(A, "final_mix.wav"), "-af",
                    "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
print("\n".join(r.stderr.strip().splitlines()[-12:]))
