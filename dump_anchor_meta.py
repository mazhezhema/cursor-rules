import os
import yaml
import json

ANCHOR_ROOT = "anchor"
dump = []

for root, _, files in os.walk(ANCHOR_ROOT):
    for f in files:
        if not f.endswith(".yaml"):
            continue
        path = os.path.join(root, f)
        try:
            with open(path, "r", encoding="utf-8") as fp:
                yml = yaml.safe_load(fp)
            dump.append({
                "file_path": path,
                "id": f.replace(".yaml", ""),
                "type": os.path.relpath(root, ANCHOR_ROOT),
                "title": yml.get("title", ""),
                "description": yml.get("description", "")
            })
        except Exception as e:
            dump.append({
                "file_path": path,
                "id": f.replace(".yaml", ""),
                "type": os.path.relpath(root, ANCHOR_ROOT),
                "error": str(e)
            })

with open("anchor_meta_dump.json", "w", encoding="utf-8") as out:
    json.dump(dump, out, indent=2, ensure_ascii=False)

print("✅ 已生成 anchor_meta_dump.json")
