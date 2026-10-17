"""Beat/shot plan for Project Phenix episode 320 — v2 re-cut on the new audio (used by plan_beats.py).
v1 images are reused via v1="beat_###"; new images mainly for spec 5.4 (speaker centred and sharp)."""

LOC = {
    "cargo_boat": "a weathered wooden-and-steel cargo supply boat travelling south across the open Maldivian sea, an open deck stacked with lashed wooden crates and sacks, a small wheelhouse, the low skyline of Malé's north harbour fading behind",
    "cargo_cabin": "the small cramped cabin of a cargo supply boat at sea, a narrow bench, a fold-down table, a small round window looking out on the grey sea",
    "villingili_harbour": "Villingili island harbour in Gaafu Alifu atoll at 9 pm, a concrete quay under a few dim yellow lamps, dark narrow sandy island lanes lined with coral-stone walls and breadfruit trees leading inland",
    "hospital_lane": "a dark sandy island lane at night leading to a quiet two-storey atoll hospital building with a few lit windows and a small lit emergency entrance",
    "hospital_corridor": "the empty upstairs corridor of a two-storey island hospital at night, pale green walls, a few dim ceiling lights, closed wooden office doors with plain blank nameplates, a polished floor",
    "raniya_office": "Dr. Raniya's small office in the island hospital: a wooden desk with stacked files and a desk lamp, a plain chair behind it, a window with dark rain outside, a filing cabinet, a heavy metal file holder on the desk",
    "office_dark": "Dr. Raniya's small hospital office plunged into total darkness, the desk with files and a heavy metal file holder, a rain-streaked window giving a faint cold glow, the wooden door to the corridor",
    "corridor_dark": "the long hospital corridor in total darkness, pale walls, closed doors, a faint emergency glow at the far end, rain-streaked windows",
    "hospital_garden": "the back garden of the island hospital at night in the rain: a lit back door, wet hibiscus and breadfruit trees, a sandy path disappearing into dark island lanes",
    "old_jetty": "an abandoned old wooden jetty on the island's west shore at night in rain, broken planks and leaning posts, black water, dense dark bushes and screwpine at the shoreline",
    "storm_sea": "the open sea between islands in a violent storm at night, huge black waves with white foaming crests, salt spray, black clouds, lightning",
    "kandu_beach": "the white sand beach of Kandu-huttaa, a deserted jungle-covered island, at night: a narrow channel through the reef behind, dense black jungle of screwpine, magoo bushes and coconut palms right behind the beach",
    "kandu_jungle": "inside the dense dark jungle of Kandu-huttaa at night: screwpine, magoo bushes and coconut palms; in a small clearing a low concrete block set into the ground with a heavy rusted steel hatch-door and a small electronic keypad panel beside it",
    "kandu_lagoon": "the lagoon of Kandu-huttaa at night seen from the edge of the jungle: black calm water inside the reef, the dark jungle-covered island, a stormy sky",
}
MOOD = {
    "cargo_boat": "dim grey-blue dawn light, a pale pink glow low on the horizon, calm sea, quiet secrecy and tension",
    "cargo_cabin": "cool grey daylight from the small window, the blue glow of a laptop, darkening storm clouds gathering outside, uneasy silence",
    "villingili_harbour": "night, cold navy-blue darkness, a few warm dim yellow lamps, damp air, watchful and quiet",
    "hospital_lane": "night, cold navy-blue darkness, the warm glow of the hospital's lit windows, deep shadows, silent and eerie",
    "hospital_corridor": "night, flat dim fluorescent light, long shadows, deserted and tense",
    "raniya_office": "night, the warm amber desk lamp against cold navy-blue shadows, rain on the window, fear and tension",
    "office_dark": "night, sudden total blackout: cold navy-blue darkness, only faint moonlight from the rain-streaked window and thin white flashlight beams, terror",
    "corridor_dark": "night, blackout, cold navy-blue darkness, a faint red emergency glow at the far end, bursts of grey dust in torchlight, panic",
    "hospital_garden": "night, heavy rain, cold navy-blue darkness, the warm light of the open back door behind, urgent escape",
    "old_jetty": "night, heavy rain, cold navy-blue darkness, faint moonlight through black clouds, wet glistening planks, exhaustion and fear",
    "storm_sea": "storm at night: black sea, white spray, flashes of lightning, a blinding white searchlight beam, deadly danger",
    "kandu_beach": "night, cold navy-blue darkness after the storm, faint moonlight breaking through clouds, white sand glowing softly, exhausted and ominous",
    "kandu_jungle": "night, cold navy-blue darkness, faint moonlight through the leaves, the small green glow of the keypad and white flashlight beams, silent dread",
    "kandu_lagoon": "night, cold navy-blue darkness, a powerful white searchlight sweeping across the black lagoon, menacing",
}

A = ("Ashham in plain civilian clothes (not a uniform): a dark-grey long-sleeved button shirt and dark trousers, "
     "short dark stubble")
AD = A + ", damp and dusty"
H = "Habeeb in his dark-grey zip-up jacket and black-rimmed glasses"
R = "Dr. Raniya in her white doctor's coat over a dusty-blue dress, navy hijab fully covering her hair and neck"
RW = ("Dr. Raniya WITHOUT her white coat: a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully "
      "covering her hair and neck, soaked dark by rain and spray but fully opaque")
LOW = "faces in the upper two-thirds, a calm dark lower third"

