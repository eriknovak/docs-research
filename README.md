# Research Docs

This repository contains the code for the research documentation project.

## ☑️ Requirements

Before starting the project make sure these requirements are available:

- [python][python]. For executing the code in this project.
- [git][git]. For versioning your code.

## 🛠️ Setup

### Create a python environment

First create the virtual environment where the service will store all the modules.

#### Using virtualenv

Using the `virtualenv` command, run the following commands:

```bash
# install the virtual env command
pip install virtualenv

# create a new virtual environment
virtualenv -p python ./.venv

# activate the environment (UNIX)
./.venv/bin/activate

# activate the environment (WINDOWS)
./.venv/Scripts/activate

# deactivate the environment (UNIX & WINDOWS)
deactivate
```

#### Using conda

Install [conda][conda], a program for creating python virtual environments. Then run the following commands:

```bash
# create a new virtual environment
conda create --name docs-research python=3.8 pip

# activate the environment
conda activate docs-research

# deactivate the environment
deactivate
```

### Install

To install the requirements run:

```bash
pip install -e .
```

## 🚀 Run

To start live-reloading the documentation run:

```bash
mkdocs serve
```

[python]: https://www.python.org/
[conda]: https://www.anaconda.com/
[git]: https://git-scm.com/
