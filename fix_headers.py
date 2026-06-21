import os

# Ordner, die wir patchen
folders = ["rrk", "en_rrk"]

# Neuer Header-Block für DE
header_de = """
    <a href="rrk-2-0.html">RRK 2.0</a>
    <a href="rrk-2-1.html">RRK 2.1</a>
    <a href="rrk-2-2.html">RRK 2.2</a>
    <a href="rrk-3-0.html">RRK 3.0</a>
    <a href="rrk-4-0.html">RRK 4.0</a>
    <a href="rrk-4-1.html">RRK 4.1</a>
    <a href="rrk-4-2.html">RRK 4.2</a>
    <a href="rrk-4-3.html">RRK 4.3</a>
    <a href="rrk-4-4.html">RRK 4.4</a>
    <a href="rrk-5-0.html">RRK 5.0</a>
    <a href="rrk-6-1.html">RRK 6.1</a>
    <a href="../rrk-evolution-de.html">RRK‑Evolution</a>
"""

# Neuer Header-Block für EN
header_en = """
    <a href="rrk-2-0-en.html">RRK 2.0</a>
    <a href="rrk-2-1-en.html">RRK 2.1</a>
    <a href="rrk-2-2-en.html">RRK 2.2</a>
    <a href="rrk-3-0-en.html">RRK 3.0</a>
    <a href="rrk-4-0-en.html">RRK 4.0</a>
    <a href="rrk-4-1-en.html">RRK 4.1</a>
    <a href="rrk-4-2-en.html">RRK 4.2</a>
    <a href="rrk-4-3-en.html">RRK 4.3</a>
    <a href="rrk-4-4-en.html">RRK 4.4</a>
    <a href="rrk-5-0-en.html">RRK 5.0</a>
    <a href="rrk-6-1-en.html">RRK 6.1</a>
    <a href="../rrk-evolution-en.html">RRK‑Evolution</a>
"""

for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            path = os.path.join(folder, filename)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Ersetze nur den <nav>-Block
            start = content.find("<nav")
            end = content.find("</nav>") + len("</nav>")

            if start == -1 or end == -1:
                print(f"⚠ Kein Header gefunden in {path}")
                continue

            old_nav = content[start:end]

            if folder == "rrk":
                new_nav = f"""
<nav class="nav">
    <img src="../rrk-logo.svg" alt="RRK Logo">
    {header_de}
</nav>
"""
            else:
                new_nav = f"""
<nav class="nav">
    <img src="../rrk-logo.svg" alt="RRK Logo">
    {header_en}
</nav>
"""

            new_content = content.replace(old_nav, new_nav)

            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"✔ Header aktualisiert: {path}")
