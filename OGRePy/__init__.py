r"""
# OGRePy: An Object-Oriented General Relativity Package for Python
v1.3.1 (2025-08-03)

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

Based on the Mathematica package [OGRe](https://github.com/bshoshany/OGRe) by Barak Shoshany.

Copyright (c) 2025 [Barak Shoshany](https://baraksh.com/). Licensed under the [MIT license](https://github.com/bshoshany/OGRePy/blob/master/LICENSE.txt).

If you use this package in software of any kind, please provide a link to [the GitHub repository](https://github.com/bshoshany/OGRePy) in the source code and documentation.

If you use this package in published research, please cite it as follows:

* Barak Shoshany, *"OGRePy: An Object-Oriented General Relativity Package for Python"*, [Journal of Open Research Software 13: 9](https://openresearchsoftware.metajnl.com/articles/10.5334/jors.558), [doi:10.5334/jors.558](https://doi.org/10.5334/jors.558), [arXiv:2409.03803](https://arxiv.org/abs/2409.03803) (July 2025)

You can use the following BibTeX entry:

```bibtex
@article{ShoshanyOGRePy,
    archiveprefix = {arXiv},
    author        = {Barak Shoshany},
    doi           = {10.5334/jors.558},
    eprint        = {2409.03803},
    issn          = {2049-9647},
    journal       = {Journal of Open Research Software},
    pages         = {9},
    publisher     = {Ubiquity Press, Ltd.},
    title         = {{OGRePy: An Object-Oriented General Relativity Package for Python}},
    volume        = {13},
    year          = {2025},
}
```

If you found this project useful, please consider [starring it on GitHub](https://github.com/bshoshany/OGRePy/stargazers)! This allows me to see how many people are using my code, and motivates me to keep working to improve it.
"""

# Import SymPy (for convenience, so we don't have to import it to the notebook separately).
import sympy as s

# Import all public OGRePy objects.
from ._core import Coordinates, CovariantD, Metric, OGRePyError, PartialD, Tensor, __version__, calc, cite, compare, diag, doc, func, info, options, release_date, sym, syms, update_check, welcome

# The names that will be exported if using `from OGRePy import *`. Contains exactly all the names imported above.
__all__: list[str] = ["Coordinates", "CovariantD", "Metric", "OGRePyError", "PartialD", "Tensor", "__version__", "calc", "cite", "compare", "diag", "doc", "func", "info", "options", "release_date", "s", "sym", "syms", "update_check", "welcome"]
