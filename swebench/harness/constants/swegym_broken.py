# Constants - SWE-Gym Repository Specifications
# These are repository specifications for SWE-Gym repositories that are not in the standard SWE-bench

TEST_MOTO = "pytest -n0 -rA"
TEST_CONAN = "pytest -n0 -rA"
TEST_DASK = "pytest -n0 -rA  --color=no"
TEST_MONAI = "pytest -rA "
TEST_DVC = "pytest -rA"
TEST_BOKEH = "pytest -rA -n0"
TEST_MODIN = "pytest -n0 -rA"
TEST_SPYDER = "pytest -n0 -rA"
TEST_HYPOTHESIS = "pytest -n0 -rA --tb=no --no-header"
TEST_PANDAS = "pytest -rA --tb=long"
TEST_HYDRA = "pytest -rA --tb=long"

# python/mypy
SPECS_MYPY = {
    k: {
        "pre_install": [
            "git submodule update --init mypy/typeshed || true",
        ],
        "python": "3.12", 
        # see https://github.com/python/mypy/mypy/test/testcheck.py#L39
        "install": "python -m pip install -r test-requirements.txt; python -m pip install -e .; hash -r",
        "test_cmd": "pytest -rA -k"
    }

SPECS_MYPY.update(
    # Working
    {
        k: {
            "pre_install": [
                "git submodule update --init mypy/typeshed || true",
            ],
            "python": "3.11", 
            "install": "python -m pip install -r test-requirements.txt; python -m pip install -e .; hash -r",
            "test_cmd": "pytest -n0 -rA -k"
        }
        for k in ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]
    }
)

SPECS_MYPY.update(
    # Working
    {
        k: {
            "pre_install": [
                "git submodule update --init mypy/typeshed || true",
            ],
            "python": "3.10", 
            "install": "python -m pip install -r test-requirements.txt; python -m pip install -e .; pip install pytest pytest-xdist; hash -r",
            "test_cmd": "pytest -n0 -rA -k"
        }
        for k in ["0.990", "0.980", "0.970", "0.960","0.950", "0.940"]
    }
)

SPECS_MYPY.update(
    # Working
    {
        k: {
            "pre_install": [
                "git submodule update --init mypy/typeshed || true",
                "sed -i '1i types-typing-extensions==3.7.3' test-requirements.txt"
            ],
            "python": "3.9", 
            # types-typing-extensions is yanked, we need to set a specific version manually
            "install": "python -m pip install -r test-requirements.txt; python -m pip install -e .; pip install pytest pytest-xdist; hash -r;",
            "test_cmd": "pytest -n0 -rA -k"
        }
        for k in ["0.920", "0.910", "0.820", "0.810", "0.800"]
    }
)

SPECS_MYPY.update(
#     {
#         k: {
#             "pre_install": [
#                 "apt-get -y update && apt-get -y upgrade && apt-get install -y gcc",
#                 "apt-get install libxml2-dev libxslt1-dev"
#             ],
#             "python": "3.8", 
#                 "apt-get update && apt-get install -y libenchant-2-dev hunspell-en-us"
#             "install": "python -m pip install -r test-requirements.txt; python -m pip install -e .; pip install pytest; hash -r;",
#             "test_cmd": "pytest -rA -k"
#         }
#         for k in []
#     }
# )

# getmoto/moto
SPECS_MOTO = {
    k: {
        "python": "3.12", 
        # see https://github.com/getmoto/moto/blob/master/CONTRIBUTING.md
        "install": "make init",
        "test_cmd": TEST_MOTO,
    }

# conan-io/conan
SPECS_CONAN = {
    k: {
        "python": "3.10", 
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && apt-get install -y build-essential cmake",
            ],

        "install": "echo 'cython<3' > /tmp/constraint.txt; export PIP_CONSTRAINT=/tmp/constraint.txt; python -m pip install -r conans/requirements.txt; python -m pip install -r conans/requirements_server.txt; python -m pip install -r conans/requirements_dev.txt ",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$PWD",
        ],
    }
}

SPECS_CONAN.update({
    k: {
        "python": "3.10", 
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && apt-get install -y build-essential cmake",
        ],
        "install": "python -m pip install -r conans/requirements.txt; python -m pip install -r conans/requirements_server.txt; python -m pip install -r conans/requirements_dev.txt ",
        "eval_commands": [
            "export PYTHONPATH=${PYTHONPATH:-}:$(pwd)",
        ],
    }
    for k in SPECS_CONAN.keys()
})

