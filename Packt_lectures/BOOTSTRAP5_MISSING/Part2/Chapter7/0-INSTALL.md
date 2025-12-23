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