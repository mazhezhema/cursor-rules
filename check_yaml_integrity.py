import os, yaml

bad_files = []
for root, dirs, files in os.walk("anchor"):
    for file in files:
        if file.endswith(".yaml"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    yaml.safe_load(f)
            except Exception as e:
                bad_files.append((path, str(e)))

if bad_files:
    print("❌ 以下 YAML 有语法问题：")
    for path, err in bad_files:
        print(f"- {path}: {err}")
else:
    print("✅ 所有 YAML 文件语法正确，无损坏。")
