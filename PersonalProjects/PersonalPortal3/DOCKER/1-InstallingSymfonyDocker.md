# From the official Symfony doc
* [The Symfony doc](https://symfony.com/doc/current/setup/docker.html) recommends [this docker GitHub project](https://github.com/dunglas/symfony-docker)
## Dunglas [Symfony Docker](https://github.com/dunglas/symfony-docker/tree/main)
  * [The README](https://github.com/dunglas/symfony-docker/blob/main/README.md) tells what to do
* For further information (for example XDebug) see [the doc folder](https://github.com/dunglas/symfony-docker/tree/main/docs)
## Requirement
```bash
jpmena@LAPTOP-E2MJK1UO:~$ docker compose version
Docker Compose version v2.38.2 # it is well above v2.10
jpmena@LAPTOP-E2MJK1UO:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.2 LTS # Ubuntu version
Release:        24.04
Codename:       noble
```
# Installing on WSL (Ubuntu 24.04)
* following [The README](https://github.com/dunglas/symfony-docker/blob/main/README.md)
## Getting [the Docker project](https://github.com/dunglas/symfony-docker/tree/main)
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ git clone git@github.com:dunglas/symfony-docker.git
Cloning into 'symfony-docker'...
remote: Enumerating objects: 1480, done.
remote: Counting objects: 100% (262/262), done.
remote: Compressing objects: 100% (148/148), done.
remote: Total 1480 (delta 185), reused 114 (delta 114), pack-reused 1218 (from 2)
Receiving objects: 100% (1480/1480), 837.89 KiB | 2.22 MiB/s, done.
Resolving deltas: 100% (803/803), done.
## Adding new images
* before installing
```bash
jpmena@LAPTOP-E2MJK1UO:~$ docker image ls
REPOSITORY                        TAG                                  IMAGE ID       CREATED         SIZE
wordpress                         latest                               c89b40a25cd1   10 months ago   700MB
ddev/ddev-webserver               v1.23.5-packt-built                  d509e26d71b2   11 months ago   1.61GB
ddev/ddev-dbserver-mariadb-10.4   v1.23.5-packt-built                  266eeb1900ab   11 months ago   690MB
ddev/ddev-ssh-agent               v1.23.5-built                        5f8091055da5   11 months ago   128MB
ddev/ddev-webserver               v1.23.5-tryddevproject-30483-built   05610360930f   11 months ago   1.58GB
ddev/ddev-webserver               v1.23.5                              aff0bb0fe24e   11 months ago   1.56GB
ddev/ddev-dbserver-mariadb-10.4   v1.23.5                              b68f807ab536   11 months ago   690MB
ddev/ddev-traefik-router          v1.23.5                              da1fc460c87f   11 months ago   210MB
ddev/ddev-ssh-agent               v1.23.5                              bfed6ff7b109   11 months ago   128MB
mysql                             8.0                                  6c55ddbef969   11 months ago   591MB
ddev/ddev-utilities               latest                               09b7b0fddb95   12 months ago   68.3MB
node                              18-buster-slim                       f7d0a48c51e6   16 months ago   187MB
busybox                           stable                               6fd955f66c23   2 years ago     4.26MB
backstopjs/backstopjs             6.2.1                                ecc6bd89109b   2 years ago     2.93GB
node                              16-alpine3.15                        477eb7db0f23   2 years ago     116MB
seleniarm/standalone-chromium     4.1.4-20220429                       11cb7be2ddf7   3 years ago     1.54GB
```
* installing
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ cd symfony-docker/ # At the place of the docker compose dans Docker files
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose build --pull --no-cache
fork/exec /usr/local/lib/docker/cli-plugins/docker-buildx: no such file or directory
```
* I start the Docker graphical interface on Windows and I get a different error message
```bash
# different version of Docker Compose
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose version
Docker Compose version v2.20.2-desktop.1
# I have another error
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose build --pull --no-cache
request returned Internal Server Error for API route and version http://%2Fvar%2Frun%2Fdocker.sock/_ping, check if the server supports the requested API version
```
* Following the [link](https://forums.docker.com/t/error-request-returned-internal-server-error-for-api-route-and-version/140375/7) especially the *sudo666 Sudipto Sarkar* solution
* I uninstall and install Docker Desktop on Windows using [the official documentation](https://docs.docker.com/desktop/setup/install/windows-install/) (and not the Microsoft Store which get stuck waiting for a window that does not appear) 
  * It installed the 44.4.7 version  
* we have a new version of docker compose
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose version
Docker Compose version v2.39.4-desktop.1 # We went from the 2.20 to the v2.39
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose build --pull --no-cache
## I takes 5 minutes doing a lot of things
=> resolving provenance for metadata file                                                                         0.0s
[+] Building 1/1
 ✔ app-php  Built
```
### What is the situation
* After the docker Desktop on Windows, I have one image and no containers ....
  * I have no more the previous images ...
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
app-php      latest    c59528bd7a62   6 minutes ago   944MB
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker container ls # no started container
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
## Starting the container
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose up --wait
[+] Running 4/4
 ✔ Network symfony-docker_default      Created                                                                     0.1s
 ✔ Volume symfony-docker_caddy_data    Created                                                                     0.0s
 ✔ Volume symfony-docker_caddy_config  Created                                                                     0.0s
 ✔ Container symfony-docker-php-1      Healthy                                                                     6.5s
 ```
* A lot of new Symfony repositories on my Host (WSL/Ubuntu 24.04)
  * vendor (empty), var, src, public, bin repositories
  * composer.json, composer.lock 
* one container created
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                   PORTS                                                                                                                   NAMES
1466f54beada   app-php   "docker-entrypoint f…"   3 minutes ago   Up 3 minutes (healthy)   0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp, 0.0.0.0:443->443/udp, [::]:443->443/udp   symfony-docker-php-1
```
### Accessing the container
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker exec -it symfony-docker-php-1 bash
root@1466f54beada:/app# php --version
PHP 8.4.13 (cli) (built: Sep 25 2025 21:14:21) (ZTS) # php version inside the container
Copyright (c) The PHP Group
Built by https://github.com/docker-library/php
Zend Engine v4.4.13, Copyright (c) Zend Technologies
    with Zend OPcache v8.4.13, Copyright (c), by Zend Technologies
    with Xdebug v3.4.5, Copyright (c) 2002-2025, by Derick Rethans # XDebug is present
root@1466f54beada:/app# composer --version
Composer version 2.8.12 2025-09-19 13:41:59
PHP version 8.4.13 (/usr/local/bin/php)
Run the "diagnose" command to get more detailed diagnostics output.
```
* vendor is empty on the Host Side, but full on the cotainer side
```bash
root@1466f54beada:/app# ls -l vendor/
total 28
-rw-r--r--  1 root root  748 Sep 27 14:00 autoload.php
-rw-r--r--  1 root root  812 Sep 27 14:00 autoload_runtime.php
drwxr-xr-x  2 root root 4096 Sep 27 14:00 bin
drwxr-xr-x  2 root root 4096 Sep 27 14:00 composer
drwxr-xr-x  6 root root 4096 Sep 27 14:00 psr
drwxr-xr-x  3 root root 4096 Sep 27 14:00 runtime
drwxr-xr-x 29 root root 4096 Sep 27 14:00 symfony
```
### Accepting the default certificate
https://localhost/ me dit *You are using Symfony 7.3.4 version*
## Stopping the container
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose down --remove-orphans
[+] Running 2/2
 ✔ Container symfony-docker-php-1  Removed                                                                         0.8s
 ✔ Network symfony-docker_default  Removed 

# Developping Visual Studio Code in the Symfony container
* [Develop PHP in a Docker Container](https://blog.devsense.com/2022/develop-php-in-docker/#step-2-initialization)
*  I have the [Docker Extension Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) I can do everynthing
*  Go to container develop app-php, right click and *Attach Visual Studio Code*
  * it starts a new instance of Visual Studio Code with the *Container app-php* mention in green down left
  * on that new VSCode I open the **/app** folder 
  * Done ...
* The Volume is only there to commit the sources ?
# An Mysql in the Docker instead of Postgres
* [using mysql instead of Postgresql](https://github.com/dunglas/symfony-docker/blob/main/docs/mysql.md)
* The remote compose command installing the orm vendor dependency, also modifies the docker - compose file to add the Mysql image ...
> The Docker configuration of this repository is extensible thanks to Flex recipes. By default, the recipe installs PostgreSQL
```bash
docker compose exec php composer req symfony/orm-pack # symfony/orm-pack includes a recipe
```
* installing [Mysql Container through a recipe](./2-InstallingMysqlDocker.md)