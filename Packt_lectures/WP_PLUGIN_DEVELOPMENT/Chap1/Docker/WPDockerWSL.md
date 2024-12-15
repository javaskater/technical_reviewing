# downloading the Official WP Plugin on my WSL/Ubuntu
* see [Wordpress Docker Installation on my Ubuntu PC at work](./WORDPRESS.md)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker$ docker compose -f docker-compose.yml up -d
WARN[0000] The "UID" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/jpmena/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 35/2
 ✔ wordpress Pulled                                           16.6s 
 ✔ db Pulled                                                  17.8s 
[+] Running 4/4
 ✔ Network docker_default        Created                                                              0.3s 
 ✔ Volume "docker_db"            Created                                                              0.0s 
 ✔ Container docker-db-1         Started                                                              4.2s 
 ✔ Container docker-wordpress-1 Started                                                               4.2s 
 jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS    PORTS                                                    NAMES
ad1d7107f91d   mysql:8.0   "docker-entrypoint.s…"   6 minutes ago   Up 6 minutes   33060/tcp, 0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp   docker-db-1
e0921d12c959   wordpress   "docker-entrypoint.s…"   6 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp                  docker-wordpress-1
 ```
## new shared wordpress folder
* Adding *Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress* to a new *.gitignore* file *Packt_lectures/WP_PLUGIN_DEVELOPMENT/.gitignore*
  * perhaps we could include some developped plugings
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT$ cat .gitignore 
/Chap1/Docker/wordpres # the shared wordpress folder is not to be saved to git
```
## The activated ports
```bash
 jpmena@LAPTOP-E2MJK1UO:~$ netstat -nta
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:3307            0.0.0.0:*               LISTEN # The docker-db-1 container exports 3306 -> 3307
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN # the docker-wordpress-1 exports 80 -> 8080
tcp        0      0 127.0.0.1:45639         0.0.0.0:*               LISTEN
tcp        0      0 10.255.255.254:53       0.0.0.0:*               LISTEN
tcp        0      0 127.0.0.1:45639         127.0.0.1:39024         ESTABLISHED
tcp        0      0 127.0.0.1:39022         127.0.0.1:45639         ESTABLISHED
tcp        0      0 127.0.0.1:39024         127.0.0.1:45639         ESTABLISHED
tcp        0      0 127.0.0.1:45639         127.0.0.1:39022         ESTABLISHED
tcp6       0      0 :::3307                 :::*                    LISTEN
tcp6       0      0 :::8080                 :::*                    LISTEN
tcp6       0      0 :::80                   :::*                    LISTEN
```
# Accessing the Worpress Site
* **http://localhost:8080/wp-admin/** user/password: admin/admin
# Accessing the mysql:8 Database
## the parameters
* from the [docker-compose file section wordpress](./docker-compose.yml)
```yaml
environment:
    WORDPRESS_DB_HOST: db
    WORDPRESS_DB_USER: exampleuser
    WORDPRESS_DB_PASSWORD: examplepass
    WORDPRESS_DB_NAME: exampledb
```
## from the Host
### using the mysql client of WSL
* installation of mysql-client (version 8.0)
```bash
jpmena@LAPTOP-E2MJK1UO:~$ sudo apt install mysql-client
[sudo] password for jpmena:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libopengl0
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  mysql-client-8.0 mysql-client-core-8.0 mysql-common
The following NEW packages will be installed:
  mysql-client mysql-client-8.0 mysql-client-core-8.0 mysql-common
0 upgraded, 4 newly installed, 0 to remove and 57 not upgraded.
Need to get 2754 kB of archives.
After this operation, 62.2 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```
* I can connect to the mysql in the [mysql docker-container like](https://stackoverflow.com/questions/33001750/connect-to-mysql-in-a-docker-container-from-the-host)
```bash
jpmena@LAPTOP-E2MJK1UO:~$ mysql -p exampledb -u exampleuser -P 3307
Enter password: #I enter examplepass
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```
* see the [answer 131](https://stackoverflow.com/questions/33001750/connect-to-mysql-in-a-docker-container-from-the-host) just add *-h 1.27.0.0.1* on the command line:
```bash
jpmena@LAPTOP-E2MJK1UO:~$ mysql -h 127.0.0.1 -p exampledb -u exampleuser -P 3307
Enter password:
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 24
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
12 rows in set (0.01 sec)
mysql> \q
Bye
```
### using [mysql Workbench on Windows](https://dev.mysql.com/downloads/workbench/)
* Same MSI 32 Bits for 32/64 Bits Windows plateforms
* I forgot my pswword on the Oracle WebSite (connection required)
### Using [DBeaver](https://dbeaver.io/)
* not as a Eclipse Plugin (like at work) but as StandAlone application
  * I choose the community version 
* downloads its own jdk
* when you connect its download the mysql jar connector.
* Excellente application !!!!
### Using [VSCode Extension MySQL management tool](https://marketplace.visualstudio.com/items?itemName=formulahendry.vscode-mysql)
* It is installed under WSL
* **PROBLEM**: it does not let me specify the DATABASE in the connection String
## from the container
* [connecting to the bash of a container](https://stackoverflow.com/questions/30172605/how-do-i-get-into-a-docker-containers-shell)
```bash
jpmena@LAPTOP-E2MJK1UO:~$ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED       STATUS       PORTS                                                    NAMES
ad1d7107f91d   mysql:8.0   "docker-entrypoint.s…"   2 hours ago   Up 2 hours   33060/tcp, 0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp   docker-db-1
e0921d12c959   wordpress   "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp                  docker-wordpress-1
jpmena@LAPTOP-E2MJK1UO:~$ docker exec -it docker-db-1 bash
bash-5.1# mysql -u exampleuser -p exampledb
Enter password:
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 31
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
Bye # quit the mysql client
bash-5.1# exit # quit the docker-db-1 container
exit
```
# giving the www-data:www-data of the container
* the uid:gid of me on the host see [paragrpah *Accessing the wordpress container* on WORDPRESS.md](./WORDPRESS.md)