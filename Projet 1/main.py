import re
import mistletoe

with open("test.md", "r", encoding="utf-8") as fichier:
    html = mistletoe.markdown(fichier)
    
def ajouter_couleur(match):
    couleur = match.group(1)
    texte = match.group(2)

    return f'<span style="color: {couleur};">{texte}</span>'


html = re.sub(
    r"\{\{([a-zA-Z]+)\|(.+?)\}\}",
    ajouter_couleur,
    html
)

with open("output.html", "w", encoding="utf-8") as fichier:
    fichier.write(html)

print("Le fichier HTML a été créé.")