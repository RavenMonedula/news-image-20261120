#!/usr/bin/env python3
"""news-image-20261120 entry: writes the front page to /output/entry.png.
The image is pre-rendered by draw_frontpage.py (PIL, no network); this
program just copies it to /output, deterministically."""
import os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(BASE, "entry.png"), "/output/entry.png")
print("wrote /output/entry.png")