# ---- the v1 beats (text unchanged, documentation; their old `to` values are overridden below)
_V1 = [
    # ---------------- CARGO BOAT SOUTH
    dict(to=3, reason="episode opening: dawn, a cargo boat leaving Malé's north harbour with Ashham and Habeeb as secret passengers",
         chars=["ashham", "habeeb"], loc="cargo_boat",
         visual=f"{A} and {H} sitting quietly among lashed wooden crates on the open deck of the cargo boat as it pulls away from Malé's north harbour at dawn, Habeeb with a laptop bag on his knees, Ashham looking back at the fading city skyline with a grave face; plain unmarked crates",
         camera=f"medium wide shot from the deck, eye level, {LOW} (the wet wooden deck)", amb="sea_boat"),
    dict(to=7, reason="action change: in the cabin Habeeb tracks Raniya on the satellite modem; Ashham watches the storm brewing through the window",
         chars=["habeeb", "ashham"], loc="cargo_cabin",
         visual=f"{H} hunched at the fold-down table over his open laptop and a small satellite modem with a blinking light, the screen angled away from the viewer, its blue glow on his glasses; {A} standing by the small round window looking out at dark storm clouds gathering over the grey sea, arms folded, serious",
         camera=f"medium shot, eye level, {LOW} (table top)", amb="sea_boat"),
    # ---------------- VILLINGILI
    dict(to=10, reason="time and scene change: next night at 9 pm they land at Villingili and walk the dark lanes to the quiet two-storey hospital",
         chars=["ashham", "habeeb"], loc="hospital_lane",
         visual=f"{A} and {H} (with a backpack) walking side by side up a dark sandy island lane between coral-stone walls, seen slightly from behind, glancing around warily; ahead at the end of the lane the quiet two-storey island hospital with a few lit windows and a small lit emergency door; far behind them a dim yellow harbour lamp",
         camera=f"medium wide shot, eye level, slightly from behind, the hospital and figures in the upper two-thirds, {LOW} (dark sandy lane)",
         amb="island_night", transition="black"),
    dict(to=11, reason="location change: inside the corridor Habeeb keeps watch while Ashham knocks on Dr. Raniya's door",
         chars=["ashham", "habeeb"], loc="hospital_corridor",
         visual=f"{A} knocking softly with his knuckles on a closed wooden office door with a blank nameplate in the empty dim corridor; a few steps behind him {H} keeping watch, glancing back down the corridor",
         camera=f"medium wide shot down the corridor, eye level, {LOW} (polished floor)", amb="hospital_corridor"),
    # ---------------- RANIYA'S OFFICE
    dict(to=14, reason="character enters: Dr. Raniya at her desk, frightened by the two strangers; Ashham shows his police card",
         chars=["raniya", "ashham", "habeeb"], loc="raniya_office",
         visual=f"{R} standing up behind her desk with stacked files, startled and frightened, one hand raised in front of her; across the room near the closed door {A} holding up a small blank police ID card with no writing, calm and firm; {H} just behind him by the door; a wide gap between her and the men",
         camera=f"medium wide shot, eye level, {LOW} (desk top and floor)", amb="hospital_room"),
    dict(to=18, reason="emotional turning point: hearing Naail's and her father's names she breaks down into her chair",
         chars=["raniya", "ashham", "habeeb"], loc="raniya_office",
         visual=f"{R} sunk into the chair behind her desk, her face in her hands, crying, shoulders shaking; {A} and {H} standing on the other side of the desk at a respectful distance, looking at her with grave sympathy",
         camera=f"medium shot, eye level, {LOW} (desk top with files)", amb="hospital_room", hum=True),
    dict(to=22, reason="framing change: calmer now, Raniya reveals the secret lab on Kandu-huttaa; Ashham leans in to ask who is behind it",
         chars=["raniya", "ashham"], loc="raniya_office",
         visual=f"close-up of {R} sitting at her desk, eyes red from crying, speaking urgently in a low voice, one hand pressed flat on a closed file; the shoulder of {A} soft and out of focus in the foreground as he leans forward across the desk",
         camera=f"close-up over Ashham's shoulder, eye level, {LOW} (desk top)", amb="hospital_room",
         sens="other", safe="the human experiments and trafficking are only described in her words; nothing of the lab is shown"),
    # ---------------- BLACKOUT AND ATTACK
    dict(to=25, reason="emotional turning point: every light in the hospital goes out; boots in the corridor; Ashham holds the door",
         chars=["ashham", "raniya", "habeeb"], loc="office_dark",
         visual=f"the office in sudden darkness: {A} braced with his shoulder against the closed wooden door, holding the handle, tense; {H} at the window pushing it open; {R} pressed back against the filing cabinet, hands clasped at her own chest, eyes wide with terror; thin white lines of flashlight light under the door",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="hospital_night", hum=True),
    dict(to=27, reason="action change: the door bursts open and three masked men stand in the doorway (no weapons shown)", loc="office_dark",
         visual="the office door flung open: three tall dark silhouettes of men in black clothes and black face masks standing in the doorway, their empty hands holding only bright white flashlights whose beams cut through the dark room toward the viewer; nothing else in their hands",
         camera=f"medium wide shot from inside the room, low angle, the silhouettes in the upper two-thirds, {LOW} (dark floor)",
         amb="hospital_night", sens="violence",
         safe="armed attackers shown as masked silhouettes with flashlights only; the rifle-butt blow to Ashham's forehead is never shown (muffled thud only)"),
    dict(to=30, reason="character focus change: in the dark, Raniya and Habeeb pressed against the wall as flashlight beams sweep",
         chars=["raniya", "habeeb"], loc="office_dark",
         visual=f"{H} and {R} pressed against the wall side by side in the dark office, not touching, a small gap between them, Raniya's hands clasped tightly at her own chest, both staring in fear toward the door; a white flashlight beam sweeping across the wall above their heads",
         camera=f"medium shot, eye level, {LOW} (dark floor)", amb="hospital_night", sens="violence",
         safe="Ashham falling and being held by the collar are never shown; Raniya 'gripping Habeeb's arm' is shown as her standing close beside him with her hands at her own chest (bible rule 8)"),
    dict(to=33, reason="action change: Ashham's eyes adjust to the dark and fix on the heavy metal file holder", chars=["ashham"], loc="office_dark",
         visual=f"close-up of {A} crouched low beside the desk in the dark, his intense eyes fixed on a heavy metal file holder standing on the desk edge, a flashlight beam glancing across his tense face; his hands empty",
         camera=f"close-up, low angle, {LOW} (dark desk side)", amb="hospital_night", sens="violence",
         safe="the strike with the file holder, the dropped gun and the tackle are never shown; only Ashham's focused face before he moves, muffled thuds offscreen"),
    dict(to=35, reason="scene change: Habeeb and Raniya flee down the dark corridor; dust bursts from the wall behind them",
         chars=["habeeb", "raniya"], loc="corridor_dark",
         visual=f"{H} and {R} running side by side down the dark hospital corridor toward the viewer, not touching, faces full of fear; behind them small bursts of grey cement dust and sparks puff from the corridor wall in a flashlight beam; nobody is hit",
         camera=f"medium wide shot, eye level, down the corridor, {LOW} (polished floor)", amb="hospital_corridor", hum=True,
         sens="violence", safe="gunfire shown only as dust and sparks bursting from the wall far behind them; Habeeb 'pulling Raniya by the hand' shown as running side by side"),
    dict(to=38, reason="action change: Ashham follows out the back door; the three vanish into the rainy island lanes",
         loc="hospital_garden",
         visual="seen from behind: three running figures slipping through the rainy back garden of the hospital away from the lit back door toward the dark island lanes - a tall man in a dark-grey shirt, a slim young man in a grey jacket with glasses, and a slim woman in a white coat and navy hijab - side by side with gaps between them, not touching; rain glittering in the light",
         camera=f"wide shot from behind, eye level, {LOW} (wet sandy path)", amb="rain_night",
         sens="violence", safe="Ashham overpowering the attackers and taking their ammunition is never shown; only the escape from behind"),
    # ---------------- OLD JETTY
    dict(to=40, reason="scene change: at the abandoned jetty on the west shore they stop, breathless; Raniya soaked and trembling",
         chars=["raniya", "ashham", "habeeb"], loc="old_jetty",
         visual=f"{RW}, standing on the old wet jetty planks trembling, arms wrapped around herself, frightened; {AD} a few steps away scanning the dark shoreline; {H} bent over catching his breath, hands on his knees; clear gaps between them, rain falling",
         camera=f"medium wide shot, eye level, {LOW} (dark wet planks and black water)", amb="rain_night"),
    dict(to=43, reason="action change: they pull the hidden fibreglass dinghy out of the bushes; Habeeb climbs in with his laptop",
         chars=["ashham", "habeeb", "raniya"], loc="old_jetty",
         visual=f"{AD} dragging a small white fibreglass dinghy with a small outboard engine out of the dark bushes into the shallow black water; {H} stepping into it clutching his laptop bag; {RW} standing a few steps away on the shore pointing toward the bushes; rain",
         camera=f"medium wide shot, eye level, {LOW} (black shallow water)", amb="rain_night"),
    dict(to=48, reason="action change: under black clouds Ashham starts the outboard; Raniya grips the side as they head out into big waves",
         chars=["ashham", "raniya", "habeeb"], loc="old_jetty",
         visual=f"the small white fibreglass dinghy beside the old jetty in rough black water. At the bow: {RW} - she wears NO white coat and NO lab coat at all, only the dark wet dusty-blue dress - gripping the dinghy's side with both hands, determined but afraid. In the middle {H} looking up anxiously at huge black storm clouds. At the stern {AD} pulling the outboard engine's starter cord. Gaps between them",
         camera=f"medium wide shot, eye level, {LOW} (choppy black water)", amb="rain_night"),
    # ---------------- STORM CROSSING
    dict(to=51, reason="scene change: the storm at full force; huge waves over the dinghy, Habeeb bailing water",
         chars=["habeeb", "ashham", "raniya"], loc="storm_sea",
         visual=f"the tiny dinghy climbing a towering black wave, white spray exploding over it; {H} bailing water with a plastic scoop, a waterproof bag strapped to his chest; {AD} at the outboard tiller squinting into the spray; {RW} crouched low gripping the side; lightning in the black clouds",
         camera=f"medium wide shot, slightly low angle, {LOW} (dark foaming water)", amb="storm_night", hum=True),
    dict(to=54, reason="action change: a powerful searchlight sweeps toward them; Ashham looks back at two fast launches",
         chars=["ashham"], loc="storm_sea",
         visual=f"{AD} sitting low inside the small white fibreglass dinghy, the dinghy's white hull and gunwale clearly visible around him, one hand resting on the long arm of the small outboard engine mounted on the stern beside him, twisting to look back over his shoulder, drenched, his face lit hard white by a powerful searchlight beam coming across the black waves from two dark fast launches in the distance behind; spray in the air",
         camera=f"medium close-up, eye level, {LOW} (black water)", amb="storm_night"),
    dict(to=57, reason="action change: the criminals' launches close in; spray bursts around the little dinghy (no gunfire shown)",
         loc="storm_sea",
         visual="wide view of the stormy black sea at night: two large dark fast launches with no markings racing through the waves, a blinding white searchlight beam pinning a tiny dinghy ahead of them, small white plumes of spray bursting from the water around the dinghy; lightning",
         camera=f"wide shot, high angle, the launches and searchlight in the upper two-thirds, {LOW} (black foaming sea)",
         amb="storm_night", hum=True, sens="violence", safe="gunfire shown only as spray plumes on the water; no weapons, nobody hit"),
    dict(to=61, reason="emotional turning point: Ashham targets the searchlight; it bursts and the sea goes dark",
         loc="storm_sea",
         visual="seen from behind: the dark silhouette of a broad-shouldered man in a dark shirt standing braced in the stern of a small dinghy, one arm raised toward the launch behind, his hand not visible against the glare; the big searchlight on the launch's bow bursting in a shower of white-orange sparks and glass fragments, the beam dying; a huge wave rising between the boats",
         camera=f"medium wide shot from behind the man, low angle, {LOW} (black water)", amb="storm_night",
         sens="violence", safe="Ashham's shot is shown only as his raised arm in silhouette from behind and the searchlight bursting into sparks; no gun visible"),
    # ---------------- KANDU-HUTTAA
    dict(to=65, reason="scene change: through the reef channel; the engine smokes and dies; they climb onto Kandu-huttaa's beach exhausted",
         chars=["raniya", "ashham", "habeeb"], loc="kandu_beach",
         visual=f"the small dinghy beached on white sand, thin grey smoke rising from its stalled outboard engine; {AD} stepping onto the sand, exhausted; {H} climbing out with his bag; {RW} standing on the beach a few steps apart, staring with dread at the pitch-black jungle; clear gaps between them",
         camera=f"medium wide shot, eye level, the jungle and figures in the upper two-thirds, {LOW} (white sand)", amb="beach_night"),
    dict(to=68, reason="action change: Habeeb checks his laptop - a jammer from the bunker blocks all messages",
         chars=["habeeb", "ashham", "raniya"], loc="kandu_beach",
         visual=f"{H} kneeling on the sand with his open laptop on his knees, the screen angled away from the viewer, its faint blue glow lighting his worried face and glasses; {AD} standing beside him looking toward the jungle, decisive; {RW} a little behind Ashham, hands at her chest",
         camera=f"medium shot, eye level, {LOW} (white sand)", amb="beach_night"),
    dict(to=72, reason="scene change: through the jungle they find the bunker's steel door, guarded by two men",
         chars=["ashham"], loc="kandu_jungle",
         visual=f"{AD} crouched in the dark bushes in the foreground, seen from behind and to the side, watching; beyond the leaves the heavy rusted steel hatch-door in its low concrete block, two guards in black clothes and black face masks standing before it holding only flashlights, beams sweeping the ground",
         camera=f"medium wide shot over Ashham's shoulder, eye level, {LOW} (dark undergrowth)", amb="jungle_night",
         sens="violence", safe="armed guards shown with flashlights only"),
    dict(to=75, reason="action change: the guards are gone; Ashham calls the others to the door", chars=["ashham"], loc="kandu_jungle",
         visual=f"the bunker's steel hatch-door with nobody guarding it; a dropped flashlight lying in the grass casting its beam across the ground; {AD} standing at the door alone, breathing hard, beckoning urgently with one empty hand toward the bushes",
         camera=f"medium wide shot, eye level, {LOW} (dark grass)", amb="jungle_night",
         sens="violence", safe="Ashham taking down both guards is never shown; only the empty doorway and the dropped flashlight afterwards; nobody on the ground"),
    dict(to=76, reason="detail: Raniya's trembling finger types the code on the keypad", chars=["raniya"], loc="kandu_jungle",
         visual=f"close-up of {RW}, her face tense in profile, her trembling finger reaching toward a small electronic keypad panel beside the steel door, its blank keys glowing soft green with no numbers or symbols",
         camera=f"close-up, eye level, {LOW} (concrete surface)", amb="jungle_night"),
    dict(to=77, reason="action change: the steel door groans open; cold chemical air pours out",
         chars=["ashham", "raniya", "habeeb"], loc="kandu_jungle",
         visual=f"the heavy steel hatch-door swinging open, cold pale mist spilling out from a dark stairway leading down under a faint cold fluorescent glow; {AD} at the edge peering down, alert; {H} and {RW} behind him at a distance, frightened faces lit by the cold light",
         camera=f"medium wide shot, eye level, {LOW} (dark ground)", amb="jungle_night", hum=True),
    dict(to=79, reason="scene change: they shut themselves in as the criminals' big launch roars into the lagoon",
         loc="kandu_lagoon",
         visual="a large dark launch with no markings roaring into the black lagoon of the deserted island, a powerful white searchlight sweeping across the water toward the dark jungle; no people visible",
         camera=f"wide shot from the jungle edge, eye level, the launch and searchlight in the upper two-thirds, {LOW} (black water)",
         amb="beach_night", hum=True),
]


