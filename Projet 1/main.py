import mistletoe
import re


# Fonction qui applique les couleurs et le surlignage
def ajouter_style(match):

    style = match.group(1)
    texte = match.group(2)

    couleur_texte = ""
    couleur_fond = ""

    # Si on trouve ",=", il y a une couleur de texte ET un surlignage
    if ",=" in style:
        couleur_texte, couleur_fond = style.split(",=", 1)

    # Si le style commence par "=", c'est seulement du surlignage
    elif style.startswith("="):
        couleur_fond = style[1:]

    # Sinon, c'est seulement la couleur du texte
    else:
        couleur_texte = style

    # Construction du style HTML
    style_html = ""

    if couleur_texte:
        style_html += f"color: {couleur_texte}; "

    if couleur_fond:
        style_html += f"background-color: {couleur_fond}; "

    return f'<span style="{style_html}">{texte}</span>'


# Ouvrir le fichier Markdown
with open("Test.md", "r", encoding="utf-8") as fichier:
    html = mistletoe.markdown(fichier)


# Chercher notre syntaxe spéciale dans le HTML
html = re.sub(
    r"\{\{([^|]+)\|(.+?)\}\}",
    ajouter_style,
    html
)


# Créer un document HTML complet
html_final = f"""<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Document Markdown</title>
</head>

<body>

{html}

</body>

</html>
"""


# Créer le fichier HTML final
with open("output.html", "w", encoding="utf-8") as fichier:
    fichier.write(html_final)


print("Le fichier HTML a été créé.")