from __future__ import annotations

import ast
from pathlib import Path


def iter_python_files(root: Path):
    for path in root.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        yield path


def to_module_name(src_root: Path, path: Path) -> str:
    rel = path.relative_to(src_root)
    return "src." + ".".join(rel.with_suffix("").parts)


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    src_root = project_root / "src"

    modules: dict[str, Path] = {}
    for path in iter_python_files(src_root):
        mod = to_module_name(src_root, path)
        modules[mod] = path

    imported: set[str] = set()
    parse_errors: list[tuple[Path, Exception]] = []

    for mod, path in modules.items():
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except Exception as exc:
            parse_errors.append((path, exc))
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.name
                    if name.startswith("src."):
                        imported.add(name)
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.module.startswith("src."):
                    imported.add(node.module)

    exclusions: set[str] = {"src.__init__"}
    for mod in modules:
        if mod.endswith(".__init__"):
            exclusions.add(mod)

    candidates: list[tuple[str, Path]] = []
    for mod, path in modules.items():
        if mod in exclusions:
            continue
        if mod not in imported:
            candidates.append((mod, path))

    print(f"Parse errors: {len(parse_errors)}")
    for path, exc in parse_errors:
        print(f" - {path.relative_to(project_root)} :: {exc!r}")

    print(f"\nPossibly-dead modules (never imported): {len(candidates)}")
    for mod, path in sorted(candidates):
        print(f" - {mod} => {path.relative_to(project_root)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
