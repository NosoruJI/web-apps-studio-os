from pathlib import Path

registry = Path("docs/REGISTRY.yaml")

if not registry.exists():

    print("REGISTRY.yaml not found")

    exit(1)

print("Registry Found")