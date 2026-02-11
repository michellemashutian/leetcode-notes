from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SOL = ROOT / "solutions"

MAP = {
    "array_string": "__AS__",
    "two_pointers": "__TP__",
    "sliding_window": "__SW__",
    "matrix": "__MX__",
    "hashmap": "__HM__",
    "intervals": "__IN__",
    "stack": "__ST__",
    "linked_list": "__LL__",
    "binary_tree": "__BT__",
    "bst": "__BST__",
    "graph": "__GR__",
    "backtracking": "__BK__",
    "dp": "__DP__",
    "bit": "__BIT__",
    "voting_algorithm": "__VA__",
}

def count(folder):
    if not folder.exists():
        return 0
    return len([p for p in folder.glob("*.py") if p.name != "_template.py"])

def main():
    text = README.read_text()
    total = 0

    for k, token in MAP.items():
        c = count(SOL / k)
        total += c
        text = text.replace(token, str(c))

    text = text.replace("__TOTAL__", str(total))
    README.write_text(text)
    print("Stats updated.")

if __name__ == "__main__":
    main()