# dask/dask
SPECS_DASK = {
    k: {
        # "python": "3.10", 
        "env_patches": [
            # dask installs latest dask from github in environment.yml
            # remove these lines and delay dask installation later
            "sed -i '/- pip:/,/^ *-/d' environment.yml"
        ],
        "packages": "environment.yml",
        "install": 'python -m pip install --no-deps -e .',
        "test_cmd": TEST_DASK,
    }

# Project-MONAI/MONAI
SPECS_MONAI = {
    k: {
        "python": "3.8", 
        # monai's requirements.txt calls each other, hard to standardize in swebench constant format
        # "packages": "requirements.txt",
        # "install": "python -m pip install -U pip; python -m pip install scikit-build; python -m pip install types-pkg-resources==0.1.3 pytest; python -m pip install -U -r requirements-dev.txt; python setup.py develop;",
        # "env_patches": [
        #     # monai installs itself from git 
        #     # remove these lines and delay dask installation later
        #     "sed -i '/^git+https:\/\/github.com\/Project-MONAI\//d' ~/requirements.txt"
        # ],
        "install": "sed -i '/^git+https:\/\/github.com\/Project-MONAI\//d' requirements-dev.txt; python -m pip install types-pkg-resources==0.1.3 pytest; pip install -r requirements-dev.txt;python setup.py develop;",
        "test_cmd": TEST_MONAI,
    }

# iterative/dvc
SPECS_DVC = {
    k: {
        "python": "3.10", 
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && apt-get install -y cmake",
            # fix moto dev version missing issue
            "[ -f setup.py ] && sed -E -i 's/moto==([0-9]+\.[0-9]+\.[0-9]+)\.dev[0-9]+/moto==\\1/' setup.py",
            # fix pyarrow version issue
            "[ -f setup.py ] && sed -i 's/pyarrow==0.15.1/pyarrow==0.16/' setup.py"
            # fix boto version conflict
            "[ -f setup.py ] && sed -i 's/boto3==1.9.115/boto3==1.9.201/' setup.py"
        ],
        "install": 'python -m pip install --upgrade pip wheel GitPython; python -m pip install "cython<3.0.0" && python -m pip install --no-build-isolation pyyaml==5.4.1; python -m pip install git+https://github.com/iterative/mock-ssh-server.git || true; python -m pip install -r tests/requirements.txt || true; python -m pip install -r test-requirements.txt || true; python -m pip install -e ".[tests,dev,all_remotes,all,testing]";',
        "test_cmd": TEST_DVC,
    }

for k in ['0.1', '0.8', '0.9', '0.12', '0.13', '0.14', '0.15', '0.16', '0.17', '0.18', '0.19', '0.20', '0.21', '0.22', '0.23', '0.24', '0.27', '0.28', '0.29', '0.30', '0.31', '0.32', '0.33', '0.34', '0.35', '0.40', '0.41', '0.50', '0.51', '0.52', '0.53', '0.54', '0.55', '0.56', '0.57', '0.58', '0.59', '0.60', '0.61', '0.62', '0.63', '0.65', '0.66', '0.68', '0.69', '0.70', '0.71', '0.74', '0.75', '0.76', '0.77', '0.78', '0.80', '0.81', '0.82', '0.83', '0.84', '0.85', '0.86', '0.87', '0.88', '0.89', '0.90', '0.91', '0.92', '0.93', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13', '2.15', '2.17', '2.19', '2.20', '2.21', '2.22', '2.23', '2.24', '2.27', '2.28', '2.30', '2.33', '2.34', '2.35', '2.38', '2.41', '2.43', '2.44', '2.45', '2.46', '2.48', '2.50', '2.51', '2.52', '2.54', '2.55', '2.56', '2.57', '2.58', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.10', '3.11', '3.12', '3.13', '3.14', '3.15', '3.17', '3.19', '3.23', '3.24', '3.28', '3.29', '3.36', '3.37', '3.38', '3.43', '3.47', '3.48', '3.49']
}
for k in [
    '0.1', '0.8', '0.9', '0.12', '0.13', '0.14', '0.15', '0.16', '0.17', '0.18', '0.19', '0.20', '0.21', '0.22', '0.23', '0.24', '0.27', '0.28', '0.29', '0.30', '0.31', '0.32', '0.33', '0.34', '0.35', '0.40', '0.41', '0.50', '0.51', '0.52', '0.53', '0.54', '0.55', '0.56', '0.57', '0.58', '0.59', '0.60', '0.61', '0.62', '0.63', '0.65', '0.66', '0.68', '0.69', '0.70', '0.71', '0.74', '0.75', '0.76', '0.77', '0.78', '0.80', '0.81', '0.82', '0.83', '0.84', '0.85', '0.86', '0.87', '0.88', '0.89', '0.90', '0.91', '0.92', '0.93', ]:
    SPECS_DVC[k]['python'] = '3.8'


for k in [
    '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13', '2.15', '2.17', '2.19', '2.20', '2.21', '2.22', '2.23', '2.24', '2.27', '2.28', '2.30', '2.33', '2.34', '2.35', '2.38', '2.41', '2.43', '2.44', '2.45', '2.46', '2.48', '2.50', '2.51', '2.52', '2.54', '2.55', '2.56', '2.57', '2.58', '3.0', '3.1', '3.2', '3.3', 
]:
    SPECS_DVC[k]['python'] = '3.9'


# bokeh/bokeh
SPECS_BOKEH = {
    k: {
        "python": "3.10", 
        "packages": "environment.yml",
        "pre_install": [
            "cd bokehjs && npm install --location=global npm && npm ci && cd ../"
        ],
        "install": "python -m pip install -e .; python -m pip install bokeh_sampledata;",
        "test_cmd": TEST_BOKEH,
    }

SPECS_BOKEH.update({
    k: {
        "python": "3.8", 
        "packages": "environment.yml",
        "env_patches": [
            ": \"${CONDA_MKL_INTERFACE_LAYER_BACKUP:=''}\"",
            # "sed -i 's/  - setuptools/  - setuptools<66/' environment.yml"
        ],
        "pre_install": [
            "cd bokehjs && npm install --location=global npm && npm ci && cd ../",
        ],
        "install": 'pip install "setuptools<66" "jinja2<3.1"; printf "1\n" | python setup.py develop; bokeh sampledata;',
        "test_cmd": TEST_BOKEH,
    }
    for k in ['2.0', '2.1', '2.3', '2.4']
})

SPECS_BOKEH.update({
    k: {
        "python": "3.8", 
        "packages": "environment.yml",
        "env_patches": [
            ": \"${CONDA_MKL_INTERFACE_LAYER_BACKUP:=''}\"",
            # "sed -i 's/  - setuptools/  - setuptools<66/' environment.yml"
        ],
        "pre_install": [
            "cd bokehjs && npm install --location=global npm && npm ci && cd ../",
        ],
        "install": 'pip install "setuptools<66" "jinja2<3.1"; printf "1\n" | python setup.py develop; bokeh sampledata;',
        "test_cmd": TEST_BOKEH,
    }
    for k in ['0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '0.10', '0.11', '0.12', '0.13', '0.1181316818', '1.0', '1.1', '1.2', '1.3', '1.4']
})

# modin-project/modin
SPECS_MODIN = {
    k: {
        "python": "3.9", 
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && apt-get install -y libpq-dev",
        ],
        "packages": "environment.yml",
        "install": "python -m pip install -e .;",
        # "install": "python -m pip install 'numpy<2.0'; python -m pip install --upgrade Cython; python -m pip install -r requirements-dev.txt; python -m pip install -e .",
        "test_cmd": TEST_MODIN,
    }

for k in ['0.1', '0.2', '0.3', '0.4', '0.6', '0.8', '0.9', '0.10', '0.11', '0.12', '0.13', '0.14', '0.15', '0.16', '0.17', '0.18', '0.19', '0.20', '0.21', '0.22', '0.23', '0.24', '0.25', '0.26', '0.27', '0.28', '0.29', '0.30']
}
for k in  ['0.1', '0.2', '0.3', '0.4', '0.6', '0.8', '0.9', '0.10', '0.11', '0.12', '0.13', '0.14', '0.15', '0.16', '0.17', '0.18', '0.19']:
    SPECS_MODIN[k]['python'] = '3.8'


# spyder-ide/spyder
SPECS_SPYDER = {
    k: {
        "python": "3.9", 
        "packages": "environment.yml",
        "pre_install": [
            "conda env update --file requirements/linux.yml",
            "conda env update --file requirements/tests.yml"
        ],
        "install": "python -m pip install -e .;",
        # "install": "python -m pip install 'numpy<2.0'; python -m pip install --upgrade Cython; python -m pip install -r requirements-dev.txt; python -m pip install -e .",
        "test_cmd": TEST_SPYDER,
    }

# HypothesisWorks/hypothesis
SPECS_HYPOTHESIS = {
    k: {
        "python": "3.10", 
        "packages": "requirements.txt", # this installs tools.txt
        "install": "python -m pip install -r requirements/test.txt; python -m pip install -e hypothesis-python/;",
        "test_cmd": TEST_HYPOTHESIS,
    }

for k in ['3.55', '3.61', '3.60', '3.59', '3.63', '3.66', '3.67', '3.68', '3.69', '3.70', '5.1', '5.5', '5.24', '5.6', '5.9', '5.8', '5.10', '5.12', '5.15', '5.20', '5.23', '5.36', '5.32', '5.33', '5.38', '5.41', '5.42', '5.43', '5.47', '6.1', '6.4', '6.6', '6.8', '6.14', '6.13', '6.18', '6.21', '6.24', '6.28', '6.29', '3.73', '3.71', '3.75', '3.79', '3.82', '3.85', '3.88', '4.0', '3.86', '4.2', '4.4', '4.15', '4.12', '4.14', '4.18', '4.23', '4.24', '4.26', '4.32', '4.38', '4.40', '4.42', '4.46', '4.44', '4.50', '4.54', '4.55', '5.2', '5.4', '6.30', '6.31', '6.36', '6.40', '6.43', '6.53', '6.45', '6.46', '6.47', '6.50', '6.54', '6.59', '6.62', '6.66', '6.71', '6.74', '6.77', '6.81', '6.87', '6.88', '6.93', '6.98', '6.99', '6.100', '6.102']
}
for k in ['3.55', '3.61', '3.60', '3.59', '3.63', '3.66', '3.67', '3.68', '3.69', '3.70', '5.1', '5.5', '5.24', '5.6', '5.9', '5.8', '5.10', '5.12', '5.15', '5.20', '5.23', '5.36', '5.32', '5.33', '5.38', '5.41', '5.42', '5.43', '5.47', '6.1', '6.4', '6.6', '6.8', '6.14', '6.13', '6.18', '6.21', '6.24', '6.28', '6.29', '3.73', '3.71', '3.75', '3.79', '3.82', '3.85', '3.88', '4.0', '3.86', '4.2', '4.4', '4.15', '4.12', '4.14', '4.18', '4.23', '4.24', '4.26', '4.32', '4.38', '4.40', '4.42', '4.46', '4.44', '4.50', '4.54', '4.55', '5.2', '5.4', '6.30', '6.31']:
    SPECS_HYPOTHESIS[k]['python'] = '3.9'



# pydantic/pydantic
SPECS_PYDANTIC = {
    k: {
        "python": "3.8",
        "pre_install": [
            "apt-get update && apt-get install -y locales",
            "apt-get install -y pipx",
            "pipx ensurepath",
            # well, this in fact uses python 3.10 as default by pipx
            "pipx install pdm",
            'export PATH="$HOME/.local/bin:$PATH"',
            "which python",
            "python --version",
        ],
        "install": 'export PATH="$HOME/.local/bin:$PATH"; pdm add pre-commit; make install;',
        "test_cmd": TEST_PYDANTIC,
    }

# pandas-dev/pandas
SPECS_PANDAS = {
    k: {
        "packages": "environment.yml",
        "pre_install": [
            "git remote add upstream https://github.com/pandas-dev/pandas.git",
            "git fetch upstream --tags"
        ],
        "install": "python -m pip install -ve . --no-build-isolation -Ceditable-verbose=true; pip uninstall pytest-qt -y;",
        "test_cmd": TEST_PANDAS,
    }

# facebookresearch/hydra
SPECS_HYDRA = {
    k: {
        "python": "3.8",
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && apt-get install -y openjdk-17-jdk openjdk-17-jre",
        ],
        "install": "pip install -r requirements/dev.txt; pip install -e .;",
        "test_cmd": TEST_HYDRA,
    }

# Constants - SWE-Gym Repository Version to Specs Mapping
MAP_REPO_VERSION_TO_SPECS_SWEGYM = {
    "python/mypy": SPECS_MYPY,
    "getmoto/moto": SPECS_MOTO,
    "conan-io/conan": SPECS_CONAN,
    "dask/dask": SPECS_DASK,
    "Project-MONAI/MONAI": SPECS_MONAI,
    "iterative/dvc": SPECS_DVC,
    "bokeh/bokeh": SPECS_BOKEH,
    "modin-project/modin": SPECS_MODIN,
    "spyder-ide/spyder": SPECS_SPYDER,
    "HypothesisWorks/hypothesis": SPECS_HYPOTHESIS,
    "pydantic/pydantic": SPECS_PYDANTIC,
    "pandas-dev/pandas": SPECS_PANDAS,
    "facebookresearch/hydra": SPECS_HYDRA,
}