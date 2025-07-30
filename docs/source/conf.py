# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Co-enseignement Python'
copyright = 'BTS LaSalle Avignon - 2025'
author = 'Thierry Vaira <thierry.vaira@gmail.com>'
version = '1.0'
release = '1.0.0'
master_doc = 'index'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['myst_parser']
extensions = [
    'sphinx.ext.githubpages',
    'myst_parser'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
#source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.vscode']

language = 'fr'

todo_include_todos = False

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

#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'
#html_theme = 'press'
#html_theme = 'python_docs_theme'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = "Co-enseignement en Python"
html_theme_options = {
   "pygments_light_style": "tango",
   "pygments_dark_style": "monokai",
    "show_toc_level": 3,
    "repository_url": "https://github.com/bts-lasalle-avignon-ressources/co-enseignement-python",
    #"path_to_docs": "{path-relative-to-site-root}",
    "use_repository_button": True,
    "use_source_button": True,
    "use_issues_button": True
}
# >>> from pygments.styles import get_all_styles
# >>> styles = list(get_all_styles())
# >>> print(styles)
# ['abap', 'algol', 'algol_nu', 'arduino', 'autumn', 'bw', 'borland', 'coffee', 'colorful', 'default', 'dracula', 'emacs', 'friendly_grayscale', 'friendly', 'fruity', 'github-dark', 'gruvbox-dark', 'gruvbox-light', 'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 'manni', 'material', 'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark', 'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 'trac', 'vim', 'vs', 'xcode', 'zenburn']
#pygments_style = 'tango'
#highlight_language = 'tango'
#pygments_style = 'sphinx'
