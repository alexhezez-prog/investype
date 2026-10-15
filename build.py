"""Construit index.html (GitHub Pages) et artifact.html (aperçu) à partir de src/page.html."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / "src/page.html").read_text(encoding="utf-8")
(root / "artifact.html").write_text(src, encoding="utf-8")
head_tags = re.findall(r'^(<(?:title|meta|link)[^\n]*)$', src, flags=re.M)
body = "\n".join(l for l in src.splitlines() if not re.match(r'^<(?:title|meta|link)', l)).strip()
head = "\n".join(['<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">', *head_tags])
html = f'<!doctype html>\n<html lang="fr">\n<head>\n{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n'
(root / "index.html").write_text(html, encoding="utf-8")
print("ok", len(html))
