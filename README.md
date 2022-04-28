# urbs

urbs is a [linear programming](https://en.wikipedia.org/wiki/Linear_programming) optimisation model for capacity expansion planning and unit commitment for distributed energy systems. Its name, latin for city, stems from its origin as a model for optimisation for urban energy systems. Since then, it has been adapted to multiple scales from neighbourhoods to continents.

[![Documentation Status](https://readthedocs.org/projects/urbs/badge/?version=latest)](http://urbs.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.594200.svg)](https://doi.org/10.5281/zenodo.594200)

## How to use this repository?

This repository contains four folders:

  * 00 Input connector: This folder containts the Jupyter notebook that converts OED (OpenEnergyDatabase) input data into the Urbs input data

  * 01a Base models: This folder contains all input files, output files and running urbs model for the base scenarios

  * 01b Variation models:  This folder contains all input files, output files and running urbs model for the variation scenarios

  * 02 Output connector:  This folder containts the Jupyter notebook that converts urbs outputs into OED outputs

The running versions of the urbs module is resides within the "runnable_model" folder for each scenario (e.g. the directory "/01a Base models/2016/runnable_model/ for the Base 2016 scenario). The following README file gives an overview on the urbs module itself, and a more detailed documentation can be accessed in https://urbs.readthedocs.io/en/latest/?badge=latest. 

## Features

  * urbs is a linear programming model for multi-commodity energy systems with a focus on optimal storage sizing and use.
  * It finds the minimum cost energy system to satisfy given demand time  series for possibly multiple commodities (e.g. electricity).
  * By default, operates on hourly-spaced time steps (configurable).
  * Thanks to [Pandas](https://pandas.pydata.org), complex data analysis is easy.
  * The model itself is quite small thanks to relying on package [Pyomo](http://www.pyomo.org/).
  * The small codebase includes reporting and plotting functionality.

## Screenshots

<a href="doc/img/plot.png"><img src="doc/img/plot.png" alt="Timeseries plot of 8 days of electricity generation in vertex 'North' in scenario_all_together in hourly resolution: Hydro and biomass provide flat base load of about 50% to cover the daily fluctuating load, while large share of wind and small part photovoltaic generation cover the rest, supported by a day-night storage." style="width:400px"></a>

<a href="doc/img/comparison.png"><img src="doc/img/comparison.png" alt="Bar chart of cumulated annual electricity generation costs for all 5 scenarios defined in runme.py." style="width:400px"></a>

## Installation

There are 2 ways to get all required packages under Windows. We recommend using the Python distribution Anaconda. If you don't want to use it or already have an existing Python (version 3.6 **recommended**, 2.7 is supported as well) installation, you can also download the required packages by yourself..

### Anaconda/Miniconda (recommended)

  1. **[Anaconda (Python 3)](http://continuum.io/downloads)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)**. Choose the 64-bit installer if possible.
     During the installation procedure, keep both checkboxes "modify PATH" and "register Python" selected! If only higher Python versions are available, you can switch to a specific Python Version by typing `conda install python=<version>`
  2. **Packages and Solver**: [GLPK](http://winglpk.sourceforge.net/).
     1. Download the [environment file](https://github.com/tum-ens/urbs/blob/master/urbs-env.yml).
     2. Launch a new command prompt (Windows: Win+R, type "cmd", Enter)
     3. Install it via conda by `conda env create -f urbs-env.yml`.
     4. Each time you open a new terminal for running urbs, you can activate the environment by `conda activate urbs`.

Continue at [Get Started](#get-started).

### Manually (the hard way)

For all packages, best take the latest release or release candidate version. Both 32 bit and 64 bit versions work, though 64 bit is recommended. The list of packages can be found in the [environment file](https://github.com/tum-ens/urbs/blob/master/urbs-env.yml).
  
## Get started

### Developers
Once installation is complete, finally [install git (for version control)](http://git-scm.com/). **Remark:** at step "Adjusting your PATH environment", select "Run Git from the Windows Command Prompt".

Then, in a directory of your choice, clone this repository by:

    git clone https://github.com/tum-ens/urbs.git
    
Continue like the users after they downloaded the zip file. 

### Users

If you are not planning on developing urbs, pick the [latest release](https://github.com/tum-ens/urbs/releases) and download the zip file.

In the downloaded directory, open a execute the runme script by using the following on the command prompt (Windows) or Terminal (Linux). (Depending on what your standard python version is, you might need to call `python3` instead of `python`.):
 
    python runme.py

Some minutes later, the subfolder `result` should contain plots and summary spreadsheets for multiple optimised energy supply scenarios, whose definitions are contained in the run script (watch out for `def scenario` lines).

## Next steps and tips

  1. Head over to the tutorial at http://urbs.readthedocs.io, which goes through runme.py step by step. 
  2. Read the source code of `runme.py` and `comp.py`. 
  3. Try adding/modifying scenarios in `scenarios.py` and see their effect on results.
  4. If you need a nice python editor, think about using [PyCharm](https://www.jetbrains.com/pycharm/download). It has many features including easy Git integration, package management, etc.
  5. Fire up IPython (`ipython3`) and run the scripts from there using the run command: `run runme` and `run comp`. Then use `whos` and inspect the workspace afterwards (`whos`). See what you can do (analyses, plotting) with the DataFrames. Take the `urbs.get_constants`, `urbs.get_timeseries` and `urbs.plot` functions as inspriation and the [Pandas docs](http://pandas.pydata.org/pandas-docs/stable/) as reference.
  
## Further reading

  - If you do not know anything about the command line, read [Command Line Crash Course](https://learnpythonthehardway.org/book/appendixa.html). Python programs are scripts that are executed from the command line, similar to MATLAB scripts that are executed from the MATLAB command prompt.
  - If you do not know Python, try one of the following ressources:
    * The official [Python Tutorial](https://docs.python.org/3/tutorial/index.html) walks you through the language's basic features.
    * [Learn Python the Hard Way](https://learnpythonthehardway.org/book/preface.html). It is meant for programming beginners.
  - The book [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do) best summarises the capabilities of the packages installed here. It starts with IPython, then adds NumPy, slowly fades to pandas and then shows first basic, then advanced data conversion and analysis recipes. Visualisation with matplotlib is given its own chapter, both with and without pandas.
  - For a huge buffet of appetizers showing the capabilities of Python for scientific computing, I recommend browsing this [gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks).
 

## Copyright

Copyright (C) 2014-2019  TUM ENS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
