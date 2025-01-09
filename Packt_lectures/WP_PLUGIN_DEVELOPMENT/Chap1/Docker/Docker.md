# [Docker installation on Linux/Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* The source list has already been completed
```bash
jmena01@M077-1840900:~$ cat /etc/apt/sources.list.d/docker.list 
deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu   focal stable
```
* I install only the docker-compose plugin
  * It only updated it, it was already there
```bash
jmena01@M077-1840900:~$ sudo apt install docker-compose-plugin
Lecture des listes de paquets... Fait
Construction de l''arbre des dépendances       
Lecture des informations d'état... Fait
Les paquets suivants seront mis à jour :
  docker-compose-plugin
1 mis à jour, 0 nouvellement installés, 0 à enlever et 469 non mis à jour.
Il est nécessaire de prendre 12,6 Mo dans les archives.
Après cette opération, 2 358 ko d'espace disque supplémentaires seront utilisés.
Réception de :1 https://download.docker.com/linux/ubuntu focal/stable amd64 docker-compose-plugin amd64 2.29.7-1~ubuntu.20.04~focal [12,6 MB]
12,6 Mo réceptionnés en 0s (33,0 Mo/s)         
(Lecture de la base de données... 275984 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de .../docker-compose-plugin_2.29.7-1~ubuntu.20.04~focal_amd64.deb ...
Dépaquetage de docker-compose-plugin (2.29.7-1~ubuntu.20.04~focal) sur (2.24.6-1~ubuntu.20.04~focal) ...
Paramétrage de docker-compose-plugin (2.29.7-1~ubuntu.20.04~focal) ...
```
* this [askUbuntu question's 31 answer](https://askubuntu-com.translate.goog/questions/1396689/docker-compose-cant-execute-command-docker-compose-not-found?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=fr&_x_tr_pto=sc) explains that from V2 version: 
  * you don't have to use *docker-compose up -d*
  * but *docker compose up -d* (compose is a plugin from Docker)
## It works with *docker compose up -d*
```bash
jmena01@M077-1840900:~/CONSULTANT$ docker compose -f docker-compose.yml up -d
WARN[0000] /home/jmena01/CONSULTANT/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 35/2
 ✔ wordpress Pulled                                                                                                                                               46.6s 
 ✔ db Pulled                                                                                                                                                      36.0s 
[+] Running 5/5
 ✔ Network consultant_default        Created                                                                                                                       0.3s 
 ✔ Volume "consultant_wordpress"     Created                                                                                                                       0.0s 
 ✔ Volume "consultant_db"            Created                                                                                                                       0.1s 
 ✔ Container consultant-wordpress-1  Started                                                                                                                      14.6s 
 ✔ Container consultant-db-1         Started                                                                                                                      14.6s
```
* new Images
```bash
jmena01@M077-1840900:~$ docker image ls
REPOSITORY                   TAG                   IMAGE ID       CREATED         SIZE
wordpress                    latest                2d7bb61bd13c   13 hours ago    701MB # The Wordpress Image
mysql                        8.0                   6c55ddbef969   5 weeks ago     591MB # The database for Wordpress
formation_drupal-php-igpde   latest                3f79c66b1f24   2 months ago    2.54GB
formation_drupal-apache      latest                e11a9fa45cef   2 months ago    85.9MB
formation_drupal-php         latest                61ae0b86d0af   2 months ago    2.54GB
wodby/postgres               14                    f2a839d99b85   3 months ago    250MB
postgres                     12                    f671527fc54a   9 months ago    419MB
hello-world                  latest                d2c94e258dcb   18 months ago   13.3kB
tomcat                       8-jre8-openjdk-slim   4504998b1398   2 years ago     213MB
tomcat                       jre11-openjdk-slim    d488a1afd78b   2 years ago     243MB
```
* new active containers
```bash
jmena01@M077-1840900:~$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED              STATUS              PORTS                                   NAMES
5b47d398344b   wordpress   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, :::8080->80/tcp   consultant-wordpress-1
821d29260ec5   mysql:8.0   "docker-entrypoint.s…"   About a minute ago   Up About a minute   3306/tcp, 33060/tcp                     consultant-db-1
```
# [Lille docker scripts](https://forge.dgfip.finances.rie.gouv.fr/dgfip/esi59/formation-drupal-administrateur/-/tree/main/docker/scripts?ref_type=heads)
* especially [docker_compose_site.sh](https://forge.dgfip.finances.rie.gouv.fr/dgfip/esi59/formation-drupal-administrateur/-/blob/main/docker/scripts/docker_compose_site.sh?ref_type=heads)
* and [execute_command_in_php_container.sh](https://forge.dgfip.finances.rie.gouv.fr/dgfip/esi59/formation-drupal-administrateur/-/blob/main/docker/scripts/execute_command_in_php_container.sh?ref_type=heads)
## Note the [simplified scripts of Manuel](https://forge.dgfip.finances.rie.gouv.fr/dgfip/esi59/formation-drupal-administrateur/-/tree/main/instance%20docker%20minimal?ref_type=heads)
## Those Lille Docker scripts
* are reused in [WP Docker 2](./WPDockerWSL.md)
  * but also in [WP Doker 1](./WORDPRESS.md) 