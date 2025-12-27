# see [Chapter 7 in the solution](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-2/chapter-7/website)
* no need to compile SASS, on those pages we use the [repository Bootstrap](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/bootstrap)
  * as well as the [repository Bootstrap icons](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/bootstrap-icons)
# running the pages on WSL
## prerequisite
* I downloaded firefox on WSL through the apt package manager
  * which made the grpahics libraries to be downloaded
## Starting the web browser
* Starting Firefox in a **native WSL Console** not in a *Visual Studio Code/ WSL integration* console
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website$ firefox index.html
# A lot of warning messages ...
```
* It is a simplified Web Browser
# Working directly on Windows
## Installing the GitHub source Code on windows 
* Just use the official [Git 4 Windows](https://git-scm.com/install/windows)
  * install directory: **C:\Program Files\Git**
## Downloading the source code
```bash
jeanp@LAPTOP-E2MJK1UO MINGW64 ~
$ cd CONSULTANT/

jeanp@LAPTOP-E2MJK1UO MINGW64 ~/CONSULTANT
$ git clone https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide.git
Cloning into 'The-Missing-Bootstrap-5-Guide'...
remote: Enumerating objects: 6081, done.
remote: Counting objects: 100% (6081/6081), done.
remote: Compressing objects: 100% (4838/4838), done.
remote: Total 6081 (delta 1377), reused 5720 (delta 1032), pack-reused 0 (from 0)
Receiving objects: 100% (6081/6081), 11.01 MiB | 17.27 MiB/s, done.
Resolving deltas: 100% (1377/1377), done.
Updating files: 100% (3381/3381), done.
```
* In the Firefox/ Chrome address bar, enter the following URL
  * **file:///C:/Users/jeanp/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website/index.html**
## ToDo node on Windows
* [take the MSI installer](https://nodejs.org/en/download)
* use for compiling SASS source files 
# problem we don't have the Bootstrap icons
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/bootstrap$ find . -name *icon*.css -type f # does return nothing
```
## installing icons locally
* see [answer 0 of this StackOverflow Post](https://stackoverflow.com/questions/63216712/use-bootstrap-icons-with-npm)
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website$ npm i bootstrap-icons

added 1 package in 869ms

1 package is looking for funding
  run `npm fund` for details
# Go insde node_modules
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website/node_modules/bootstrap-icons$ find . -name *.scss
./font/bootstrap-icons.scss
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website/node_modules/bootstrap-icons$ find . -name *.css
./font/bootstrap-icons.css
./font/bootstrap-icons.min.css
```
## changing in the html/head part
* from 
```html
    <link rel="stylesheet" href="../../../bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="../../../bootstrap-icons/font/bootstrap-icons.css"> <!--not present there forgotten by the author-->
```
* to 
```html
    <link rel="stylesheet" href="../../../bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="node_modules/bootstrap-icons/font/bootstrap-icons.css">  <!-- newly dowloaded through npm -->
```
# installing the bootstrap-icons on windows
## installing node on Windows
* on the [website](https://nodejs.org/en/download) choose *Standalone Windows Installer msi* (not the Docker Image I don't want a nodeJS as a server) 
* It is a standard msi installer, He does not find the application in the Microsoft Store
  * install it anyway
  * By default it installs all at **C:\Program Files\nodejs\**
  * By default (options) it proposes to add node and npm (as well the npm modules) to PATH
### Testing the windows installation
* on pwershell I am not allowed to execution npm script
```powershell
PS C:\Users\jeanp\CONSULTANT\The-Missing-Bootstrap-5-Guide\part-2\chapter-7\website> node --version
v24.12.0
PS C:\Users\jeanp\CONSULTANT\The-Missing-Bootstrap-5-Guide\part-2\chapter-7\website> npm --version
npm : Impossible de charger le fichier C:\Program Files\nodejs\npm.ps1, car l’exécution de scripts est désactivée sur
ce système. Pour plus d’informations, consultez about_Execution_Policies à l’adresse
https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ npm --version
+ ~~~
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
#### [Solving the Execution Policy on Windos](https://dev.to/jackfd120/resolving-npm-execution-policy-error-in-powershell-a-step-by-step-guide-for-developers-32ip)
* On my french Windows Computer type *WINDOW Key + x*
* select *Terminal (administrateur)*
* In the new PowerShell Console then type
```powershell
PS C:\Users\jeanp> Set-ExecutionPolicy RemoteSigned
PS C:\Users\jeanp> Get-ExecutionPolicy
RemoteSigned
```
* In the still opened non admin console the command now does not throw a security exception anymore
  * we don't have reopened it
```powershell
PS C:\Users\jeanp\CONSULTANT\The-Missing-Bootstrap-5-Guide\part-2\chapter-7\website> npm --version
11.6.2 # no Security exception thrown
```
#### Git Bash has solved this problem from the beginning
```bash
jeanp@LAPTOP-E2MJK1UO MINGW64 /
$ node --version
v24.12.0

jeanp@LAPTOP-E2MJK1UO MINGW64 /
$ npm --version # no exection problems on windows, it has the rigths
11.6.2 
# to go to my home directory on Windows using Git Bash just type cd
jeanp@LAPTOP-E2MJK1UO MINGW64 /
$ cd
# going to the project
jeanp@LAPTOP-E2MJK1UO MINGW64 ~
$ cd CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website/
jeanp@LAPTOP-E2MJK1UO MINGW64 ~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website (main)
# installing the bootstrap icons
jeanp@LAPTOP-E2MJK1UO MINGW64 ~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website (main)
$ pwd
/c/Users/jeanp/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website

jeanp@LAPTOP-E2MJK1UO MINGW64 ~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website (main)
$ npm i bootstrap-icons

added 1 package in 2s

1 package is looking for funding
  run `npm fund` for details
npm notice
npm notice New minor version of npm available! 11.6.2 -> 11.7.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
npm notice To update run: npm install -g npm@11.7.0
npm notice
```
* The icons css is now at
```bash
jeanp@LAPTOP-E2MJK1UO MINGW64 ~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-7/website (main)
$ ls -ltr node_modules/bootstrap-icons/font/
total 300
-rw-r--r-- 1 jeanp 197609 87008 Dec 27 16:10 bootstrap-icons.min.css
-rw-r--r-- 1 jeanp 197609 53043 Dec 27 16:10 bootstrap-icons.json
-rw-r--r-- 1 jeanp 197609 99556 Dec 27 16:10 bootstrap-icons.css # The icons css
-rw-r--r-- 1 jeanp 197609 58496 Dec 27 16:10 bootstrap-icons.scss
drwxr-xr-x 1 jeanp 197609     0 Dec 27 16:10 fonts/
```
* adpating the header now works