# 21
* I access the wordpress files from the Host at *Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress*
  * the *Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/docker-compose.yml*
* and in the *Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/docker-compose.yml* we have:
```yaml
  wordpress:
    image: wordpress
    user: ${UID}
    restart: always
    ports:
      - 8080:80
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: exampleuser
      WORDPRESS_DB_PASSWORD: examplepass
      WORDPRESS_DB_NAME: exampledb
    volumes:
      - ./wordpress:/var/www/html # the subdirectory wordpress contains all the web files includinf the index.php of my wordpress installation
``` 
## adding an info.php
* At the root *Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/info.php*
```php
<?php phpinfo() ?>
```
* accessible via *http://localhost:8080/info.php*
  * php is version 8.2.26
## Adding a simple module
```bash
jpmena@LAPTOP-E2MJK1UO:~$ docker exec -it docker-wordpress-1 bash # Accessing the wordpress container
root@dc28d9c259c0:/var/www/html# ll wp-content/plugins/
bash: ll: command not found
root@dc28d9c259c0:/var/www/html# ls -l wp-content/plugins/
total 16
drwxr-xr-x 4 1000 1000 4096 Nov 21 14:07 akismet
drwxr-xr-x 2 1000 1000 4096 Dec 21 14:06 ch2-plugin-header # 1000 is me on the host that I translated as www-data in the container
-rw-r--r-- 1 1000 1000 2578 Mar 18  2019 hello.php
-rw-r--r-- 1 1000 1000   28 Jun  5  2014 index.php
root@dc28d9c259c0:/var/www/html# ls -al wp-content/plugins/ch2-plugin-header/
total 12
drwxr-xr-x 2 1000 1000 4096 Dec 21 14:06 .
drwxr-xr-x 4 1000 1000 4096 Dec 21 14:06 ..
-rw-r--r-- 1 1000 1000  232 Dec 21 14:10 ch2-plugin-header.php # 1000 is me on the host that I translated as www-data in the container
```
* 1000  on the Host is no more **www-data** in the *docker-wordpress-1* container!!!!
  * I have to pass again the Lille commands see the end of [Docker on WSL Ubuntu](../Chap1/Docker/WPDockerWSL.md)
```bash
jpmena@LAPTOP-E2MJK1UO:~$ docker exec -it docker-wordpress-1 bash # Accessing the wordpress container
# I have to pass again the Lille commands
root@dc28d9c259c0:/var/www/html# usermod -u 1000 www-data # Lille command
root@dc28d9c259c0:/var/www/html# groupmod -g 1000 www-data # Lille command
root@dc28d9c259c0:/var/www/html# ls -al #verification
total 268
drwxr-xr-x  5 www-data www-data  4096 Dec 16 16:15 .
drwxr-xr-x  1 root     root      4096 Dec  3 03:26 ..
-rw-r--r--  1 www-data www-data   261 Dec 15 15:27 .htaccess
-rw-r--r--  1 www-data www-data   405 Feb  6  2020 index.php
-rw-r--r--  1 www-data www-data    18 Dec 21 14:01 info.php
-rw-r--r--  1 www-data www-data 19915 Jan  1  2024 license.txt
-rw-r--r--  1 www-data www-data  7409 Jun 18  2024 readme.html
-rw-r--r--  1 www-data www-data  7387 Feb 13  2024 wp-activate.php
drwxr-xr-x  9 www-data www-data  4096 Nov 21 14:07 wp-admin
-rw-r--r--  1 www-data www-data   351 Feb  6  2020 wp-blog-header.php
-rw-r--r--  1 www-data www-data  2323 Jun 14  2023 wp-comments-post.php
-rw-r--r--  1 www-data www-data  5815 Dec  3 04:28 wp-config-docker.php
-rw-r--r--  1 www-data www-data  3336 Oct 15 15:24 wp-config-sample.php
-rw-r--r--  1 www-data www-data  5919 Dec 15 15:11 wp-config.php
drwxr-xr-x  6 www-data www-data  4096 Dec 15 15:26 wp-content
-rw-r--r--  1 www-data www-data  5617 Aug  2 19:40 wp-cron.php
drwxr-xr-x 30 www-data www-data 16384 Nov 21 14:07 wp-includes
-rw-r--r--  1 www-data www-data  2502 Nov 26  2022 wp-links-opml.php
-rw-r--r--  1 www-data www-data  3937 Mar 11  2024 wp-load.php
-rw-r--r--  1 www-data www-data 51367 Sep 30 19:12 wp-login.php
-rw-r--r--  1 www-data www-data  8543 Sep 18 22:37 wp-mail.php
-rw-r--r--  1 www-data www-data 29032 Sep 30 17:08 wp-settings.php
-rw-r--r--  1 www-data www-data 34385 Jun 19  2023 wp-signup.php
-rw-r--r--  1 www-data www-data  5102 Oct 18 15:56 wp-trackback.php
-rw-r--r--  1 www-data www-data  3246 Mar  2  2024 xmlrpc.php
root@dc28d9c259c0:/var/www/html# cat /etc/group | grep ^www
www-data:x:1000: # it is now 1000 and no more 33
root@dc28d9c259c0:/var/www/html# cat /etc/passwd | grep ^www
www-data:x:1000:1000:www-data:/var/www:/usr/sbin/nologin # it is now 1000:1000 and no more 33:33
```
