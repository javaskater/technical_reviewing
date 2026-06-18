## Getting a virtual tests environment

```bash
jmena01@m077-2281091:~/CONSULTANT$ python3 -m venv TestBinary
jmena01@m077-2281091:~/CONSULTANT$ source TestBinary/bin/activate
```

# testing with --prefer-binary

- It compiles with --prefer-bianry

```bash
(TestBinary) jmena01@m077-2281091:~/CONSULTANT$ python -m pip install /home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/req_matplotlib.txt
ERROR: Invalid requirement: '/home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/req_matplotlib.txt'
Hint: It looks like a path. The path does exist.
(TestBinary) jmena01@m077-2281091:~/CONSULTANT$ python -m pip install -r /home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/req_matplotlib.txt
(TestBinary) jmena01@m077-2281091:~/CONSULTANT$ python -m pip install --prefer-binary -r /home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/req_matplotlib.txt
Collecting matplotlib==3.5.1 (from -r /home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/req_matplotlib.txt (line 1))
  Using cached matplotlib-3.5.1.tar.gz (35.3 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
  ###########################
  error: Failed to download any of the following: ['http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz'].  Please download one of these urls and extract it into 'build/' at the top-level of the source repository. # not allowed by the corporate proxy
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for matplotlib
Failed to build matplotlib
ERROR: Could not build wheels for matplotlib, which is required to install pyproject.toml-based projects
```

- same error as before http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz not allowed by the corporate proxy

# Testing with only-binary

- see [pip documentation](https://pip.pypa.io/en/latest/cli/pip_install/)

```bash
(TestBinary) jmena01@m077-2281091:~/CONSULTANT$ python -m pip install --only-binary ":all:" -r /home/jmena01/CONSULTANT/technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/req_matplotlib.txt
ERROR: Ignored the following yanked versions: 3.9.1
ERROR: Could not find a version that satisfies the requirement matplotlib==3.5.1 (from versions: 3.7.3, 3.7.4, 3.7.5, 3.8.0, 3.8.1, 3.8.2, 3.8.3, 3.8.4, 3.9.0rc2, 3.9.0, 3.9.1.post1, 3.9.2, 3.9.3, 3.9.4, 3.10.0rc1, 3.10.0, 3.10.1, 3.10.3, 3.10.5, 3.10.6, 3.10.7, 3.10.8, 3.10.9, 3.11.0rc1, 3.11.0rc2, 3.11.0)
ERROR: No matching distribution found for matplotlib==3.5.1
```

- With the --only-binary option in the \_requirements.txt_il it downloads anyway the latest bersion that has a binary ...
  - it has a different behaviour from just above

# prefer-binary

- It didn't find a binary for the 3.5.1 version of matplotlib. It then compiles from the sources
  - that is the defaut behaviour of --prefer-binary
- is --prefer-binary the default option of pip install ???
