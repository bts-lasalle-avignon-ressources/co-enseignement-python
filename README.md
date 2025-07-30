# Co-enseignement en Python

Accès : [https://bts-lasalle-avignon-ressources.github.io/co-enseignement-python/](https://bts-lasalle-avignon-ressources.github.io/co-enseignement-python/README.html)

> Le fichier source est au format Markdown [./docs/source/README.md](./docs/source/README.md). La documentation HTML a été générée avec [Sphinx](https://www.sphinx-doc.org/) et le thème [Book](https://sphinx-themes.org/sample-sites/sphinx-book-theme/).

---

## Générer un site HTML avec Sphinx sur GitHub Pages

[Sphinx](https://www.sphinx-doc.org/) est un générateur de documentation libre. Il s'appuie sur des fichiers au format [reStructuredText](https://fr.wikipedia.org/wiki/ReStructuredText) ou [Markdown](https://fr.wikipedia.org/wiki/Markdown) qu'il convertit en **HTML**, PDF, [EPUB](https://fr.wikipedia.org/wiki/EPUB), ou [man](https://fr.wikipedia.org/wiki/Man_(Unix)). Il supporte aussi l'autogénération à partir du code source.

> Il a été développé par Georg Brandl pour la communauté Python en 2008. C'est le générateur de la documentation officielle des projets Python, Django et Selenium.
> Liste des thèmes : https://sphinx-themes.org/

Il est possible de déployer la documentation générée sur [GitHub Pages](https://pages.github.com/).

Installer [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html) :

```sh
$ pip install -U sphinx
```

Exécuter le script appelé `sphinx-quickstart` pour créer le répertoire source, le fichier de configuration `conf.py` et le document racine `index.rst` :

```sh
$ sphinx-quickstart docs
Bienvenue dans le kit de démarrage rapide de Sphinx 8.1.3.

Veuillez saisir des valeurs pour les paramètres suivants (tapez Entrée pour accepter la valeur par défaut, lorsque celle-ci est indiquée entre crochets).

Chemin racine sélectionné : docs

Vous avez deux options pour l'emplacement du répertoire de construction de la sortie de Sphinx.
Soit vous utilisez un répertoire "_build" dans le chemin racine, soit vous séparez les répertoires "source" et "build" dans le chemin racine.
> Séparer les répertoires source et de sortie (y/n) [n]: y

Le nom du projet apparaîtra à plusieurs endroits dans la documentation construite.
> Nom du projet: Co-enseignement Python
> Nom(s) de(s) l'auteur(s): Thierry VAIRA
> Version du projet []: 1.0

Si les documents doivent être rédigés dans une langue autre que l’anglais, vous pouvez sélectionner une langue ici grâce à son identifiant. Sphinx utilisera ensuite cette langue pour traduire les textes que lui-même génère.

Pour une liste des identifiants supportés, voir
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Langue du projet [en]: fr

...

Terminé : la structure initiale a été créée.
...
```

Les fichiers de base qui serviront à générer la documentation sont placés dans le répertoire [./docs/source/](./docs/source/). Ici, le contenu est défini par le document [./docs/source/README.md](./docs/source/README.md) qui est au format Markdown.

Le document racine [./docs/source/index.rst](./docs/source/index.rst) définit une table des matières (`toctree`) de profondeur (`maxdepth`) `3` et le document [./docs/source/README.md](./docs/source/README.md) comme contenu :

```rst
.. toctree::
   :maxdepth: 3

   README.md
```

Pour utiliser le format [Markdown](https://fr.wikipedia.org/wiki/Markdown) avec [Sphinx](https://www.sphinx-doc.org/fr/master/usage/markdown.html), il faut installer _MyST-Parser_ :

```sh
$ pip install --upgrade myst-parser
```

On va utiliser le [thème](https://sphinx-themes.org/) [Book](https://sphinx-themes.org/sample-sites/sphinx-book-theme/) qu'il faut installer :

```sh
$ pip install sphinx-book-theme
```

Le fichier de configuration [./docs/source/conf.py](./docs/source/conf.py) est ensuite modifié pour notamment séléctionner le thème et l'extension :

```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'Co-enseignement Python'
copyright = 'BTS LaSalle Avignon - 2025'
author = 'Thierry Vaira <thierry.vaira@gmail.com>'
version = '1.0'
release = '1.0.0'
language = 'fr'
master_doc = 'index'
todo_include_todos = False

extensions = [
    'sphinx.ext.githubpages',
    'myst_parser'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.vscode']

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = "Co-enseignement en Python"
html_theme_options = {
   "pygments_light_style": "tango",
   "pygments_dark_style": "monokai",
    "show_toc_level": 3,
    "repository_url": "https://github.com/bts-lasalle-avignon-ressources/co-enseignement-python",
    "use_repository_button": True,
    "use_source_button": True,
    "use_issues_button": True
}
```

Tester localement la génération HTML :

```sh
$ sphinx-build -M html docs/source/ docs/build/

# ou :
$ cd docs
$ make html
```

La documentation est générée dans le répertoire `docs/build/html/`.

Déployer sur [GitHub Pages](https://pages.github.com/) :

On va utiliser [GitHub Actions](https://github.com/features/actions) pour automatiser la génération de la documentation ansi que son déploiement.

On crée le fichier [.github/workflows/sphinx.yml](.github/workflows/sphinx.yml) :

```yml
name: "Documentation HTML Sphinx"

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Build HTML
        uses: sphinx-notes/pages@v3
        with:
          documentation_path: "docs/source"
          publish: false

      - run: mkdir -p docs/build/html/
      - run: cp -r /tmp/sphinxnotes-pages/* docs/build/html/

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: html-docs
          path: docs/build/html/

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/build/html
```

Si une modification (`push`) est effectuée sur la branche `main`, la documentation est générée dans `docs/build/html` puis transférée vers la branche `gh-pages`.

> Il est possible de préciser des paquets Python à installer dans le fichier [./docs/requirements.txt](./docs/requirements.txt).

Il faut activer GitHub Pages sur le dépôt. Pour cela, il faut aller dans `Settings` (Paramètres), puis `Pages` dans la barre latérale gauche. On choisit "_Deploy from a branch_" dans le menu déroulant « Source » puis on sélectionne la branche `gh-pages` et `/ (root)`. Il faut cliquer sur « Save » (Enregistrer).

Après quelques minutes, le site est disponible. Ici pour ce dépôt : [https://bts-lasalle-avignon-ressources.github.io/co-enseignement-python/](https://bts-lasalle-avignon-ressources.github.io/co-enseignement-python/README.html)

> Le fichier [test_theme_book.md](./test_theme_book.md) contient quelques exemples spéficiques au thème Book.

---
&#x1f12f; BTS LaSalle Avignon - 2025 - [Thierry Vaira](thierry.vaira@gmail.com)
