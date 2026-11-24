#!/usr/bin/env python3
"""Write the deterministic editorial image required by the make.fun harness."""
from pathlib import Path
import os
import shutil

ROOT = Path(__file__).resolve().parent
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = ROOT / "entry.png"
TARGET = OUTPUT / "entry.png"

if not SOURCE.is_file():
    raise FileNotFoundError(f"missing image asset: {SOURCE}")
OUTPUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)
