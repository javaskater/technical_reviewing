# We can use conda or python with Virtual Environments
* [The Requirement file of the Book on GitHub](https://github.com/PacktPublishing/Building-Statistical-Models-in-Python/blob/main/requirements.txt)
* this is a file for Python 3.8
# Windows
## On my WSL Environment (Ubuntu 24.04)
```bash
jpmena@jpmena:~$ python3 --version
Python 3.12.3
```
### pip is not installed, install it
* first update the source list and then upgrade the packages
```bash
jpmena@jpmena:~$ sudo apt update #update the sources list
###############"" a lot of updates
jpmena@jpmena:~$ sudo apt upgrade #update the packages themselves
###########"##### a lot of installs
# now it will find python3-pip
jpmena@jpmena:~$ sudo apt install python3-pip
jpmena@jpmena:~$ sudo apt install python3-pip
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libdrm-nouveau2 libdrm-radeon1 libgl1-amber-dri libglapi-mesa libllvm17t64 libwayland-server0 libxcb-dri2-0
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-13 cpp-13-x86-64-linux-gnu cpp-x86-64-linux-gnu dpkg-dev fakeroot g++ g++-13
  g++-13-x86-64-linux-gnu g++-x86-64-linux-gnu gcc gcc-13 gcc-13-base gcc-13-x86-64-linux-gnu gcc-x86-64-linux-gnu
  javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libaom3 libasan8 libatomic1
  libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev libde265-0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libgcc-13-dev libgd3 libgomp1 libheif-plugin-aomdec libheif-plugin-aomenc libheif-plugin-libde265 libheif1
  libhwasan0 libisl23 libitm1 libjs-jquery libjs-sphinxdoc libjs-underscore liblsan0 libmpc3 libpython3-dev libpython3.12-dev
  libquadmath0 libstdc++-13-dev libtsan2 libubsan1 libxpm4 linux-libc-dev lto-disabled-list make manpages-dev python3-dev
  python3-wheel python3.12-dev rpcsvc-proto zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-13-locales cpp-13-doc debian-keyring g++-multilib g++-13-multilib gcc-13-doc gcc-multilib autoconf automake
  libtool flex bison gdb gcc-doc gcc-13-multilib gdb-x86-64-linux-gnu apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libheif-plugin-x265 libheif-plugin-ffmpegdec libheif-plugin-jpegdec libheif-plugin-jpegenc libheif-plugin-j2kdec
  libheif-plugin-j2kenc libheif-plugin-rav1e libheif-plugin-svtenc libstdc++-13-doc make-doc
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-13 cpp-13-x86-64-linux-gnu cpp-x86-64-linux-gnu dpkg-dev fakeroot g++ g++-13
  g++-13-x86-64-linux-gnu g++-x86-64-linux-gnu gcc gcc-13 gcc-13-base gcc-13-x86-64-linux-gnu gcc-x86-64-linux-gnu
  javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libaom3 libasan8 libatomic1
  libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev libde265-0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libgcc-13-dev libgd3 libgomp1 libheif-plugin-aomdec libheif-plugin-aomenc libheif-plugin-libde265 libheif1
  libhwasan0 libisl23 libitm1 libjs-jquery libjs-sphinxdoc libjs-underscore liblsan0 libmpc3 libpython3-dev libpython3.12-dev
  libquadmath0 libstdc++-13-dev libtsan2 libubsan1 libxpm4 linux-libc-dev lto-disabled-list make manpages-dev python3-dev
  python3-pip python3-wheel python3.12-dev rpcsvc-proto zlib1g-dev
0 upgraded, 66 newly installed, 0 to remove and 2 not upgraded.
Need to get 80.7 MB of archives.
After this operation, 283 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
```
* the installed libraries
```bash
jpmena@jpmena:~$ pip --version
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```
* a lot of libraries already installed
```bash
jpmena@jpmena:~$ pip list
Package             Version
------------------- ---------------
attrs               23.2.0
Automat             22.10.0
Babel               2.10.3
bcrypt              3.2.2
blinker             1.7.0
certifi             2023.11.17
chardet             5.2.0
click               8.1.6
cloud-init          25.2
colorama            0.4.6
command-not-found   0.3
configobj           5.0.8
constantly          23.10.4
cryptography        41.0.7
dbus-python         1.3.2
distro              1.9.0
distro-info         1.7+build1
httplib2            0.20.4
hyperlink           21.0.0
idna                3.6
incremental         22.10.0
Jinja2              3.1.2
jsonpatch           1.32
jsonpointer         2.0
jsonschema          4.10.3
launchpadlib        1.11.0
lazr.restfulclient  0.14.6
lazr.uri            1.0.6
markdown-it-py      3.0.0
MarkupSafe          2.1.5
mdurl               0.1.2
netifaces           0.11.0
oauthlib            3.2.2
pip                 24.0 # pip itself is a python module
pyasn1              0.4.8
pyasn1-modules      0.2.8
pycurl              7.45.3
Pygments            2.17.2
PyGObject           3.48.2
PyHamcrest          2.1.0
PyJWT               2.7.0
pyOpenSSL           23.2.0
pyparsing           3.1.1
pyrsistent          0.20.0
pyserial            3.5
python-apt          2.7.7+ubuntu5.2
pytz                2024.1
PyYAML              6.0.1
requests            2.31.0
rich                13.7.1
service-identity    24.1.0
setuptools          68.1.2
six                 1.16.0
systemd-python      235
Twisted             24.3.0
typing_extensions   4.10.0
ubuntu-pro-client   8001
unattended-upgrades 0.1
urllib3             2.0.7
wadllib             1.3.6
wheel               0.42.0
zope.interface      6.1
```
# On the Windows itself:
* Powershell console
```powershell
PS C:\Users\jeanp> python --version
Python 3.14.3
PS C:\windows\System32> python -m pip list # only pip is already installed
Package Version
------- -------
pip     25.3
```
# Creating virtual environments [official documentation](https://docs.python.org/3/library/venv.html)
## on WSL 
* the venv module is not present by défault
```bash
jpmena@jpmena:~$ python3 -m pip list | grep venv # no result no venv module by default
#we install it using apt
jpmena@jpmena:~$ sudo apt install python3.12-venv
[sudo] password for jpmena:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libdrm-nouveau2 libdrm-radeon1 libgl1-amber-dri libglapi-mesa libllvm17t64 libwayland-server0 libxcb-dri2-0
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 2 not upgraded.
Need to get 2429 kB of archives.
After this operation, 2777 kB of additional disk space will be used.
Do you want to continue? [Y/n]
#######################""""" lots of installs
# venv is not a pip module
jpmena@jpmena:~$ python3 -m pip list | grep venv # still no result
# it works anyway
jpmena@jpmena:~$ python3 -m venv test_env
jpmena@jpmena:~$ source test_env/bin/activate
(test_env) jpmena@jpmena:~$ deactivate
jpmena@jpmena:~$
```
## on Python Window
* it works by default
```powershell
PS C:\Users\jeanp> python -m venv test_env
PS C:\Users\jeanp> .\test_env\Scripts\activate
.\test_env\Scripts\activate : Impossible de charger le fichier C:\Users\jeanp\test_env\Scripts\Activate.ps1, car
l’'exécution de scripts est désactivée sur ce système. Pour plus d'’informations, consultez about_Execution_Policies à
l’'adresse https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ .\test_env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
* see [answer 734 of this Stack Exchange Thread](https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts)
* Running  windows powershell ad Administrator I type
```powershell
PS C:\windows\system32> Set-ExecutionPolicy remotesigned                                                                                                                                                                                        Modification de la stratégie d''exécution                                                                                La stratégie d’'exécution permet de vous prémunir contre les scripts que vous jugez non fiables. En modifiant la         stratégie d'’exécution, vous vous exposez aux risques de sécurité décrits dans la rubrique d’'aide                        about_Execution_Policies à l'’adresse https://go.microsoft.com/fwlink/?LinkID=135170. Voulez-vous modifier la stratégie  d’'exécution ?                                                                                                           [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « N ») : O
```
* now I retry (without restarting WPS)
```powershell
PS C:\Users\jeanp> .\test_env\Scripts\activate
(test_env) PS C:\Users\jeanp> deactivate
PS C:\Users\jeanp>
```
## DownLoad the source files
### on WSL
```bash
jpmena@jpmena:~/CONSULTANT/technical_reviewing$ cd ..
jpmena@jpmena:~/CONSULTANT$ git clone git@github.com:PacktPublishing/Building-Statistical-Models-in-Python.git
Cloning into 'Building-Statistical-Models-in-Python'...
remote: Enumerating objects: 171, done.
remote: Counting objects: 100% (171/171), done.
remote: Compressing objects: 100% (140/140), done.
remote: Total 171 (delta 58), reused 124 (delta 30), pack-reused 0 (from 0)
Receiving objects: 100% (171/171), 7.38 MiB | 8.62 MiB/s, done.
Resolving deltas: 100% (58/58), done.
```
## on Windows with [Git on Windows](https://git-scm.com/install/windows)
* TODO
### Does VSCode Git works on windows ?