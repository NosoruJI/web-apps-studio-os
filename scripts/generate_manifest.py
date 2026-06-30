from pathlib import Path

docs = Path("docs")

count = 0

for _ in docs.rglob("*"):

    count += 1

print(f"Repository contains {count} files")