[![Author: Barak Shoshany](https://img.shields.io/badge/author-Barak_Shoshany-009933)](https://baraksh.com/)
[![DOI: 10.5334/jors.558](https://img.shields.io/badge/DOI-10.5334%2Fjors.558-b31b1b)](https://doi.org/10.5334/jors.558)
[![arXiv:2409.03803](https://img.shields.io/badge/arXiv-2409.03803-b31b1b)](https://arxiv.org/abs/2409.03803)
[![License: MIT](https://img.shields.io/github/license/bshoshany/OGRePy)](https://github.com/bshoshany/OGRePy/blob/master/LICENSE.txt)
[![Language: Python 3.14](https://img.shields.io/badge/Language-Python_3.14-yellow)](https://python.org/)
[![GitHub stars](https://img.shields.io/github/stars/bshoshany/OGRePy?style=flat&color=009999)](https://github.com/bshoshany/OGRePy/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bshoshany/OGRePy?style=flat&color=009999)](https://github.com/bshoshany/OGRePy/forks)
[![GitHub release](https://img.shields.io/github/v/release/bshoshany/OGRePy?color=660099)](https://github.com/bshoshany/OGRePy/releases)
[![PyPI - Version](https://img.shields.io/pypi/v/OGRePy)](https://pypi.org/project/OGRePy/)
[![Open in Visual Studio Code](https://img.shields.io/badge/Open_in_Visual_Studio_Code-007acc)](https://vscode.dev/github/bshoshany/OGRePy)

# OGRePy: An Object-Oriented General Relativity Package for Python

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPI project: <https://pypi.org/project/OGRePy/>

* [Version history](#version-history)
    * [v2.0.0 (2026-05-11)](#v200-2026-05-11)
    * [v1.3.1 (2025-08-03)](#v131-2025-08-03)
    * [v1.3.0 (2025-02-04)](#v130-2025-02-04)
    * [v1.2.0 (2024-09-15)](#v120-2024-09-15)
    * [v1.1.0 (2024-09-08)](#v110-2024-09-08)
    * [v1.0.1 (2024-09-04)](#v101-2024-09-04)

## Version history

### v2.0.0 (2026-05-11)

* This new version of OGRePy is released shortly after the [OGRe](https://github.com/bshoshany/OGRe) v2.0.0 release, and includes many of the new features, performance optimizations, and bug fixes from that release, as well as additional improvements specific to the Python version.
* New features:
    * `Metric.weyl()` can now be used to calculate the Weyl tensor.
    * `Metric.volume_element_squared()` has been renamed to `Metric.det()`, as this is a more accurate name for what the method actually calculates: the determinant of the metric, which may be negative for pseudo-Riemannian metrics.
    * `Metric.volume_element()` is a new method that calculates the actual volume element of a given metric in the form $\mathrm{d}V = \sqrt{|\det(g)|} \, {\mathrm{d}x}^{0} \wedge \cdots \wedge {\mathrm{d}x}^{n-1}$, where $n$ is the number of dimensions.
    * [OGRePy Live](https://bshoshany.github.io/OGRePy/lab/index.html?path=OGRePy_Live.ipynb) now includes a more helpful starting notebook with some coordinate systems and metrics pre-defined, as well as suggestions for things to try.
* Derivative shorthand notation:
    * Partial derivatives are now displayed correctly. Previously, a function with two partial derivatives, e.g. `f.diff(x, y)`, was incorrectly displayed by `list()` and `show()` as $\partial_{x}f$, ignoring any derivatives after the first one. Now, the same function is correctly displayed as $\partial_{x}\partial_{y}f$.
    * `list()` and `show()` now use a clearer shorthand notation for higher-order derivatives. Previously the shorthand for something like `f.diff(x, 2)` was $\partial_{x^2}f$, which was confusing, especially because it seems like the derivative is with respect to $x^2$, rather than a second derivative with respect to $x$. Now the shorthand for the same is $\partial_{x}^{2} f$, which more closely resembles familiar tensor notation.
    * The shorthand notation has been made clearer in cases where the derivative is raised to a power. Previously the shorthand for something like `f.diff(x)**2` was $\partial_{x} f^2$, which makes it look like the function itself is squared, instead of the derivative. Now the shorthand for the same is $(\partial_{x} f)^2$, which is much more clear.
    * The shorthand notation has also been improved in cases where the function is multiplied by its derivative. Previously, `f * f.diff(x)` was displayed as $\partial_{x} f f$, which is very confusing. Now the same is displayed as $f \partial_{x} f$.
* Geodesics:
    * Index transformations for the `GeodesicFromLagrangian` and `GeodesicFromChristoffel` classes now use the metric components evaluated along the curve, instead of the unmodified metric components.
    * The `GeodesicFromLagrangian` class now follows the Euler-Lagrange equations more rigorously: the defining representation now has a lower index, and the sign has been corrected.
    * The `GeodesicTimeParam` class now rejects index transformations, since these equations do not transform as a tensor.
    * The docstring for `geodesic_time_param()` now shows the correct formula and return value.
* Performance optimizations:
    * Christoffel symbols and Riemann tensors are now recalculated directly when requested in a new coordinate system, instead of transforming the existing components. This improves performance, both because coordinate transformations on rank 3 or 4 tensors are slow, and because the directly calculated components are easier to simplify.
    * All built-in tensors derived from a metric are now calculated directly from the component formulas instead of using overloaded tensor operators, avoiding the overhead.
    * Index transformations now raise or lower one index at a time, simplifying and caching intermediate representations for later reuse, as in OGRe; this is more efficient than performing the full transformation in one step. The transformations start from the closest cached index configuration to minimize the number of raising/lowering steps.
    * Coordinate and index transformations now use direct component contractions instead of full SymPy tensor products.
    * Coordinate and index transformations now use sparse matrices to skip zero transformation terms.
    * The constructor of the `Metric` class has been optimized; it now avoids calculating the determinant.
* Bug fixes:
    * Fixed a bug where the welcome message did not render correctly.
    * Fixed a bug where `permute()` failed for derived tensor classes, such as metrics and curvature tensors. `permute()` now always returns a generic `Tensor` instead of the original class.
    * Fixed a bug where `permute()` did not propagate the permuted index specification to the new tensor, which caused errors if it was used subsequently in calculations.
    * Fixed a bug where attempting to register a non-invertible coordinate transformation with `set_coord_transformation()` could leave the transformation state inconsistent.
    * Fixed a bug where adding tensors of rank 11 or higher produced incorrect results.
    * Fixed the type validation for the `syms()` function.
    * Fixed the default index letters (previously, $\epsilon$ appeared twice and $\eta$ was unused).
    * `T.compare(..., exact=True)` now uses exact comparison when comparing the associated metrics of the tensors. (Previously, the metrics were always compared using `exact=False`.)
    * Fixed various typos in the documentation.
* The package now has a comprehensive internal test suite which thoroughly tests all OGRePy functions, classes, and methods and verifies that it accurately reproduces a wide variety of known results from differential geometry and general relativity, ensuring users can fully trust OGRePy as a reliable tool for research and pedagogy. This is currently used only internally, but will eventually be made available on the GitHub repository, once it matures a bit more and is cleaned up and properly documented.

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
    * Tensor components in OGRePy are now **immutable**, meaning that they are specified once and for all and cannot be changed. This is done for consistency and simplicity. This means that `permute()` now returns a new tensor with its indices permuted instead of modifying the original tensor. Similarly, `simplify()` now returns a new tensor with its components simplified instead of simplifying the original tensor.
* Citing the package:
    * This package now has an [arXiv paper](https://arxiv.org/abs/2409.03803)! If you use this package in published research, please cite it as follows:
        * Barak Shoshany, *"OGRePy: An Object-Oriented General Relativity Package for Python"*, [doi:10.48550/arXiv.2409.03803](https://doi.org/10.48550/arXiv.2409.03803), [arXiv:2409.03803](https://arxiv.org/abs/2409.03803) (September 2024)
    * Added a `CITATION.cff` file (in YAML format) to the GitHub repository. This should add [an option to get a citation in different formats](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) directly from the GitHub repository by clicking on "cite this repository" on the sidebar to the right.
    * Added a `CITATION.bib` file (in BibTeX format) to the GitHub repository. You can use it to easily cite this package in your papers.
    * For your convenience, the citing information can always be obtained by executing the function `T.cite()`.

### v1.1.0 (2024-09-08)

* Bug fixes:
    * Fixed a bug where tensor contraction failed when generating a symbol for the new tensor. See [#1](https://github.com/bshoshany/OGRePy/issues/1).
    * Fixed math in documentation (apparently Jupyter and GitHub have very different rules with regard to displaying math).
* New features:
    * The documentation is now available in HTML format ([`OGRePy_Documentation.html`](https://github.com/bshoshany/OGRePy/blob/master/docs/OGRePy_Documentation.html)) and PDF format ([`OGRePy_Documentation.pdf`](https://github.com/bshoshany/OGRePy/blob/master/docs/OGRePy_Documentation.pdf)) in addition to Jupyter Notebook format ([`OGRePy_Documentation.ipynb`](https://github.com/bshoshany/OGRePy/blob/master/docs/OGRePy_Documentation.ipynb)).
    * Added links to open the documentation in any of these three formats to the welcome message. Note that the documentation is bundled with the package, so this will work offline as well.
    * The welcome message can now be disabled either by defining `OGREPY_DISABLE_WELCOME = True` in the notebook or by setting the environment variable `OGREPY_DISABLE_WELCOME` to `True` (which allows you to disable it permanently). This must be done before importing the package.
    * The package now automatically checks for updates from [PyPI](https://pypi.org/project/OGRePy/) when it is imported. This can be disabled by defining `OGREPY_DISABLE_UPDATE_CHECK = True` in the notebook, or setting the environment variable `OGREPY_DISABLE_UPDATE_CHECK` to `True`, before importing the package. In that case, you can still check for updates manually if you wish, using `T.update_check()`. However, note that this check is performed asynchronously, so it does not increase the load time of the package, and you can continue working while the check is being performed. If the welcome message is disabled, the startup update check is performed in "quiet mode", meaning that it only notifies you if a new version is available, but not if you are running the latest version.
    * Changing the curve parameter now applies retroactively to any tensors previously calculated. Behind the scenes, the curve parameter is stored only as a placeholder, which is replaced dynamically with the user's chosen symbol when the components are displayed with `show()` or `list()` or extracted with `components()`.

### v1.0.1 (2024-09-04)

* Initial release.
* OGRePy is a Python port of my Mathematica package [OGRe](https://github.com/bshoshany/OGRe). Most features have already been fully ported, with a few remaining ones, such as importing/exporting tensors and parallelization, left for subsequent releases in the near future.
