r"""
# OGRePy: An Object-Oriented General Relativity Package for Python
v1.3.0 (2025-02-04)

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

* Barak Shoshany, *"OGRePy: An Object-Oriented General Relativity Package for Python"*, [doi:10.48550/arXiv.2409.03803](https://doi.org/10.48550/arXiv.2409.03803), [arXiv:2409.03803](https://arxiv.org/abs/2409.03803) (September 2024)

You can use the following BibTeX entry:

```bibtex
@article{Shoshany2024_OGRePy,
    archiveprefix = {arXiv},
    author        = {Barak Shoshany},
    doi           = {10.48550/arXiv.2409.03803},
    eprint        = {2409.03803},
    title         = {{OGRePy: An Object-Oriented General Relativity Package for Python}},
    year          = {2024}
}
```

If you found this project useful, please consider [starring it on GitHub](https://github.com/bshoshany/OGRePy/stargazers)! This allows me to see how many people are using my code, and motivates me to keep working to improve it.
"""

import json
import subprocess
import sys
from typing import TypedDict


class Package(TypedDict):
    """A class to store information about a package."""

    name: str
    version: str
    latest_version: str
    latest_filetype: str


def main() -> None:
    """Update the packages."""
    try:
        print("=== Updating pip... ===")
        _ = subprocess.run(args=[sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        print("=== Listing packages... ===")
        result: subprocess.CompletedProcess[str] = subprocess.run(
            args=[sys.executable, "-m", "pip", "list", "--outdated", "--format=json"],
            capture_output=True,
            text=True,
            check=True,
        )
        packages: list[Package] = json.loads(result.stdout)
        print(f"=== Found {'no' if len(packages) == 0 else len(packages)} outdated package{'s' if len(packages) != 1 else ''}. ===")
        for pkg in packages:
            print(f"=== Updating {pkg['name']}: {pkg['version']} -> {pkg['latest_version']} ({pkg['latest_filetype']})... ===")
            _ = subprocess.run(
                args=[sys.executable, "-m", "pip", "install", "--upgrade", pkg["name"]],
                check=True,
            )
        print("=== Done! ===")
    except Exception as exc:
        sys.exit(f"=== Error: {exc} ===")


if __name__ == "__main__":
    main()
