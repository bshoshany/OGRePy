#!/usr/bin/env pwsh

<#
.SYNOPSIS
OGRePy: An Object-Oriented General Relativity Package for Python by Barak Shoshany (baraksh@gmail.com) (https://baraksh.com/) v1.0.1 (2024-09-04)
.DESCRIPTION
This script compiles the Markdown documentation to a Jupyter notebook, and then executes the notebook in place so that cell outputs will be included.
.NOTES
Copyright (c) 2024 Barak Shoshany. Licensed under the MIT license. If you found this project useful, please consider starring it on GitHub! If you use this package in published software or research, please provide a link to the GitHub repository <https://github.com/bshoshany/OGRePy> in the source code and documentation.
.LINK
https://github.com/bshoshany/OGRePy
#>

$Venv = '.OGRePy-env\Scripts\Activate.ps1'
If (Test-Path $Venv)
{
    & $Venv
}

$Env:PYTHONPATH = Get-Location

$Source = 'README.md'
$Target = 'docs/OGRePy_Documentation.ipynb'

If (Test-Path $Target)
{
    Remove-Item $Target
}

jupytext $source --to notebook --output $Target

jupyter execute $Target --inplace