def V(k, to, **o):
    """A beat that keeps the v1 image of old beat_k (old visual/camera/chars/loc/amb/sens/safe kept as documentation)."""
    d = dict(_V1[k - 1]); d.pop("to", None); d.pop("hum", None)
    d.update(to=to, v1=f"beat_{k:03d}"); d.update(o); return d


def RU(new_id, base, to, **o):
    """In-episode reuse of the image already shown by beat `new_id` (NEW numbering)."""
    d = dict(base); d.pop("v1", None); d.pop("hum", None)
    d.update(to=to, reuse=new_id); d.update(o); return d


# ---- NEW v2 images (spec 5.4 speaker framing + one outfit fix)
N_RAN_DESK = dict(reason="5.4 dialogue: Raniya speaks ('Who are you? Get out!') - in the v1 image she stands at the far left edge; new image framed on her",
    chars=["raniya", "ashham", "habeeb"], loc="raniya_office", speaker="raniya",
    visual=f"{R} half-rising from the chair behind her desk with stacked files and a lit desk lamp, startled and frightened, speaking sharply, one hand raised in front of her, her face clearly visible and centred in the frame; in the soft blurred foreground at the lower left and lower right edges the backs of the shoulders of {A} and {H} standing near the door, out of focus; a wide gap between her and the men",
    camera=f"medium close-up over the two men's shoulders, eye level, Raniya centred in the upper half and sharp, {LOW} (desk top)",
    amb="hospital_room")
