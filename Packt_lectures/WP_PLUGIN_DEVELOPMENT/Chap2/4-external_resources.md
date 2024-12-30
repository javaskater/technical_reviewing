# Script to pass after each start
* I automated the Lille commands in [after_starting_container.sh](../Chap1/Docker/scripts/after_starting_container.sh)
# 29
* I forgot to activate the Plugin
  * before that The system must know that my plugin exists
  * the following comment must be at the start of *wordpress/wp-content/plugins/ch2-favicon/ch2-favicon.php*
    * the main php file has the smae name than the directory 
```php
/*
  Plugin Name: Chapter 2 - Favicon
  Plugin URI:
  Description: Companion to recipe 'Using WordPress path utility functions'
  Author: ylefebvre
  Version: 1.0
  Author URI: http://ylefebvre.ca/
 */
```
# 30
* The site icon can only be defined under General Settings
 * it is not specific to a particular theme
 * our plugin is also not specific to a particular theme