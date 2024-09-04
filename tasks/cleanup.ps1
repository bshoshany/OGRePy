#!/usr/bin/env pwsh

<#
.SYNOPSIS
OGRePy: An Object-Oriented General Relativity Package for Python by Barak Shoshany (baraksh@gmail.com) (https://baraksh.com/) v1.0.1 (2024-09-04)
.DESCRIPTION
This script cleans up Python and Jupyter cache folders.
.NOTES
Copyright (c) 2024 Barak Shoshany. Licensed under the MIT license. If you found this project useful, please consider starring it on GitHub! If you use this package in published software or research, please provide a link to the GitHub repository <https://github.com/bshoshany/OGRePy> in the source code and documentation.
.LINK
https://github.com/bshoshany/OGRePy
#>

Function Write-Text()
{
    Write-Host @args -ForegroundColor 'Yellow'
}

Function Remove-IfExists([String] $File)
{
    If (Test-Path $File)
    {
        Write-Text "Removing $File..."
        Remove-Item $File -Recurse
    }
    Else
    {
        Write-Text "$File does not exist."
    }
}

Remove-IfExists .\OGRePy\__pycache__
Remove-IfExists docs/.ipynb_checkpoints