N_RAN_CHAIR = dict(reason="5.4 dialogue: Raniya, sunk into her chair in tears, speaks ('You... you know everything?', 'They killed Naail...') - the v1 image hid her face in her hands",
    chars=["raniya"], loc="raniya_office", speaker="raniya",
    visual=f"{R} sunk into the chair behind her desk, her legs given way, tears running down her cheeks, looking up with a broken, pleading face, lips parted as she speaks, her hands resting limp on the files, her face clearly visible and centred; the warm desk lamp beside her, the dark rainy window behind her soft",
    camera=f"medium close-up, eye level, Raniya centred in the upper half and sharp, {LOW} (desk top with files)",
    amb="hospital_room", transition="cut")
N_HAB_OFFICE = dict(reason="5.4 dialogue: Habeeb answers ('Yes, we have Naail's call recording') - in the v1 image he is at the right edge looking down; reverse shot over Raniya's shoulder",
    chars=["habeeb", "raniya"], loc="raniya_office", speaker="habeeb",
    visual=f"{H} standing on the other side of the desk, leaning slightly forward, speaking gently and seriously, his face clearly visible, centred and in sharp focus in the warm lamp light; in the soft blurred foreground at the lower edge the navy hijab and white-coated shoulder of Dr. Raniya seen from behind as she sits at the desk; nobody else in the frame",
    camera=f"medium close-up over Raniya's shoulder (reverse shot), eye level, Habeeb centred in the upper half, {LOW} (desk top)",
    amb="hospital_room", transition="cut")
N_ASH_LEAN = dict(reason="5.4 dialogue: Ashham leans forward and asks who the mastermind in Malé is - the v1 close-up shows only the back of his head; reverse shot",
    chars=["ashham", "raniya"], loc="raniya_office", speaker="ashham",
    visual=f"{A} leaning forward across the desk toward the viewer, both hands flat on the desk, asking an urgent question, intense eyes, his face clearly visible, centred and sharp in the warm lamp light; in the soft blurred foreground at the lower edge the navy hijab and white-coated shoulder of Dr. Raniya seen from behind; rain on the dark window behind him",
    camera=f"medium close-up over Raniya's shoulder (reverse shot), eye level, Ashham centred in the upper half, {LOW} (desk top)",
    amb="hospital_room", transition="cut")
N_HAB_DARK = dict(reason="5.4 dialogue: in the blackout Habeeb cries out that the backup power is cut too - in the v1 dark-office image he is a profile at the left edge",
    chars=["habeeb", "raniya"], loc="office_dark", speaker="habeeb",
    visual=f"the office in sudden total darkness: {H} by the rain-streaked window, turning toward the viewer in alarm and calling out, his face lit by the faint cold light from the window, clearly visible, centred and sharp, glasses glinting; behind him in the dark, soft and out of focus, Dr. Raniya in her white coat and navy hijab pressed back against a filing cabinet, hands clasped at her own chest",
    camera=f"medium close-up, eye level, Habeeb centred in the upper half, {LOW} (dark floor)",
    amb="hospital_night", transition="cut")
N_ASH_DOOR = dict(reason="5.4 dialogue: Ashham, holding the door shut, shouts 'Habeeb, open the window!' - in the v1 image he is at the right edge",
    chars=["ashham"], loc="office_dark", speaker="ashham",
    visual=f"{A} braced with his shoulder against the closed wooden door of the dark office, one hand gripping the door handle, turning his head toward the viewer and shouting an order, his face clearly visible in a thin cold light, centred and sharp; thin white lines of flashlight light glowing under the door; his other hand open and empty",
    camera=f"medium close-up, eye level, Ashham centred in the upper half, {LOW} (dark floor)",
    amb="hospital_night", transition="cut")
