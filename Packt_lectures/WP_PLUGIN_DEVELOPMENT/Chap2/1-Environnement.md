# Starting the Environmnt
* see [My docker Wordpress on my WSL Ubuntu](../Chap1/Docker/WPDockerWSL.md)
## the conitainers
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker$ docker compose up -d
WARN[0000] The "UID" variable is not set. Defaulting to a blank string. 
WARN[0000] /home/jpmena/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Network docker_default        Created                                                                                                 0.2s 
 ✔ Container docker-wordpress-1  Started                                                                                                 1.0s 
 ✔ Container docker-db-1         Started 
```
## The Database
* from the WSL/Host
```bash
jpmena@LAPTOP-E2MJK1UO:~$ mysql -h 127.0.0.1 -p exampledb -u exampleuser -P 3307
Enter password:
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
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
* From DBeaver on Windows (Host) it also works