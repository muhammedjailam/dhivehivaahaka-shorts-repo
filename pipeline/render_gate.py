"""Sequential renderer that yields to other sessions: before each episode it waits until no other render_beats.py
process is running (two concurrent renders exhaust RAM). Episodes are read from <series_dir>/render_queue.txt
(one per line, 'END' stops when everything before it is done), like render_queue.py, then qc.py runs.
Usage: python render_gate.py <series_dir> <series_name>
"""
import os, subprocess, sys, time

series_dir, series = sys.argv[1], sys.argv[2]
Q = os.path.join(series_dir, "render_queue.txt")
here = os.path.dirname(os.path.abspath(__file__))
env = dict(os.environ, PYTHONIOENCODING="utf-8", RENDER_WORKERS=os.environ.get("RENDER_WORKERS", "5"))


def others_rendering():
    out = subprocess.run(["powershell", "-NoProfile", "-Command",
                          "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
                          "ForEach-Object { $_.CommandLine }"], capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if "render_beats.py" in l]


done = set()
while True:
    items = [l.strip() for l in open(Q, encoding="utf-8")] if os.path.exists(Q) else []
    todo = [x for x in items if x and x != "END" and x not in done]
    if not todo:
        if "END" in items: break
        time.sleep(20); continue
    busy = others_rendering()
    if busy:
        print(f"waiting: another render is running ({busy[0][:100]})", flush=True)
        while others_rendering(): time.sleep(30)
    n = todo[0]
    ep = os.path.join(series_dir, f"episode-{n}")
    t0 = time.time()
    print(f"=== render {n}", flush=True)
    with open(os.path.join(ep, "work", "render_beats.log"), "w", encoding="utf-8") as log:
        r = subprocess.run([sys.executable, os.path.join(here, "render_beats.py"), ep, series, n],
                           stdout=log, stderr=subprocess.STDOUT, env=env)
    if r.returncode == 0:
        with open(os.path.join(ep, "work", "qc.log"), "w", encoding="utf-8") as log:
            subprocess.run([sys.executable, os.path.join(here, "qc.py"), ep, series, n], stdout=log, stderr=subprocess.STDOUT, env=env)
    print(f"=== {n} rc={r.returncode} {time.time() - t0:.0f}s", flush=True)
    done.add(n)
print("queue finished")