N_RAN_JETTY = dict(reason="5.4 dialogue: at the jetty Raniya speaks at length (what now, the hidden dinghy, her father) - in the v1 jetty image she stands at the far left edge",
    chars=["raniya", "ashham", "habeeb"], loc="old_jetty", speaker="raniya",
    visual=f"{RW} standing on the old wet jetty in the rain, trembling, arms wrapped around herself, speaking in panic, her frightened face clearly visible, centred and in sharp focus; behind her, soft and out of focus at a distance on both sides, {AD} scanning the shoreline and {H} catching his breath; clear gaps between her and the men; rain, black water",
    camera=f"medium close-up, eye level, Raniya centred in the upper half, {LOW} (dark wet planks)",
    amb="rain_night", transition="cut")
N_DINGHY = dict(reason="action change: they drag the hidden dinghy into the sea (v2 fix: the v1 image showed Raniya still wearing her white doctor's coat after the escape)",
    chars=["ashham", "habeeb", "raniya"], loc="old_jetty",
    visual=f"{AD} and {H} dragging a small white fibreglass dinghy with a small outboard engine out of the dark bushes into the shallow black water beside the old jetty; {RW} - she wears NO white coat and NO lab coat at all, only the soaked dark dusty-blue dress and the navy hijab - standing a few steps apart on the shore pointing toward the bushes; rain; clear gaps between her and the men",
    camera=f"medium wide shot, eye level, {LOW} (black shallow water)", amb="rain_night")
N_ASH_HELM = dict(reason="5.4 dialogue: Ashham decides 'No time - Kandu-huttaa' and asks Raniya for the code while starting the engine - in the v1 dinghy image he is at the left edge",
    chars=["ashham", "habeeb", "raniya"], loc="old_jetty", speaker="ashham",
    visual=f"{AD} sitting at the stern of the small white fibreglass dinghy beside the old jetty, one hand on the small outboard engine, looking toward the viewer and speaking firmly, decisive, his face clearly visible, centred and sharp; in the soft blurred foreground the backs of Habeeb (grey zip jacket) and Raniya (navy hijab, dusty-blue dress, no white coat) sitting in the dinghy, out of focus, apart from each other; huge black storm clouds above, choppy black water, rain",
    camera=f"medium close-up from the bow (reverse shot), eye level, Ashham centred in the upper half, {LOW} (choppy black water)",
    amb="rain_night", transition="cut")
N_RAN_DINGHY = dict(reason="5.4 dialogue: in the dinghy Raniya speaks ('armed guards inside', later 'They've seen us!') - in the v1 boat images she is at the right edge",
    chars=["raniya"], loc="storm_sea", speaker="raniya",
    visual=f"{RW} crouched low in the small white fibreglass dinghy, gripping its side with both hands, drenched by spray, speaking out in fear toward the viewer, her face clearly visible, centred and sharp; behind her, soft, black waves with white crests and dark storm clouds",
    camera=f"medium close-up, eye level, Raniya centred in the upper half, {LOW} (dark foaming water)",
    amb="rain_night", transition="cut")
N_RAN_BEACH = dict(reason="5.4 dialogue: on the beach Raniya says 'We've only reached the field of death... under this island is hell' - in the v1 beach image she is a small figure at the right edge",
    chars=["raniya"], loc="kandu_beach", speaker="raniya",
    visual=f"{RW} standing on the white sand beach at night, exhausted and soaked, looking at the pitch-black jungle and speaking in a low, dread-filled voice, her face clearly visible in three-quarter view, centred and sharp; behind her the dense black jungle of screwpine and palms; the beached dinghy small and soft in the background",
    camera=f"medium close-up, eye level, Raniya centred in the upper half, {LOW} (white sand)",
    amb="beach_night")
N_ASH_BUSH = dict(reason="5.4 dialogue: crouched in the bushes Ashham whispers 'They're guarding the bunker... Habeeb, wait here with Raniya' - in the v1 image he is seen from behind",
    chars=["ashham", "habeeb", "raniya"], loc="kandu_jungle", speaker="ashham",
    visual=f"{AD} crouched in the dark bushes, turned toward the viewer, whispering an instruction, one open empty hand raised flat in a 'wait here' gesture, his face clearly visible in faint moonlight, centred and sharp; in the soft blurred foreground at the lower edges the backs of the heads of Habeeb (glasses, dark-grey zip jacket) and Raniya (navy hijab and a soaked dark dusty-blue dress - she wears NO white coat, nothing white at all) crouching, out of focus, apart from each other; far behind him through the leaves the faint white glow of two flashlights near the bunker door",
    camera=f"medium close-up (reverse shot), eye level, Ashham centred in the upper half, {LOW} (dark undergrowth)",
    amb="jungle_night", transition="cut")

