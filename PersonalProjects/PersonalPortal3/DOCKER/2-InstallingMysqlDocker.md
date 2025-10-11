# Remember see [Installing Symfony Doker](./1-InstallingSymfonyDocker.md)
## starting the Symfony container
* First on Windows start the Docker on Windows App
* Then start the container
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose up --wait
[+] Running 2/2
 ✔ Network symfony-docker_default  Created                                                                                             0.1s 
 ✔ Container symfony-docker-php-1  Healthy 
```
* accessing the container bash
```bash
# Which are the running containers
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                   PORTS                                                                                                                   NAMES
8cca7540cdbc   app-php   "docker-entrypoint f…"   3 minutes ago   Up 3 minutes (healthy)   0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp, 0.0.0.0:443->443/udp, [::]:443->443/udp   symfony-docker-php-1
## The container's name symfony-docker-php-1
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker exec -it symfony-docker-php-1 bash
root@8cca7540cdbc:/app# php --version
PHP 8.4.13 (cli) (built: Sep 25 2025 21:14:21) (ZTS)
Copyright (c) The PHP Group
Built by https://github.com/docker-library/php
Zend Engine v4.4.13, Copyright (c) Zend Technologies
    with Zend OPcache v8.4.13, Copyright (c), by Zend Technologies
    with Xdebug v3.4.5, Copyright (c) 2002-2025, by Derick Rethans
