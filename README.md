<!-- remove-after-compile -->
[![Author: Barak Shoshany](https://img.shields.io/badge/author-Barak_Shoshany-009933)](https://baraksh.com/)
[![DOI: 10.48550/arXiv.2409.03803](https://img.shields.io/badge/DOI-10.48550%2FarXiv.2409.03803-b31b1b)](https://doi.org/10.48550/arXiv.2409.03803)
[![arXiv:2409.03803](https://img.shields.io/badge/arXiv-2409.03803-b31b1b)](https://arxiv.org/abs/2409.03803)
[![License: MIT](https://img.shields.io/github/license/bshoshany/OGRePy)](https://github.com/bshoshany/OGRePy/blob/master/LICENSE.txt)
[![Language: Python 3.12](https://img.shields.io/badge/Language-Python_3.12-yellow)](https://python.org/)
[![GitHub stars](https://img.shields.io/github/stars/bshoshany/OGRePy?style=flat&color=009999)](https://github.com/bshoshany/OGRePy/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/bshoshany/OGRePy?style=flat&color=009999)](https://github.com/bshoshany/OGRePy/forks)
[![GitHub release](https://img.shields.io/github/v/release/bshoshany/OGRePy?color=660099)](https://github.com/bshoshany/OGRePy/releases)
[![PyPI - Version](https://img.shields.io/pypi/v/OGRePy)](https://pypi.org/project/OGRePy/)
[![Open in Visual Studio Code](https://img.shields.io/badge/Open_in_Visual_Studio_Code-007acc)](https://vscode.dev/github/bshoshany/OGRePy)
<!-- /remove-after-compile -->

# OGRePy: An Object-Oriented General Relativity Package for Python

By **Barak Shoshany**\
Email: <baraksh@gmail.com>\
Website: <https://baraksh.com/>\
GitHub: <https://github.com/bshoshany>

GitHub repository: <https://github.com/bshoshany/OGRePy>\
PyPi project: <https://pypi.org/project/OGRePy/>

This is the complete documentation for **v1.3.0** of the package, released on **2025-02-04**.

<!-- remove-after-compile -->
<div style="color: red">

**Note: While this Markdown document can be read on its own, it is meant to be compiled into a Jupyter notebook so that the output of the executed statements will be shown. Some parts will not make sense without seeing the output. The files [`OGRePy/docs/OGRePy_Documentation.ipynb`](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.ipynb), [`OGRePy/docs/OGRePy_Documentation.html`](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.html), and [`OGRePy/docs/OGRePy_Documentation.pdf`](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.pdf) are the compiled notebook versions of this Markdown documentation, including all cell outputs.**

</div>
<!-- /remove-after-compile -->

* [Introduction](#introduction)
    * [Summary](#summary)
    * [Features](#features)
    * [The object-oriented design philosophy](#the-object-oriented-design-philosophy)
* [Installing and loading the package](#installing-and-loading-the-package)
    * [Global installation](#global-installation)
    * [Installing in a virtual environment](#installing-in-a-virtual-environment)
    * [Creating a Jupyter notebook](#creating-a-jupyter-notebook)
    * [Importing the package](#importing-the-package)
    * [Getting help](#getting-help)
* [Creating and displaying tensor objects](#creating-and-displaying-tensor-objects)
    * [Defining coordinates](#defining-coordinates)
    * [Error checking](#error-checking)
    * [Defining metrics](#defining-metrics)
    * [Displaying tensors](#displaying-tensors)
    * [Changing the output style](#changing-the-output-style)
    * [Line and volume elements](#line-and-volume-elements)
    * [Choosing index letters](#choosing-index-letters)
    * [Creating tensors in a given manifold](#creating-tensors-in-a-given-manifold)
* [Operations on single tensors](#operations-on-single-tensors)
    * [Changing a tensor's symbol](#changing-a-tensors-symbol)
    * [Raising and lowering indices](#raising-and-lowering-indices)
    * [Coordinate transformations](#coordinate-transformations)
    * [Replacing symbols in the tensor components](#replacing-symbols-in-the-tensor-components)
    * [Customizing the simplification function](#customizing-the-simplification-function)
    * [Getting information about tensors](#getting-information-about-tensors)
    * [Getting the components of a tensor](#getting-the-components-of-a-tensor)
    * [Comparing tensors](#comparing-tensors)
* [Calculations with tensors](#calculations-with-tensors)
    * [Addition of tensors](#addition-of-tensors)
    * [More on index specifications](#more-on-index-specifications)
    * [Multiplication of tensor by scalar](#multiplication-of-tensor-by-scalar)
    * [Taking traces and contracting tensors: theoretical review](#taking-traces-and-contracting-tensors-theoretical-review)
    * [Taking traces and contracting tensors: OGRePy syntax](#taking-traces-and-contracting-tensors-ogrepy-syntax)
* [Derivatives and curvature tensors](#derivatives-and-curvature-tensors)
    * [The Christoffel symbols](#the-christoffel-symbols)
    * [The Riemann tensor](#the-riemann-tensor)
    * [Exact sign checks with `list()`](#exact-sign-checks-with-list)
    * [The `riemann()` method and caching](#the-riemann-method-and-caching)
    * [The Kretschmann scalar](#the-kretschmann-scalar)
    * [The Ricci tensor and scalar](#the-ricci-tensor-and-scalar)
    * [The Einstein tensor](#the-einstein-tensor)
    * [Covariant derivatives](#covariant-derivatives)
* [Curves and geodesics](#curves-and-geodesics)
    * [The curve Lagrangian](#the-curve-lagrangian)
    * [Geodesic equations from the Lagrangian](#geodesic-equations-from-the-lagrangian)
    * [Geodesic equations from the Christoffel symbols](#geodesic-equations-from-the-christoffel-symbols)
    * [Geodesics equations in terms of the time coordinate](#geodesics-equations-in-terms-of-the-time-coordinate)
    * [Changing the curve parameter](#changing-the-curve-parameter)
* [About the project](#about-the-project)
    * [Bug reports and feature requests](#bug-reports-and-feature-requests)
    * [Contribution and pull request policy](#contribution-and-pull-request-policy)
    * [Starring the repository](#starring-the-repository)
    * [Acknowledgements](#acknowledgements)
    * [Copyright and citing](#copyright-and-citing)
    * [Other projects to check out](#other-projects-to-check-out)

## Introduction

### Summary

OGRePy is a modern Python package for differential geometry and tensor calculus, designed to be both powerful and user-friendly. It can be used in a variety of contexts where tensor calculations are needed, in both mathematics and physics, but it is especially suitable for general relativity.

Tensors are abstract objects, which can be represented as multi-dimensional arrays once a choice of index configuration and coordinate system is made. OGRePy stays true to this definition, but takes away the complexities that come with combining tensors in different representations. This is done using an object-oriented programming approach, taking advantage of principles such as encapsulation and class invariants to eliminate the possibility of user error.

The user initially defines each tensor in OGRePy using its explicit components in any single representation. Operations on this tensor are then done abstractly, without needing to specify which representation to use. Possible operations include addition of tensors, multiplication of tensor by scalar, trace, contraction, and partial and covariant derivatives.

OGRePy will automatically choose which representation to use for each tensor based on how the tensors are combined. For example, if two tensors are added, then OGRePy will automatically use the same index configuration (upper and lower indices) for both. Similarly, if two tensors are contracted, then OGRePy will automatically ensure that the contracted indices are one upper (contravariant) and one lower (covariant). OGRePy will also automatically transform all tensors being operated on to the same coordinate system.

Transformations between representations are done behind the scenes; all the user has to do is specify which metric to use for raising and lowering indices, and how to transform between the coordinate systems being used. This information only needs to be given once and for all when first defining the tensors and coordinate systems, and will be used automatically from that point on.

This also means that there is no room for user error. The user cannot mistakenly perform "illegal" operations such as $2A^{\mu\nu}+B_ {\mu\lambda}C_ {\lambda\nu}$. Instead, the user simply inputs the names of the tensors, the order (but **not** the configuration) of indices for each, and the operations to perform - and the correct combination $2A^{\mu\nu}+B^{\mu}{}_ {\lambda}C^{\lambda\nu}$ will be automatically deduced.

OGRePy is a Python port of the popular Mathematica package [OGRe](https://github.com/bshoshany/OGRe), first released in February 2021, used by many general relativity researchers worldwide. The Python port uses the same robust and performance-oriented algorithms, and retains the package's core design principles. It was made to be as flexible and powerful as possible, while also being simple to learn and easy to use, and suitable for both experienced and novice researchers. OGRePy uses [SymPy](https://www.sympy.org/) to facilitate symbolic computations and [Jupyter](https://jupyter.org/) as a notebook interface.

The Python port was specifically designed to mimic as much of the original Mathematica package's syntax as possible, while also greatly improving on that syntax in many ways due to the fact that Python, unlike Mathematica, is a truly object-oriented language. The documentation for both packages was also kept as similar in structure and scope as possible, with the same practical examples. This means that anyone who is familiar with the Mathematica version should easily be able to use the Python version, and vice versa.

### Features

* Define coordinate systems and the transformation rules between them. The Jacobians are automatically calculated. Tensor components are then transformed automatically between coordinates behind the scenes as needed.
* Each tensor is associated with a specific metric. Tensor components are then transformed automatically between different index configurations, raising and lowering indices behind the scenes as needed.
* Display any tensor in any index configuration and coordinate system, either in vector/matrix form or as a list of all unique non-zero elements. Metrics can also be displayed as a line element.
* Automatically simplify tensor components, optionally with a user-defined simplification function.
* Easily calculate arbitrary tensor formulas using any combination of addition, multiplication by scalar, trace, contraction, partial derivative, covariant derivative, and permutation of indices.
* Built-in methods for calculating the Christoffel symbols (Levi-Civita connection), Riemann tensor, Ricci tensor and scalar, Einstein tensor, Kretschmann scalar, curve Lagrangian, and volume element from a metric.
* Calculate the geodesic equations in terms of an affine curve parameter, in two different ways: from the Christoffel symbols or from the curve Lagrangian. For spacetime metrics, the geodesic equations can be calculated in terms of the time coordinate.
* Easily keep track of all tensors created in a notebook session, including the relations between them - for example, see which metrics were created and which tensors are associated with each metric.
* Export tensor components in TeX or Mathematica format.
* Designed with speed and performance in mind, using optimized algorithms developed specifically for this package.
* Clear and detailed documentation, with many examples, in [Jupyter Notebook](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.ipynb), [HTML](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.html), and [PDF](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.pdf) formats.
* Open source. The code is extensively documented; please feel free to fork and modify it as you see fit.
* Under continuous and active development. Bug reports and feature requests are welcome, and should be made via [GitHub issues](https://github.com/bshoshany/OGRePy/issues).

### The object-oriented design philosophy

**Object-oriented programming** refers to a paradigm where a program's code is organized around objects. An **object** belongs to a user-defined type, called a **class**. The class defines the **data** that the object stores, as well as **methods** or **member functions** that read or manipulate that data. One of the fundamental principles of object-oriented programming is **encapsulation**, which means that the user may only access an object's data using the methods defined by the class, and is unable to access the object's data directly.

Importantly, encapsulation allows for the preservation of **class invariants**. An invariant is a condition of validity that can always be assumed to be satisfied by the data stored in each object. If the methods make sure to preserve the invariant whenever they store or manipulate the data, and the user is prevented from changing the data manually and thus potentially violating the invariant, then the implementation of the class can be greatly simplified, and performance can be improved, because the class will not need to verify that the data is valid every time it performs an operation.

The main idea behind OGRePy is to simplify the use of tensors by encoding all the information about a tensor in a single, self-contained object. As I mentioned above, a tensor is an abstract object. One can find components which represent this abstract entity in a particular coordinate system and index configuration, but the tensor is **not** its components. In OGRePy, a tensor object is initially defined (or **constructed**) by providing the components of the tensor in a particular representation - but once this is done, the user does not need to worry about coordinates or indices anymore, or even remember which coordinates and indices were initially used. The abstract tensor object will automatically transform the initial data to a different coordinate system or index configuration as needed, based on the context in which it was used.

As a tensor object holds the components of the same tensor in many different representations, the most important class invariant is the assumption that the different components indeed represent the same tensor. This is achieved using encapsulation; the object's data can only be modified by private methods that preserve the invariant, and thus the user cannot accidentally cause a violation of the invariant by assigning components to one representation that are not related to the components of all other representations by the appropriate coordinate and/or index transformation.

Since Mathematica is not an object-oriented language, the original OGRe package merely simulated classes and objects using associative arrays, resulting in a somewhat awkward syntax. Python, on the other hand, is an inherently object-oriented language, and the Python package takes full advantage of that. Tensors are objects, and the various tensor operations are done directly on these objects using methods and overloaded operators. Class invariants and encapsulation guarantee that the different representations of the tensor objects are always consistent, and the correct representation is chosen on demand for each calculation using intelligent algorithms.

## Installing and loading the package

### Global installation

To install OGRePy from [PyPI](https://pypi.org/project/OGRePy/) using `pip`, simply run the following command in the terminal:

```
pip install OGRePy
```

The current version of OGRePy officially supports only **Python v3.12 and above**. It may also work with older versions of Python 3, but this is not guaranteed, as development and testing was only done with the indicated Python version. If your global Python installation is an older version, and you cannot upgrade it, consider using [pyenv](https://github.com/pyenv/pyenv) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) to install multiple Python versions in parallel, or use a portable local installation to run OGRePy.

Installing OGRePy using `pip` will also automatically install its dependent packages, [ipykernel](https://pypi.org/project/ipykernel/) and [sympy](https://pypi.org/project/sympy/), if they are not already installed. The current version of OGRePy officially supports only **ipykernel v6.29 and above** and **sympy v1.13 and above**, so if you are still using older versions, you should upgrade these packages using the command `pip install --upgrade ipykernel sympy`.

### Installing in a virtual environment

Advanced users may wish to install OGRePy inside a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to avoid potential dependency conflicts with other packages. To do this, first open the directory where you would like to store your new virtual environment in the terminal, and run:

* `python -m venv .OGRePy-env --upgrade-deps` on Windows,
* `python3 -m venv .OGRePy-env --upgrade-deps` on WSL/Linux/macOS.

This will create a virtual environment under the `.OGRePy-env` subdirectory. The `--upgrade-deps` flag automatically upgrades `pip` to the latest version. To activate the virtual environment, run:

* `.OGRePy-env\Scripts\activate.bat` on Windows (Command Prompt),
* `& .OGRePy-env\Scripts\Activate.ps1` on Windows (PowerShell),
* `source .OGRePy-env/bin/activate` on WSL/Linux/macOS.

If this worked correctly, you will see the text `(.OGRePy-env)` at the beginning of the terminal prompt. Now you can install OGRePy using `pip` as above. To deactivate the virtual environment, simply run the command `deactivate` in the terminal.

### Creating a Jupyter notebook

OGRePy is designed to run within a [Jupyter](https://jupyter.org/) notebook. It is also possible to run it from within a Python script, usually for automation purposes, but Jupyter is required for interactivity and for displaying tensors and their components as rendered TeX equations.

OGRePy supports two Jupyter notebook interfaces:

* [Visual Studio Code](https://code.visualstudio.com/): **This is the officially recommended way to use OGRePy, due to helpful features such as IntelliSense, tooltips, and type checking.** Download and install from the [official website](https://code.visualstudio.com/). Run VS Code, then create a new file with the `.ipynb` extension and open it, or press F1 to open the Command Pallette and choose the option "Create: New Jupyter Notebook". This will prompt you to automatically install the required VS Code extensions and Python packages if they are not already installed.
* [JupyterLab](https://jupyter.org/): Install with `pip install jupyterlab`. Run by executing `jupyter-lab` in the terminal, and then create a new notebook in the web browser. **Please note that JupyterLab is not officially supported, as development and testing was only done with VS Code, although I have verified that the package does work in JupyterLab.**

If you are running OGRePy in a virtual environment:

* With Visual Studio Code, open the folder where you create the virtual environment, press F1 to open the Command Pallette, choose the option "Python: Select Interpreter", and select the `.OGRePy-env` environment. The interpreter can also be selected for individual Jupyter notebooks in VS Code using the "Select Kernel" button at the top right of the notebook.
* With JupyterLab, first activate the virtual environment in the terminal as explained above, and then run `jupyter-lab` from the same terminal.

### Importing the package

To load OGRePy, type the following code in a Jupyter notebook cell and execute it using Shift+Enter:

```python
import OGRePy as T
```

All of OGRePy's functions are now accessible via the `T` namespace. While it is not common practice in Python to import packages as single letters, OGRePy uses this convention because in the original [Mathematica version of OGRe](https://github.com/bshoshany/OGRe), all module names started with a capital T (which stands for "Tensor"). However, you can change that to another namespace if you prefer, for example `import OGRePy as gr`.

If desired, the welcome message can be disabled by defining `OGREPY_DISABLE_WELCOME = True` in the notebook before importing the package. Alternatively, you could set the environment variable `OGREPY_DISABLE_WELCOME` to `True`, which allows you to disable it permanently. If you changed your mind later and you want to see the welcome message (for example, if you want a link to the documentation), execute the command `T.welcome()`.

OGRePy also automatically checks for updates from [PyPI](https://pypi.org/project/OGRePy/) when it is imported. This can be disabled by defining `OGREPY_DISABLE_UPDATE_CHECK = True` in the notebook, or setting the environment variable `OGREPY_DISABLE_UPDATE_CHECK` to `True`, before importing the package. In that case, you can still check for updates manually if you wish, using `T.update_check()`.

However, note that this check is performed asynchronously, so it does not increase the load time of the package, and you can continue working while the check is being performed. If the welcome message is disabled, the startup update check is performed in "quiet mode", meaning that it only notifies you if a new version is available, but not if you are running the latest version.

### Getting help

One of the reasons I recommend Visual Studio Code as the preferred notebook interface for this package is the IntelliSense feature, which displays a helpful popup with suggestions and information about various language components. To test this feature, once OGRePy is loaded in the notebook, create a new code cell and start typing `T.` - once you write the dot character, you will see a popup menu listing all the functions contained in the `T` namespace.

Browse the menu using the arrow keys. There will be an additional popup next to this menu with the documentation for each function. If you do not see the documentation, press Ctrl+Space. You can also start typing to filter the options in the menu. For example, if you type `w`, the `welcome()` function will be selected, and you will see the documentation for that function. In the same way, you can view the documentation and usage instructions for all OGRePy functions.

Press Tab to complete the code and write down the full function `welcome()`. Once the code is written, the popup will disappear, but it will reappear again after you write `(` to display the parameters that should go into the parentheses. You can also hover with the mouse over any function to read its documentation.

If you are using JupyterLab instead of VS Code, the popups will not be displayed automatically by default, but you can press <kbd>Ctrl+,</kbd> to go to the settings, then click on "Code Completion" and check "Show the documentation panel" and "Enable autocompletion". (However, note that the documentation will not be formatted as nicely on JupyterLab.)

You can also view the documentation for a particular OGRePy function using the function `doc()`. For example:

```python
T.doc(T.welcome)
```

`doc()` itself also has documentation:

```python
T.doc(T.doc)
```

The documentation files [`OGRePy_Documentation.ipynb`](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.ipynb), [`OGRePy_Documentation.html`](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.html), and [`OGRePy_Documentation.pdf`](https://github.com/bshoshany/OGRePy/blob/master/OGRePy/docs/OGRePy_Documentation.pdf) are bundled with the package, so you can view them at any time - even offline - by simply clicking the links in the welcome message.

## Creating and displaying tensor objects

### Defining coordinates

To define tensors, we first need to define the manifold on which they reside. Since we are focusing on general relativity, we will use 4-dimensional spacetime manifolds in the following examples, but this package works equally well with manifolds that are purely spatial and/or have a different number of dimensions.

The first step is to define the coordinate system. We can represent a coordinate system as a vector $x^{\mu}$ (or a tensor of rank 1) defining a point in space(time). In OGRePy, coordinates are represented as objects of the class `Coordinates`. Therefore, defining a coordinate system is a simple matter of constructing a new `Coordinates` object. The constructor for this class is defined as follows:

```python
T.doc(T.Coordinates)
```

For example, let us create an object for the **Cartesian spacetime coordinates** $(t, x, y, z)$. First we will need some SymPy `Symbol` objects to represent the individual coordinates $t$, $x$, $y$, and $z$. Conveniently, OGRePy contains a module, `OGRePy.abc`, which contains SymPy symbols for all English and Greek letters, both lowercase and uppercase. Note that the Greek letter lambda (lowercase $\lambda$, uppercase $\Lambda$) is accessed via the symbols `lamda` and `Lamda` respectively, since `lambda` is a reserved keyword in Python.

For users familiar with SymPy: `OGRePy.abc` is similar to `sympy.abc`, except that `OGRePy.abc` explicitly assumes that all symbols are real, and also contains uppercase Greek letters. If complex symbols are desired, they should be imported from `sympy.abc` or created directly via `sympy.Symbol` or `sympy.symbols()` instead.

We import the symbols as follows:

```python
from OGRePy.abc import t, x, y, z
```

Now we have direct access to the symbols `t`, `x`, `y`, and `z` in our notebook. Let us use them to construct our Cartesian coordinate system:

```python
Cartesian = T.Coordinates(t, x, y, z)
```

Here is a breakdown of the code:

* `Cartesian` is the name of the new object we are creating.
* `T` is the namespace we chose for OGRePy when we imported it via `import OGRePy as T`.
* `Coordinates` is the name of the class we want to construct an instance of. This class represents a coordinate system in OGRePy.
* `Coordinates()` is the **constructor**, that is, the function that creates a new `Coordinates` object representing a particular coordinate system.
* We can pass any number of arguments to the constructor. Usually these will be SymPy symbols representing the coordinates (but it is also possible to pass strings, which will be converted to symbols automatically).
* `t`, `x`, `y`, and `z` are the symbols we exported above.

We can similarly define the **spherical spacetime coordinates** $(t, r, \theta, \phi)$:

```python
from OGRePy.abc import phi, theta

r = T.sym("r", nonnegative=True)

Spherical = T.Coordinates(t, r, theta, phi)
```

Note that Greek letters are imported using the full name of the letter: `theta` stands for $\theta$. Similarly, `Theta` will be the uppercase $\Theta$. One thing you should be aware of is that the letters $\lambda$ and $\Lambda$ are imported as `lamda` and `Lamda` respectively, because `lambda` (with a `b`) is a reserved keyword in Python.

Another thing to note here is that we defined the $r$ coordinate manually as a SymPy `Symbol` object using OGRePy's `sym()` function instead of importing it from `OGRePy.abc`. The reason for defining $r$ separately this way is that we get more control over the properties of this coordinate. As mentioned above, any symbol imported from `OGRePy.abc` is automatically assumed to be real. However, for $r$, we also want to indicate that it is a non-negative symbol. This signals to SymPy to treat $r$ as non-negative when doing calculations or performing simplifications.

To illustrate this point, consider that $t$, defined above using `from OGRePy.abc import t`, is a real coordinate that can be positive, negative, or zero. Therefore, when we try to simplify $\sqrt{t^2}$, we get the **absolute value** of $t$:

```python
T.s.simplify(T.s.sqrt(t**2))
```

On the other hand, when we do the same to $r$, which is designated as non-negative, we simply get $r$ back, without an absolute value:

```python
T.s.simplify(T.s.sqrt(r**2))
```

In these examples, note that SymPy is automatically imported into the OGRePy namespace as `s`, which means we can access the entire SymPy namespace as `T.s`. This is done purely for convenience, so you don't have to import SymPy to the notebook separately. However, you could also `import sympy` directly if you prefer. Because SymPy is available as `T.s`, we could access the SymPy `simplify()` function directly via `T.s.simplify()`.

OGRePy offers two functions that can be used to create your own symbols: `sym()`, which is the preferred alternative to calling SymPy's `Symbol()` constructor, and `syms()`, which is the preferred alternative to calling SymPy's `symbols()` function. The main differences between OGRePy's `sym()` and `syms()` and SymPy's `Symbol()` and `symbols()` are:

1. OGRePy's functions always add the assumption that the symbols are real, which helps with simplification.
2. OGRePy's functions always convert strings to TeX codes. This is important, because in SymPy, `Symbol("mu") != Symbol(r"\mu")`, even though they are both displayed using the same symbol. On the other hand, in OGRePy, `sym("mu") == sym(r"\mu")`, which prevent errors.

### Error checking

OGRePy contains robust error checking. If you call the constructor with invalid input, the construction will fail and you will get an error message telling you what to fix. For example, if you try typing `T.Coordinates(42)` you will get the following friendly error message:

&#x1f4b1; <b style="color: #cf514b;">The components must be either a SymPy `Array` object or a list. The object `42` is of type `int`.</b>

If you are an advanced user who prefers to see the full traceback and/or catch the exceptions and handle them on your own, you can set `T.options.friendly_errors = False` to turn off the friendly error messages and raise exceptions instead. Set it back to `True` to re-enable the friendly error messages.

### Defining metrics

To finish defining a (Riemannian or pseudo-Riemannian) manifold, we need to define its metric tensor. Like any other tensor in OGRePy, the metric tensor is an abstract tensor that has multiple representations. We "jump start" the tensor by providing its components in one particular representation, and all the other representations will be calculated automatically.

In the case of a metric tensor, the defining representation must always be the one with two indices down: $g_ {\mu\nu}$. However, it can be given in any coordinate system. In OGRePy, metrics are represented as objects of the class `Metric`. Therefore, as with coordinates, defining a metric is a simple matter of constructing a new `Metric` object. The constructor for this class is defined as follows:

```python
T.doc(T.Metric)
```

Let us create a tensor object for the **Minkowski metric**, specifying the components in Cartesian coordinates:

```python
Minkowski = T.Metric(
    coords=Cartesian,
    components=T.diag(-1, 1, 1, 1),
    symbol="eta",
)
```

To define the components we used the OGRePy `diag()` function, which generates a diagonal matrix (a SymPy `Matrix` object) with the given components on the diagonal. OGRePy's `diag()` is a convenient shorthand for SymPy's `Matrix.diag()`.

For the symbol, we used the string `"eta"`, which will be displayed as the Greek letter $\eta$. Alternatively, we could have used any TeX string, such as `r"\eta"`. (Note the `r` in front of the string, indicating that it is a "raw" string literal, so the `\` in the string is treated as an actual `\` and not an escape character.) Internally, the string `"eta"` is actually converted to `r"\eta"`. The `symbol` argument also accepts SymPy `Symbol` objects, in which case it extracts the TeX code from the object, so we could have also used `from OGRePy.abc import eta` and then entered `eta` as the symbol, but that is more cumbersome.

Similarly, let us define the **Schwarzschild metric**, this time specifying the components in spherical coordinates:

```python
from OGRePy.abc import M

Schwarzschild = T.Metric(
    coords=Spherical,
    components=T.diag(
        -(1 - 2 * M / r),
        1 / (1 - 2 * M / r),
        r**2,
        r**2 * T.s.sin(theta) ** 2,
    ),
)
```

Here we imported the symbol `M` to use as the mass. Be careful not to write something like `2M` instead of `2 * M`. While `2M` makes sense mathematically, it is not a legal Python expression. Note that we did not specify a symbol, so the symbol $g$ will be used by default.

### Displaying tensors

In OGRePy, the term **tensor object** refers to any object of the `Tensor` class or its derived classes, which include `Metric` (but not `Coordinates`, which is not a tensor, just a list of symbols) Every tensor object in OGRePy has a method called `show()`, which shows the symbol, indices, coordinates, and components in those indices and coordinates, in vector or matrix form when applicable. Let us try it for the two metrics we created:

```python
Minkowski.show()
```

```python
Schwarzschild.show()
```

In fact, calling the `show()` method explicitly is not necessary. If the output of a notebook cell is a tensor object, the output of the `show()` method will be displayed automatically:

```python
Minkowski
```

A coordinate system is not a tensor, but it does have a `show()` method as well, and it is also executed automatically if it's the output of a notebook cell:

```python
Cartesian.show()
```

```python
Spherical
```

The other method available for displaying the contents of tensors is `list()`, which lists all of the unique (up to sign), non-zero components of the tensor. It is usually the best option for higher-rank tensors, which cannot be displayed in vector or matrix form, such as the Christoffel symbols or Riemann tensor (see below). For example, let us list the components of the Minkowski metric:

```python
Minkowski.list()
```

There is a convenient shortcut for calling `list()`: simply use the `~` (invert) operator in front of the tensor. For example:

```python
~Schwarzschild
```

A `Coordinates` object does not have a `list()` method, as it wouldn't make sense to list its components in this manner.

If, as in the examples above, no additional arguments are given to `show()` and `list()`, they display the tensors in their default indices and default coordinates, which are the ones first used to define the tensor (unless you change them later). So, for example, the default indices of the Minkowski metric are two lower indices, and its default coordinates are Cartesian. We will show later how to change these defaults, and how to display any tensor in any index configuration and coordinate system. Note that if a tensor object is displayed automatically as the output of a cell, or using the `~` shortcut for `list()`, it will always be displayed in its default indices and coordinates.

A good practice when using OGRePy is to set up the notebook so that the result of the last assignment in the cell is automatically printed out. This will save us the trouble of writing an extra line every time we want to print out tensors we assign to variables. This is achieved by executing the following command:

```python
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "last_expr_or_assign"
```

### Changing the output style

The `options` object of the OGRePy package is used to set various options, which will then be respected by all functions and classes in the package. We already saw above that we can use it to turn off the friendly error message by setting `T.options.friendly_errors = False`.

To control the style of the output, you can change the property `T.options.css_style` to any string of your choice. The default is just an empty string, but we can change this to any [CSS style](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS) we want. For example:

```python
T.options.css_style = "background-color: #000; color: #fff; font-size: 20px; padding: 5px"
~Schwarzschild
```

To reset the style to the default value, we simply "delete" the property using `del`:

```python
del T.options.css_style
```

Now the style is back to normal:

```python
~Schwarzschild
```

This is common to all properties of `options`; the `del` operator does not delete the property, it simply resets it to the default value.

### Line and volume elements

In the case of metrics, we can also display them as a line element using the method `line_element()`. For example, here are the line elements for our two metrics:

```python
Minkowski.line_element()
```

```python
Schwarzschild.line_element()
```

Note that these are standard SymPy expressions, so they can be manipulated like any other expressions, including operations such as simplifying or factoring. As an example of a more interesting (non-diagonal) line element, consider the **Alcubierre warp drive metric**:

```python
v_t = T.func("v")(t)
f_t_x_y_z = T.func("f")(t, x, y, z)
Alcubierre = T.Metric(
    coords=Cartesian,
    components=[
        [-1 + f_t_x_y_z**2 * v_t**2, 0, 0, -f_t_x_y_z * v_t],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-f_t_x_y_z * v_t, 0, 0, 1],
    ],
)
```

Here we used OGRePy's `func()` function, which is a wrapper around SymPy's `Function` class which also defines the function to be real. Note that the metric was automatically printed in matrix form, since we configured the notebook to print out the result of the last assignment. Here is a list of its non-zero components:

```python
~Alcubierre
```

$f$ is a form function which is equal to 1 inside a "warp bubble" of finite radius and 0 outside it, and $v$ is the velocity of the bubble, which can be faster than the speed of light ($v > 1$). Note that for $v$ and $f$ we used a new type of object: a SymPy `Function` object. This represents a function of the elements given as the arguments to the constructor, so $v$ is a function of $t$ while $f$ is a function of all of the coordinates.

It is easy to see that the metric is flat where $f = 0$, that is, outside the bubble. Its line element is:

```python
Alcubierre.line_element()
```

We can simplify it as follows. First, we expand the parentheses:

```python
Alcubierre.line_element().expand()
```

Using the `args` method, we can split this expansion into individual terms (we put the result inside a SymPy `Array` so the terms will be properly displayed as SymPy expressions in the notebook):

```python
args = Alcubierre.line_element().expand().args
T.s.Array(args)
```

Now we can factorize the third, fifth, and sixth terms together, then add the rest: (recall that indices start from zero!)

```python
args[0] + args[1] + args[3] + T.s.factor(args[2] + args[4] + args[5])
```

In this form, it is immediately clear that the metric is flat outside the warp bubble (where $f$ is $0$), and inside the warp bubble (when $f$ is $1$) it is a flat metric translated by an amount $v\left(t\right)\mathrm{d}t$ in the $z$ direction.

Another thing we can do with a metric is calculate its volume elements squared, which is simply the determinant of the metric, using the method `volume_element_squared()`. For example:

```python
Minkowski.volume_element_squared()
```

```python
Schwarzschild.volume_element_squared()
```

```python
Alcubierre.volume_element_squared()
```

As with the line elements, these are SymPy expressions, so they can be modified just like any other expression. Therefore, to calculate the volume element itself, we can just take the square root (adding a minus sign if the metric is Lorentzian):

```python
T.s.simplify(T.s.sqrt(-Schwarzschild.volume_element_squared()))
```

### Choosing index letters

By default, the `show()` method uses Greek letters for the indices, in a specific pre-determined order. The letters can be changed by setting the property `T.options.index_letters` to a list of symbols. The default letters are:

```python
T.options.index_letters
```

As you can see, they are given as strings containing TeX symbols. We can display these symbols more nicely in the notebook using the IPython package:

```python
from IPython.display import Math

Math(",".join(T.options.index_letters))
```

This means that the letter $\mu$ will be used for the first index, $\nu$ for the second, and so on. However, sometimes we want to use different letters. `T.options.index_letters` can accept a list of TeX symbols, SymPy symbols, and/or strings in the same format as SymPy's `symbols()` function, that is, a space- or comma-separated list of one or more letters or TeX codes - or a mix and match of all of the above, as long as it's inside a list. Ranges of letters can be indicated using a colon, so for example, here is how to change the indices to lowercase English letters in alphabetical order:

```python
T.options.index_letters = ["a:z"]
```

`show()` will now use these letters - in this particular order - when displaying tensors:

```python
Minkowski
```

As always with the `options` object, to reset the `index_letters` property to its default value, we "delete" it using `del`:

```python
del T.options.index_letters
```

Note that `list()` always uses the coordinate symbols themselves for the indices (e.g. $\eta_ {tt}$, $\eta_ {xx}$, etc.), so it is not affected by `T.options.index_letters`.

### Creating tensors in a given manifold

Any tensors other than coordinates and metrics are created as objects of the OGRePy class `Tensor`. The constructor for this class is defined as follows:

```python
T.doc(T.Tensor)
```

In OGRePy, all tensor objects must have an **associated metric** - except coordinate objects, and the metric tensors themselves. This is because OGRePy automatically raises and lowers indices as appropriate for various operations such as adding and contracting tensors, and it cannot do so without knowing which metric to use. Even scalars, which have no indices, should still be associated to a specific metric - since they can multiply other tensors, and you cannot multiply tensors from different manifolds together.

The index configuration of the tensor is a tuple. The number of indices is the rank of the tensor. Each element in the tuple corresponds to one index, with +1 specifying an upper index and -1 specifying a lower index. For example, `(-1, -1)` corresponds to a tensor such as the metric $g_ {\mu\nu}$, which has two lower indices, while `(1, -1, -1, -1)` corresponds to a tensor such as the Riemann tensor $R^{\rho}{}_ {\sigma\mu\nu}$, which has one upper index followed by three lower indices.

The components of the tensor can be given in several equivalent forms: a list, a SymPy `Array` object, or (for rank 2 tensors) a SymPy `Matrix` object. Usually, a list is the simplest option if we are specifying the components explicitly. (For advanced users: The components can, more generally, be any SymPy `NDimArray`, including mutable and/or sparse arrays, but OGRePy always stores the components as an immutable dense array, no matter what form the input was originally in.)

The components are the representation of the new tensor in the given index configuration and coordinate system. If a coordinate system is not specified, the default coordinate system of the associated metric will be used - but it is recommended to always specify the coordinate system explicitly, to avoid accidentally defining the tensor with the wrong components. The components will be automatically converted to different indices or coordinates later as needed, as we will demonstrate below.

To create a **scalar**, or a tensor of rank 0 (with no indices), we must input an empty tuple `()` for the indices, and a list with exactly one item for the components. Note that a "bare" expression, not inside a list, will not work. For example, let us define the **Kretschmann scalar** in the Schwarzschild spacetime (below we will show how to calculate it directly from the metric):

```python
SchwarzschildKretschmann = T.Tensor(
    metric=Schwarzschild,
    coords=Spherical,
    indices=(),
    components=[(48 * M**2) / r**6],
    symbol="K",
)
```

Similarly, we can create a **vector**, or a tensor of rank 1 (with one index). For example, let us create a vector for the 4-velocity of a particle moving at 3-velocity $v$ along the $x$ direction in Minkowski space. Since the 4-velocity has an upper index by definition, we make sure to define the components in the representation of the tensor with an upper index by specifying the index configuration as `(1,)`:

```python
from OGRePy.abc import v

FourVelocity = T.Tensor(
    metric=Minkowski,
    coords=Cartesian,
    indices=(1,),
    components=T.s.Array([1, v, 0, 0]) / T.s.sqrt(1 - v**2),
)
```

There are a few important things to note here:

1. In Python, a tuple of one element must be specified with a comma, i.e. `(1,)`, because `(1)` would be interpreted as an integer.
2. We used a SymPy `Array` object to define the components since this allowed us to divide each component by the square root $\sqrt{1-v^2}$. This would not be possible with a normal Python list.
3. Since we did not specify a symbol for this tensor, its symbol is just a placeholder $\square$. We will give it a proper symbol below.

Finally, as an example of a tensor of rank 2 (with two indices), let us define the **stress-energy tensor** $T^{\mu\nu}$ for a perfect fluid, using its matrix representation with two upper indices by specifying the index configuration `(1, 1)`:

```python
from OGRePy.abc import p, rho

PerfectFluid = T.Tensor(
    metric=Minkowski,
    coords=Cartesian,
    indices=(1, 1),
    components=T.diag(rho, p, p, p),
    symbol="T",
)
```

In a similar manner, we could also define tensors of rank 3 and above. However, such tensors are most often derived by operating on lower-rank tensors, rather than defined manually via their components. We will see an example of such a derivation when we derive the Christoffel symbols and Riemann tensor from the metric below.

## Operations on single tensors

### Changing a tensor's symbol

If we ever want to change the symbol used to display a tensor, we can simply change the property `symbol` to any string, TeX code, or SymPy `Symbol`. For example, let us give the symbol $u$ to the four-velocity:

```python
FourVelocity.symbol = "u"
```

Now, when we display the tensor using `show()` or `list()`, this is the symbol that will be used:

```python
FourVelocity
```

### Raising and lowering indices

Raising and lowering indices is one of the most basic tensor operations. For example, if we have a vector represented with one upper index, $v^{\nu}$, we can turn it into a covector, which is represented with one lower index, by **contracting** it with the metric:

$$
v_ {\mu} = g_ {\mu\nu} v^{\nu}.
$$

This is called "lowering an index". Here and in the rest of this documentation, we will be using the **Einstein summation convention**, where the same index repeated **exactly twice**, once as an upper index and once as a lower index, implies summation over that index. In this case, the implied summation is over $\nu \in {0, 1, 2, 3}$:

$$
v_ {\mu} = \sum_ {\nu=0}^{3} g_ {\mu\nu} v^{\nu} = g_ {\mu 0} v^{0} + g_ {\mu 1} v^{1} + g_ {\mu 2} v^{2} + g_ {\mu 3} v^{3}.
$$

Such a sum over an index is called a contraction, and it is a generalization of the inner product, as we will describe in more details below. Conversely, if we have a covector $w_ {\mu}$, we can raise its index by contracting it with the inverse metric:

$$
w^{\mu} = g^{\mu\nu} w_ {\nu}.
$$

This works the same for indices of higher-rank tensors. For example, if we have a tensor of rank 2 represented with two upper indices, $T^{\mu\lambda}$, we can lower either one or both of its indices:

$$
T^{\mu}{}_ {\nu} = g_ {\nu\lambda} T^{\mu\lambda},\quad T_ {\mu\nu} = g_ {\mu\rho} g_ {\nu\lambda} T^{\rho\lambda}.
$$

In OGRePy, since tensor objects are **abstract tensors**, independent of any specific index configuration, **there is no notion of raising or lowering the indices of a tensor object**. Instead, one simply request to **display** the components of the tensor with the desired index configuration, without modifying the object itself. This works with both the `show()` and `list()` methods, by simply providing as an argument the list of indices in the format $(\pm 1, \pm 1, ...)$, as when we created a new tensor.

As an example, let us use `show()` to display the vector `FourVelocity` with a lower index, that is, with index configuration `(-1,)`:

```python
FourVelocity.show(indices=(-1,))
```

OGRePy automatically knows to use the `Minkowski` metric to lower the index, which means that a minus sign has been added to the first component, as expected. Similarly, here is `PerfectFluid` with just the second index lowered, this time displayed using `list()`:

```python
PerfectFluid.list(indices=(1, -1))
```

The components of the representation of the metric with two upper indices are the components of the inverse metric, since

$$
g_ {\mu\lambda} g^{\lambda\nu} = \delta_ {\mu}^{\nu}.
$$

Therefore, a quick way to show the components of the inverse metric is to display it with the index configuration `(1, 1)`:

```python
Schwarzschild.show(indices=(1, 1))
```

For the same reason, the metric with one upper and one lower index is just the identity matrix:

```python
Schwarzschild.list(indices=(1, -1))
```

As explained above, if `show()` or `list()` are called without any arguments, the tensor is displayed in its **default index configuration**, which is the one first used to define the tensor. So the 4-velocity has one upper index by default, and the stress tensor has two upper indices by default, because that is how we initially defined them. However, the default indices can be changed by setting the property `default_indices`. For example, let us change the default indices of the perfect fluid stress tensor to two lower indices:

```python
PerfectFluid.default_indices = (-1, -1)
```

Now, when we display the tensor using `show()` or `list()` without any arguments, this is the index configuration that will be used:

```python
PerfectFluid
```

### Coordinate transformations

The components of any tensor may be transformed from one coordinate system $x^{\mu}$ to another coordinate system $x^{\mu'}$ using the following prescription:

* For every lower index $\mu$, add a factor of $\partial x^{\mu} / \partial x^{\mu'}$ (i.e. the derivative of the old coordinates with respect to the new, or the **Jacobian**).
* For every upper index $\mu$, add a factor of $\partial x^{\mu'} / \partial x^{\mu}$ (i.e. the derivative of the new coordinates with respect to the old, or the inverse of the Jacobian).

For example, given a tensor with components $T_ {\alpha\beta}$ in a coordinate system $x^{\mu}$, we can transform to components $T_ {\alpha'\beta'}$ in another coordinate system $x^{\mu'}$ as follows:

$$
T_ {\alpha'\beta'}(x^{\mu'}) = \frac{\partial x^{\alpha}}{\partial x^{\alpha'}} / \frac{\partial x^{\beta}}{\partial x^{\beta'}}
$$

For a general rank $(p, q)$ tensor with $p$ upper indices $\alpha_ {1}, \ldots, \alpha_ {p}$ and $q$ lower indices $\beta_ {1}, \ldots, \beta_ {q}$, the transformation takes the form

$$
T_ {\beta_ {1}^{\prime}\cdots\beta_ {q}^{\prime}}^{\alpha_ {1}^{\prime}\cdots\alpha_ {p}^{\prime}}(x^{\mu'})=\left(\frac{\partial x^{\alpha_ {1}^{\prime}}}{\partial x^{\alpha_ {1}}}\cdots\frac{\partial x^{\alpha_ {p}^{\prime}}}{\partial x^{\alpha_ {p}}}\right)\left(\frac{\partial x^{\beta_ {1}^{\prime}}}{\partial x^{\beta_ {1}}}\cdots\frac{\partial x^{\beta_ {q}^{\prime}}}{\partial x^{\beta_ {q}}}\right)T_ {\beta_ {1}\cdots\beta_ {q}}^{\alpha_ {1}\cdots\alpha_ {p}}(x^{\mu})
$$

As a mnemonic for this formula, recall that two indices may only be contracted if one of them is an upper index and the other is a lower index. If an index is in the denominator of a derivative, then its role is reversed (upper $\leftrightarrow$ lower). Thus the old (non-primed) and new (primed) indices can only be in places that allow properly contracting the Jacobian or inverse Jacobian with the tensor. For example, $\alpha_ {1}$ is an upper index in $T$ and therefore must be contracted with a lower index. Thus, $\partial x^{\alpha_ {1}}$ must be in the denominator, to lower its index and allow it to be contracted with the tensor.

As we saw above, OGRePy automatically knows how to raise or lower indices as needed using the appropriate metric. Similarly, any operation that requires transforming to another coordinate system will preform the transformation automatically behind the scenes. However, for this to happen, OGRePy needs to know the appropriate transformation rules. These are defined between the tensor objects representing the coordinates, which were created as `Coordinates` objects. The rules for transforming from a source coordinate system to a target coordinate system are stored within the tensor object representing the source. This is done using the method `set_coord_transformation()`. To illustrate, let us define transformations from `Cartesian` to `Spherical` and back:

```python
Cartesian.set_coord_transformation(
    target=Spherical,
    rules={
        x: r * T.s.sin(theta) * T.s.cos(phi),
        y: r * T.s.sin(theta) * T.s.sin(phi),
        z: r * T.s.cos(theta),
    },
)

Spherical.set_coord_transformation(
    target=Cartesian,
    rules={
        r: T.s.sqrt(x**2 + y**2 + z**2),
        theta: T.s.acos(z / T.s.sqrt(x**2 + y**2 + z**2)),
        phi: T.s.atan2(y, x),
    },
)
```

As you can see, the rules are supplied as a dictionary specifying the transformation from each source coordinate to the target coordinates. Note that we did not have to input a rule for `t`, since it stays the same in both cases; the transformation is in the spatial coordinates only.

Now OGRePy knows how to convert back and forth between these two coordinate systems - and this will happen automatically whenever required. We just needed to provide these rules once and for all, and any tensor initially defined in one coordinate system can now be automatically converted to the other.

As in the case of raising and lowering indices, displaying a tensor in a different coordinate system is a simple matter of calling the methods `show()` or `list()` with an additional argument specifying the coordinate system to use. For example, let us show the Minkowski metric in spherical coordinates:

```python
Minkowski.show(coords=Spherical)
```

We can also ask to see a tensor in a specific index configuration **and** a specific coordinate system:

```python
PerfectFluid.show(coords=Spherical, indices=(1, 1))
```

The method `list()` works in exactly the same way, for example:

```python
SchwarzschildKretschmann.list(coords=Cartesian)
```

Just as with default indices, every tensor has a default coordinate system, which is, initially, the one we used to create it. We can change it by setting the property `default_coords`, and then whenever we display the tensor, it will be displayed in that coordinate system if no other coordinate system is specified. For example, let's change the default coordinates of the perfect fluid stress tensor to spherical coordinates:

```python
PerfectFluid.default_coords = Spherical
```

Now, when we display the tensor using `show()` or `list()` without any arguments (or with just a choice of indices), this is the coordinate system that will be used:

```python
~PerfectFluid
```

Note that the coordinate transformation we defined is only invertible for $r \ge 0$. However, since we defined the coordinate $r$ above as a non-negative symbol, this is already taken care of by SymPy behind the scenes. To illustrate this, let us define a new scalar in Minkowski space, which is equal to the spatial distance from the origin:

```python
SpatialDistance = T.Tensor(
    metric=Minkowski,
    coords=Cartesian,
    indices=(),
    components=[T.s.sqrt(x**2 + y**2 + z**2)],
    symbol="d",
)
```

When we convert this scalar to spherical coordinates, we get $r$, as expected:

```python
SpatialDistance.show(coords=Spherical)
```

However, if we did not define $r$ as a non-negative symbol, we would have obtained $|r|$ instead.

### Replacing symbols in the tensor components

By using the `replace` argument of `list()` and `show()`, we can replace symbols in the tensor components with other symbols or numerical values. The replacement must be in the form of a dictionary, where each key in the dictionary will be replaced with its value. Each of the keys and the values of the dictionary can be either a SymPy `Symbol` object or a SymPy `Expr` object. The components will then be simplified, and the tensor will be displayed with the new components. Note that this only applies to **displaying** the components; the tensor data itself will not change.

For example, perhaps we would like to display the value of the Kretschmann scalar for a particular choice of $M$ and $r$:

```python
SchwarzschildKretschmann.show(replace={M: 1, r: 10})
```

Or maybe we would like to display the perfect fluid stress tensor with $p$ equal to $\rho$:

```python
PerfectFluid.list(replace={p: rho})
```

The replacement can, of course, also be combined with a choice of indices and/or coordinates:

```python
PerfectFluid.list(coords=Cartesian, indices=(1, 1), replace={p: rho})
```

Another, more advanced, thing we can do with `list()` and `show()` is to pass a function to be executed on each tensor component before printing it. We will see an example below, in the "Geodesic equations from the Lagrangian" section.

### Customizing the simplification function

Whenever OGRePy performs an operation that creates or modifies tensor components, such as converting between index representations or coordinate systems, it automatically simplifies the result using SymPy's `simplify()`. However, advanced users may want to have more control over this simplification process. This can be done using by setting `T.options.simplify_func` to a function of your choice.

For example, you may want to customize the arguments passed to simplify (such as `ratio` or `inverse`, see [here](https://docs.sympy.org/latest/modules/simplify/simplify.html) for more information), or you may want to use specific SymPy simplification functions such as `powsimp()` or `logcombine()` in a specific combination, or even `refine()` with specific assumptions.

In extreme situations, you may even want to cancel simplification altogether, if it is taking too long, which can be achieved using `T.options.simplify_func = lambda x: x` - that is, replacing the simplification function with the identity function.

As usual with the `options` object, you may restore the simplification function to the default, SymPy's `simplify()`, with the command `del T.options.simplify_func`.

Note that changing the simplification function will **not** automatically apply it to any existing tensors. The reason is that when OGRePy calculates the components of a tensor in a particular representation, it calculates them **once and for all**, and then saves them in the object's data to be reused later. This is done to improve performance, so that the components don't have to be recalculated every time they are needed.

We can force re-simplification of the stored components of a specific tensor using the method `simplify()`. This will return a new tensor with its components simplified; the original tensor will remain unchanged. However, you can write `MyTensor = MyTensor.simplify()` to store the simplified tensor under the same name.

### Getting information about tensors
The `info()` method can be used to display the information encoded in a tensor object in human-readable form. Here is an example:

```python
Minkowski.info()
```

As for `show()` and `list()`, OGRePy defines a convenient shortcut for calling `info()`: use the `+` (unary plus) operator in front of the tensor. For example:

```python
+PerfectFluid
```

A `Coordinates` object also has an `info()` method, and it can be used to check which tensors use this coordinate system as their default:

```python
+Cartesian
```

It is also possible to get each of these properties of the tensor individually, using the properties `symbol`, `default_indices`, and `default_coords` and the methods `rank()`, `dim()`, and `metric()`. Note that the symbol, default indices, and default coordinates are properties that can be changed, but `rank()`, `dim()`, and `metric()` are read-only properties obtained using methods, as it doesn't make sense to change these properties. Here are some examples of using these properties and methods. The symbol is a bit cryptic:

```python
PerfectFluid.symbol
```

The purpose of the `[0][1]` is to serve as a placeholders for indices, since the actual letters that will be used as the indices can be different each time. (These placeholders are added automatically when we create the tensor, there is no need to specify them manually, although you can if you want.) To get the symbol as a TeX string, we can use the `tex_symbol()` method, and pass its output to the IPython `Math()` function to display it in the notebook:

```python
Math(PerfectFluid.tex_symbol())
```

Similarly, we can use the `default_indices` and `default_coords` properties to obtain the default indices and coordinates:

```python
PerfectFluid.default_indices
```

```python
PerfectFluid.default_coords
```

And we can use the `metric()` method to obtain the associated metric:

```python
PerfectFluid.metric()
```

In the last two examples, `default_coords` and `metric()`, notice that the output directly shows the tensors used as the default coordinates and associated metric respectively. This is because `default_coords` and `metric()` return a **reference** to the relevant `Coordinates` or `Metric` object respectively, and that object then gets displayed in the notebook using the `show()` method, as it is the output of the cell.

However, since we are working inside a notebook, it would be helpful to know the name of the notebook variable referring to this `Coordinates` or `Metric` object. It turns out that is not at all straightforward to obtain this information in Python, since an object reference might not even be associated to any specific variable, or it may be associated to more than one variable. Luckily, OGRePy comes with a special algorithm to figure out which notebook variables refer to which objects. We already saw that algorithm in action when we used the `info()` method above. However, we can also obtain the name of the variable by simply converting the object to a string using the `str` constructor. This works on both `Coordinate` and `Metric` objects:

```python
str(PerfectFluid.default_coords)
```

```python
str(PerfectFluid.metric())
```

That same algorithm powers the module function `info()`, which lists all the tensors created so far, including the names of the variables used to define these tensors. Here are all the tensors we defined so far in this notebook:

```python
T.info()
```

We see that we created 9 tensors in total so far: 2 coordinate systems, 3 metrics, 3 tensors associated with the Minkowski metric, and 1 tensor associated with the Schwarzschild metric.

### Getting the components of a tensor

Sometimes you may want to extract the components of a tensor in a specific representation as a list, so you can use them outside of this package, as regular SymPy expressions rather than tensor objects. This is done using the `components()` method. For example, we can retrieve the components of the inverse Schwarzschild metric (with two upper indices):

```python
InverseSchwarzschild = Schwarzschild.components(coords=Spherical, indices=(1, 1))
```

We can now treat `InverseSchwarzschild` as any other SymPy `Array` - for example, extract the element at a particular position:

```python
InverseSchwarzschild[0, 0]
```

If the desired index configuration and/or coordinate system are not specified, the default ones will be used. However, it is important to always know exactly which representation the components are in, to avoid confusion. Thus, you will be notified which representation was used:

```python
Schwarzschild.components()
```

This warning can be disabled by adding the argument `warn=False`.

Since `components()` returns a SymPy `Array`, we can use the `subs()` method to perform replacements, just like the `replace` argument of `show()` and `list()` (see above). For example, here are the components of the Schwarzschild metric on the hypersurface with $\theta = \pi/2$:

```python
Schwarzschild.components().subs({theta: T.s.pi / 2})
```

In the case of a coordinate system, that is, a `Coordinates` object, `components()` takes no arguments, since a coordinate system cannot have multiple representations:

```python
Spherical.components()
```

### Comparing tensors

`Tensor` objects can be compared using the function `T.compare()`. Two tensors are considered equal if:

1. Their components are the same, and
2. They are associated with the same metric.

Internally, the comparison is only done in a single representation (if not specified, the default representation of the first tensor will be used), because if the two tensors have the same metric then it is guaranteed that if they are equal in one representation, they will be equal in all representations.

Conversely, tensors with different metrics are always considered not equal, since even if they happen to have the same components in one representation, they will necessarily have different components in another representation. (Also, if two tensors have different metrics then they exist on different manifolds, and therefore cannot be compared.)

As an example, let us create copies of the Minkowski metric and the perfect fluid tensor, and then compare the latter with the original perfect fluid tensor:

```python
Minkowski2 = T.Metric(
    coords=Cartesian,
    components=T.diag(-1, 1, 1, 1),
    symbol="eta",
)

PerfectFluid2 = T.Tensor(
    metric=Minkowski2,
    coords=Cartesian,
    indices=(1, 1),
    components=T.diag(rho, p, p, p),
    symbol="T",
)

T.compare(PerfectFluid, PerfectFluid2)
```

We see that the tensors `PerfectFluid` and `PerfectFluid2` are considered equal, because they have the same components, and their metrics have the same components (and are thus considered equal as well).

It is important to know the difference between the `T.compare()` function, which compares the components of different tensor objects, and the `==` or `is` operators, which for `Tensor` objects merely check if two variables point to the same object. Even though `T.compare(PerfectFluid, PerfectFluid2)` is `True`, we can see that `PerfectFluid == PerfectFluid2` and `PerfectFluid is PerfectFluid2` are both `False`:

```python
PerfectFluid == PerfectFluid2
```

```python
PerfectFluid is PerfectFluid2
```

You may be wondering why the `==` operator is equivalent to the `is` operator, and not to the `T.compare()` function. The reason is that the `==` operator would be ambiguous in this case, as only the components are compared, so two objects will be considered equal even if the symbol, default indices, or default coordinates are different. (Furthermore, in Python, overloading the `==` operator would cause issues when using tensors as dictionary keys or set elements, since these containers are implemented as hash tables.)

## Calculations with tensors

Now that we have all the bookkeeping of tensors out of the way, we can finally discuss how to use those tensors in calculations. In OGRePy, all tensor calculations are performed by simply using normal operations such as addition and multiplications on the tensors. However, this does not work the same as operating, for example, on integers; in most tensor operations, we also have to specify **indices**. Some of these indices will be *free indices**, which will remain in the final result, while others may be **contraction indices**, which will be contracted upon.

OGRePy supports a comprehensive collection of tensor operations. A tensor calculation in OGRePy can involve any number of tensor objects and can contain any combination of addition, multiplication by scalar, trace, contraction, partial derivative, and covariant derivative. The result will be stored in a new tensor object. Let us now go over these operations one by one, and give some examples.

### Addition of tensors

Addition of tensors in OGRePy is represented by a sum of the form `tensor1(index1, index2, ...) + tensor2(index1, index2, ...)`, where `tensor1` and `tensor2` are the tensor objects to be added, and `(index1, index2, ...)` are the **index specifications** for each tensor, given as SymPy symbols. (Note that an index specification is **not** the same as an index **configuration**, which is a tuple of the form `(±1, ±1, ...)` specifying which indices are up (+1) and which are down (-1).)

Note that you do **not** specify the position (upper or lower) of the indices. Furthermore, just like in any tensor equation, **the index letters themselves have no meaning**; they are just placeholders. Therefore, `(a, b, c)`, `(X, Y, Z)`, and `(alpha, beta, gamma)` are all completely equivalent. The only requirement is that the indices are **consistent**; in the case of addition, this means that both tensors being added must have **the same indices up to permutation**.

The following constraints apply to addition of tensors:

* You may not add a tensor representing a coordinate system to any other tensor, since coordinates do not transform like tensors.
* You may not add two tensors associated with different metrics, since their sum would have undefined transformation properties.
* You may not add two tensors with different ranks, since that is not a well-defined operation.
* As stated above, both tensors must have the same indices up to permutation. $A^{\mu\nu} + B^{\mu\nu}$ and $A^{\mu\nu} + B^{\nu\mu}$ (with inverted indices on the second tensor) are both okay, but $A^{\mu\nu} + B^{\alpha\beta}$ doesn't make sense, as it has more free indices than the rank of the result (that is, the result will be of the form $T^{\mu\nu\alpha\beta}$ instead of $T^{\mu\nu}$).

As an example, let us add the Minkowski metric $\eta_ {\mu\nu}$ and the perfect fluid stress tensor $T_ {\mu\nu}$. First we import symbols from `OGRePy.abc` to use as indices, then we perform the actual sum:

```python
from OGRePy.abc import mu, nu

result = Minkowski(mu, nu) + PerfectFluid(mu, nu)
```

Notice that the addition operation returned a new tensor object. This tensor's symbol has been automatically set to reflect the formula that was used to create it. However, often we want the new tensor to have its own single-letter symbol. To do that, we can use the `symbol` property:

```python
result.symbol = "S"
result
```

With this symbol, the tensor equation we calculated becomes:

$$
S_ {\mu\nu} = \eta_ {\mu\nu} + T_ {\mu\nu}.
$$

The order of indices we specify for each tensor matters. To give an example, let us define the following non-symmetric tensor:

```python
NonSymmetric = T.Tensor(
    metric=Minkowski,
    coords=Cartesian,
    indices=(-1, -1),
    components=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    symbol="N",
)
```

If we add it to the Minkowski metric, we get:

```python
Minkowski(mu, nu) + NonSymmetric(mu, nu)
```

Note that in this example we did not save the new tensor object in a variable, we just showed the result. However, if we flip its index specification from `(mu, nu)` to `(nu, mu)`, then we instead get:

```python
Minkowski(mu, nu) + NonSymmetric(nu, mu)
```

To stress an important point, there is no difference between `NonSymmetric(mu, nu)` and `NonSymmetric(nu, mu)` on its own, as **the index labels themselves are meaningless** unless there is some context in which they obtain meaning - as is always the case for tensor expressions. However, there is a big difference between, for example, `Minkowski(mu, nu) + NonSymmetric(mu, nu)` and `Minkowski(mu, nu) + NonSymmetric(nu, mu)`, as the indices have a different order, and thus the two expressions refer to adding different components.

Of course, any number of tensors can be added, not just two - and the same tensor can be added multiple times, with different index specifications each time. For example, we can calculate the following expression:

```python
Minkowski(mu, nu) + PerfectFluid(mu, nu) + NonSymmetric(mu, nu) + NonSymmetric(nu, mu)
```

### More on index specifications

For calculations that involve many indices, it may be more convenient to specify the indices as a string instead of individual symbols. This also saves us the trouble of importing or defining those symbols explicitly. This string must be given in the same format as SymPy's `symbols()` function, that is, a space- or comma-separated list of one or more letters or TeX codes. It is also possible to provide a list of strings, or even mix and match symbols and strings. For example, the previous calculation can also be written as follows:

```python
Minkowski(mu, nu) + PerfectFluid("mu nu") + NonSymmetric("mu", nu) + NonSymmetric("nu", "mu")
```

Index specifications have a use even if we are not doing a calculation: they change the indices that appear when `show()` is called, instead of the default index letters (as specified using `T.options.index_letters`). For example, with the default index letters, `NonSymmetric` will be displayed with the indices $\mu\nu$:

```python
NonSymmetric
```

However, if we want to display it with the indices $\alpha\beta$ instead, we can simply indicate these indices in parentheses:

```python
NonSymmetric("alpha beta")
```

Another alternative syntax is available for those who prefer the index specification format from the Mathematica version of OGRe: a string where each letter is a separate symbol, with no spaces between the letters, e.g. "abc" corresponds to (a, b, c). This format is less useful in the Python version since there is no easy way to enter Greek indices as individual letters; in Mathematica it's easy to write e.g. "μν" using escape sequences, but in Python it's easier to write "mu nu" or use symbols named `mu` and `nu` explicitly. The Mathematica format is accessible via square brackets, e.g.:

```python
NonSymmetric["ab"]
```

### Multiplication of tensor by scalar

Multiplication of tensor by scalar in OGRePy is represented by a product of the form `scalar * tensor(index1, index2, ...)`, where `tensor` is the tensor object to be multiplied, `(index1, index2, ...)` is an index specification as for addition, and `scalar` is the scalar to multiply by. Note that `scalar` should be a number or SymPy expression, and **not** a tensor object of rank 0. To multiply a tensor by a tensor of rank 0, use contraction instead, as detailed in the next section.

As an example, let us multiply the Minkowski metric $\eta_ {\mu\nu}$ by 2:

```python
2 * Minkowski(mu, nu)
```

While in this example the indices seem redundant, they are necessary because in most non-trivial situations we would like to combine multiplication with other operations, such as addition or contraction, in which the order of indices matters. For example, consider:

```python
2 * t * Minkowski(mu, nu) - 3 * x * PerfectFluid(mu, nu) + 4 * y * NonSymmetric(mu, nu) - 5 * z * NonSymmetric(nu, mu)
```

### Taking traces and contracting tensors: theoretical review

The most complicated tensor operation is **contraction**, a generalization of the vector inner product. This is done by summing over one or more disjoint pairs of indices, with each pair containing exactly one upper index and one lower index. Raising and lowering indices is one example of contraction: the metric (or its inverse) is contracted with a tensor. Coordinate transformations are another example, where we contract the Jacobian (or its inverse) with a tensor.

The simplest example of contraction is the **vector inner product**, which is defined as the contraction of a vector (one upper index) with a covector (one lower index):

$$
v^{\mu} w_ {\mu} = g_ {\mu\nu} v^{\mu} w^{\nu} = g(\mathbf{v},\mathbf{w}).
$$

The middle part of this equality comes from the fact that, as explained above, when we lower an index on $w^{\nu}$, we use the metric:

$$
w_ {\mu} = g_ {\mu\nu} w^{\nu}.
$$

This, in turn, justifies the notation $g(\mathbf{v},\mathbf{w})$ on the right-hand side, as this is, in fact, an inner product of two vectors using the metric $g$ (in index-free notation).

Contraction of indices in higher-rank tensors is simply a generalization of the inner product, for example:

$$
A^{\mu\alpha} B_ {\alpha\nu} = g_ {\alpha\beta} A^{\mu\alpha} B^{\beta}{}_ {\nu}.
$$

We can also contract more than one index:

$$
A^{\mu\nu} B_ {\mu\nu} = g_ {\mu\alpha} g_ {\nu\beta} A^{\mu\nu}B^{\alpha\beta}.
$$

This simply amounts to the fact that lowering both indices of $B^{\alpha\beta}$ involves contracting each index with the metric. We can even contract two indices **of the same tensor**:

$$
A^{\mu}{}_ {\mu} = g_ {\mu\nu}A^{\mu\nu}.
$$

This is called **taking the trace**. Furthermore, it is also possible to contract pairs of indices from more than two tensors at the same time:

$$
A^{\mu\nu} B_ {\nu\rho} C^{\rho\sigma} = g_ {\nu\alpha} g_ {\rho\beta} A^{\mu\nu} B^{\alpha\beta} C^{\rho\sigma}.
$$

However, such operations can always be broken down into individual contractions of pairs of tensors. For example, in this case, one could first contract $B_ {\nu\rho}$ with $C^{\rho\sigma}$ and then contract the result with $A^{\mu\nu}$ - which is indeed how this kind of contraction will be performed in OGRePy in practice:

$$
 A^{\mu\nu} B_ {\nu\rho} C^{\rho\sigma} = A^{\mu\nu} \left( B_ {\nu\rho} C^{\rho\sigma} \right).
$$

In a contraction, there are two types of indices: **contracted indices**, which are summed upon, and **free indices**, which are not summed upon. The rank of the tensor that results from the contraction is the number of free indices. So for example, in the expression $A^{\mu\alpha} B_ {\alpha\nu}$ we have one contracted index, $\alpha$, and two free indices, $\mu$ and $\nu$. Therefore, the resulting tensor is of rank two:

$$
T^{\mu}{}_ {\nu} = A^{\mu\alpha} B_ {\alpha\nu}.
$$

### Taking traces and contracting tensors: OGRePy syntax

Contraction of tensors in OGRePy is represented by an expression of the form `tensor1(index1, index2, ...) @ tensor2(index1, index2, ...)`, where `tensor1` and `tensor2` are the tensor objects to be contracted, and `(index1, index2, ...)` are the index specifications for each tensor. Any matching indices in both index specifications will be contracted. This means that, for example, $v^{\mu} w_ {\mu}$ is calculated using `v(mu) @ w(mu)` and $A^{\mu\nu} B_ {\nu\rho} C^{\rho\sigma}$ is calculated using `A(mu, nu) @ B(nu, rho) @ C(rho, sigma)`. Note that the user doesn't need to worry about the contracted indices being one upper and one lower, which is a common source of errors when contracting tensors by hand; the order of the indices, and whether the same index repeats twice, is all that matters.

As a first example, let us create the stress-energy tensor for a perfect fluid with a 4-velocity $u^{\mu}$. This is defined as follows:

$$
T^{\mu\nu} = (\rho + p) u^{\mu} u^{\nu} + p g^{\mu\nu}.
$$

Even though this does not involve any contractions, it still counts as a "trivial" contraction, since two tensors (the 4-velocities) are juxtaposed next to each other to create another tensor. This is also known as an **outer product**. Therefore, it uses the same `@` operator syntax as any other contraction, except that there are **no matching indices**. Note that this expression involves not just contraction (in the first term), but also multiplication by scalar (in both terms), and addition of the two terms together. Again, OGRePy takes care of everything behind the scene, so this just works:

```python
PerfectFluidFromVelocity = (rho + p) * FourVelocity(mu) @ FourVelocity(nu) + p * Minkowski(mu, nu)
PerfectFluidFromVelocity.symbol = "T"
PerfectFluidFromVelocity
```

Indeed, for $v = 0$ we get the previously defined stress tensor:

```python
PerfectFluidFromVelocity.show(replace={v: 0})
```

Multiplying a tensor by a scalar (i.e. a tensor of rank 0) is also done using a "trivial" contraction with no contracted indices. For example:

```python
(SpatialDistance() @ Minkowski(mu, nu)).show(coords=Spherical)
```

Note the empty index specification `()`, which is mandatory in order for OGRePy to recognize that the scalar is involved in a tensor calculation. We can also multiply a scalar by another scalar:

```python
SpatialDistance() @ SpatialDistance()
```

Now let us demonstrate some non-trivial contractions. First, we have the inner product of vectors - in this case, we get the norm (squared) of the 4-velocity, since we are contracting it with itself:

```python
FourVelocity(mu) @ FourVelocity(mu)
```

We can also contract several tensors together, with **two** matching pairs of indices:

```python
FourVelocity(mu) @ PerfectFluidFromVelocity(mu, nu) @ NonSymmetric(nu, rho)
```

Finally, to take the trace of a tensor, we simply match pairs of indices in that tensor's index specification:

```python
Minkowski(mu, mu)
```

```python
PerfectFluid("mu mu")
```

Of course, this also works for tensors with more than two indices, as we will see below. Any combination of indices can be used, with no limit on the number of traces taken for each tensor.

## Derivatives and curvature tensors

The **partial derivative** $\partial_ {\mu}$ is represented in OGRePy using the class `PartialD`. It can be contracted with other tensors using the usual OGRePy contraction notation - including an appropriate index specification - to calculate gradients and divergences.

The **gradient** of a tensor is the partial derivative $\partial_ {\mu}$ acting on the tensor with a free index, e.g. $\partial_ {\mu}\phi$ for a tensor, $\partial_ {\mu} u^{\nu}$ for a vector, or $\partial_ {\mu} T^{\nu\lambda}$ for a rank-2 tensor, resulting in a tensor of **one rank higher** (due to the extra index). In OGRePy, this is done by contracting the `PartialD` object from the left with the tensor, using the contraction operator `@`. For example, we can calculate the gradient $\partial_ {\mu} K$ of the Kretschmann scalar as follows:

```python
T.PartialD(mu) @ SchwarzschildKretschmann()
```

And here is the gradient of the Schwarzschild metric:

```python
~(T.PartialD(mu) @ Schwarzschild("alpha beta"))
```

The **divergence** of a tensor is the contraction of the partial derivative $\partial_ {\mu}$ with one of the tensor's indices, e.g. $\partial_ {\mu} u^{\mu}$ for a vector or $\partial_ {\mu} T^{\mu\nu}$ for a rank-2 tensor, resulting in a tensor of **one rank lower**. To illustrate, let us create the position vector of a particle in Minkowski space:

```python
Position = T.Tensor(
    metric=Minkowski,
    coords=Cartesian,
    indices=(1,),
    components=[t, x, y, z],
    symbol="x",
)
```

Its gradient is:

```python
T.PartialD(mu) @ Position(nu)
```

And its divergence is:

```python
T.PartialD(mu) @ Position(mu)
```

As you can see, the syntax for both the gradient and divergence is the same; if the index specification of `PartialD` matches one of the indices of the tensor to its right, then the divergence will be calculated, otherwise the gradient will be calculated.

**WARNING: When applying partial derivatives to tensors, the result generally does not transform like a tensor under a coordinate transformation.** For this reason, in general relativity we normally use the **covariant derivative** instead of a partial derivative. However, there are three important exceptions, where partial derivatives must be used: in the covariant derivative itself, the **Levi-Civita connection**, and the **Riemann tensor**, all of which will be discussed below.

Of these three special cases, the covariant derivative and the Riemann tensor turn out to nonetheless transform like tensors under coordinate transformations, due to cancellations. However, the Levi-Civita connection, whose components are called the **Christoffel symbols**, has a special transformation rule, which is used automatically by OGRePy, as we will show.

In all other cases, if the user creates an arbitrary tensor using partial derivatives, the result will generally **transform incorrectly** under a coordinate transformation in OGRePy. Therefore, it is highly recommended to avoid using partial derivatives in OGRePy unless you really know what you're doing.

### The Christoffel symbols

The **Christoffel symbols** are a very important tensor-like object in differential geometry. They are the components of the **Levi-Civita connection**, which is the unique torsion-free connection that preserves the metric. The Christoffel symbols are defined as follows:

$$
\Gamma_ {\mu\nu}^{\lambda} = \frac{1}{2} g^{\lambda\sigma} \left( \partial_ {\mu} g_ {\nu\sigma} + \partial_ {\nu} g_ {\sigma\mu} - \partial_ {\sigma} g_ {\mu\nu} \right).
$$

Each of the terms inside the parentheses is a gradient of the metric, with different indices. For example, the first term $\partial_ {\mu} g_ {\nu\sigma}$ is represented in OGRePy as `T.PartialD(mu) @ metric(nu, sigma)` where `metric` is the tensor object representing the metric. Since OGRePy allows us to easily perform an arbitrary number of contraction, addition, multiplication by scalar, and partial derivative operations, we can calculate the Christoffel symbols of the Schwarzschild metric directly as follows: (We used SymPy's `Rational` class to create a symbolic 1/2 in the front, otherwise it would have been a numeric 0.5)

```python
from OGRePy.abc import lamda, sigma

WrongSchwarzschildChristoffel = T.s.Rational(1, 2) * Schwarzschild(lamda, sigma) @ (T.PartialD(mu) @ Schwarzschild(nu, sigma) + T.PartialD(nu) @ Schwarzschild(sigma, mu) - T.PartialD(sigma) @ Schwarzschild(mu, nu))
WrongSchwarzschildChristoffel.symbol = "Gamma"
WrongSchwarzschildChristoffel.default_indices = (1, -1, -1)
~WrongSchwarzschildChristoffel
```

However, there is a problem; as we mentioned above, **the Christoffel symbols are not the components of a tensor**, meaning that the Levi-Civita connection does not transform as a tensor does under a coordinate transformation. Indeed, by transforming the metric in the definition, one can show that

$$
\Gamma_ {\mu'\nu'}^{\lambda'} = \frac{\partial x^{\mu}}{\partial x^{\mu'}} \frac{\partial x^{\nu}}{\partial x^{\nu'}} \frac{\partial x^{\lambda'}}{\partial x^{\lambda}} \Gamma_ {\mu\nu}^{\lambda} + \frac{\partial x^{\lambda'}}{\partial x^{\lambda}} \frac{\partial^{2} x^{\lambda}}{\partial x^{\mu'} \partial x^{\nu'}}.
$$

The first term is the familiar transformation rule for a tensor, with one factor of the Jacobian per index as usual. However, there is also an extra second term, meaning that the Christoffel symbols do not transform like a tensor.

(Similarly, you are also not supposed to raise or lower indices in the Christoffel symbols, but in practice, you can do that as long as you make it clear that it's just an abuse of notation - you are only adding factors of the metric, not creating a new tensor representation with different transformation properties.)

Due to the extra transformation term, the tensor object `WrongSchwarzschildChristoffel` we calculated manually above **must not be used**! Instead, we should use the method `christoffel()` of the `Metric` class, which not only performs the calculation automatically for us, but also marks the result as a special tensor object with special transformation properties (more precisely, it will be an instance of the `Christoffel` subclass):

```python
~Schwarzschild.christoffel()
```

These are the same components we got before, as can be seen by explicitly comparing the components of the two tensor objects using the `T.compare()` operator:

```python
T.compare(Schwarzschild.christoffel(), WrongSchwarzschildChristoffel)
```

However, this comparison is only done in the default coordinate system, which is `Spherical`. The crucial difference between `WrongSchwarzschildChristoffel` and `Schwarzschild.christoffel()` is that `WrongSchwarzschildChristoffel` has the correct components **only** in spherical coordinates, while `Schwarzschild.christoffel()` is guaranteed to have the correct components in any coordinate system. In addition, `Schwarzschild.christoffel()` automatically has the correct index configuration `(1, -1, -1)`.

For maximal clarity, let us demonstrate the discrepancy in the coordinate transformation with a simple test metric:

```python
SimpleMetric = T.Metric(
    coords=Cartesian,
    components=T.diag(-x, 1, 1, 1),
)
```

We calculate its Christoffel symbols in two ways. First manually, as we did above for the Schwarzschild metric:

```python
WrongSimpleMetricChristoffel = T.s.Rational(1, 2) * SimpleMetric(lamda, sigma) @ (T.PartialD(mu) @ SimpleMetric(nu, sigma) + T.PartialD(nu) @ SimpleMetric(sigma, mu) - T.PartialD(sigma) @ SimpleMetric(mu, nu))
WrongSimpleMetricChristoffel.symbol = "Gamma"
WrongSimpleMetricChristoffel.default_indices = (1, -1, -1)
~WrongSimpleMetricChristoffel
```

Then, with the built-in `christoffel()` method:

```python
~(SimpleMetricChristoffel := SimpleMetric.christoffel())
```

Note that in this example we used Python's "walrus operator" `:=`, which is an assignment operator which returns the result of the assignment (this is also called an "assignment expression"). This allowed us to easily call `list()` on the result by prepending the `~` operator, instead of having to write an additional line.

The two results have the same components, as expected. But now, let us now transform them to spherical coordinates. First, we transform the tensor object obtained using `christoffel()`:

```python
SimpleMetricChristoffel.list(coords=Spherical)
```

This is the **correct** representation of the Christoffel symbols in spherical coordinates, as the extra term in the transformation was taken into account. However, if we transform the Christoffel symbols we obtained by manual calculation, we get:

```python
WrongSimpleMetricChristoffel.list(coords=Spherical)
```

This is **not** the correct result, since the transformation did not take into account the extra term. To verify that the former result is indeed the correct one, let us change the default coordinate system of `SimpleMetric` to spherical:

```python
SimpleMetric.default_coords = Spherical
```

Now, when we calculate the Christoffel symbols manually from this metric, we will get their correct representation in spherical coordinates. This is because OGRePy always performs the calculations internally in the default coordinates of the first tensor in any operation (e.g. `A` for the contraction `A @ B`), so the result will be calculated **from scratch** in spherical coordinates, instead of being calculated first in Cartesian coordinates and then transformed:

```python
WrongSimpleMetricChristoffel2 = T.s.Rational(1, 2) * SimpleMetric(lamda, sigma) @ (T.PartialD(mu) @ SimpleMetric(nu, sigma) + T.PartialD(nu) @ SimpleMetric(sigma, mu) - T.PartialD(sigma) @ SimpleMetric(mu, nu))
WrongSimpleMetricChristoffel2.symbol = "Gamma"
WrongSimpleMetricChristoffel2.default_indices = (1, -1, -1)
~WrongSimpleMetricChristoffel2
```

Indeed, this is the exact same result we got when we transformed `SimpleMetricChristoffel` to spherical coordinates. We have learned an important lesson: since the Christoffel symbols do not transform like a tensor, we should always use the built-in method `christoffel()` of the `Metric` class to calculate them, which ensures that they transform properly. (Of course, this method is also much more convenient than writing the explicit definition...)

For future use, let us define the **Friedmann-Lemaitre-Robertson-Walker (FLRW) metric**, which describes an expanding universe:

```python
a_t = T.func("a")(t)
FLRW = T.Metric(
    coords=Spherical,
    components=T.diag(-1, a_t**2, a_t**2 * r**2, a_t**2 * r**2 * T.s.sin(theta) ** 2),
)
```

Here, $a(t)$ is the **scale factor**. This metric has the line element:

```python
FLRW.line_element()
```

and the volume element squared:

```python
FLRW.volume_element_squared()
```

Its Christoffel symbols can be easily calculated using `christoffel()`:

```python
~FLRW.christoffel()
```

### The Riemann tensor

The **Riemann curvature tensor** $R^{\rho}{}_ {\sigma\mu\nu}$ can be calculated from the Christoffel symbols using the definition:

$$
R^{\rho}{}_ {\sigma\mu\nu} = \partial_ {\mu}\Gamma^{\rho}_ {\nu\sigma} - \partial_ {\nu}\Gamma^{\rho}_ {\mu\sigma} + \Gamma^{\rho}_ {\mu\lambda} \Gamma^{\lambda}_ {\nu\sigma} - \Gamma^{\rho}_ {\nu\lambda} \Gamma^{\lambda}_ {\mu\sigma}
$$

Even though it contains partial derivatives, it nonetheless transforms like a tensor under a change of coordinates, because the extra transformation terms exactly cancel each other. To calculate this tensor, we can simply write down the formula explicitly with the correct indices contracted:

```python
~(SchwarzschildRiemann := (
    T.PartialD(mu) @ Schwarzschild.christoffel(rho, nu, sigma) - T.PartialD(nu) @ Schwarzschild.christoffel(rho, mu, sigma) + Schwarzschild.christoffel(rho, mu, lamda) @ Schwarzschild.christoffel(lamda, nu, sigma) - Schwarzschild.christoffel(rho, nu, lamda) @ Schwarzschild.christoffel(lamda, mu, sigma)
))
```

Notice that this time we used the `christoffel()` method with arguments corresponding to an index specification; this is simply a shortcut for using the `()` operator on the resulting tensor, as we have done above. Let us change the symbol to $R$, since the current symbol contains the entire formula, and is very cumbersome to display multiple times:

```python
SchwarzschildRiemann.symbol = "R"
~SchwarzschildRiemann
```

Here we run into another issue: we wanted $R^{\rho}{}_ {\sigma\mu\nu}$, but what we actually got was $R_ {\mu}^{\rho}{}_ {\nu\sigma}$, since this is the order of indices from left to right in the definition. There are two ways to fix this in OGRePy. One is to use the `permute()` method. We simply need to call `permute()` with $\mu \rho \nu \sigma$ as the old indices and $\rho \sigma \mu \nu$ as the new indices to fix the issue:

```python
SchwarzschildRiemann = SchwarzschildRiemann.permute(old=[mu, rho, nu, sigma], new=[rho, sigma, mu, nu])
~SchwarzschildRiemann
```

Note that `permute()` creates a new tensor which is equal to the original tensor but with permuted indices; it does not change the original tensor. Tensor components in OGRePy are **immutable**, meaning that they are specified once and for all and cannot be changed. Therefore, the only way to permute the indices, which changes the tensor's components, is to create a new tensor with the permuted components.

Now we have obtained the correct expression for the Riemann tensor of the Schwarzschild metric. In fact, we did not have to specify the old indices explicitly; since `SchwarzschildRiemann` is the result of a tensor calculation, it actually remembers the index specification it obtained as a result of the calculation, and this will be used automatically if the `old` argument is not specified.

The other way to fix this is to wrap the original calculation inside the `calc()` function, which is simply a convenience function that allows us to calculate a tensor, change its symbol, and permute its indices in just one function call. We will show examples of its usage below.

### Exact sign checks with `list()`

The sharp-eyed reader may have noticed that, when we used `list()` on the Schwarzschild Riemann tensor above, it listed, for example, the components $R^{t}{}_ {rtr}$ and $R^{t}{}_ {rrt}$ separately, even though they are the negatives of each other. Unfortunately, SymPy's comparison operation is very rudimentary, comparing the general structure of the expression rather than an actual mathematical comparison. This can be seen on even simpler comparisons - for example, the following comparison will yield `False` even though the two expressions are clearly mathematically equal:

```python
expr1 = 1 / (1 - x)
expr2 = -(1 / (x - 1))
expr1 == expr2
```

This can be resolved by noticing that $a = b$ if and only if $a - b = 0$. So if we subtract one expression from the other, simplify the result, and compare to zero, we will get a correct answer:

```python
T.s.simplify(expr1 - expr2) == 0
```

Normally, `list()` doesn't do this for every single component of the tensor, since that could be a very time-consuming task for large tensors with complicated components. However, we could ask `list()` to perform these more precise comparisons by adding the `exact=True` option:

```python
SchwarzschildRiemann.list(exact=True)
```

You can see that now `list()` correctly identifies all of the components that are negatives of each other, resulting in a much shorter list. If you're wondering why this option only applies to comparing components that are the negative of each other, rather than all comparison - that is because OGRePy automatically simplifies all tensor components in advance, so if two components are the same, they should already be simplified to the exact same expression.

The Riemann tensor with all its indices lowered satisfies the following symmetry and anti-symmetry relations:

$$
R_ {\rho\sigma\mu\nu} = -R_ {\sigma\rho\mu\nu} = -R_ {\rho\sigma\nu\mu} = R_ {\mu\nu\rho\sigma}
$$

We can verify this for the Schwarzschild Riemann tensor using `list()` with `exact=True`:

```python
SchwarzschildRiemann.list(indices=(-1, -1, -1, -1), exact=True)
```

This shows that the symmetry and anti-symmetry relations are indeed satisfied.

### The `riemann()` method and caching

Don't worry - you don't need to write the explicit definition of the Riemann tensor every time you want to calculate it. Instead, OGRePy offers the method `riemann()` of the `Metric` class. For example, for the FLRW metric we get:

```python
FLRW.riemann().list(exact=True)
```

Notice two things here. First, we did not save the result in a variable. The reason is that the results of the `riemann()` method, and in fact all similar methods such as `christoffel()`, are cached. This means that the next time we call `FLRW.riemann()`, we will get the exact same tensor - indeed, it won't just be another tensor with the same components, it will be a reference to the exact same object we got the first time.

Second, calculating the Riemann tensor requires first calculating the Christoffel symbols, which we did not do. Behind the scenes, the `riemann()` method obtains the Christoffel symbols by calling the `christoffel()` method. In turn, the `christoffel()` checks if the Christoffel symbols have already been calculated. If so, it returns the cached results, and if not, it calculated, caches, and returns the results.

As a result, even though we did not call `FLRW.christoffel()` before, the Christoffel symbols have in fact already been calculated and cached for us, so if we call it now we will get the result immediately:

```python
~FLRW.christoffel()
```

The same principle also applies to the other built-in methods for calculating curvature tensors, which we will present below; they always calculate and cache any intermediate tensors in their definitions automatically as needed.

**Standard practice when using OGRePy is to never save the Christoffel symbols, Riemann tensor, etc. in their own variables. Instead, you must call the `christoffel()`, `riemann()`, etc. methods every time you want to access these tensors.**

The reason behind this is to maintain consistency between the metric and its curvature tensors. For example, let's say we decided to redefine the FLRW metric. Since tensor components in OGRePy are immutable, meaning they cannot be changed after the tensor object is created, this means we actually create a new `Metric` object and save it in the same `FLRW` variable. If we previously calculated the Christoffel symbols and saved them in a variable called `FLRWChristoffel`, that variable now stores the Christoffel symbols for the **old** FLRW metric, and is therefore inconsistent with the new one. On the other hand, if we simply use the `FLRW.christoffel()` method, we are guaranteed to always get the correct Christoffel symbols for the metric stored in the `FLRW` variable.

In this documentation, we will continue to create variables for curvature tensors because we will be calculating them explicitly and therefore they are not cached, but in normal use you should instead simply rely on OGRePy's comprehensive caching algorithms.

### The Kretschmann scalar

The Kretschmann scalar is a curvature invariant calculated by contracting all the indices of the Riemann tensor with itself:

$$
K = R_ {\rho\sigma\nu\mu} R^{\rho\sigma\nu\mu}.
$$

Recall that above, we gave the Kretschmann scalar for the Schwarzschild metric as an example of a scalar. Now that we have the Riemann tensor, and the ability to contract tensors, we can actually calculate the Kretschmann scalar from scratch:

```python
Schwarzschild.riemann(rho, sigma, mu, nu) @ Schwarzschild.riemann(rho, sigma, mu, nu)
```

Note that like the `christoffel()` method, the `riemann()` method allows you to pass an index specification for use in calculations. As usual, OGRePy allows you to calculate this curvature tensor directly, using the method `kretschmann()` of the `Metric` class, without typing the formula explicitly.

This method follows the same caching algorithm as `christoffel()` and `riemann()`: it will calculate the Riemann tensor (and as a side effect, the Christoffel symbols) if they have not already been calculated, otherwise it will use the cached results, and it will cache its own result for later use.

### The Ricci tensor and scalar

The **Ricci tensor** $R_ {\mu\nu}$ is the trace of the first and third indices of the Riemann tensor:

$$
R_ {\mu\nu} = R^{\lambda}{}_ {\mu\lambda\nu}.
$$

Therefore, we can calculate it by taking the trace, with the usual OGRePy syntax. For the Schwarzschild metric, the Ricci tensor vanishes:

```python
~Schwarzschild.riemann(lamda, mu, lamda, nu)
```

We can also use the convenience method `ricci_tensor()` of the `Metric` class. For example, here is the Ricci tensor for the FLRW metric:

```python
~FLRW.ricci_tensor()
```

The **Ricci scalar** is the trace of the Ricci tensor:

$$
R = R^{\lambda}{}_ {\lambda} = g^{\mu\nu} R_ {\mu\nu}
$$

We can calculate it from the Ricci tensor by taking the trace:

```python
FLRW.ricci_tensor(mu, mu)
```

Or, as usual, we can simply use the shorthand method `ricci_scalar()` to calculate it directly from the metric:

```python
FLRW.ricci_scalar()
```

### The Einstein tensor

The Einstein tensor $G_ {\mu\nu}$ is given by:

$$
G_ {\mu\nu} = R_ {\mu\nu} - \frac{1}{2} R g_ {\mu\nu}.
$$

As with all other curvature tensors, we can calculate it by combining the previously calculated tensors with the usual syntax:

```python
~(FLRW.ricci_tensor(mu, nu) - T.s.Rational(1, 2) * FLRW.ricci_scalar() @ FLRW(mu, nu))
```

Or we can use the built-in module `einstein()`:

```python
~FLRW.einstein()
```

### Covariant derivatives

The partial derivative has limited use in general relativity, as **it does not transform like a tensor**. Therefore, it is only used in special cases, such as calculating the Christoffel symbols and the Riemann tensor. The **covariant derivative** $\nabla_ {\mu}$ is a generalization of the partial derivative, which does transform like a tensor (as long as it acts on a proper tensor). It is defined as follows:

* On a scalar $\Phi$, the covariant derivative acts as $\nabla_ {\mu} \Phi = \partial_ {\mu} \Phi$.
* On a vector $v^{\mu}$, the covariant derivative acts as $\nabla_ {\mu} v^{\nu} = \partial_ {\mu} v^{\nu} + \Gamma^{\nu}_ {\mu\lambda} v^{\lambda}$.
* On a covector $w_ {\mu}$, the covariant derivative acts as $\nabla_ {\mu} w_ {\nu} = \partial_ {\mu} w_ {\nu} - \Gamma^{\lambda}_ {\mu\nu} w_ {\lambda}$.

More generally, on a rank $(p, q)$ tensor with components $T^{\nu_ {1} \cdots \nu_ {p}}{}_ {\sigma_ {1} \cdots \sigma_ {q}}$, the covariant derivative $\nabla_ {\mu} T^{\nu_ {1} \cdots \nu_ {p}}{}_ {\sigma_ {1} \cdots \sigma_ {q}}$ is defined as follows:

* The first term will be the partial derivative $\partial_ {\mu} T^{\nu_ {1} \cdots \nu_ {p}}{}_ {\sigma_ {1} \cdots \sigma_ {q}}$.
* We **add** one term $\Gamma^{\nu_ {i}}_ {\mu\lambda} T^{\nu_ {1} \cdots \lambda \cdots \nu_ {p}}{}_ {\sigma_ {1} \cdots \sigma_ {q}}$ for each **upper** index $\nu_ {i}$.
* We **subtract** one term $\Gamma^{\lambda}_ {\mu\sigma_ {i}} T^{\nu_ {1} \cdots \nu_ {p}}{}_ {\sigma_ {1} \cdots \lambda \cdots \sigma_ {q}}$ for each **lower** index $\sigma_ {i}$.

Note that even though the covariant derivative is made from ingredients that do not transform like tensors - the partial derivative and the Christoffel symbols - the unwanted terms in the transformations of these ingredients cancel each other exactly, so that in the end, the entire sum does transform like a tensor.

As usual, we can, of course, write down the covariant derivative manually. For example, the covariant divergence of the metric is:

$$
\nabla_ {\mu} g_ {\alpha\beta} = \partial_ {\mu} g_ {\alpha\beta} - \Gamma^{\lambda}_ {\mu\alpha} g_ {\lambda\beta} - \Gamma^{\lambda}_ {\mu\beta} g_ {\alpha\lambda}.
$$

It should vanish, by definition, for any metric; this is what we meant when we said the Levi-Civita connection **preserves** the metric. Indeed, we have for the Schwarzschild metric:

```python
from OGRePy.abc import alpha, beta

~(T.PartialD(mu) @ Schwarzschild(alpha, beta) - Schwarzschild.christoffel(lamda, mu, alpha) @ Schwarzschild(lamda, beta) - Schwarzschild.christoffel(lamda, mu, beta) @ Schwarzschild(alpha, lamda))
```

Much more conveniently, the covariant derivative is represented in OGRePy using the class `CovariantD`. It will automatically add the correct terms, as detailed above, for each of the tensor's indices, using the (possibly cached) Christoffel symbols of the tensor's associated metric. To use it, simply contract it with any tensor, just like `PartialD`. For example, we can check that the covariant derivative of the FLRW metric also vanishes:

```python
~(T.CovariantD(mu) @ FLRW(mu, nu))
```

The covariant divergence of the Einstein tensor is:

$$
\nabla_ {\mu} G^{\mu\nu} = \partial_ {\mu} G^{\mu\nu} + \Gamma^{\mu}_ {\mu\lambda} G^{\lambda\nu} + \Gamma^{\nu}_ {\mu\lambda} G^{\mu\lambda}.
$$

Note that it involves a contraction in the index $\mu$, which becomes a trace in the first Christoffel symbol. This expression vanishes because of the **Bianchi identity**:

$$
\nabla_ {\mu} R^{\mu\nu} = \frac{1}{2} \nabla^{\nu} R \quad \Longrightarrow \quad \nabla_ {\mu} G^{\mu\nu} = 0.
$$

To calculate it in OGRePy, we simply write:

```python
~(T.CovariantD(mu) @ FLRW.einstein(mu, nu))
```

Finally, for a non-trivial result, let us recall that the stress-energy tensor should be **conserved**:

$$
\nabla_ {\mu} T^{\mu\nu} = \partial_ {\mu} T^{\mu\nu} + \Gamma^{\mu}_ {\mu\lambda} T^{\lambda\nu} + \Gamma^{\nu}_ {\mu\lambda} T^{\mu\lambda} = 0.
$$

This follows from the fact that $\nabla_ {\mu} G^{\mu\nu} = 0$, combined with the **Einstein equation**:

$$
G_ {\mu\nu} = \kappa T_ {\mu\nu},
$$

where $\kappa = 8 \pi G$ and $G$ is Newton's gravitational constant. However, unlike $\nabla_ {\mu} G^{\mu\nu} = 0$, the relation $\nabla_ {\mu} T^{\mu\nu} = 0$ is **not** an identity; it is an **energy-momentum conservation equation**. To derive the equation for the FLRW metric, let us first define the rest-frame fluid 4-velocity in this spacetime:

```python
RestVelocity = T.Tensor(metric=FLRW, coords=Spherical, indices=(1,), components=[1, 0, 0, 0], symbol="u")
```

Using the 4-velocity and the metric, we redefine the perfect fluid stress tensor in the FLRW spacetime using the formula $T^{\mu\nu} = (\rho + p) u^{\mu} u^{\nu} + p g^{\mu\nu}$, and give $\rho$ and $p$ spacetime dependence:

```python
rho_t_r_t_p = T.func("rho")(t, r, theta, phi)
p_t_r_t_p = T.func("p")(t, r, theta, phi)
PerfectFluidFLRW = T.calc(
    formula=(rho_t_r_t_p + p_t_r_t_p) * RestVelocity(mu) @ RestVelocity(nu) + p_t_r_t_p * FLRW(mu, nu),
    symbol="T",
)
```

Finally, we take the covariant derivative of the stress tensor:

```python
~(T.CovariantD(mu) @ PerfectFluidFLRW(mu, nu))
```

From demanding that the $t$ component vanishes, we get the following equation:

$$
\dot{\rho} = -3 (\rho + p) \frac{\dot{a}}{a}.
$$

We see that in an expanding universe, energy is not conserved, but rather, the energy density changes with time in a way that depends on the scale factor. If the universe is not expanding, that is, $\dot{a} = 0$, then energy will be conserved.

## Curves and geodesics

### The curve Lagrangian

Consider a **curve**, which is a function $x^{\mu}(\lambda)$ on the manifold where $\lambda$ is called the **curve parameter**. The **curve Lagrangian** of a metric is defined as the norm-squared of the tangent to the curve:

$$
L=g_ {\mu\nu} \dot{x}^{\mu} \dot{x}^{\nu},
$$

where $\dot{x}^{\mu}$ is the first derivative of $x^{\mu}$ with respect to the curve parameter $\lambda$ (in Newton dot notation). We can calculate it using the method `lagrangian()` of the `Metric` class. For example:

```python
Minkowski.lagrangian()
```

```python
Schwarzschild.lagrangian()
```

```python
FLRW.lagrangian()
```

```python
Alcubierre.lagrangian()
```

Notice how `show()` (and `list()` as well) use Newton dot notation for the derivatives of the coordinate functions, for improved readability. To get the full expressions with the explicit derivatives, we can use `components()`. For example:

```python
Minkowski.lagrangian().components()
```

### Geodesic equations from the Lagrangian

By applying the **Euler-Lagrange equations** to the curve Lagrangian:

$$
\frac{\mathrm{d}}{\mathrm{d}\lambda} \left( \frac{\partial L}{\partial\dot{x}^{\mu}} \right) - \frac{\partial L}{\partial x^{\mu}} = 0,
$$

we can obtain the geodesic equations for our spacetime. This is done using the method `geodesic_from_lagrangian()` of the `Metric` class. For the Minkowski metric, the geodesic equations are:

```python
~Minkowski.geodesic_from_lagrangian()
```

Note that this method only calculates the left-hand side of the Euler-Lagrange equations; if we equate the result to zero, we will get the actual geodesics equations. This is hinted at visually by setting the resulting tensor's symbol to 0, so that you actually see the equations when using `list()`. It is trivial to see that the solution to these equations is simply a curve with a constant velocity; in a flat Minkowski spacetime, particles experience no gravitational force, and thus no acceleration (unless some other force acts on them, of course).

The derivatives with respect to the curve parameter $\lambda$ are kept unevaluated in the output of `geodesic_from_lagrangian()`, by using the SymPy `Derivative` class and passing `doit=False` to `simplify()`. This simplifies the equations, and can sometimes help solve them by inspection. In this simple example, since SymPy simplifies the second derivatives even if `doit=False` is used, the second derivatives are actually evaluated (except from the first one, due to the minus sign), but in more complicated metrics they will remain unevaluated.

If we want to activate the derivatives, we simply need to apply the `doit()` method to them. Recall that `list()` and `show()` can apply a function to the tensor's components before displaying them, so we just need to pass a `lambda` function that executes the `doit()` method on each component:

```python
Minkowski.geodesic_from_lagrangian().list(function=lambda x: x.doit())
```

Now the derivatives have been activated.

As with the Lagrangian itself, the geodesic equations are displayed in compact notation when using `list()`. If we want the full expressions with the explicit derivatives, for example in order to pass them to `dsolve()` and actually solve the equations, we can use `components()` - remembering to apply `doit()` to activate the derivatives:

```python
Minkowski.geodesic_from_lagrangian().components().doit()
```

This is a SymPy `Array` where each of the 4 components is a differential equation (with $= 0$ assumed). It can be easily solved by passing it to SymPy's `dsolve()`:

```python
T.s.Array(T.s.dsolve(Minkowski.geodesic_from_lagrangian().components().doit()))
```

Note that this will return a list of solutions, so we converted it back to a SymPy `Array` so it will be displayed nicely in the notebook.

We can similarly find the geodesic equations of other metrics. For example, here they are for the Schwarzschild metric:

```python
~Schwarzschild.geodesic_from_lagrangian()
```

<div style="font-size: smaller">

(Note that the $r$ component is very long, ugly, and complicated. In the [Mathematica version of OGRe](https://github.com/bshoshany/OGRe), we get a much shorter and nicer expression, but if the two expressions are compared by exporting this expression from SymPy to Mathematica (which can be done using the `mathematica()` method), it turns out that the SymPy expression is in fact correct, just not simplified properly. This appears to be an issue with SymPy's `simplify()` function, but it could perhaps be resolved by using [specific SymPy simplification functions](https://docs.sympy.org/latest/modules/simplify/simplify.html), and it is possible that in the future SymPy's simplification algorithms will improve.)

</div>

As another example, here are the geodesic equations for the FLRW metric:

```python
~FLRW.geodesic_from_lagrangian()
```

And finally, here they are for the Alcubierre metric:

```python
~Alcubierre.geodesic_from_lagrangian()
```

The latter is a good example of how we can solve the geodesic equations by inspection. Indeed, it is easy to see that

$$
\dot{x}^{\mu} = (1, 0, 0, vf)
$$

is a solution to this system of equations, since then we have $\dot{x} = \dot{y} = 0$ and $(f v \dot{t} - \dot{z}) = 0$, and both terms in each equation vanish (the last term in the first equation will reduce to $\partial_ {\lambda}(-1)$, which is of course zero). We can check this solution by replacing the coordinate functions with their solutions; since we will be left with $\partial_ {\lambda}(-1)$ in the first equation, we must also activate the derivative.

However, for this we have to write the coordinates explicitly as functions of the curve parameter, even when they are arguments of a function; for example, $v(t)$ should be instead be $v(t(\lambda))$. Luckily, OGRePy offers several ways to simplify this process. The `Coordinates` class contains the method `of_param()`, which returns the coordinates as functions of the curve parameter:

```python
Cartesian.of_param()
```

However, what we really want is an easy way to **replace** the coordinates with functions of the curve parameter. We can obtain a list of such replacements using the method `of_param_dict()`:

```python
param = Cartesian.of_param_dict()
```

Similarly, `of_param_dot()` returns the first derivatives of the coordinates:

```python
Cartesian.of_param_dot()
```

But again, what we really want is a dictionary of replacements, obtained using `of_param_dot_dict()`:

```python
dot = Cartesian.of_param_dot_dict()
```

We can now use the `param` dictionary as an argument to the `subs()` method to replace the arguments in the function $v$ and $f$:

```python
display(v_t.subs(param))
display(f_t_x_y_z.subs(param))
```

The explicit solution is given by

$$
\begin{align*}
    \dot{t}(\lambda) &= 1, \\
    \dot{x}(\lambda) &= 0, \\
    \dot{y}(\lambda) &= 0, \\
    \dot{z}(\lambda) &= v(t(\lambda)) \times f(t(\lambda), x(\lambda), y(\lambda), z(\lambda)). \\
\end{align*}
$$

Let us define a dictionary of replacements which maps each derivative of the coordinates to its solution:

```python
solution = {dot[t]: 1, dot[x]: 0, dot[y]: 0, dot[z]: v_t.subs(param) * f_t_x_y_z.subs(param)}
```

Now all we need to do is perform these substitution, and then simplify. We can do this by passing the dictionary as the value of the `replace` argument to instruct `list()`, and setting `simplify=True` to the expression after doing the replacement. Note that `simplify()` will also automatically call `doit()` to evaluate the derivatives with respect to $\lambda$:

```python
Alcubierre.geodesic_from_lagrangian().list(replace=solution, simplify=True)
```

Since this solution zeros all the elements, it must be the correct solution to the geodesic equations. We could use a substitution procedure similar to the one we used here to verify solutions to any geodesic equations.

This solution indicates that we are traveling with velocity $v$ in the $z$ direction; the warp bubble (inside which, as you recall, $f = 1$) moves whatever is inside it, such as a spaceship, through space at the velocity $v$, but there is no limit on $v$ - it can even be faster than light!

### Geodesic equations from the Christoffel symbols

Another way of obtaining the geodesic equations is using the covariant derivative, and thus the Christoffel symbols:

$$
\dot{x}^{\rho} \nabla_ {\rho} \dot{x}^{\sigma} = 0 \quad \Longrightarrow \quad \ddot{x}^{\sigma} + \Gamma^{\sigma}_ {\mu\nu} \dot{x}^{\mu} \dot{x}^{\nu} = 0.
$$

In OGRePy, we can calculate the left-hand side of this equation using the `geodesic_from_christoffel()` method of the `Metric` class. For example:

```python
~Minkowski.geodesic_from_christoffel()
~Schwarzschild.geodesic_from_christoffel()
~FLRW.geodesic_from_christoffel()
~Alcubierre.geodesic_from_christoffel()
```

Often, you will find that the Lagrangian method produces simpler equations, which can even be solved by inspection, as we did for the Alcubierre metric. This is due to the possibility of leaving the $\lambda$ derivative unevaluated. However, in other cases, the Christoffel method might produce simpler equations. We can clearly see that by comparing the geodesics equations for the Schwarzschild metric obtained via the Lagrangian vs. Christoffel methods.

The best thing to do is to try both methods and see which one produces simpler or nicer results for the specific metric in question. Note that the system of equations obtained using `geodesic_from_lagrangian()` will often be different from the one obtained using `geodesic_from_christoffel()`, but both systems will always have the same solutions.

### Geodesics equations in terms of the time coordinate

If the metric is a spacetime metric, it is often convenient to obtain the geodesic equations in terms of the time parameter, instead of an affine curve parameter. It can be shown that the geodesic equations in terms of the time coordinate are given by

$$
\frac{\mathrm{d}^{2} x^{\sigma}}{\mathrm{d} t^{2}} + \left( \Gamma^{\sigma}_ {\mu\nu} - \Gamma^{0}_ {\mu\nu} \frac{\mathrm{d} x^{\sigma}}{\mathrm{d} t} \right) \frac{\mathrm{d} x^{\mu}}{\mathrm{d} t} \frac{\mathrm{d} x^{\nu}}{\mathrm{d} t} = 0,
$$

where we are assuming the time coordinate is $t$ and it is the first (zero) coordinate. These equations can be obtained using the `geodesic_time_param()` method of the `Metric` class. Note that `geodesic_time_param()` assumes time is the first coordinate, but the coordinate does not need to have the symbol $t$. As an example, the equations for the FLRW metric in Cartesian coordinates in terms of a curve parameter are:

```python
FLRW.geodesic_from_christoffel().list(coords=Cartesian)
```

But in terms of $t$, we only need 3 equations:

```python
FLRW.geodesic_time_param().list(coords=Cartesian)
```

These equations are easier to solve. For simplicity, assume that we are only moving along the x coordinate. Then we only have one equation to solve:

```python
FLRW_eq = FLRW.geodesic_time_param().components(coords=Cartesian, indices=(1,))[1]
```

We are assuming that $\dot{y}(t) = \dot{z}(t) = 0$, so let us remove them from the equation. First, let us get dictionaries mapping the coordinates to functions of time. This is identical to what we did above for the Alcubierre metric, except that this time we pass $t$ to the `of_param` functions so we get functions of $t$ instead of $\lambda$:

```python
param = Cartesian.of_param_dict(t)
```

```python
dot = Cartesian.of_param_dot_dict(t)
```

If we now substitute $\dot{y}(t) = \dot{z}(t) = 0$ in the equation, it simplifies considerably:

```python
FLRW_eq.subs({dot[y]: 0, dot[z]: 0})
```

The solution can be obtained using `dsolve()` in terms of an integral over $a(t)$, passing $x(t)$ in the second argument as the function to solve for. The command to do that is `all_solutions = T.s.Array(T.s.dsolve(FLRWEq.subs({dot[y]: 0, dot[z]: 0}), param[x]))`, but I did not include it in the notebook because it takes a very long time to run. The solution found by SymPy is (after some beautification):

$$
x(t) = C_ {1} \pm \int \frac{1}{a(t) \sqrt{1 + C_ {2} a^{2}(t)}} \mathrm{d}t
$$

We can use the `rhs` property to obtain the right-hand side of the equation, selecting the positive solution (at position 1 of the array): `all_solutions[1].rhs`. By taking the derivative with respect to $t$, `all_solutions[1].rhs.diff(t)`, we can get the coordinate velocity $\dot{x}$ along $x$:

$$
\dot{x}(t) = \frac{1}{a(t) \sqrt{1 + C_ {2} a^{2}(t)}}
$$

### Changing the curve parameter

By default, the curve parameter is $\lambda$. This can be seen by extracting the components of a tensor that uses the curve parameter, such as the Lagrangian:

```python
Minkowski.lagrangian().components()
```

However, sometimes we want to use another parameter - for example, $\tau$ for proper time. To change the parameter, we can set `T.options.curve_parameter` to a symbol of our choice, whether as a string, a TeX symbol, or a SymPy `Symbol`. As an example, let us change it to $\tau$:

```python
T.options.curve_parameter = "tau"
```

Changing the curve parameter applies retroactively to any tensors previously calculated. Behind the scenes, the curve parameter is stored only as a placeholder, which is replaced dynamically with the user's chosen symbol when the components are displayed with `show()` or `list()` or extracted with `components()`. If we now display the components of the Lagrangian again, the curve parameter will be changed to $\tau$:

```python
Minkowski.lagrangian().components()
```

## About the project

### Bug reports and feature requests

This package is under continuous and active development. If you encounter any bugs, or if you would like to request any additional features, please feel free to [open a new issue on GitHub](https://github.com/bshoshany/OGRePy/issues) and I will look into it as soon as I can.

### Contribution and pull request policy

Contributions are always welcome. However, I release my projects in cumulative updates after editing and testing them locally on my system, so **my policy is to never accept any pull requests**. If you open a pull request, and I decide to incorporate your suggestion into the project, I will first modify your code to comply with the project's coding conventions (formatting, syntax, naming, comments, programming practices, etc.), and perform some tests to ensure that the change doesn't break anything. I will then merge it into the next release of the project, possibly together with some other changes. The new release will also include a note in `CHANGELOG.md` with a link to your pull request, and modifications to the documentation in `README.md` as needed.

To create a development environment for this package, download the source code directly from the [GitHub repository](https://github.com/bshoshany/OGRePy), then create a virtual environment in the root folder of the repository [as explained above](#installing-in-a-virtual-environment), activate it, and run `pip install jupyterlab jupytext playwright sympy` to install the development packages, then run `playwright install` to install the browser binaries for HTML to PDF conversion (if desired).

For your convenience, a Python script, [update_packages.py](https://github.com/bshoshany/OGRePy/blob/master/tasks/update_packages.py), is provided in the GitHub repository to allow easily updating all outdated packages. Another script, [compile_docs.py](https://github.com/bshoshany/OGRePy/blob/master/tasks/compile_docs.py), is used to compile the documentation in `README.md` to `.ipynb`, `.html`, and `.pdf` formats. Finally, [cleanup.py](https://github.com/bshoshany/OGRePy/blob/master/tasks/cleanup.py) is used to clean up Python and Jupyter cache folders.

This package was developed in [Visual Studio Code](https://code.visualstudio.com/). The `.vscode` folder is provided in the GitHub repository for your convenience, including tasks for running the above scripts. It is highly recommended to install the following linters:

* [Pyright](https://github.com/microsoft/pyright): install the Pylance [VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).
* [Ruff](https://github.com/astral-sh/ruff): `pip install ruff` and install the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).
* [Pylint](https://www.pylint.org/): `pip install pylint` and install the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint).

Configurations for all 3 linters are included in the `pyproject.toml` file in the GitHub repository.

### Starring the repository

If you found this project useful, please consider [starring it on GitHub](https://github.com/bshoshany/OGRePy/stargazers)! This allows me to see how many people are using my code, and motivates me to keep working to improve it.

### Acknowledgements

I would like to thank my student Jared Wogan, whose undergraduate research project, a preliminary Python port of my Mathematica package OGRe, motivated and inspired me to eventually write my own port, OGRePy. I acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC), RGPIN-2024-04063.

### Copyright and citing

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

For your convenience, this citing information can always be obtained by executing the function `T.cite()`.

Please note that the paper on [arXiv](https://arxiv.org/abs/2409.03803) is not up to date with the latest version of the package. It is only intended to facilitate discovery of this package by scientists, and to enable citing it in scientific research. Documentation for the latest version is always available in the [the GitHub repository](https://github.com/bshoshany/OGRePy).

### Other projects to check out

This package is a Python port of [OGRe](https://github.com/bshoshany/OGRe): An Object-Oriented General Relativity Package for Mathematica. You may also be interested in [`BS::thread_pool`](https://github.com/bshoshany/thread-pool): a fast, lightweight, modern, and easy-to-use C++17 / C++20 / C++23 thread pool library.
