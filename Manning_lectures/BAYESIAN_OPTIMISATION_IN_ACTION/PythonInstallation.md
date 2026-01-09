# The installation is 
## explained p xxiii (25/426) of [Manning Book Bayesian Optimisation in Action](https://www.manning.com/books/bayesian-optimization-in-action)
* in order not to pollute our main des environment
* we'll use pip in virtual environment like explained int the [Python official package documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

# Creating a virtual environment (for our python3 and all its dependencies)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python3 -m venv .BayesianOptimisation
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/jpmena/CONSULTANT/.BayesianOptimisation/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']
# we install the python3-venv package as suggested before
## But before I have  to do an apt update followed by an apt upgrade
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ sudo apt install python3-venv
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libopengl0
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  python3-distutils python3-lib2to3 python3-pip-whl python3-setuptools-whl python3.10-venv
The following NEW packages will be installed:
  python3-distutils python3-lib2to3 python3-pip-whl python3-setuptools-whl python3-venv python3.10-venv
0 upgraded, 6 newly installed, 0 to remove and 2 not upgraded.
Need to get 1685 kB/2691 kB of archives.
After this operation, 4062 kB of additional disk space will be used.
Do you want to continue? [Y/n] 
### ............................
Setting up python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.1) ...
Setting up python3-pip-whl (22.0.2+dfsg-1ubuntu0.4) ...
Setting up python3-lib2to3 (3.10.8-1~22.04) ...
Setting up python3-distutils (3.10.8-1~22.04) ...
Setting up python3.10-venv (3.10.12-1~22.04.3) ...
Setting up python3-venv (3.10.6-1~22.04) ...
```
* I retry the command of installing a virtual environment for the examples of the book:
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ python3 -m venv .BayesianOptimisation # no output it worked
# To activate the new variables in the path
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ source .BayesianOptimisation/bin/activate
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ which python # the prompt did change
/home/jpmena/CONSULTANT/.BayesianOptimisation/bin/python # We have a new Python PATH
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ deactivate #simplement pour quitter l'environnement virtuel
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$
```
## Getting the requirements.txt
* I got the requirements.txt file at the root of [the Code Associated with the Book](https://github.com/KrisNguyen135/bayesian-optimization-in-action) it is **~/CONSULTANT/bayesian-optimization-in-action-main/placeholder.txt**
## Test1:
### Going virutal env _.BayesianOptimisation/bin/activate_
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action-main$ source ../.BayesianOptimisation//bin/activate
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action-main
```
## installing using the requirement file
* The [same documentation as for the virtual env](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-a-requirements-file) tells us the command using a requirement file
```bash
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action-main$ python3 -m pip install -r requirements.txt 
Collecting botorch==0.6.0
  Downloading botorch-0.6.0-py3-none-any.whl (325 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 326.0/326.0 KB 156.5 kB/s eta 0:00:00
Collecting gpytorch==1.6.0
  Downloading gpytorch-1.6.0.tar.gz (310 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 310.6/310.6 KB 125.4 kB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting jupyter==1.0.0
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting jupyterlab==3.2.5
  Downloading jupyterlab-3.2.5-py3-none-any.whl (8.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.6/8.6 MB 226.1 kB/s eta 0:00:00
Collecting matplotlib==3.5.1
  Downloading matplotlib-3.5.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.9/11.9 MB 219.9 kB/s eta 0:00:00
Collecting notebook==6.4.6
  Downloading notebook-6.4.6-py3-none-any.whl (9.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 230.6 kB/s eta 0:00:00
Collecting numpy==1.21.4
  Downloading numpy-1.21.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (15.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.9/15.9 MB 192.3 kB/s eta 0:00:00
Collecting pandas==1.3.5
  Downloading pandas-1.3.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.5/11.5 MB 277.2 kB/s eta 0:00:00
Collecting scikit-learn==1.0.1
  Downloading scikit-learn-1.0.1.tar.gz (6.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 276.0 kB/s eta 0:00:00
  Installing build dependencies ... \
    Installing build dependencies ... \
done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [53 lines of output]
      Partial import of sklearn during the build process.
      C compiler: x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -fPIC
      
      compile options: '-c'
      x86_64-linux-gnu-gcc: test_program.c
      
      
      [Errno 2] No such file or directory: 'x86_64-linux-gnu-gcc'
      
      
      Traceback (most recent call last):
        File "/home/jpmena/CONSULTANT/.BayesianOptimisation/lib/python3.10/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 363, in <module>
          main()
        File "/home/jpmena/CONSULTANT/.BayesianOptimisation/lib/python3.10/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 345, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
        File "/home/jpmena/CONSULTANT/.BayesianOptimisation/lib/python3.10/site-packages/pip/_vendor/pep517/in_process/_in_process.py", line 164, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 366, in prepare_metadata_for_build_wheel
          self.run_setup()
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 487, in run_setup
          super().run_setup(setup_script=setup_script)
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 311, in run_setup
          exec(code, locals())
        File "<string>", line 319, in <module>
        File "<string>", line 315, in setup_package
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/core.py", line 135, in setup
          config = configuration()
        File "<string>", line 201, in configuration
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/misc_util.py", line 1014, in add_subpackage
          config_list = self.get_subpackage(subpackage_name, subpackage_path,
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/misc_util.py", line 980, in get_subpackage
          config = self._get_configuration_from_setup_py(
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/misc_util.py", line 922, in _get_configuration_from_setup_py
          config = setup_module.configuration(*args)
        File "/tmp/pip-install-_psswc8v/scikit-learn_81df2de8e04944eeafc2db9a380939f0/sklearn/setup.py", line 85, in configuration
          cythonize_extensions(top_path, config)
        File "/tmp/pip-install-_psswc8v/scikit-learn_81df2de8e04944eeafc2db9a380939f0/sklearn/_build_utils/__init__.py", line 47, in cythonize_extensions
          basic_check_build()
        File "/tmp/pip-install-_psswc8v/scikit-learn_81df2de8e04944eeafc2db9a380939f0/sklearn/_build_utils/pre_build_helpers.py", line 113, in basic_check_build
          compile_test_program(code)
        File "/tmp/pip-install-_psswc8v/scikit-learn_81df2de8e04944eeafc2db9a380939f0/sklearn/_build_utils/pre_build_helpers.py", line 70, in compile_test_program
          ccompiler.compile(
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/ccompiler.py", line 89, in <lambda>
          m = lambda self, *args, **kw: func(self, *args, **kw)
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/ccompiler.py", line 366, in CCompiler_compile
          single_compile(o)
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/ccompiler.py", line 326, in single_compile
          self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/ccompiler.py", line 89, in <lambda>
          m = lambda self, *args, **kw: func(self, *args, **kw)
        File "/tmp/pip-build-env-nazhq_t0/overlay/lib/python3.10/site-packages/numpy/distutils/unixccompiler.py", line 57, in UnixCCompiler__compile
          raise CompileError(msg) from None
      distutils.errors.CompileError: Command "x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -fPIC -c test_program.c -o objects/test_program.o" failed with exit status 127
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
```
* *[Errno 2] No such file or directory: 'x86_64-linux-gnu-gcc'*
* [Installing gcc on Ubuntu 22.04](https://www.cherryservers.com/blog/how-to-install-gcc-on-ubuntu)
# Second try for the installation
* Installing __gcc__
```bash
# after an update and an upgrade
jpmena@LAPTOP-E2MJK1UO:~$ sudo apt install gcc
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libopengl0
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  gcc-11 libasan6 libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev libgcc-11-dev libitm1 liblsan0 libnsl-dev libtirpc-dev libtsan0 libubsan1
  linux-libc-dev manpages-dev rpcsvc-proto
Suggested packages:
  gcc-multilib autoconf automake libtool flex bison gdb gcc-doc gcc-11-multilib gcc-11-doc gcc-11-locales glibc-doc
The following NEW packages will be installed:
  gcc gcc-11 libasan6 libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev libgcc-11-dev libitm1 liblsan0 libnsl-dev libtirpc-dev libtsan0 libubsan1
  linux-libc-dev manpages-dev rpcsvc-proto
0 upgraded, 18 newly installed, 0 to remove and 0 not upgraded.
Need to get 32.8 MB/35.6 MB of archives.
After this operation, 116 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```
* Most of the posts recommend installing **python3-dev**
```bash
jpmena@LAPTOP-E2MJK1UO:~$ sudo apt install python3-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libopengl0
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libexpat1-dev libjs-sphinxdoc libjs-underscore libpython3-dev libpython3.10-dev python3.10-dev zlib1g-dev
The following NEW packages will be installed:
  libexpat1-dev libjs-sphinxdoc libjs-underscore libpython3-dev libpython3.10-dev python3-dev python3.10-dev zlib1g-dev
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
Need to get 5417 kB/5871 kB of archives.
After this operation, 23.8 MB of additional disk space will be used.
```
* Entering the virtualenv:
```bash
jpmena@LAPTOP-E2MJK1UO:~$ cd CONSULTANT/bayesian-optimization-in-action-main/
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action-main$ source ../.BayesianOptimisation/bin/activate
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action-main$
```
* installing through the requirement.txt file
  * to check the error I _tee_ them in a log file (the output and the error consoles)
```bash
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action$ python3 -m pip install -r requirements.txt 2>&1 | tee requirement.log
```
* for the log File of the installation see [requirement.log in this folder (link)](./requirement.log)
* the requirements.txt files which seems to work is
  * I changed for the latest version of _torch, torchvision, botorch, gpytorch_
```bash
(.BayesianOptimisation) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action$ cat requirements.txt
botorch==0.9.5
gpytorch==1.11
jupyter==1.0.0
jupyterlab==3.2.5
matplotlib==3.5.1
notebook==6.4.6
numpy==1.21.4
pandas==1.3.5
scikit-learn==1.3.1
scipy==1.7.3
seaborn==0.11.2
torch==2.1.1
torchvision==0.17.1
tqdm==4.62.3
```
## It does not work
* My __venv__ is empty see [answer 36 of this Stack Post](https://stackoverflow.com/questions/15961926/how-can-i-make-a-list-of-installed-packages-in-a-certain-virtualenv) 
* The main environment is not empty:
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/bayesian-optimization-in-action$ python3 -m pip list
Package             Version
------------------- -------------
blinker             1.4
command-not-found   0.3
cryptography        3.4.8
dbus-python         1.2.18
distro              1.7.0
distro-info         1.1+ubuntu0.2
httplib2            0.20.2
importlib-metadata  4.6.4
jeepney             0.7.1
keyring             23.5.0
launchpadlib        1.10.16
lazr.restfulclient  0.14.4
lazr.uri            1.0.6
more-itertools      8.10.0
netifaces           0.11.0
numpy               1.21.5
oauthlib            3.2.0
pip                 22.0.2
pycairo             1.20.1
PyGObject           3.42.1
PyJWT               2.3.0
pyparsing           2.4.7
PyQt5               5.15.6
PyQt5-sip           12.9.1
python-apt          2.4.0+ubuntu3
PyYAML              5.4.1
SecretStorage       3.3.1
setuptools          59.6.0
six                 1.16.0
systemd-python      234
ubuntu-pro-client   8001
ufw                 0.36.1
unattended-upgrades 0.1
wadllib             1.3.6
wheel               0.37.1
zipp                1.0.0
```
# TODO
* install the required libraries see [The PythonLibs used in the CNAM / RCP 217 Project](https://github.com/javaskater/rcp217_project/blob/main/docs/INSTALLATIONS/PYTHONLIBS.md)