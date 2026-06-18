# Installation on my PC at work running Ubuntu 24.04

```bash
jmena01@m077-2281091:~/CONSULTANT$ python3 -m venv .BayesianOptimisation
jmena01@m077-2281091:~/CONSULTANT$ python3 --version
Python 3.12.3
# we enter the virtual environment
jmena01@m077-2281091:~/CONSULTANT$ source .BayesianOptimisation/bin/activate
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT$ which python
/home/jmena01/CONSULTANT/.BayesianOptimisation/bin/python
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT$ python --version
Python 3.12.3
```

# Testing the [requirements.txt file](https://github.com/KrisNguyen135/bayesian-optimization-in-action/blob/main/requirements.txt)

- It is dated from 3 years ago
- I put it with the md files

```bash
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT$ cp -pv bayesian-optimization-in-action/requirements.txt ~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/
'bayesian-optimization-in-action/requirements.txt' -> '/home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/requirements.txt'
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT$ cd /home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$
```

# First Try

I changed

```bash
botorch==0.6.0
gpytorch==1.6.0
jupyter==1.0.0
jupyterlab==3.2.5
matplotlib==3.5.1
notebook==6.4.6
numpy==1.26.0 # originally 1.21.4
pandas==3.0.3 # originally 1.3.5
scikit-learn==1.9.0 # originally 1.0.1
scipy==1.17.1 #originally 1.7.3 linked to scikit-learn
seaborn==0.13.2
torch==2.12.0
torchvision==0.27.0
tqdm==4.62.3
```

# I finally downloaded

- a lot of cuda big libraries (More thant 1Gb of libraries) see [the requirmentts' log file](./requirement_16062026_125313.log)

# trying to compile matplotlib

```bash
chmod a-w builds/unix/freetype2.pc.tmp
      mv builds/unix/freetype2.pc.tmp builds/unix/freetype2.pc
      Extracting /project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz
      Building freetype in build/freetype-2.6.1
      error: Failed to download any of the following: ['http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz'].  Please download one of these urls and extract it into 'build/' at the top-level of the source repository.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for matplotlib
Successfully built gpytorch
Failed to build matplotlib
ERROR: Could not build wheels for matplotlib, which is required to install pyproject.toml-based projects
```

- **http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz** is indeed blocked by the corporates's Firewall
  - same for *http://www.qhull.org/*

## WHAT COMES NEXT

- try to install matplotlib alone in an other virtual environment
- [--prefer-binary --only-binary](https://pip.pypa.io/en/stable/cli/pip_install/#pip-install-examples)
  - to not compile for example matplotlib
  - [more about requirement files](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
    - prefer-binary can be put on the line itself

```bash
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ python -m pip install -r requirements.txt
Usage: __main__.py [options]

ERROR: Invalid requirement: matplotlib==3.5.1 --only-binary
__main__.py: error: --only-binary option requires 1 argument

```

- the requirements.txt becomes

```
botorch==0.6.0
gpytorch==1.6.0
jupyter==1.0.0
jupyterlab==3.2.5
--only-binary matplotlib==3.5.1
notebook==6.4.6
numpy==2.4.6
pandas==3.0.3
scikit-learn==1.9.0
scipy==1.17.1
seaborn==0.13.2
torch==2.12.0
torchvision==0.27.0
tqdm==4.62.3
```

# SUCCESS !!!

- the 18th of june 10 a.m.

## in the log mathplotlib is downloaded no more compiled

```bash
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ python -m pip install -r requirements.txt
#####################################""
Downloading matplotlib-3.11.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (10.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.0/10.0 MB 17.4 MB/s eta 0:00:00
#################################################""
```

- it installs the 3.11 version which is the latest version (11th of june 2026) at that time because it is the only one which has a binary ???
  - [I only see source code for the 3.5.1 on gitHub ](https://github.com/matplotlib/matplotlib/releases/tag/v3.5.1)

## If I relaunch an install

```bash
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ python -m pip install -r requirements.txt 2>&1 | tee requirements.log
```

- It just tell me that all requirements are already completed
  - see [the log of the output console](./requirements.log)

```bash
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ grep matplotlib requirements.log | head -1
Requirement already satisfied: matplotlib!=3.6.1,>=3.4 in /home/jmena01/CONSULTANT/.BayesianOptimisation/lib/python3.12/site-packages (from seaborn==0.13.2->-r requirements.txt (line 11)) (3.11.0)
```

## Installed version

```bash
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ python -m pip freeze | grep matplot
matplotlib==3.11.0 # While such a big version it is the version of june 11 2026!!!
matplotlib-inline==0.2.2
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ python -m pip freeze | grep numpy
numpy==2.4.6
(.BayesianOptimisation) jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION$ python -m pip freeze | grep jupyter
jupyter==1.0.0
jupyter-console==6.6.3
jupyter-server==1.24.0
jupyter_client==8.9.1
jupyter_core==5.9.1
jupyterlab==3.2.5
jupyterlab_pygments==0.3.0
jupyterlab_server==2.28.0
jupyterlab_widgets==3.0.16
```

- explanation of the matplotlib version see [trying to install a 3.5.1 version in only binary](./4-InstallASpecificVersionInBinary.md)