root@8cca7540cdbc:/app# ls -l
total 212
-rw-r--r-- 1 1000 1000   2615 Oct 11 13:40 Dockerfile
-rw-r--r-- 1 root root   1055 May 29 08:09 LICENSE
-rw-r--r-- 1 1000 1000   2311 Sep 27 13:03 README.md
drwxr-xr-x 2 root root   4096 Sep 27 14:40 bin
-rw-r--r-- 1 1000 1000   1005 Oct 11 13:40 compose.override.yaml # present in the container so composer recipe can modify it
-rw-r--r-- 1 1000 1000    285 Sep 27 13:03 compose.prod.yaml # present in the container so composer recipe can modify it
-rw-r--r-- 1 1000 1000   2664 Oct 11 13:40 compose.yaml # present in the container so composer recipe can modify it
-rw-r--r-- 1 root root   2012 Oct 11 13:40 composer.json # composer with recipe
-rw-r--r-- 1 root root 146494 Oct 11 13:40 composer.lock
drwxr-xr-x 4 root root   4096 Sep 27 14:00 config
drwxr-xr-x 2 1000 1000   4096 Sep 27 13:03 docs
drwxr-xr-x 3 1000 1000   4096 Sep 27 13:03 frankenphp
drwxr-xr-x 2 root root   4096 Oct 11 13:40 migrations
drwxr-xr-x 2 root root   4096 Sep 27 14:00 public
drwxr-xr-x 5 root root   4096 Oct 11 13:40 src
-rw-r--r-- 1 root root   2739 Oct 11 13:40 symfony.lock
drwxr-xr-x 3 root root   4096 Oct 11 13:31 var
drwxr-xr-x 8 root root   4096 Oct 11 13:40 vendor
root@8cca7540cdbc:/app# exit # we leave then container
exit
```
# Adding the [Mysql container through a recipe](https://github.com/dunglas/symfony-docker/blob/main/docs/mysql.md)
## From the Host run the Reciepe
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php composer req symfony/orm-pack
The repository at "/app" does not have the correct ownership and git refuses to use it:

fatal: detected dubious ownership in repository at '/app'
To add an exception for this directory, call:

        git config --global --add safe.directory /app

./composer.json has been updated
The repository at "/app" does not have the correct ownership and git refuses to use it:

fatal: detected dubious ownership in repository at '/app'
To add an exception for this directory, call:

        git config --global --add safe.directory /app

Running composer update symfony/orm-pack
Loading composer repositories with package information
Restricting packages listed in "symfony/symfony" to "7.3.*"
Updating dependencies
Lock file operations: 17 installs, 0 updates, 0 removals
  - Locking doctrine/collections (2.3.0)
  - Locking doctrine/dbal (3.10.3)
  - Locking doctrine/deprecations (1.1.5)
  - Locking doctrine/doctrine-bundle (2.17.2)
  - Locking doctrine/doctrine-migrations-bundle (3.4.2)
  - Locking doctrine/event-manager (2.0.1)
  - Locking doctrine/inflector (2.1.0)
  - Locking doctrine/instantiator (2.0.0)
  - Locking doctrine/lexer (3.0.1)
  - Locking doctrine/migrations (3.9.4)
  - Locking doctrine/orm (3.5.2)
  - Locking doctrine/persistence (4.1.0)
  - Locking doctrine/sql-formatter (1.5.2)
  - Locking symfony/doctrine-bridge (v7.3.4)
  - Locking symfony/orm-pack (v2.4.1)
  - Locking symfony/polyfill-php84 (v1.33.0)
  - Locking symfony/stopwatch (v7.3.0)
Writing lock file
Installing dependencies from lock file (including require-dev)
Package operations: 17 installs, 0 updates, 0 removals
  - Downloading symfony/polyfill-php84 (v1.33.0)
  - Downloading doctrine/deprecations (1.1.5)
  - Downloading doctrine/collections (2.3.0)
  - Downloading doctrine/inflector (2.1.0)
  - Downloading doctrine/instantiator (2.0.0)
  - Downloading doctrine/lexer (3.0.1)
  - Downloading symfony/stopwatch (v7.3.0)
  - Downloading doctrine/event-manager (2.0.1)
  - Downloading doctrine/dbal (3.10.3)
  - Downloading doctrine/migrations (3.9.4)
  - Downloading doctrine/sql-formatter (1.5.2)
  - Downloading doctrine/persistence (4.1.0)
  - Downloading symfony/doctrine-bridge (v7.3.4)
  - Downloading doctrine/orm (3.5.2)
  - Downloading doctrine/doctrine-bundle (2.17.2)
  - Downloading doctrine/doctrine-migrations-bundle (3.4.2)
  - Installing symfony/polyfill-php84 (v1.33.0): Extracting archive
  - Installing doctrine/deprecations (1.1.5): Extracting archive
  - Installing doctrine/collections (2.3.0): Extracting archive
  - Installing doctrine/inflector (2.1.0): Extracting archive
  - Installing doctrine/instantiator (2.0.0): Extracting archive
  - Installing doctrine/lexer (3.0.1): Extracting archive
  - Installing symfony/stopwatch (v7.3.0): Extracting archive
  - Installing doctrine/event-manager (2.0.1): Extracting archive
  - Installing doctrine/dbal (3.10.3): Extracting archive
  - Installing doctrine/migrations (3.9.4): Extracting archive
  - Installing doctrine/sql-formatter (1.5.2): Extracting archive
  - Installing doctrine/persistence (4.1.0): Extracting archive
  - Installing symfony/doctrine-bridge (v7.3.4): Extracting archive
  - Installing doctrine/orm (3.5.2): Extracting archive
  - Installing doctrine/doctrine-bundle (2.17.2): Extracting archive
  - Installing doctrine/doctrine-migrations-bundle (3.4.2): Extracting archive
  - Installing symfony/orm-pack (v2.4.1)
Generating autoload files
42 packages you are using are looking for funding.
Use the `composer fund` command to find out more!

Symfony operations: 3 recipes (48f24e846f12b4c1ade06acd208687ea) # The RECIPE
  - Configuring doctrine/deprecations (>=1.0): From github.com/symfony/recipes:main
  - Configuring doctrine/doctrine-bundle (>=2.13): From github.com/symfony/recipes:main
  - Configuring doctrine/doctrine-migrations-bundle (>=3.1): From github.com/symfony/recipes:main
  - Unpacked symfony/orm-pack
Executing script cache:clear [OK]
Executing script assets:install public [OK]
              
 What's next? 
              

Some files have been created and/or updated to configure your new packages.
Please review, edit and commit them: these files are yours.

 doctrine/doctrine-bundle  instructions:

  * Modify your DATABASE_URL config in .env

  * Configure the driver (postgresql) and
    server_version (16) in config/packages/doctrine.yaml

No security vulnerability advisories found.
```
## now My My Docker Compose Files have been modified
### compose.yaml has the following added
```yaml
###> doctrine/doctrine-bundle ###
  database:
    image: postgres:${POSTGRES_VERSION:-16}-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-app}
      # You should definitely change the password in production
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-!ChangeMe!}
      POSTGRES_USER: ${POSTGRES_USER:-app}
    healthcheck:
      test: ["CMD", "pg_isready", "-d", "${POSTGRES_DB:-app}", "-U", "${POSTGRES_USER:-app}"]
      timeout: 5s
      retries: 5
      start_period: 60s
    volumes:
      - database_data:/var/lib/postgresql/data:rw
      # You may use a bind-mounted host directory instead, so that it is harder to accidentally remove the volume and lose all your data!
      # - ./docker/db/data:/var/lib/postgresql/data:rw
###< doctrine/doctrine-bundle ###
```
### compose.override.yaml has the following added
```yaml
###> doctrine/doctrine-bundle ###
  database:
    ports:
      - "5432"
###< doctrine/doctrine-bundle ###
```
### Dockerfile has the following added
```yaml
###> recipes ###
###> doctrine/doctrine-bundle ###
RUN install-php-extensions pdo_pgsql
###< doctrine/doctrine-bundle ###
###< recipes ###
```
# [Changing from Postgres to Mysql](https://github.com/dunglas/symfony-docker/blob/main/docs/mysql.md)
* To change the files you have to access them in the Container itself using code see [testing the Symfony Container with VisualStudio Code](./1-InstallingSymfonyDocker.md)
## Changing the DockerFile 
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ sudo cp -pv Dockerfile Dockerfile_back_$(date '+%d%m%Y')
[sudo] password for jpmena: 
'Dockerfile' -> 'Dockerfile_back_11102025'
# Modify the file in the container to see the modification on the host
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ diff -u Dockerfile Dockerfile_back_$(date '+%d%m%Y')
--- Dockerfile  2025-10-11 16:09:06.075704130 +0200
+++ Dockerfile_back_11102025    2025-10-11 15:40:00.664221087 +0200
@@ -41,8 +41,7 @@
 
 ###> recipes ###
 ###> doctrine/doctrine-bundle ###
