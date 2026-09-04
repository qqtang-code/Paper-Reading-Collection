"""End-to-end live check: every page + every referenced image on GitHub Pages."""
import re, urllib.request, urllib.parse

BASE = "https://qqtang-code.github.io/Paper-Reading-Collection"
PAGES = [
    "/",
    "/efficient-inference/declarative-attention/",
    "/efficient-inference/declarative-attention/Declarative-Attention论文精读_HTML.html",
    "/efficient-inference/declarative-attention/en.html",
    "/efficient-inference/freetoken/",
    "/efficient-inference/freetoken/en.html",
    "/efficient-inference/reset/",
    "/efficient-inference/reset/en.html",
    "/benchmarks/mmlongembed/",
    "/benchmarks/mmlongembed/en.html",
]

def get(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "verify/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, b""
        except Exception as e:  # transient TLS/network drops: retry
            last = e
    raise last

total, fail = 0, 0
for p in PAGES:
    url = BASE + urllib.parse.quote(p)
    code, body = get(url)
    total += 1
    if code != 200:
        fail += 1
        print(f"!! PAGE {code} {p}")
        continue
    imgs = sorted(set(re.findall(r'src="(figs/[^"]+)"', body.decode("utf-8", "ignore"))))
    d = p.rsplit("/", 1)[0] + "/" if p.endswith(".html") else p
    bad = []
    for im in imgs:
        try:
            icode, _ = get(BASE + urllib.parse.quote(d + im))
        except urllib.error.HTTPError as e:
            icode = e.code
        if icode != 200:
            bad.append((im, icode))
        total += 1
        fail += len(bad)
    print(f"OK  {code} {p:70s} imgs={len(imgs)} bad={len(bad)}")
    for im, ic in bad:
        print(f"    !! {im} -> {ic}")
print(f"=== TOTAL requests={total}, failures={fail} ===")
