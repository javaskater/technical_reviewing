# Reintall all Manning libraries on this Ominbook / Ubuntu
## venv is not supported by default
```bash
jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ python3 -m venv ManningBayesian
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.14-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/jpmena/CONSULTANT/ManningBayesian/bin/python3
# I install it
jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ sudo apt install python3.14-venv
[sudo: authenticate] Mot de passe :           
Installation de :                               
  python3.14-venv

Installation de dépendances : 
  python3-pip-whl  python3-setuptools-whl

Sommaire :
  Mise à niveau de : 0. Installation de : 3, Supprimé : 0. Non mis à jour : 2
Taille du téléchargement : 2 609 ko
  Espace nécessaire : 2 952 ko / 467 Go disponible
  #########################################################
# I create my virtual environment
jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ python3 -m venv ManningBayesian
jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ ll ManningBayesian/ # The content of my virtual environment !!!
total 36
drwxrwxr-x 7 jpmena jpmena 4096 Aug  6 10:39 ./
drwxrwxr-x 5 jpmena jpmena 4096 Aug  6 10:55 ../
-rw-rw-r-- 1 jpmena jpmena   69 Aug  6 10:16 .gitignore
drwxrwxr-x 2 jpmena jpmena 4096 Aug  6 11:25 bin/
drwxrwxr-x 3 jpmena jpmena 4096 Aug  6 10:39 etc/
drwxrwxr-x 2 jpmena jpmena 4096 Aug  6 10:02 include/
drwxrwxr-x 3 jpmena jpmena 4096 Aug  6 10:02 lib/
lrwxrwxrwx 1 jpmena jpmena    3 Aug  6 10:02 lib64@ -> lib
-rw-rw-r-- 1 jpmena jpmena  178 Aug  6 10:16 pyvenv.cfg
drwxrwxr-x 6 jpmena jpmena 4096 Aug  6 10:40 share/
# I activate my virtual environment
jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ source ManningBayesian/bin/activate
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ 
# I am in 3.14 version
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ python --version
Python 3.14.4 # I hope of no problems with the age of libraries
```
# I required all the necessary libraries
* see [Install third try with the latest version of Mathplotlib](./3-PytonInstallationThirdTry.md)
# First try:
```bash
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ python -m pip install -r technical_reviewing/Manning_lectures/BAYESIAN_OPTIMISATION_IN_ACTION/requirementsOmnibook.txt 2>&1 | tee requirementsOmnibook.log
########################################################
Successfully installed MarkupSafe-3.0.3 Send2Trash-2.1.0 anyio-3.7.1 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 asttokens-3.0.2 attrs-26.1.0 babel-2.18.0 beautifulsoup4-4.15.0 bleach-6.4.0 botorch-0.6.0 certifi-2026.7.22 cffi-2.1.1 charset_normalizer-3.4.9 comm-0.2.3 contourpy-1.3.3 cuda-bindings-13.3.1 cuda-pathfinder-1.6.0 cuda-toolkit-13.0.2 cycler-0.12.1 debugpy-1.8.21 defusedxml-0.7.1 executing-2.2.1 fastjsonschema-2.22.1 filelock-3.32.2 fonttools-4.63.0 fsspec-2026.7.0 gpytorch-1.6.0 idna-3.18 ipykernel-7.3.0 ipython-9.16.1 ipython-genutils-0.2.0 ipython-pygments-lexers-1.1.1 ipywidgets-8.1.8 jedi-0.20.0 jinja2-3.1.6 joblib-1.5.3 json5-0.15.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 jupyter-1.0.0 jupyter-client-8.9.1 jupyter-console-6.6.3 jupyter-core-5.9.1 jupyter-server-1.24.0 jupyterlab-3.2.5 jupyterlab-pygments-0.3.0 jupyterlab-server-2.28.0 jupyterlab_widgets-3.0.16 kiwisolver-1.5.0 matplotlib-3.11.0 matplotlib-inline-0.2.2 mistune-3.3.4 mpmath-1.3.0 narwhals-2.24.0 nbclassic-0.5.6 nbclient-0.11.0 nbconvert-7.17.1 nbformat-5.10.4 nest-asyncio-1.6.0 nest-asyncio2-1.7.2 networkx-3.6.1 notebook-6.4.6 notebook-shim-0.2.4 numpy-2.4.6 nvidia-cublas-13.1.1.3 nvidia-cuda-cupti-13.0.85 nvidia-cuda-nvrtc-13.0.88 nvidia-cuda-runtime-13.0.96 nvidia-cudnn-cu13-9.20.0.48 nvidia-cufft-12.0.0.61 nvidia-cufile-1.15.1.6 nvidia-curand-10.4.0.35 nvidia-cusolver-12.0.4.66 nvidia-cusparse-12.6.3.3 nvidia-cusparselt-cu13-0.8.1 nvidia-nccl-cu13-2.29.7 nvidia-nvjitlink-13.0.88 nvidia-nvshmem-cu13-3.4.5 nvidia-nvtx-13.0.85 packaging-26.3 pandas-3.0.3 pandocfilters-1.5.1 parso-0.8.7 pexpect-4.9.0 pillow-12.3.0 platformdirs-4.11.0 prometheus-client-0.26.0 prompt_toolkit-3.0.53 psutil-7.2.2 ptyprocess-0.7.0 pure-eval-0.2.3 pycparser-3.0 pygments-2.20.0 pyparsing-3.3.2 python-dateutil-2.9.0.post0 pyzmq-27.1.0 qtconsole-5.7.2 qtpy-2.4.3 referencing-0.37.0 requests-2.34.2 rpds-py-2026.6.3 scikit-learn-1.9.0 scipy-1.17.1 seaborn-0.13.2 setuptools-81.0.0 six-1.17.0 sniffio-1.3.1 soupsieve-2.9.1 stack_data-0.6.3 sympy-1.14.0 terminado-0.18.1 threadpoolctl-3.6.0 tinycss2-1.5.1 torch-2.12.0 torchvision-0.27.0 tornado-6.5.7 tqdm-4.62.3 traitlets-5.16.1 triton-3.7.0 typing-extensions-4.16.0 urllib3-2.7.0 wcwidth-0.8.2 webencodings-0.5.1 websocket-client-1.9.0 widgetsnbextension-4.0.15
```
- du premier coup ça marche (cet ordinateur est vraiment rapide)
# Running the Notebook on the examples
- [Running Jupyter seems really simple](https://docs.jupyter.org/en/latest/running.html)
- From my virtual environment
## First crash
- [see this StackOverflow Post](https://stackoverflow.com/questions/77549493/modulenotfounderror-no-module-named-jupyter-server-contents?noredirect=1&lq=1)
- I uninstall my old versions (of the requirements.txr)
```bash
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ pip uninstall jupyter
Found existing installation: jupyter 1.0.0
Uninstalling jupyter-1.0.0:
  Would remove:
    /home/jpmena/CONSULTANT/ManningBayesian/lib/python3.14/site-packages/jupyter-1.0.0.dist-info/*
    /home/jpmena/CONSULTANT/ManningBayesian/lib/python3.14/site-packages/jupyter.py
Proceed (Y/n)? Y
  Successfully uninstalled jupyter-1.0.0
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ pip uninstall jupyterlab
Found existing installation: jupyterlab 3.2.5
Uninstalling jupyterlab-3.2.5:
  Would remove:
##################################################
```
- I install the [latest Jupyter version](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html)
  - the command is given in the previous website 
```bash
# command given on the wesite
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ pip install notebook --upgrade
Requirement already satisfied: notebook in ./ManningBayesian/lib/python3.14/site-packages (6.4.6)
Collecting notebook
  Downloading notebook-7.6.1-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: jupyter-builder<2,>=1.0.2 in ./ManningBayesian/lib/python3.14/site-packages (from notebook) (1.2.1)
Requirement already satisfied: jupyter-server<3,>=2.19.0 in ./ManningBayesian/lib/python3.14/site-packages (from notebook) (2.20.0)
Requirement already satisfied: jupyterlab-server<3,>=2.28.0 in ./ManningBayesian/lib/python3.14/site-packages (from notebook) (2.28.0)
Collecting jupyterlab<4.7,>=4.6.2 (from notebook)
##################################################################
#################################################################
Downloading notebook-7.6.1-py3-none-any.whl (5.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 24.9 MB/s eta 0:00:00
Using cached jupyterlab-4.6.2-py3-none-any.whl (17.2 MB)
Installing collected packages: jupyterlab, notebook
  Attempting uninstall: notebook
    Found existing installation: notebook 6.4.6
    Uninstalling notebook-6.4.6:
      Successfully uninstalled notebook-6.4.6
Successfully installed jupyterlab-4.6.2 notebook-7.6.1
```
- starting the notebook now works
```bash
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ jupyter notebook
###########################################
[I 2026-08-06 11:31:19.815 ServerApp] nbclassic | extension was successfully loaded.
[I 2026-08-06 11:31:19.819 ServerApp] notebook | extension was successfully loaded.
[I 2026-08-06 11:31:19.820 ServerApp] Serving notebooks from local directory: /home/jpmena/CONSULTANT
[I 2026-08-06 11:31:19.820 ServerApp] Jupyter Server 2.20.0 is running at:
[I 2026-08-06 11:31:19.820 ServerApp] http://localhost:8888/tree?token=f61a25b63dc313117324cbddf99403ad88c11d3baf3acdd1
[I 2026-08-06 11:31:19.821 ServerApp]     http://127.0.0.1:8888/tree?token=f61a25b63dc313117324cbddf99403ad88c11d3baf3acdd1
[I 2026-08-06 11:31:19.821 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2026-08-06 11:31:19.925 ServerApp] 
    
    To access the server, open this file in a browser:
        file:/home/jpmena/.local/share/jupyter/runtime/jpserver-29032-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=f61a25b63dc313117324cbddf99403ad88c11d3baf3acdd1
        http://127.0.0.1:8888/tree?token=f61a25b63dc313117324cbddf99403ad88c11d3baf3acdd1
[I 2026-08-06 11:31:20.114 ServerApp] Skipped non-installed server(s): basedpyright, bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyrefly, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
Gtk-Message: 11:31:20.222: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
```
## Which are the installed versions
```bash
# for Jupyter
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ python -m pip freeze | grep -i jupyter
jupyter-console==6.6.3
jupyter-events==0.12.1
jupyter-lsp==2.3.1
jupyter_builder==1.2.1
jupyter_client==8.9.1
jupyter_core==5.9.1
jupyter_server==2.20.0
jupyter_server_terminals==0.5.4
jupyterlab==4.6.2
jupyterlab_pygments==0.3.0
jupyterlab_server==2.28.0
jupyterlab_widgets==3.0.16
# for notebook
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ python -m pip freeze | grep -i notebook
notebook==7.6.1
notebook_shim==0.2.4
```
- Other way to get the Jupyter version
```bash
(ManningBayesian) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ jupyter --version
Selected Jupyter core packages...
IPython          : 9.16.1
ipykernel        : 7.3.0
ipywidgets       : 8.1.8
jupyter_client   : 8.9.1
jupyter_core     : 5.9.1
jupyter_server   : 2.20.0
jupyterlab       : 4.6.2
nbclient         : 0.11.0
nbconvert        : 7.17.1
nbformat         : 5.10.4
notebook         : 7.6.1
qtconsole        : 5.7.2
traitlets        : 5.16.1
```

## CTRL + Enter 
- to run a python cell !!!
# CTRL + C 
- to stop the notebook server
# deactivate
- to quit the virtual env