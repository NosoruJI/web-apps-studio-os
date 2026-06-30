from pathlib import Path

ROOT = Path("docs")

required = [
    "id:",
    "title:",
    "version:",
    "status:"
]

errors = []

for md in ROOT.rglob("*.md"):

    text = md.read_text(encoding="utf-8")

    for field in required:

        if field not in text:

            errors.append(f"{md} missing {field}")

if errors:

    print("Metadata Validation Failed")

    for e in errors:

        print(e)

    exit(1)

print("Metadata Validation Passed")