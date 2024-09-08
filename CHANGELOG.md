# OGRePy: An Object-Oriented General Relativity Package for Python

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

* [Version history](#version-history)
    * [v1.1.0 (2024-09-08)](#v110-2024-09-08)
    * [v1.0.1 (2024-09-04)](#v101-2024-09-04)

## Version history

### v1.1.0 (2024-09-08)

* Bug fixes:
    * Fixed a bug where tensor contraction failed when generating a symbol for the new tensor. See [#1](https://github.com/bshoshany/OGRePy/issues/1).
    * Fixed math in documentation (apparently Jupyter and GitHub have very different rules with regards to displaying math).
* New features:
    * The documentation is now available in HTML format ([`OGRePy_Documentation.html`](https://github.com/bshoshany/OGRePy/blob/master/docs/OGRePy_Documentation.html)) and PDF format ([`OGRePy_Documentation.pdf`](https://github.com/bshoshany/OGRePy/blob/master/docs/OGRePy_Documentation.pdf)) in addition to Jupyter Notebook format ([`OGRePy_Documentation.ipynb`](https://github.com/bshoshany/OGRePy/blob/master/docs/OGRePy_Documentation.ipynb)).
    * Added links to open the documentation in any of these three formats to the welcome message. Note that the documentation is bundled with the package, so this will work offline as well.
    * The welcome message can now be disabled either by defining `OGREPY_DISABLE_WELCOME = True` in the notebook or by setting the environment variable `OGREPY_DISABLE_WELCOME` to `True` (which allows you to disable it permanently). This must be done before importing the package.
    * The package now automatically checks for updates from [PyPI](https://pypi.org/project/OGRePy/) when it is imported. This can be disabled by defining `OGREPY_DISABLE_UPDATE_CHECK = True` in the notebook, or setting the environment variable `OGREPY_DISABLE_UPDATE_CHECK` to `True`, before importing the package. In that case, you can still check for updates manually if you wish, using `T.update_check()`. However, note that this check is performed asynchronously, so it does not increase the load time of the package, and you can continue working while the check is being performed. If the welcome message is disabled, the startup update check is performed in "quiet mode", meaning that it only notifies you if a new version is available, but not if you are running the latest version.
    * Changing the curve parameter now applies retroactively to any tensors previously calculated. Behind the scenes, the curve parameter is stored only as a placeholder, which is replaced dynamically with the user's chosen symbol when the components are displayed with `show()` or `list()` or extracted with `components()`.

### v1.0.1 (2024-09-04)

* Initial release.
* OGRePy is a Python port of my Mathematica package [OGRe](https://github.com/bshoshany/OGRe). Most features have already been fully ported, with a few remaining ones, such as importing/exporting tensors and parallelization, left for subsequent releases in the near future.
