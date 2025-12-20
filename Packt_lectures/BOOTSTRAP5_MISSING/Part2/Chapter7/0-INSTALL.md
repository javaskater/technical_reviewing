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