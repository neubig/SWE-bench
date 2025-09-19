# SWE-Gym repository specifications extracted from swegym harness
# These are the additional repositories supported by SWE-Gym that are not in standard SWE-bench

# python/mypy
SPECS_MYPY = {
    "1.0.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# getmoto/moto  
SPECS_MOTO = {
    "4.0.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# conan-io/conan
SPECS_CONAN = {
    "1.59.0": {
        "python": "3.10",
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && apt-get install -y build-essential cmake",
        ],
        "install": "echo 'cython<3' > /tmp/constraint.txt; export PIP_CONSTRAINT=/tmp/constraint.txt; python -m pip install -r conans/requirements.txt; python -m pip install -r conans/requirements_server.txt; python -m pip install -r conans/requirements_dev.txt",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# dask/dask
SPECS_DASK = {
    "2022.12.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# bokeh/bokeh
SPECS_BOKEH = {
    "2.4.0": {
        "python": "3.10", 
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# modin-project/modin
SPECS_MODIN = {
    "0.15.1": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# spyder-ide/spyder
SPECS_SPYDER = {
    "5.4.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# HypothesisWorks/hypothesis
SPECS_HYPOTHESIS = {
    "6.68.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# pydantic/pydantic
SPECS_PYDANTIC = {
    "1.10.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# pandas-dev/pandas
SPECS_PANDAS = {
    "1.5.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# Project-MONAI/MONAI
SPECS_MONAI = {
    "0.9.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# iterative/dvc
SPECS_DVC = {
    "2.34.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# facebookresearch/hydra
SPECS_HYDRA = {
    "1.2.0": {
        "python": "3.10",
        "install": "python -m pip install -e .",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

# Aggregate all SWE-Gym repository specifications
MAP_REPO_VERSION_TO_SPECS_SWEGYM = {
    "python/mypy": SPECS_MYPY,
    "getmoto/moto": SPECS_MOTO,
    "conan-io/conan": SPECS_CONAN,
    "dask/dask": SPECS_DASK,
    "bokeh/bokeh": SPECS_BOKEH,
    "modin-project/modin": SPECS_MODIN,
    "spyder-ide/spyder": SPECS_SPYDER,
    "HypothesisWorks/hypothesis": SPECS_HYPOTHESIS,
    "pydantic/pydantic": SPECS_PYDANTIC,
    "pandas-dev/pandas": SPECS_PANDAS,
    "Project-MONAI/MONAI": SPECS_MONAI,
    "iterative/dvc": SPECS_DVC,
    "facebookresearch/hydra": SPECS_HYDRA,
}