import os

ENTRY = "By accepting these Terms, you waive the right to your own reflection, which the Company may use in mirrors, puddles, and haunted houses."

# Gate self-check (1-200 chars, one sentence, no trailing newline).
# The clause is deadpan boilerplate until "haunted houses" — the joke
# comes from the register as much as from the words, per the judge brief.
assert 1 <= len(ENTRY) <= 200 and ENTRY == ENTRY.strip() and ENTRY.endswith(".")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/makefun-out")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
