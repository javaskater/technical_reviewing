# [Wordpress Official Image](https://hub.docker.com/_/wordpress)
* the [source code of this Docker Image](https://github.com/docker-library/wordpress)
* I use the [docker-compose proposed file](./docker-compose.yml) (at the end of the page)
## Wordpress volume
```yaml
    volumes:
      - ./wordpress:/var/www/html # you have to give a path on the host side ./wordpress and not wordpress
```
* If you just say *wordpress* it is the name of an internal contniner's volume with no link to the host
* If you just say *./wordpress* it is the path on the host of a mount point with the /var/www/html directory on the container's side
### Permissions
* On the host's side all is www-data
```bash
jmena01@M077-1840900:~/CONSULTANT$ ll wordpress/wp-content/
total 20
drwxr-xr-x 4 www-data www-data 4096 nov.  22 10:59 ./
drwxr-xr-x 5 www-data www-data 4096 nov.  22 10:58 ../
-rw-r--r-- 1 www-data www-data   28 janv.  8  2012 index.php
drwxr-xr-x 3 www-data www-data 4096 nov.  21 15:07 plugins/
drwxr-xr-x 5 www-data www-data 4096 nov.  21 15:07 themes/
```
* [in the Lille DockerFile](https://forge.dgfip.finances.rie.gouv.fr/dgfip/esi59/formation-drupal-administrateur/-/blob/main/docker/images/Dockerfile.php?ref_type=heads) they are playing with permissions
* * on mys side, I just do:
```bash
jmena01@M077-1840900:~/CONSULTANT$ sudo chmod 777 wordpress/wp-content/plugins/
```
* I want to access the plugin directory to let it create a directory
## First test trying to start the image
* See [page about Docker](./Docker.md)
# Accessing the Wordpress
## The URL
* The first time *http://localhost:8080/* brings me to *http://localhost:8080/wp-admin/install.php*
* The volume are internal 
* for the wordpress volume I have to change for  a link
* my *user/password* is **admin/admin**
* see Chapter2 the plugin is well seen.
  * I can Activate or deactivate it
## Accessing the 2 containers
```bash
jmena01@M077-1840900:~/CONSULTANT$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED             STATUS             PORTS                                   NAMES
97db226dfc84   wordpress   "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:8080->80/tcp, :::8080->80/tcp   consultant-wordpress-1
56369dc0bfde   mysql:8.0   "docker-entrypoint.s…"   About an hour ago   Up About an hour   3306/tcp, 33060/tcp                     consultant-db-1
```
### Accessing the wordpress container
```bash
jmena01@M077-1840900:~/CONSULTANT$ docker exec -it consultant-wordpress-1 bash
root@97db226dfc84:/var/www/html# ls -l wp-content/plugins/
total 16
drwxr-xr-x 4 www-data www-data 4096 Nov 21 14:07 akismet
drwxr-xr-x 2   120344  3100035 4096 Nov 22 11:38 ch2-plugin-header # 120344 is the userid on the host 3100035 is the group id on the host
-rw-r--r-- 1 www-data www-data 2578 Mar 18  2019 hello.php
-rw-r--r-- 1 www-data www-data   28 Jun  5  2014 index.php
```
* userid and groupid on the host
```bash
jmena01@M077-1840900:~/CONSULTANT$ id -u
120344 # the user id I am working with on the host
jmena01@M077-1840900:~/CONSULTANT$ id -g
3100035 #the group id I am working with on the host
```
* If I pass the [Lille php DockerFilee commands](https://forge.dgfip.finances.rie.gouv.fr/dgfip/esi59/formation-drupal-administrateur/-/blob/main/docker/images/Dockerfile.php?ref_type=heads)

* on the container side
```bash
root@97db226dfc84:/var/www/html# usermod -u 120344 www-data # Lille command
root@97db226dfc84:/var/www/html# groupmod -g  3100035 www-data # Lille command
root@97db226dfc84:/var/www/html# ls -l wp-content/plugins/
total 16
drwxr-xr-x 4       33       33 4096 Nov 21 14:07 akismet
drwxr-xr-x 2 www-data www-data 4096 Nov 22 11:38 ch2-plugin-header
-rw-r--r-- 1       33       33 2578 Mar 18  2019 hello.php
-rw-r--r-- 1       33       33   28 Jun  5  2014 index.php
root@97db226dfc84:/var/www/html# chown -R www-data:www-data /var/www/html # Lille command
root@97db226dfc84:/var/www/html# ls -l wp-content/plugins/
total 16
drwxr-xr-x 4 www-data www-data 4096 Nov 21 14:07 akismet
drwxr-xr-x 2 www-data www-data 4096 Nov 22 11:38 ch2-plugin-header
-rw-r--r-- 1 www-data www-data 2578 Mar 18  2019 hello.php
-rw-r--r-- 1 www-data www-data   28 Jun  5  2014 index.php
```
* on the host side
```bash
jmena01@M077-1840900:~/CONSULTANT$ mkdir wordpress/wp-content/plugins/ch2-plugin-header2 # No problem to create a directory
```
* on the container side
```bash
root@97db226dfc84:/var/www/html# ls -l wp-content/plugins/
total 20
drwxr-xr-x 4 www-data www-data 4096 Nov 21 14:07 akismet
drwxr-xr-x 2 www-data www-data 4096 Nov 22 11:38 ch2-plugin-header
drwxr-xr-x 2 www-data www-data 4096 Nov 22 12:01 ch2-plugin-header2 # It has been translated to www-data
-rw-r--r-- 1 www-data www-data 2578 Mar 18  2019 hello.php
-rw-r--r-- 1 www-data www-data   28 Jun  5  2014 index.php
```
### Accessing the mysql (db) conntainer
* The access parameters for the database are in the [Docker compose File](./docker-compose.yml)
```bash
jmena01@M077-1840900:~/CONSULTANT$ docker exec -it consultant-db-1 bash
bash-5.1# mysql -u exampleuser exampledb -p
Enter password: # enter examplepass for the parameters see the docker-compose.yml file
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 49
Server version: 8.0.40 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables;
+-----------------------+
| Tables_in_exampledb   |
+-----------------------+
| wp_commentmeta        |
| wp_comments           |
| wp_links              |
| wp_options            |
| wp_postmeta           |
| wp_posts              |
| wp_term_relationships |
| wp_term_taxonomy      |
| wp_termmeta           |
| wp_terms              |
| wp_usermeta           |
| wp_users              |
+-----------------------+
12 rows in set (0.00 sec)

mysql> \q
Bye
```
### Accessing the database from the Host
* through port 33060/tcp
* installing mysql-client
```bash
jmena01@M077-1840900:~/CONSULTANT$ sudo apt install mysql-client
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances       
Lecture des informations d'état... Fait
Les paquets supplémentaires suivants seront installés : 
  mysql-client-8.0 mysql-client-core-8.0
Les NOUVEAUX paquets suivants seront installés :
  mysql-client mysql-client-8.0 mysql-client-core-8.0
0 mis à jour, 3 nouvellement installés, 0 à enlever et 469 non mis à jour.
Il est nécessaire de prendre 5 119 ko dans les archives.
Après cette opération, 74,7 Mo d'espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n] O
Réception de :1 http://10.154.53.200/ubuntu focal-updates/main amd64 mysql-client-core-8.0 amd64 8.0.39-0ubuntu0.20.04.1 [5 088 kB]
Réception de :2 http://10.154.53.200/ubuntu focal-updates/main amd64 mysql-client-8.0 amd64 8.0.39-0ubuntu0.20.04.1 [22,0 kB]
Réception de :3 http://10.154.53.200/ubuntu focal-updates/main amd64 mysql-client all 8.0.39-0ubuntu0.20.04.1 [9 364 B]
5 119 ko réceptionnés en 0s (70,1 Mo/s)      
Sélection du paquet mysql-client-core-8.0 précédemment désélectionné.
(Lecture de la base de données... 275984 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de .../mysql-client-core-8.0_8.0.39-0ubuntu0.20.04.1_amd64.deb ...
Dépaquetage de mysql-client-core-8.0 (8.0.39-0ubuntu0.20.04.1) ...
Sélection du paquet mysql-client-8.0 précédemment désélectionné.
Préparation du dépaquetage de .../mysql-client-8.0_8.0.39-0ubuntu0.20.04.1_amd64.deb ...
Dépaquetage de mysql-client-8.0 (8.0.39-0ubuntu0.20.04.1) ...
Sélection du paquet mysql-client précédemment désélectionné.
Préparation du dépaquetage de .../mysql-client_8.0.39-0ubuntu0.20.04.1_all.deb ...
Dépaquetage de mysql-client (8.0.39-0ubuntu0.20.04.1) ...
Paramétrage de mysql-client-core-8.0 (8.0.39-0ubuntu0.20.04.1) ...
Paramétrage de mysql-client-8.0 (8.0.39-0ubuntu0.20.04.1) ...
Paramétrage de mysql-client (8.0.39-0ubuntu0.20.04.1) ...
Traitement des actions différées (« triggers ») pour man-db (2.9.1-1) ...
```
* can connect through sock from the host
```bash
jmena01@M077-1840900:~/CONSULTANT$ mysql -h 127.0.0.1 -P 33060 -u exampleuser exampledb -p
Enter password: 
ERROR 2003 (HY000): Can't connect to MySQL server on '127.0.0.1:33060' (111)
```
* The port is not exported:
```bash
jmena01@M077-1840900:~/CONSULTANT$ netstat -tln
Connexions Internet actives (seulement serveurs)
Proto Recv-Q Send-Q Adresse locale          Adresse distante        Etat      
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN     
tcp6       0      0 :::3389                 :::*                    LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
tcp6       0      0 :::8080                 :::*                    LISTEN     
tcp6       0      0 ::1:3350                :::*                    LISTEN     
tcp6       0      0 :::5900                 :::*                    LISTEN     
tcp6       0      0 ::1:631                 :::*                    LISTEN
```
* No port exporting:
```bash
jmena01@M077-1840900:~/CONSULTANT$ docker port consultant-db-1
jmena01@M077-1840900:~/CONSULTANT$ docker port consultant-wordpress-1
80/tcp -> 0.0.0.0:8080
80/tcp -> [::]:8080
```
* I filed the [issue 931 on the wordpress on docker website](https://github.com/docker-library/wordpress/issues/931)