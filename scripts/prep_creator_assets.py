#!/usr/bin/env python3
"""Normalize creator-shared PNGs into a small static gallery for Trainer Lab.

Input MUST be an archive fetched from the original artist's public resource link.
Does not handle, fetch, or republish the non-redistributable Ultimate packs.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path
from PIL import Image, ImageFile
Image.MAX_IMAGE_PIXELS = 12_000_000
ImageFile.LOAD_TRUNCATED_IMAGES = False

CATEGORIES = (
 ("hair", ("hair", "hairstyle", "bangs", "fringe", "ponytail")),
 ("body", ("body", "base", "skin", "boy", "girl", "male", "female")),
 ("tops", ("top", "shirt", "jacket", "coat", "uniform", "hoodie", "dress")),
 ("bottoms", ("pant", "short", "skirt", "bottom", "trouser")),
 ("shoes", ("shoes", "boots", "sneaker")),
 ("accessories", ("hat", "cap", "glasses", "bandana", "scarf", "accessory", "neck")),
 ("bags", ("bag", "backpack", "satchel")),
 ("trainer", ("trainer", "front", "back")),
 ("overworld", ("walk", "run", "bike", "overworld", "ow")),
)
def categorize(name):
 text = name.lower().replace("_", " ").replace("-", " ")
 for category, words in CATEGORIES:
  if any(re.search(r"\b"+re.escape(word)+r"\b",text) for word in words): return category
 return "other"

def main():
 if len(sys.argv) != 3: raise SystemExit("usage: prep_creator_assets.py EXTRACTED_DIR OUTPUT_DIR")
 src, dest = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
 if not src.is_dir(): raise SystemExit("No extracted pack directory")
 dest.mkdir(parents=True,exist_ok=True)
 results=[]
 seen=set()
 total_bytes=0
 for path in sorted(src.rglob("*")):
  if not path.is_file() or path.suffix.lower() not in (".png", ".gif", ".webp"): continue
  if path.stat().st_size>12_000_000: continue
  if len(results)>=3500:break
  try:
   with Image.open(path) as im:
    im.load()
    if not im.width or not im.height or im.width*im.height>12_000_000:continue
    converted=im.convert("RGBA")
    digest=hashlib.sha256(converted.tobytes()).hexdigest()
    if digest in seen:continue
    seen.add(digest)
    base=re.sub("[^a-z0-9-]+","-",path.stem.lower()).strip("-")[:55] or "sprite"
    category=categorize(str(path.relative_to(src)))
    filename=f"{category}/{base}-{digest[:12]}.png"
    out=dest/filename
    out.parent.mkdir(parents=True,exist_ok=True)
    converted.save(out,optimize=True)
    total_bytes+=out.stat().st_size
    if total_bytes>75_000_000:
     out.unlink(missing_ok=True); break
    results.append({
     "path":"assets/poltergeist/"+filename,"name":path.stem,
     "source_path":str(path.relative_to(src)).replace("\\","/"),
     "category":category,"width":converted.width,"height":converted.height,
     "source":"Coffee Cup / Poltergeist",
    })
  except (OSError,ValueError,Image.DecompressionBombError): continue
 if not results:raise SystemExit("Pack contained no usable PNG/GIF/WebP images; aborting publish.")
 manifest={"source_id":"poltergeist-gen4","source_name":"Character Customization Resources (Gen 4)",
           "creator":"Coffee Cup / Poltergeist",
           "source_url":"https://eeveeexpo.com/resources/317/",
           "usage":"Creator allows editing, use and sharing; underlying Pokémon-derived artwork subject to separate rights.",
           "count":len(results),"assets":results}
 (dest/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
 print("CREATOR_GALLERY_IMAGE_COUNT:",len(results))
 print("TOTAL_NORMALIZED_BYTES:",total_bytes)
 print("EXAMPLE_SOURCE_PATHS:")
 for entry in results[:24]:
  print(" - ",entry["source_path"],"→",entry["category"],entry["width"],"x",entry["height"])
 print("CATEGORY_COUNTS:", {c:sum(a["category"]==c for a in results) for c,_ in CATEGORIES})
if __name__=="__main__":main()
