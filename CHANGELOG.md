# OGRePy: An Object-Oriented General Relativity Package for Python

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

* [Version history](#version-history)
    * [v1.3.1 (2025-08-03)](#v131-2025-08-03)
    * [v1.3.0 (2025-02-04)](#v130-2025-02-04)
    * [v1.2.0 (2024-09-15)](#v120-2024-09-15)
    * [v1.1.0 (2024-09-08)](#v110-2024-09-08)
    * [v1.0.1 (2024-09-04)](#v101-2024-09-04)

## Version history

### v1.3.1 (2025-08-03)

* New features:
    * Introducing: [OGRePy Live](https://bshoshany.github.io/OGRePy/lab/index.html?path=OGRePy_Live.ipynb)! You can now run OGRePy directly in your browser - no installation needed, and you don't even need to have Python installed on your computer. See the documentation for details.
* Citing the package:
    * This package is now published in the Journal of Open Research Software! If you use this package in published research, please cite it as follows:
        * Barak Shoshany, *"OGRePy: An Object-Oriented General Relativity Package for Python"*, [Journal of Open Research Software 13: 9](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.558), [doi:10.5334/jors.558](https://doi.org/10.5334/jors.558), [arXiv:2409.03803](https://arxiv.org/abs/2409.03803) (July 2025)
    * The `CITATION.cff` and `CITATION.bib` files have been updated accordingly.
    * For your convenience, the citing information can always be obtained by executing the function `T.cite()`.

### v1.3.0 (2025-02-04)

* Just a small maintenance update; more substantial updates are coming soon.
* When cleaning up notation, OGRePy now turns derivatives with respect to the coordinates into partial derivatives of the form $\partial_{x^{n}}$ if the order $n$ of the derivative is higher than 1, similarly to the Mathematica package.
* If the documentation files cannot be found, the welcome message will now link to the files on the GitHub repository instead.
* Replaced the PowerShell script `update_packages.ps1` in the `tasks` folder with a Python script `update_packages.py`.

### v1.2.0 (2024-09-15)

* New features:
    * Tensor objects can now be compared using the `T.compare()` function. Two tensors are considered equal if their components are the same, and they are associated with the same metric.
    * OGRePy now correctly displays Markdown and TeX output in JupyterLite.
    * Tensor components in OGRePy are now **immutable**, meaning that they are specified once and for all and cannot be changed. This is done for consistency and simplicity. This means that `permute()` now returns a new tensor with its indices permuted instead of modifying the original tensor. Similarly, `simplify()` now returns a new tensor with its components simplified of simplifying the original tensor.
* Citing the package:
    * This package now has an [arXiv paper](https://arxiv.org/abs/2409.03803)! If you use this package in published research, please cite it as follows:
        * Barak Shoshany, *"OGRePy: An Object-Oriented General Relativity Package for Python"*, [doi:10.48550/arXiv.2409.03803](https://doi.org/10.48550/arXiv.2409.03803), [arXiv:2409.03803](https://arxiv.org/abs/2409.03803) (September 2024)
    * Added a `CITATION.cff` file (in YAML format) to the GitHub repository. This should add [an option to get a citation in different formats](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) directly from GitHub repository by clicking on "cite this repository" on the sidebar to the right.
    * Added a `CITATION.bib` file (in BibTeX format) to the GitHub repository. You can use it to easily cite this package in your papers.
    * For your convenience, the citing information can always be obtained by executing the function `T.cite()`.

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