BEATS = [
    V(1, 2),                                                             # beat_001 cargo boat deck
    V(2, 7),                                                             # beat_002 cabin: Habeeb (3-4), Ashham (5-6) by crop
    V(3, 10),                                                            # beat_003 next night, lane to hospital (black)
    V(4, 11),                                                            # beat_004 knock ('Come in' = unseen voice)
    dict(N_RAN_DESK, to=13),                                             # beat_005 NEW Raniya: 'Who are you?'
    V(5, 16, transition="cut"),                                          # beat_006 Ashham shows card (crop on Ashham)
    dict(N_RAN_CHAIR, to=17),                                            # beat_007 NEW Raniya in tears
    dict(N_HAB_OFFICE, to=18),                                           # beat_008 NEW Habeeb: the recording
    RU("beat_007", N_RAN_CHAIR, 20, transition="cut"),                    # beat_009 Raniya: 'They killed Naail'
    V(7, 24),                                                            # beat_010 Raniya explains the lab (crop on her)
    dict(N_ASH_LEAN, to=25),                                             # beat_011 NEW Ashham asks; lights out
    dict(N_HAB_DARK, to=26),                                             # beat_012 NEW Habeeb: backup cut
    V(8, 27),                                                            # beat_013 boots in the corridor
    dict(N_ASH_DOOR, to=28),                                             # beat_014 NEW Ashham: 'open the window!'
    V(9, 30, transition="cut"),                                          # beat_015 masked men in the doorway
    V(10, 32),                                                           # beat_016 Raniya and Habeeb at the wall
    RU("beat_015", _V1[8], 33, transition="cut",
      reason="5.4 dialogue: the masked man in front orders Ashham to move - return to the masked figures, centred on the middle one (identity hidden)"),
    V(11, 37),                                                           # beat_018 Ashham spots the file holder; 'Habeeb, out!'
    V(12, 39),                                                           # beat_019 corridor run
    V(13, 42),                                                           # beat_020 back garden
    V(14, 43),                                                           # beat_021 jetty arrival
    dict(N_RAN_JETTY, to=47),                                            # beat_022 NEW Raniya speaks at the jetty
    dict(N_DINGHY, to=48),                                               # beat_023 NEW (fix) dragging the dinghy
    V(16, 50),                                                           # beat_024 Habeeb: dangerous trip (crop on him)
    dict(N_ASH_HELM, to=53),                                             # beat_025 NEW Ashham at the helm
    dict(N_RAN_DINGHY, to=54),                                           # beat_026 NEW Raniya in the dinghy
    RU("beat_024", _V1[15], 55, transition="cut",
      reason="return: the dinghy heads out of the lagoon into the waves"),
    V(17, 58, hum=None),                                                 # beat_028 storm; Habeeb: 'a launch!'
    V(18, 59),                                                           # beat_029 Ashham looks back at the searchlight
    RU("beat_026", N_RAN_DINGHY, 60, amb="storm_night", transition="cut",
      reason="5.4 dialogue: Raniya screams 'They've seen us!' - return to her framing"),
    RU("beat_029", _V1[17], 61, transition="cut",
      reason="5.4 dialogue: Ashham shouts 'Zayaan! Hold on!' and swings the helm - return to his framing"),
    V(19, 62),                                                           # beat_032 launches, spray
    RU("beat_028", _V1[16], 63, transition="cut",
      reason="5.4 dialogue: Habeeb shouts 'Sir, we're going to die!' - return to the storm dinghy framed on him"),
    V(20, 67),                                                           # beat_034 searchlight shot out
    V(21, 69),                                                           # beat_035 beached dinghy
    dict(N_RAN_BEACH, to=71),                                            # beat_036 NEW Raniya: 'field of death'
    V(22, 75),                                                           # beat_037 laptop: Ashham / Habeeb by crop
    V(23, 76),                                                           # beat_038 bunker door with two guards
    dict(N_ASH_BUSH, to=78),                                             # beat_039 NEW Ashham whispers the plan
    RU("beat_038", _V1[22], 79, transition="cut",
      reason="return: the stone is thrown, a guard goes to look"),
    V(24, 82),                                                           # beat_041 guards gone; 'Come quickly!'
    V(25, 83),                                                           # beat_042 keypad
    V(26, 85),                                                           # beat_043 the door opens; 'only the beginning'
    V(27, 87),                                                           # beat_044 launch enters the lagoon
]
for _b in BEATS:
    _b.pop("hum", None)

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# focus points [x%, y%] read off work/grid (v1 sheets for v1 images, grid/new for the new ones)
sh(1, "In the dim light of dawn, Ashham and Habeeb were aboard a cargo boat that had left Malé's north harbour.",
   [("boat_engine", "ބޯޓެއްގެ", -20)])
sh(2, "This boat carries goods to the southern atolls. Because the boat's captain was an old friend of Ashham's, they boarded as secret passengers.")
sh(3, "Habeeb sat using his satellite modem to follow Dr. Raniya's movements. Sir, Raniya is on duty at the hospital right now.",
   [("keyboard_typing", "މޮޑެމް", -24)], speaker="habeeb", crop="tight", focus=[30, 44])
sh(4, "Her phone's location shows she's there. But there are lots of calls from unknown numbers around her too.",
   [("phone_buzz", "ކޯލްތަކެއް", -24)], speaker="habeeb", crop="tight", focus=[30, 44])
sh(5, "Those are their guards. Ashham looked out of the small window. Raniya is",
   speaker="ashham", crop="tight", focus=[59, 35])
sh(6, "inside a locked cage. Unless she's rescued, there's no way to learn the truth.",
   speaker="ashham", crop="tight", focus=[59, 35])
sh(7, "The rest of the voyage passed in silence. Yet both of them knew that behind that silence lay the secret of a great storm.",
   [("thunder", "ތޫފާނެއްގެ", -22)], hum=True)
sh(8, "Reaching the island. The next night at nine o'clock, the boat came alongside Villingili harbour in Gaafu Alifu.",
   [("boat_engine", "ކައިރިކުރި", -22)])
sh(9, "The island's harbour lay under a few dim lamps. Dressed like ordinary people, Ashham and Habeeb got off the boat and walked through the dark lanes toward the hospital.",
   [("footsteps_sand", "ހިނގާފައި", -22)])
sh(10, "The island's hospital is a two-storey building. At that hour the hospital was very quiet. Entering through the emergency door, Ashham headed toward the doctors' rooms.",
   [("door_open", "ވަދެ", -22)])
sh(11, "While Habeeb kept watch, Ashham went and knocked on the door of the room bearing Dr. Raniya's name. Come in.",
   [("knock", "ޓަކިޖަހާލި", -16)])
sh(12, "A woman's voice came from inside. Ashham went in, shut the door and locked it. Raniya sat at her desk looking through files.",
   [("door_close", "ލައްޕާ", -20), ("lock_click", "ތަޅުލި", -20)])
sh(13, "As she raised her head and looked up, she saw two strangers in front of her and took fright. Who are you? Get out of here!",
   [("gasp", "ބިރުގަތް", -22)], speaker="raniya")
sh(14, "Dr. Raniya, stay calm. Raniya stood up. Ashham showed her his police card.",
   speaker="ashham", crop="tight", focus=[69, 35])
sh(15, "I'm Ashham, from police Serious Crimes. We came about Naail's death.",
   speaker="ashham", crop="tight", focus=[69, 35])
