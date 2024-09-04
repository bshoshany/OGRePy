#!/usr/bin/env pwsh

<#
.SYNOPSIS
OGRePy: An Object-Oriented General Relativity Package for Python by Barak Shoshany (baraksh@gmail.com) (https://baraksh.com/) v1.0.1 (2024-09-04)
.DESCRIPTION
This script updates all Python packages in the current environment. If the virtual environment .OGRePy-env exists, it will be activated, otherwise the global environment will be updated.
.NOTES
Copyright (c) 2024 Barak Shoshany. Licensed under the MIT license. If you found this project useful, please consider starring it on GitHub! If you use this package in published software or research, please provide a link to the GitHub repository <https://github.com/bshoshany/OGRePy> in the source code and documentation.
.LINK
https://github.com/bshoshany/OGRePy
#>

Function Write-Text()
{
    Write-Host @args -ForegroundColor 'Yellow'
}

$Venv = '.OGRePy-env\Scripts\Activate.ps1'
If (Test-Path $Venv)
{
    Write-Text 'Activating virtual environment...'
    & $Venv
}
Else
{
    Write-Text 'Virtual environment not found, updating global packages.'
}

Write-Text 'Upgrading pip...'
python -m pip install --upgrade pip

Write-Text 'Checking for outdated packages...'
$PythonPackages = pip list --outdated | Select-Object -Skip 2
If ($PythonPackages.Count -eq 0)
{
    Write-Text 'All packages are up to date.'
}
Else
{
    If ($PythonPackages.Count -eq 1)
    {
        Write-Text 'Updating 1 package...'
    }
    Else
    {
        Write-Text "Updating $($PythonPackages.Count) packages..."
    }
    $PythonPackages | ForEach-Object {
        $Parts = $_ -Split '\s+'
        Write-Text "[Package: $($Parts[0]) | Installed: $($Parts[1]) | Latest: $($Parts[2]) | Type: $($Parts[3])]"
        pip install --upgrade $Parts[0]
    }
}
