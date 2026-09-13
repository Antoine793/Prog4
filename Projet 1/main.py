import mistletoe
import re


# Couleurs acceptées par le programme
couleurs_valides = [
    "red", "blue", "green", "yellow", "orange",
    "purple", "pink", "black", "white",
    "gray", "grey", "brown",
    "lightblue", "lightgreen",
    "darkred", "darkblue"
]


# Vérifie si une couleur est valide
def couleur_valide(couleur):

    # Couleur normale comme "red" ou "blue"
    if couleur.lower() in couleurs_valides:
        return True

    # Code hexadecimal comme #FF0000
    if re.fullmatch(r"#[0-9a-fA-F]{6}", couleur):
        return True

    return False


# Applique la couleur et le surlignage
def ajouter_style(match):

    style = match.group(1)
    texte = match.group(2)

    couleur_texte = ""
    couleur_fond = ""

    # Couleur du texte + surlignage
    if ",=" in style:
        couleur_texte, couleur_fond = style.split(",=", 1)

    # Seulement le surlignage
    elif style.startswith("="):
        couleur_fond = style[1:]

    # Seulement la couleur du texte
    else:
        couleur_texte = style

    # Vérifie la couleur du texte
    if couleur_texte and not couleur_valide(couleur_texte):
        print(f"ERREUR : couleur '{couleur_texte}' non reconnue.")
        return texte

    # Vérifie la couleur du fond
    if couleur_fond and not couleur_valide(couleur_fond):
        print(f"ERREUR : couleur '{couleur_fond}' non reconnue.")
        return texte

    # Création du style HTML
    style_html = ""

    if couleur_texte:
        style_html += f"color: {couleur_texte}; "

    if couleur_fond:
        style_html += f"background-color: {couleur_fond}; "

    return f'<span style="{style_html}">{texte}</span>'


# Lire le fichier Markdown
with open("Test.md", "r", encoding="utf-8") as fichier:
    texte = fichier.read()


# Permet d'écrire un titre comme :
# {{red|# Mon titre}}
texte = re.sub(
    r'^\{\{([^|]+)\|(#{1,6})\s+(.+?)\}\}$',
    r'\2 {{\1|\3}}',
    texte,
    flags=re.MULTILINE
)


# Conserve les sauts de ligne entre deux textes stylés
texte = re.sub(
    r"\}\}\n(?=\{\{)",
    "}}  \n",
    texte
)


# Conversion Markdown vers HTML
html = mistletoe.markdown(texte)


# Remplace la syntaxe {{couleur|texte}}
html = re.sub(
    r"\{\{([^|]+)\|(.+?)\}\}",
    ajouter_style,
    html
)


# Création du document HTML complet
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


# Création du fichier HTML
with open("output.html", "w", encoding="utf-8") as fichier:
    fichier.write(html_final)


print("Le fichier HTML a été créé.")