-#RUN install-php-extensions pdo_pgsql
-RUN install-php-extensions pdo_mysql
+RUN install-php-extensions pdo_pgsql
 ###< doctrine/doctrine-bundle ###
 ###< recipes ###
```
## Changing compose.yaml and compose.override.yaml
* I just forgot to backup compose.yaml
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ sudo cp -pv compose.override.yaml compose.override.yaml_back_$(date '+%d%m%Y')
'compose.override.yaml' -> 'compose.override.yaml_back_11102025'
```
# [Restart The environment](https://github.com/dunglas/symfony-docker/blob/main/docs/mysql.md#final-steps)
## create the new php Image
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose down --remove-orphans && docker compose build --pull --no-cache
[+] Running 2/2
 ✔ Container symfony-docker-php-1  Removed                                                                                             1.4s 
 ✔ Network symfony-docker_default  Removed                                                                                             0.4s 
[+] Building 96.4s (28/28) FINISHED                                                                                                         
 => [internal] load local bake definitions                                                                                             0.0s
 => => reading from stdin 598B                                                                                                         0.0s
 => [internal] load build definition from Dockerfile                                                                                   0.1s
 => => transferring dockerfile: 2.69kB                                                                                                 0.0s
 => resolve image config for docker-image://docker.io/docker/dockerfile:1                                                              2.0s
 => [auth] docker/dockerfile:pull token for registry-1.docker.io                                                                       0.0s
 => docker-image://docker.io/docker/dockerfile:1@sha256:b6afd42430b15f2d2a4c5a02b919e98a525b785b1aaff16747d2f623364e39b6               1.1s
 => => resolve docker.io/docker/dockerfile:1@sha256:b6afd42430b15f2d2a4c5a02b919e98a525b785b1aaff16747d2f623364e39b6                   0.0s
 => => sha256:77246a01651da592b7bae79e0e20ed3b4f2e4c00a1b54b7c921c91ae3fa9ef07 13.57MB / 13.57MB                                       0.8s
 => => extracting sha256:77246a01651da592b7bae79e0e20ed3b4f2e4c00a1b54b7c921c91ae3fa9ef07                                              0.2s
 => [internal] load metadata for docker.io/dunglas/frankenphp:1-php8.4                                                                 0.5s
 => [auth] dunglas/frankenphp:pull token for registry-1.docker.io                                                                      0.0s
 => [internal] load .dockerignore                                                                                                      0.0s
 => => transferring context: 498B                                                                                                      0.0s
 => [frankenphp_upstream 1/1] FROM docker.io/dunglas/frankenphp:1-php8.4@sha256:d656fa836a1f1e4b75a7838d817276e7c45b20c6714f6af336a6c  0.0s
 => => resolve docker.io/dunglas/frankenphp:1-php8.4@sha256:d656fa836a1f1e4b75a7838d817276e7c45b20c6714f6af336a6c7eb1638531b           0.0s
 => [internal] load build context                                                                                                      0.0s
 => => transferring context: 260B                                                                                                      0.0s
 => CACHED [frankenphp_base 1/7] WORKDIR /app                                                                                          0.0s
 => [frankenphp_base 2/7] RUN apt-get update && apt-get install -y --no-install-recommends  file  git  && rm -rf /var/lib/apt/lists/*  9.2s
 => [frankenphp_base 3/7] RUN set -eux;  install-php-extensions   @composer   apcu   intl   opcache   zip  ;                          55.4s 
 => [frankenphp_base 4/7] RUN install-php-extensions pdo_mysql                                                                        10.5s 
 => [frankenphp_base 5/7] COPY --link frankenphp/conf.d/10-app.ini /usr/local/etc/php/app.conf.d/                                      0.1s 
 => => merging                                                                                                                         0.0s 
 => [frankenphp_base 6/7] COPY --link --chmod=755 frankenphp/docker-entrypoint.sh /usr/local/bin/docker-entrypoint                     0.0s 
 => [frankenphp_base 7/7] COPY --link frankenphp/Caddyfile /etc/frankenphp/Caddyfile                                                   0.1s 
 => => merging                                                                                                                         0.1s 
 => [frankenphp_dev 1/3] RUN mv "/usr/local/etc/php/php.ini-development" "/usr/local/etc/php/php.ini"                                  0.2s 
 => [frankenphp_dev 2/3] RUN set -eux;  install-php-extensions   xdebug  ;                                                            12.9s
 => [frankenphp_dev 3/3] COPY --link frankenphp/conf.d/20-app.dev.ini /usr/local/etc/php/app.conf.d/                                   0.2s 
 => exporting to image                                                                                                                 3.3s 
 => => exporting layers                                                                                                                2.3s 
 => => exporting manifest sha256:5c98925d56d2876478555f01f3f9d83ec00364076acd5b09a944231a91db298d                                      0.0s 
 => => exporting config sha256:14b718c03322110a7941eeb28aeedbdaecb15b21bdc0bdad8c033ace590f8c64                                        0.0s 
 => => exporting attestation manifest sha256:43e92bdc1e3f2c9b4ae7e3b136b94525893b0bb6264c0e526901e92984899d44                          0.0s 
 => => exporting manifest list sha256:69be3a10ae503962c80b8099a75f518c9f43b7248fe665fd679fd8d615295874                                 0.0s
 => => naming to docker.io/library/app-php:latest                                                                                      0.0s
 => => unpacking to docker.io/library/app-php:latest                                                                                   0.8s
 => resolving provenance for metadata file                                                                                             0.0s
[+] Building 1/1
 ✔ app-php  Built                
```
* It only built app **app-php**
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
app-php      latest    69be3a10ae50   3 minutes ago   957MB
```
## import the database image and start the 2 containers
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose up --wait
[+] Running 11/11
 ✔ database Pulled                                                                                                                                                                18.0s 
   ✔ 46d5b31c795a Pull complete                                                                                                                                                    0.4s 
   ✔ a49b4bec6f69 Pull complete                                                                                                                                                    0.6s 
   ✔ f56ec30544fc Pull complete                                                                                                                                                   16.5s 
   ✔ 69718387e824 Pull complete                                                                                                                                                    5.2s 
   ✔ 806f49275cbf Pull complete                                                                                                                                                    4.8s 
   ✔ 7a99a8dca35c Pull complete                                                                                                                                                    6.2s 
   ✔ 8389b884d3d6 Pull complete                                                                                                                                                    4.9s 
   ✔ d3dc946e9b73 Pull complete                                                                                                                                                    0.6s 
   ✔ 35a745903ff9 Pull complete                                                                                                                                                    0.6s 
   ✔ 970f697f30e8 Pull complete                                                                                                                                                    0.6s 
[+] Running 3/4
 ✔ Network symfony-docker_default       Created                                                                                                                                    0.1s 
 ✔ Volume symfony-docker_database_data  Created                                                                                                                                    0.0s 
 ✔ Container symfony-docker-database-1  Healthy                                                                                                                                   11.9s 
 ⠇ Container symfony-docker-php-1       Waiting                                                                                                                                   11.9s 
container symfony-docker-php-1 is unhealthy
```
### The Database Image is now present
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
app-php      latest    69be3a10ae50   7 minutes ago   957MB
mysql        8         5367102acfef   2 weeks ago     1.07GB # The new Image (Mysql:8)
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker container ls # The 2 containers have been added
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                   PORTS                                                                                                                   NAMES
ed9c77025553   app-php   "docker-entrypoint f…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp, 0.0.0.0:443->443/udp, [::]:443->443/udp   symfony-docker-php-1
678aea28081a   mysql:8   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:49679->3306/tcp, [::]:49679->3306/tcp                                                                           symfony-docker-database-1
```
# Acces to the mysql from the host
## Trough the Symfony console 
* It is a good example of running the Symfony console from the host
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php bin/console dbal:run-sql -q "SELECT 1" && echo "OK" || echo "Connection is not working"
OK
```
* [dbal il the component Doctrine DBAL](https://symfony.com/doc/current/doctrine/dbal.html)
*  dbal is the default configuration see [config/packages/doctrine.yaml](https://symfony.com/doc/current/doctrine/dbal.html#registering-custom-mapping-types)
  * the file config/packages/doctrine.yaml starts with
```yaml
doctrine:
    dbal:
        url: '%env(resolve:DATABASE_URL)%' # see the .env file

        # IMPORTANT: You MUST configure your server version,
        # either here or in the DATABASE_URL env var (see .env file)
        #server_version: '16'

        profiling_collect_backtrace: '%kernel.debug%'
        use_savepoints: true
``` 

## more on tht console command from the Host
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php bin/console dbal:run -help
Description:
  Executes arbitrary SQL directly from the command line.

Usage:
  dbal:run-sql [options] [--] <sql>

Arguments:
  sql                          The SQL statement to execute.

Options:
      --connection=CONNECTION  The named database connection
      --depth=DEPTH            Dumping depth of result set (deprecated).
      --force-fetch            Forces fetching the result.
  -h, --help                   Display help for the given command. When no command is given display help for the list command
      --silent                 Do not output any message
  -q, --quiet                  Only errors are displayed. All other output is suppressed
  -V, --version                Display this application version
      --ansi|--no-ansi         Force (or disable --no-ansi) ANSI output
  -n, --no-interaction         Do not ask any interactive question
  -e, --env=ENV                The Environment name. [default: "dev"]
      --no-debug               Switch off debug mode.
      --profile                Enables profiling (requires debug).
  -v|vv|vvv, --verbose         Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Help:
  The dbal:run-sql command executes the given SQL query and
  outputs the results:
  
  php bin/console dbal:run-sql "SELECT * FROM users"
```

## Exporting the port of the Mysql Container
* changing the port in **compose.override.yaml**
  * the part of the Database Symfony Recipe becomes
```yaml
###> doctrine/doctrine-bundle ###
  database:
    ports:
      - target: 3306
        published: 33066 # exporting the 3306 (Container) to the 33066 on the Host
        protocol: tcp #mandatory to have the php container healthy
###< doctrine/doctrine-bundle ###
```
* restarting the containers
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose down # shutting down the 2 containers
[+] Running 3/3
 ✔ Container symfony-docker-database-1  Removed                                                                                        2.2s 
 ✔ Container symfony-docker-php-1       Removed                                                                                        0.6s 
 ✔ Network symfony-docker_default       Removed                                                                                        0.4s 
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose up --wait # starting up the 2 containers
[+] Running 3/3
 ✔ Network symfony-docker_default       Created                                                                                        0.1s 
 ✔ Container symfony-docker-database-1  Healthy                                                                                        5.7s 
 ✔ Container symfony-docker-php-1       Healthy                                                                                        6.2s
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker container ls #it is unhealty but started
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                        PORTS                                                                                                                   NAMES
6c8022b7c65b   app-php   "docker-entrypoint f…"   2 minutes ago   Up About a minute (healthy)   0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp, 0.0.0.0:443->443/udp, [::]:443->443/udp   symfony-docker-php-1
01475b9706e7   mysql:8   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes (healthy)        0.0.0.0:33066->3306/tcp, [::]:33066->3306/tcp                                                                           symfony-docker-database-1
 ```
 * now on the Host (in WSL) I see the Mysql exposed port (3306 -> 33066)
```bash
jpmena@LAPTOP-E2MJK1UO:~$ netstat -an | grep 3306
tcp6       0      0 :::33066                :::*                    LISTEN
```
## Connecting DBeaver on my Windows Computer
![Parametring DBeaver on Windows Host](./files/dBeaver.png)
* following the Symfony connection URL underneath (in the root's .env file), I enter the parameters above
```bash
# DATABASE_URL="mysql://app:!ChangeMe!@127.0.0.1:3306/app?serverVersion=10.11.2-MariaDB&charset=utf8mb4"
DATABASE_URL=mysql://${MYSQL_USER:-app}:${MYSQL_PASSWORD:-!ChangeMe!}@database:3306/${MYSQL_DATABASE:-app}?serverVersion=${MYSQL_VERSION:-8}&charset=${MYSQL_CHARSET:-utf8mb4}
###< doctrine/doctrine-bundle ###
```
* The only difference it the exposed port **33066** 
## Connecting mysql client on WSL
* [more on the Mysql command line](https://dev.mysql.com/doc/refman/8.4/en/connecting.html)
* don't use localhost on the WSL Host Command line use 127.0.0.1 instead
```bash
jpmena@LAPTOP-E2MJK1UO:~$ mysql --host=127.0.0.1 --user=app --port=33066 -p app
Enter password: # enter !ChangeMe!
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 28
Server version: 8.4.6 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```
* Or (due to the specifics of the password simple quotes are mandatory!!!) 
```bash
jpmena@LAPTOP-E2MJK1UO:~$ mysql --host=127.0.0.1 --user=app --port=33066 --password='!ChangeMe!' app # simple quotes mandatory for the password !!!
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 33
Server version: 8.4.6 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```