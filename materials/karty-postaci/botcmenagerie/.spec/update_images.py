import json
import os
from pathlib import Path

root = Path(r"c:\projects\games\BOTC-materials---Krew-na-wiezy-zegarowej\materials\karty-postaci\botcmenagerie")
assets_dir = root / "assets"

asset_files = [p for p in assets_dir.iterdir() if p.is_file()]
asset_map = {}
for p in asset_files:
    name = p.stem
    key = name.replace("_", "").lower()
    asset_map[key] = p.name

updated_files = []
matched_assets = set()
processed_jsons = 0

for json_path in root.rglob("*.json"):
    if assets_dir in json_path.parents:
        continue
    if json_path.parent.name == ".spec":
        continue

    processed_jsons += 1
    data = json.loads(json_path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        continue
    if "id" not in data or "image" not in data:
        continue

    asset_key = data["id"].replace("_", "").lower()
    if asset_key not in asset_map:
        continue

    original_file = asset_map[asset_key]
    url = (
        f"https://github.com/czaurus/BOTC-materials---Krew-na-wiezy-zegarowej/blob/master/"
        f"materials/karty-postaci/botcmenagerie/assets/{original_file}"
    )
    new_image = [url]

    if data["image"] != new_image:
        data["image"] = new_image
        json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        updated_files.append(str(json_path.relative_to(root)))

    matched_assets.add(asset_key)

unmatched_assets = [filename for key, filename in asset_map.items() if key not in matched_assets]
report = {
    "asset_count": len(asset_files),
    "processed_json_files": processed_jsons,
    "updated_json_files": len(updated_files),
    "updated_files": updated_files,
    "unmatched_assets": unmatched_assets,
}
print(json.dumps(report, indent=2, ensure_ascii=False))
