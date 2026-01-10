# See the accompagnying WebSite
* [README.md](https://github.com/KrisNguyen135/bayesian-optimization-in-action/blob/main/README.md#installation)
  * we have to install [Pythonrequirement file](https://github.com/KrisNguyen135/bayesian-optimization-in-action/blob/main/requirements.txt)
  * We do it in a virtual environment see [Previous installation Tests](./1-PythonInstallationFirstTry.md)
# on my WSL
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ source .BayesianOptimisation/bin/activate
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python --version
Python 3.12.3
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python -m pip install -r bayesian-optimization-in-action/requirements.txt
/home/jpmena/CONSULTANT/.BayesianOptimisation/bin/python: No module named pip
```
## pip is present but it cannot call a pip module
```bash

jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/.BayesianOptimisation/bin$ ./pip
Traceback (most recent call last):
  File "/home/jpmena/CONSULTANT/.BayesianOptimisation/bin/./pip", line 5, in <module>
    from pip._internal.cli.main import main
ModuleNotFoundError: No module named 'pip'
```
## Solution erase and create the virtual env
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ rm -rf .BayesianOptimisation # remove the virtual env
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python3 -m venv .BayesianOptimisation # create again the virtual env
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ source .BayesianOptimisation/bin/activate # go to the virtual env
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python3 -m pip list # This time it works
Package Version
------- -------
pip     24.0
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$
```
# Retry the [requirement file](https://github.com/KrisNguyen135/bayesian-optimization-in-action/blob/main/requirements.txt) in the virtual env
* The [same documentation as for the virtual env](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-a-requirements-file)
```bash
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python3 -m pip install -r bayesian-optimization-in-action/requirements.txt 2>&1 | tee requirement.log
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ééé
Collecting notebook==6.4.6 (from -r bayesian-optimization-in-action/requirements.txt (line 6))
  Downloading notebook-6.4.6-py3-none-any.whl.metadata (2.4 kB)
ERROR: Ignored the following versions that require a different python version: 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
ERROR: Could not find a version that satisfies the requirement numpy==1.21.4 (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0, 1.11.1, 1.11.2, 1.11.3, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 1.13.3, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.21.0, 1.21.1, 1.22.0, 1.22.1, 1.22.2, 1.22.3, 1.22.4, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.23.5, 1.24.0, 1.24.1, 1.24.2, 1.24.3, 1.24.4, 1.25.0, 1.25.1, 1.25.2, 1.26.0, 1.26.1, 1.26.2, 1.26.3, 1.26.4, 2.0.0, 2.0.1, 2.0.2, 2.1.0, 2.1.1, 2.1.2, 2.1.3, 2.2.0, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 2.3.0, 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.4.0rc1, 2.4.0, 2.4.1)
ERROR: No matching distribution found for numpy==1.21.4
```
## What did it install??
* it does show nothing ...
* install all or nothing
## [last numpy version](https://numpy.org/doc/2.1/release/1.26.0-notes.html)
* I replaced the numpy line in the [requirements.txt](https://github.com/KrisNguyen135/bayesian-optimization-in-action/blob/main/requirements.txt)  with
```bash
numpy==1.26.0
```
# Python Scikitlearn
* code error in the I changed for the [librairy used in RCP217](https://github.com/javaskater/rcp217_project/blob/main/docs/INSTALLATIONS/PYTHONLIBS.md)
```bash
scikit-learn==1.6.1
```
* [Latest version of Scipy](https://scipy.org/news/)
* I chosed:
```bash
scipy==1.16.3
```
## The problem is now on seaborn
* [latest versions](https://seaborn.pydata.org/whatsnew/index.html)
* The problem is with [torch old version](https://pypi.org/project/torch/#history)
  * I test
```bash
seaborn==0.13.2
torch==2.9.1
```
# The problem is now torchvision not compatible
[links between versions of torch and torchvision](https://pytorch.org/get-started/previous-versions/)
* now my requirements.txt is
```bash
botorch==0.6.0
gpytorch==1.6.0
jupyter==1.0.0
jupyterlab==3.2.5
matplotlib==3.5.1
notebook==6.4.6
numpy==1.26.0
pandas==1.3.5
scikit-learn==1.8.0
scipy==1.16.3
seaborn==0.13.2
torch==2.9.1
torchvision==0.24.0 # to make it compatible with torch and my python distribution (3.12.3)
tqdm==4.62.3
```
* It goes far away but we have a dependency problem
```bash
ERROR: Cannot install -r bayesian-optimization-in-action/requirements.txt (line 1), -r bayesian-optimization-in-action/requirements.txt (line 13), -r bayesian-optimization-in-action/requirements.txt (line 2) and torch==2.9.1 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested torch==2.9.1
    botorch 0.6.0 depends on torch>=1.9
    gpytorch 1.6.0 depends on torch>=1.9
    torchvision 0.24.0 depends on torch==2.9.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
```
# TOSOLVE (TODO)
* I saveed the [log on Git](./logs/requirement.log)