"""Sequential render queue: renders episodes listed (one per line) in <series_dir>/render_queue.txt, one at a time,
then runs qc.py. A line 'END' stops the runner once everything before it is done.
Usage: python render_queue.py <series_dir> <series_name>
"""
import os, subprocess, sys, time

series_dir, series = sys.argv[1], sys.argv[2]
Q = os.path.join(series_dir, "render_queue.txt")
here = os.path.dirname(os.path.abspath(__file__))
done = set()
env = dict(os.environ, PYTHONIOENCODING="utf-8", RENDER_WORKERS=os.environ.get("RENDER_WORKERS", "6"))
while True:
    items = [l.strip() for l in open(Q, encoding="utf-8")] if os.path.exists(Q) else []
    todo = [x for x in items if x and x != "END" and x not in done]
    if not todo:
        if "END" in items: break
        time.sleep(20); continue
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
