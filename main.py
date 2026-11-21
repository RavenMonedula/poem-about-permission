import os

POEM = """The Cane

Can I hold it? I asked.
He put the cane in my hands.
Heavier than I thought —
oak, worn smooth by his palm.

I tapped it on the step.
He smiled. Now you know, he said,
how much of me it carries.

This morning he took my arm.
I carried the cane in my other hand."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
# Gate: entry.txt must be 1-280 Unicode characters, not only whitespace.
assert 1 <= len(POEM) <= 280 and POEM.strip(), "poem outside the 1-280 char gate"
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