sh(16, "And to save your father. At the names of Naail and her father, tears rolled from Raniya's eyes.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True, speaker="ashham", crop="tight", focus=[69, 35])
sh(17, "Her legs gave way and she sank onto the chair. You... you know everything?",
   [("cloth_rustle", "ތިރިވެވުނު", -24)], hum=True, speaker="raniya")
sh(18, "Yes, we have the recording of Naail's phone call, Habeeb said. Raniya put her hands over her face and began to cry.",
   [("sob_breath", "ރޯން", -22)], hum=True, speaker="habeeb")
sh(19, "They've killed Naail. I told him", speaker="raniya")
sh(20, "not to get into this. They're not people with any mercy. Locked in.", speaker="raniya")
sh(21, "Once she had calmed down, Raniya began to talk. On Kandu-huttaa there is a secret lab of a foreign pharmaceutical company.",
   speaker="raniya", crop="medium", focus=[40, 42])
sh(22, "What they're making there is a new master drug. To test that drug, they use",
   speaker="raniya", crop="tight", focus=[40, 35])
sh(23, "foreigners smuggled secretly into the Maldives. There's a huge amount of human trafficking in this.",
   speaker="raniya", crop="medium", focus=[42, 42])
sh(24, "Naail found out because their shipments came in through his father's company. Who's the mastermind in Malé?",
   speaker="raniya", crop="tight", focus=[40, 35])
sh(25, "Ashham asked, leaning forward. Just as Raniya opened her mouth to say something, suddenly every light in the hospital went out.",
   [("power_down", "ނިވުނު", -16)], hum=True, speaker="ashham")
sh(26, "The whole place sank into darkness. Sir! The backup power's been cut too! Habeeb said in alarm.",
   [("breath_heavy", "ހާސްވެފައި", -24)], speaker="habeeb")
sh(27, "At that moment, from the corridor came the sound of heavy boots and of guns being loaded. They were coming into the hospital.",
   [("boots_march", "ބޫޓުތަކެއްގެ", -18), ("lock_click", "ލޯޑްކުރާ", -22)], hum=True)
sh(28, "They're here! Raniya screamed in fear. Habeeb, open the window! We have to get out of here!",
   [("gasp", "ހަޅޭއްލަވައިގަތް", -18)], speaker="ashham")
sh(29, "Ashham said, holding the door shut. At that moment the door was flung open with a loud bang, and three armed men in black masks came in.",
   [("door_slam", "ހުޅުވާލާފައި", -14)], hum=True)
sh(30, "The butt of one man's gun struck Ashham on the forehead. Escaping the hospital attack.",
   [("soft_thud", "ޖެހި", -23)])
sh(31, "In the pitch darkness that filled the room, Ashham fell. One of the men in black masks held him by the collar.",
   [("cloth_rustle", "ހިފެހެއްޓި", -22)])
sh(32, "The man's breathing could be heard close by. Raniya was next to Habeeb. In fear she gripped Habeeb's arm tightly. Move,",
   [("breath_heavy", "ނޭވާގެ", -20)])
sh(33, "forward, without a sound! the criminal in front ordered Ashham in a heavy voice.",
   speaker="masked_man", crop="tight", focus=[31, 35])
sh(34, "Ashham is an experienced officer who has faced many dangerous situations like this.")
sh(35, "As his eyes got used to the dark, he spotted the heavy metal file holder on the desk. Suddenly, without any warning, Ashham ducked down and swung the holder at the head of the man in front.",
   [("heartbeat", "ފާހަގަކުރި", -20), ("soft_thud", "ވީއްލާލި", -22)], hum=True)
sh(36, "With that, the gun slipped from his hand and fell to the floor. Habeeb! Get out the door!",
   [("metal_clang", "ވެއްޓުނު", -22)], speaker="ashham", crop="tight", focus=[54, 35])
sh(37, "Ashham shouted, and grabbing the second man hard round the body, brought him to the floor.",
   [("soft_thud", "ވައްޓާލި", -24)])
sh(38, "Habeeb took Raniya by the hand and ran out of the room's door. At that moment the third man started firing after them. Tishun...",
   [("footsteps_pavement", "ދުއްވައިގަތް", -20)], hum=True)
sh(39, "Tishun - the bullets hit the corridor wall. Cement crumbled off the hospital wall. Screams and crying echoed from all over.",
   [("crash_clatter", "ބުރައިގެން", -22)])
sh(40, "Lying on the floor, Ashham turned their own guns on them and brought two of them down. The third man lay unconscious from the hard blow to his head.")
sh(41, "Taking the rounds left in their guns, Ashham ran after Habeeb and the others and came out through the hospital's back door.",
   [("door_open", "ދޮރުން", -20)])
sh(42, "They came out through the hospital's back garden and vanished into the island's dark lanes. It was still raining.",
   [("rain_start", "ވާރޭ", -18)])
sh(43, "When they reached the abandoned old jetty on the island's west shore, they were all out of breath.",
   [("breath_heavy", "މާނޭވާލެވިފައި", -18)])
sh(44, "Raniya's clothes were soaked. She was trembling with fear. What do we do now? They'll search the whole island for us.",
   [("breath", "ތުރުތުރު", -22)], speaker="raniya")
sh(45, "Raniya said in a voice full of panic. There should be a small dinghy I hid here.", speaker="raniya")
sh(46, "It's something I got ready so I could escape from the island. I tried to escape so many times.", speaker="raniya")
sh(47, "But with my father in their hands, and scared of what they'd do, I never dared. Raniya said slowly.", speaker="raniya")
sh(48, "They pulled out a small fibreglass dinghy hidden among the bushes and put it in the sea. It had a small outboard engine.",
   [("leaves_rustle", "ގަސްތަކުގެ", -18), ("splash", "މޫދަށް", -18)])
sh(49, "Habeeb got into it at once, trying to keep his laptop safe. Sir, this is going to be a very dangerous trip. The sea is really rough.",
   speaker="habeeb", crop="tight", focus=[44, 39])
sh(50, "The only option we have is to go to another island near here. Zayaan said, looking up at the sky.",
   speaker="habeeb", crop="medium", focus=[44, 42])
sh(51, "Black clouds covered the whole sky. No, there's no time. We have to go to Kandu-huttaa.",
   [("wind_gust", "ކަޅުވިލާތަކުން", -18)], speaker="ashham")
sh(52, "If we can get there and into that bunker, we'll learn all their secrets. Ashham said, starting the dinghy's engine.",
   [("boat_engine", "ސްޓާޓްކޮށްލަމުން", -16)], speaker="ashham")
sh(53, "Raniya, do you have the bunker code? Yes, it's on my phone. But", speaker="ashham")
sh(54, "there'll be armed guards inside. Raniya said, gripping the side of the dinghy.", speaker="raniya")
sh(55, "The dinghy left the island's lagoon and headed into the sea's huge waves. Storm at sea.",
   [("wave_crash", "ރާޅުތަކުގެ", -18)])
sh(56, "As soon as they were out on the open sea, the storm showed its real strength. Huge waves like mountains kept crashing down on the dinghy.",
   [("wind_howl", "ތޫފާނުގެ", -18), ("wave_crash", "ރާޅުތައް", -14)], hum=True)
sh(57, "The salt spray made it hard even to open their eyes. Habeeb sat bailing water out of the dinghy. His laptop was in its waterproof bag,",
   [("splash", "ދިޔަހިއްކަން", -20)])
sh(58, "wrapped in another plastic bag, hung round his neck and strapped to his body. Sir! A big launch is coming from the other side!",
   [("engine_rev", "ލޯންޗެއް", -18)], speaker="habeeb", crop="tight", focus=[33, 35])
sh(59, "Habeeb shouted. Ashham looked back. In the distance, the light of a powerful searchlight was coming toward them over the sea spray.")
sh(60, "It was the criminals' two powerful launches. Their speed was far greater. They've seen us! Raniya screamed in fear.",
   [("engine_rev", "ލޯންޗު", -16)], speaker="raniya")
sh(61, "Zayaan! Hold on! Ashham swung the dinghy's helm and drove it into the waves. From the launch behind, they started firing.",
   [("wave_crash", "ރާޅުތަކުގެ", -16)], speaker="ashham", crop="tight", focus=[34, 35])
sh(62, "The bullets hit the sea spray with a pop, pop. Because the waves were so strong, they kept losing their aim. Even so, they kept getting closer.",
   [("splash", "ޕޮޕް", -22)], hum=True)
sh(63, "It was as if the big launch would come and ram the dinghy's side and smash it to pieces. Sir, we're going to die!",
   [("engine_rev", "ލޯންޗު", -14)], hum=True, speaker="habeeb", crop="tight", focus=[33, 35])
sh(64, "Habeeb shouted. Ashham took the gun he had seized at the hospital and aimed behind. But taking aim on such heavy waves was impossible.",
   [("heartbeat", "އަމާޒުކުރި", -20)])
sh(65, "After a moment's thought, he switched his aim to the big searchlight on the front of the launch. Bang!",
   [("soft_thud", "ބޭންގް", -22)], hum=True)
sh(66, "With a single round the searchlight burst, and the whole area went dark again. At that moment a huge wave came and crashed between the two launches.",
   [("glass_break", "ގޮވައި", -14), ("wave_crash", "ރާޅެއް", -14)])
sh(67, "With that, the criminals' launch was pushed far away. By then they were almost at Kandu-huttaa. Seizing the chance, Ashham steered the dinghy in through a narrow channel near the island's reef.",
   [("engine_rev", "ލޯންޗު", -22), ("wave_crash", "ފަރުކައިރީގައި", -20)])
sh(68, "A small hope. Entering Kandu-huttaa's lagoon, things calmed down. But smoke started to rise from the dinghy's engine.",
   [("steam_hiss", "ދުން", -20)])
sh(69, "Water got into the engine and it stopped completely. The dinghy drifted slowly onto the island's white sand. The three got off the dinghy and climbed onto the beach.",
   [("power_down", "ހުއްޓުނީ", -22), ("footsteps_sand", "އެރި", -18)])
sh(70, "They were utterly exhausted and worn out. We've only just reached the field of death.", speaker="raniya")
sh(71, "Under this island's ground is hell. Raniya said, looking at the pitch-dark trees around them.",
   [("leaves_rustle", "ގަސްތަކަށް", -22)], hum=True, speaker="raniya")
sh(72, "Habeeb, is your equipment working? Ashham asked. Zayaan took out his laptop and opened it. The battery was at fifteen percent.",
   [("computer_beep", "ހުޅުވާލި", -22)], speaker="ashham", crop="tight", focus=[63, 35])
sh(73, "Sir, there's a satellite signal. But because of a jammer coming from this island's bunker, no message can be sent to Malé.",
   speaker="habeeb", crop="tight", focus=[41, 44])
sh(74, "We have to get inside the bunker and switch off the main switch. Let's go. Raniya, you stay behind me.",
   speaker="habeeb", crop="medium", focus=[42, 44])
sh(75, "Walk without making a sound. Ashham said. They moved forward through the trees to find the big concrete bunker door Ashham had seen before.",
   [("leaves_rustle", "ގަސްތަކުގެ", -20)], speaker="ashham", crop="tight", focus=[63, 35])
sh(76, "At the bunker's door. Searching through the thick trees, they found that heavy steel door.",
   [("leaves_rustle", "ގަސްތަކުގެ", -22)])
sh(77, "This time two guards with weapons stood beside the door. They were very alert. They're guarding the bunker.",
   hum=True, speaker="ashham")
sh(78, "I have to take those two out. Habeeb, you wait here with Raniya.", speaker="ashham")
sh(79, "Ashham said quietly. Ashham picked up a big stone from the ground and threw it far off. Thud! At the sound of the stone, one guard went to look.",
   [("soft_thud", "ތްލަޑް", -18), ("footsteps_sand", "ދިޔަ", -22)])
sh(80, "Ashham came up from behind, clamped one hand over his mouth and nose, wrapped the other arm round his chest, brought him down and knocked him out.",
   [("soft_thud", "ވައްޓާލައި", -24)])
sh(81, "With that, just as the other guard, startled, raised his gun, Ashham ran at him, kicked him in the chest and brought him to the ground.")
sh(82, "After a short struggle both guards were down on the ground. Come quickly! Ashham called. Raniya and Zayaan ran to the door.",
   [("footsteps_sand", "ދުވެފައި", -18)], speaker="ashham", crop="tight", focus=[33, 35])
sh(83, "With her trembling hand, Raniya began typing the secret code into the bunker's electronic keypad. Four... eight...",
   [("computer_beep", "ކީޕޭޑްގައި", -20)], hum=True)
sh(84, "Nine... one... zero... Beep! With a loud noise the steel door began to open.",
   [("computer_beep", "ބީޕް", -14), ("metal_door", "ހުޅުވެން", -14)])
sh(85, "Out came cold air carrying a chemical smell. This is only the beginning, be careful. Let's go in.",
   [("wind_gust", "ވައިރޯޅިއެއް", -22)], speaker="ashham", crop="tight", focus=[55, 35])
sh(86, "Ashham said. As they went into the bunker and shut the door, the sound of a big launch entering the island's lagoon was heard outside.",
   [("metal_door", "ލެއްޕުމާއެކު", -14), ("engine_rev", "ލޯންޗެއް", -16)])
sh(87, "The criminals' main group had come to the island. Ashham and the others were now locked inside the bunker. To be continued.",
   [("heartbeat", "ބަންދުވެފަ", -18)], hum=True)
# 5.4 framing on the NEW v2 images (focus read off work/grid/new_##.jpg after generation)
FOC = {13: ("medium", [45, 42]),                       # beat_005 Raniya: 'Who are you?'
       17: ("medium", [46, 42]),                       # beat_007 Raniya in tears
       18: ("medium", [47, 42]),                       # beat_008 Habeeb
       19: ("tight", [46, 35]), 20: ("medium", [46, 42]),          # beat_009 = beat_007
       25: ("medium", [47, 42]),                       # beat_011 Ashham leans in
       26: ("medium", [36, 42]),                       # beat_012 Habeeb in the dark
       28: ("medium", [56, 42]),                       # beat_014 Ashham at the door
       44: ("medium", [46, 42]), 45: ("tight", [46, 35]), 46: ("medium", [46, 42]), 47: ("tight", [46, 35]),  # beat_022
       51: ("medium", [46, 42]), 52: ("tight", [46, 35]), 53: ("medium", [46, 42]),  # beat_025 Ashham at the helm
       54: ("medium", [45, 42]), 60: ("tight", [45, 35]),          # beat_026 / beat_030 Raniya in the dinghy
       70: ("medium", [46, 42]), 71: ("tight", [46, 35]),          # beat_036 Raniya on the beach
       77: ("medium", [45, 42]), 78: ("tight", [45, 35])}          # beat_039 Ashham whispers
for _i, (_c, _f) in FOC.items():
    S[_i][2].update(crop=_c, focus=_f)
SHOTS = S
