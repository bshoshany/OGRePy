r"""
# OGRePy: An Object-Oriented General Relativity Package for Python
v1.2.0 (2024-09-15)

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

Based on the Mathematica package [OGRe](https://github.com/bshoshany/OGRe) by Barak Shoshany.

Copyright (c) 2024 [Barak Shoshany](https://baraksh.com/). Licensed under the [MIT license](https://github.com/bshoshany/OGRePy/blob/master/LICENSE.txt).

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

import os
import pathlib
import re
import shutil
import subprocess
import sys
import time

from playwright.sync_api import Browser, Page, sync_playwright

source: str = "README.md"
target: str = "OGRePy_Documentation.ipynb"
docs_folder: str = "OGRePy/docs"


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


# Clean up the cache and docs folders.
print("Cleaning up cache and docs folders...")
remove_folder_if_exists("OGRePy/__pycache__", docs_folder)

# Recreate the docs folder.
print("Creating docs folder...")
pathlib.Path(docs_folder).mkdir()

# Set up the PYTHONPATH environment variable so that it can find OGRePy's local module folder.
os.environ["PYTHONPATH"] = pathlib.Path.cwd().as_posix()

# Look for the virtual environment; if it doesn't exist, fall back to the global environment.
venv_path: pathlib.Path = pathlib.Path(".OGRePy-env/Scripts")
if not venv_path.exists():
    venv_path = pathlib.Path()


def execute(
    *args: str | pathlib.Path,
) -> None:
    """
    Execute the given command and measure its execution time.
    #### Parameters:
    * `args`: The arguments to pass to `subprocess.run()`.
    """
    start: float = time.perf_counter()
    try:
        _ = subprocess.run(args, check=True)
        print(f"Successfully completed in {time.perf_counter() - start:.2f} seconds.")
    except Exception as exc:
        print(f"Failed: {exc}.")
        sys.exit()


target_path: pathlib.Path = pathlib.Path(docs_folder).joinpath(target)

# Compile the notebook.
print("Compiling notebook...")
execute(venv_path.joinpath("jupytext"), source, "--to", "notebook", "--output", target_path)

# Execute the notebook in place.
print("Executing notebook...")
os.environ["OGREPY_DISABLE_UPDATE_CHECK"] = "True"
execute(venv_path.joinpath("jupyter"), "execute", target_path, "--inplace")

# Clean up the notebook.
print("Cleaning up notebook...")
to_cleanup: str = target_path.read_text(encoding="utf-8")
to_cleanup = re.sub(
    pattern=r"<!-- remove-after-compile -->(.*?)<!-- /remove-after-compile -->",
    repl="",
    string=to_cleanup,
    flags=re.DOTALL,
)
to_cleanup = re.sub(
    pattern=r'"Documentation: <a href=(.*?)</a>\*\*"',
    repl=r'"Documentation: <a href=\"https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.ipynb\">.ipynb</a>, <a href=\"https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.pdf\">.pdf</a>, <a href=\"https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.html\">.html</a>**"',
    string=to_cleanup,
    count=1,
    flags=re.DOTALL,
)
_ = target_path.write_text(to_cleanup, encoding="utf-8")

# Convert the notebook to HTML.
print("Converting notebook to HTML...")
execute(venv_path.joinpath("jupyter"), "nbconvert", target_path, "--to", "html", "--output", target.replace("ipynb", "html"), "--output-dir", docs_folder)

# Convert the HTML to PDF.
start_time: float = time.perf_counter()
print("Converting HTML to PDF...")
try:
    with sync_playwright() as p:
        # Launch the browser (generating a PDF with Playwright is currently only supported in Chromium).
        browser: Browser = p.chromium.launch()
        # Create a new page.
        page: Page = browser.new_page()
        # Load the HTML file.
        html: str = pathlib.Path(target_path.as_posix().replace("ipynb", "html")).read_text(encoding="utf-8")
        # Load the content into the page, injecting a CSS stylesheet to make the text justified.
        css = """
        <style>
            p, li { text-align: justify !important; }
        </style>
        """
        page.set_content(css + html)
        # Hide the In[] and Out[] prompts.
        page.evaluate('for (element of document.querySelectorAll(".jp-InputPrompt, .jp-OutputPrompt")) element.style.display = "none"')
        # Wait for MathJax to finish rendering. Note that nbconvert currently uses MathJax 2, so we need to use MathJax.Hub.Queue.
        page.evaluate("MathJax.Hub.Queue(() => { window.mathJaxDone = true; });")
        _ = page.wait_for_function("window.mathJaxDone === true")
        # Wait a few more seconds to ensure the math rendering is 100% complete.
        time.sleep(5)
        # Print the page to a PDF.
        _ = page.pdf(path=target_path.as_posix().replace("ipynb", "pdf"), print_background=True)
        # Close the browser.
        browser.close()
    print(f"Successfully completed in {time.perf_counter() - start_time:.2f} seconds.")
except Exception as exc:
    print(f"Failed: {exc}.")
    sys.exit()

# Clean up the cache folders.
print("Cleaning up cache folders...")
remove_folder_if_exists("OGRePy/__pycache__", docs_folder + "/.ipynb_checkpoints")

print("Done!")
