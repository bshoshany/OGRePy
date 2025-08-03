<#
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
#>

$TempFolder = '.jupyterlite'
$OutFolder = 'JupyterLite'

# Activate the virtual environment.
& .OGRePy-env\Scripts\Activate.ps1

# Clean up any previous builds.
if (Test-Path $TempFolder)
{
    Remove-Item $TempFolder -Recurse -Force
}
New-Item $TempFolder -ItemType 'Directory'
if (Test-Path $OutFolder)
{
    Remove-Item $OutFolder -Recurse -Force
}
New-Item $OutFolder -ItemType 'Directory'

# Create a wheel for the package in the JupyterLite directory and clean up build files.
python -m build --wheel --outdir $TempFolder/pypi
Remove-Item build -Recurse -Force
Remove-Item OGRePy.egg-info -Recurse -Force

# Copy the settings overrides file to the JupyterLite directory.
Copy-Item OGRePyLive/overrides.json $TempFolder/

# Copy the demo notebook and docs to the JupyterLite directory. Anything under `files/` will be accessible in the JupyterLite site.
New-Item $TempFolder/files -ItemType 'Directory'
Copy-Item OGRePyLive/OGRePy_Live.ipynb $TempFolder/files/
Copy-Item OGRePy/docs/* $TempFolder/files/

# Build the JupyterLite site.
Set-Location $TempFolder
jupyter lite build --output-dir ../$OutFolder

# Remove the temporary folder.
Set-Location ../$OutFolder
Remove-Item ../$TempFolder -Recurse -Force

Write-Output "`nDone! Run`n    jupyter lite serve`nin the JupyterLite folder and visit`n    http://127.0.0.1:8000/lab/index.html?path=OGRePy_Live.ipynb`nto test the site."
