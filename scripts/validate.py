"""Simple repository checks. Runs in CI on every pull request and locally: python scripts/validate.py"""
import json
import pathlib
import py_compile
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP = {".git", "node_modules", ".venv"}
FORBIDDEN = [".env", "*.pem", "*.csv", "*.parquet", "local.settings.json"]
SECRET_PATTERNS = {
    "storage account key": re.compile(r"AccountKey=[A-Za-z0-9+/=]{20,}"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "hard-coded password": re.compile(r"(?i)\bpassword\s*=\s*['\"][^'\"]{4,}['\"]"),
}
failures = []


def files():
    for path in ROOT.rglob("*"):
        if path.is_file() and not (set(path.relative_to(ROOT).parts) & SKIP):
            yield path


def fail(path, message):
    failures.append(f"{path.relative_to(ROOT)}: {message}")


for path in files():
    if any(path.match(pattern) for pattern in FORBIDDEN):
        fail(path, "file type must not be committed (see .gitignore)")

    if path.name.endswith((".json", ".platform")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            fail(path, f"invalid JSON ({error})")

    if path.suffix == ".ipynb":
        for cell in json.loads(path.read_text(encoding="utf-8")).get("cells", []):
            if cell.get("outputs"):
                fail(path, "notebook has saved outputs; clear them before committing")
                break

    if path.suffix == ".py":
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as error:
            fail(path, f"does not compile ({error.msg.strip()})")

    if path.suffix in {".py", ".sql", ".json", ".md", ".yml", ".yaml", ".txt", ".ipynb"} and path.name != "validate.py":
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(path, f"possible {label}")

if failures:
    print("Checks failed:")
    for line in failures:
        print(f"  - {line}")
    sys.exit(1)

print("All checks passed.")
