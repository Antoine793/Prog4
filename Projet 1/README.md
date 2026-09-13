# Extension Markdown – Couleurs et surlignage

## Description

Ce projet permet d'ajouter des couleurs et du surlignage à un document Markdown à l'aide de Python et de la bibliothèque Mistletoe.

Le programme convertit le fichier `Test.md` en HTML et crée automatiquement un fichier `output.html` contenant le résultat.


## Fonctionnement

Pour changer la couleur d'un texte :

`{{red|Texte rouge}}`

Pour surligner un texte :

`{{=yellow|Texte surligné en jaune}}`

Pour combiner une couleur de texte et un surlignage :

`{{red,=yellow|Texte rouge surligné en jaune}}`

Il est aussi possible d'utiliser d'autres couleurs selon les besoins.


## Utilisation

1. Ouvrir le fichier `Test.md`.

2. Écrire le texte en Markdown en utilisant les raccourcis de couleur ou de surlignage.

3. Lancer le programme avec :

`python main.py`

4. Le programme convertit le Markdown avec Mistletoe et applique les couleurs demandées.

5. Ouvrir le fichier `output.html` pour voir le résultat final.


## Exemple

Dans `Test.md` :

`{{blue|Bonjour tout le monde}}`

Le programme produira un texte bleu dans le fichier HTML.


## Fichiers principaux

`main.py` : contient le programme Python.

`Test.md` : contient le document Markdown à convertir.

`output.html` : contient le résultat final de la conversion.