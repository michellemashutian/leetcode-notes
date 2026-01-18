import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "solutions" / "_template.py").read_text()

def main():
    if len(sys.argv) < 5:
        print("Usage: python scripts/new_problem.py <id> <slug> <category> <title>")
        return

    pid, slug, category, title = sys.argv[1:5]
    pid = pid.zfill(4)

    out_dir = ROOT / "solutions" / category
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{pid}_{slug.replace('-', '_')}.py"
    content = (
        TEMPLATE
        .replace("<ID>", pid)
        .replace("<Title>", title)
        .replace("<slug>", slug)
        .replace("<category>", category)
    )

    path = out_dir / filename
    path.write_text(content)
    print(f"Created {path}")

if __name__ == "__main__":
    main()

