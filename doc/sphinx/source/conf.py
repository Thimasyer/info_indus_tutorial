# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Cours d'informatique industrielle avec ROS2!"
copyright = '2026, Eyer Thomas'
author = 'Eyer Thomas'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinx_design",
]
myst_enable_extensions = ["colon_fence"]
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = [".rst", ".md"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_sidebars = {
    "**": [
        "globaltoc.html",  # Use the global TOC instead of the local one
        "relations.html",  # Adds links to the previous and next chapters
        "searchbox.html",  # Adds a search box
    ]
}


# -- Options for copybutton extension ----------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

html_static_path = ['_static']

html_css_files = [

    "css/custom.css",

]


# -- Custom prolog

rst_prolog = """
.. role:: text-bold-black-on-red
   :class: text-bold-black-on-red

.. |br| raw:: html
        <br>
"""