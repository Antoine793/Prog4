import mistletoe

with open("test.md", "r", encoding="utf-8") as fichier:
    html = mistletoe.markdown(fichier)

print(html)