# The Solution
* on the [GitHub Account page](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/tree/main/ch2/ch2-nav-menu-filter)
# 44
* In my case (official Docker Wordpress Image) I don't have a detailed explanation of the error.
* I don't see the line and the message

## Fommowing a [Cali Blog Post](https://carlosguzman.dev/how-to-see-the-error-logs-in-wordpress-with-docker-in-linux/)
* First solution proposed
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/wp-content/plugins/ch2-nav-menu-filter$ docker logs docker-wordpress-1 | grep -i error
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.19.0.3. Set the 'ServerName' directive globally to suppress this message
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.19.0.3. Set the 'ServerName' directive globally to suppress this message
[Sun Jan 05 09:33:38.577427 2025] [mpm_prefork:notice] [pid 1:tid 1] AH00163: Apache/2.4.62 (Debian) PHP/8.2.26 configured -- resuming normal operations
[Sun Jan 05 09:33:38.578114 2025] [core:notice] [pid 1:tid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
[Sun Jan 05 09:55:51.064617 2025] [php:error] [pid 74:tid 74] [client 172.19.0.1:45580] PHP Parse error:  syntax error, unexpected identifier "ch2nmf_new_nav_menu_items" in /var/www/html/wp-content/plugins/ch2-nav-menu-filter/ch2-nav-menu-filter.php on line 14, referer: http://localhost:8080/wp-admin/plugins.php # My error like in the book
172.19.0.1 - - [05/Jan/2025:09:55:51 +0000] "GET /wp-admin/plugins.php?error=true&plugin=ch2-nav-menu-filter%2Fch2-nav-menu-filter.php&_error_nonce=5c9f4a21bd HTTP/1.1" 200 16274 "http://localhost:8080/wp-admin/plugins.php" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
```
* Second solution: output only terminal 2
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/wp-content/plugins/ch2-nav-menu-filter$ docker logs docker-wordpress-1 > /dev/null #only terminal 2 (errors) I don't need filtering
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.19.0.3. Set the 'ServerName' directive globally to suppress this message
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.19.0.3. Set the 'ServerName' directive globally to suppress this message
[Sun Jan 05 09:33:38.577427 2025] [mpm_prefork:notice] [pid 1:tid 1] AH00163: Apache/2.4.62 (Debian) PHP/8.2.26 configured -- resuming normal operations
[Sun Jan 05 09:33:38.578114 2025] [core:notice] [pid 1:tid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
[Sun Jan 05 09:55:51.064617 2025] [php:error] [pid 74:tid 74] [client 172.19.0.1:45580] PHP Parse error:  syntax error, unexpected identifier "ch2nmf_new_nav_menu_items" in /var/www/html/wp-content/plugins/ch2-nav-menu-filter/ch2-nav-menu-filter.php on line 14, referer: http://localhost:8080/wp-admin/plugins.php # My error like in the book
```
## Repeating the erro while the plugin is activated
* the propose me a [link to debug Wordpress](https://fr.wordpress.org/support/article/debugging-in-wordpress/)
* using [WP_DEBUG](https://fr.wordpress.org/support/article/debugging-in-wordpress/#wp_debug)
* I have in *Docker/wordpress/wp-config.php*:
```php
/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', !!getenv_docker('WORDPRESS_DEBUG', '') );
```
* It is explained in that [StackOverflow Post](https://stackoverflow.com/questions/73109392/enabling-wordpress-debug-mode-in-docker-compose-environment) 