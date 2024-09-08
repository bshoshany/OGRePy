r"""
# OGRePy: An Object-Oriented General Relativity Package for Python
v1.1.0 (2024-09-08)

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

Based on the Mathematica package [OGRe](https://github.com/bshoshany/OGRe) by Barak Shoshany.

Copyright (c) 2024 [Barak Shoshany](https://baraksh.com/). Licensed under the [MIT license](https://github.com/bshoshany/OGRePy/blob/master/LICENSE.txt).

If you use this package in published software or research, please provide a link to [the GitHub repository](https://github.com/bshoshany/OGRePy) in the source code and documentation.
"""

import pathlib
import shutil


def remove_folder_if_exists(
    *folders: str,
) -> None:
    """
    Remove the given folder, if it exists.
    #### Parameters:
    * `folders`: The paths of the folders to remove.
    """
    for folder in folders:
        if pathlib.Path(folder).exists():
            print(f"Removing folder {folder}...")
            shutil.rmtree(folder)


# Clean up the cache folders.
remove_folder_if_exists("OGRePy/__pycache__", "OGRePy/docs/.ipynb_checkpoints")
