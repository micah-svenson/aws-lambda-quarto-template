# Quarto Project Template

This project template is for a generic python based quarto project. It contains boiler plate for a python package, and a basic quarto project folder.

## Installation and Use

1. create and activate a python virtual environment

```bash
python3 -m venv venv
source ./venv/bin/activate
```

1. Install requirements, including the editable python package.

```bash
pip install -r requirements.txt
```

1. To generate quarto projects

```bash
quarto render reports/
```

## Organization

### reports

The `reports` folder contains a single quarto project. There is room for multiple quarto projects under this folder

### src

The `src` folder contains boiler plate for a python package to help organize code that will be run in the reports.

The pyproject.toml file in this repo is used to build the src folder into a package


### requirements.txt

Requirements.txt will install the src package as a dependency as well as any other items.