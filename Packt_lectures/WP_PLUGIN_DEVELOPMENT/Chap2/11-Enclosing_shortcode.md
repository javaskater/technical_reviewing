# 54
* The [solution on GitHub](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/tree/main/ch2/ch2-private-item-text)
* *Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/wp-content/plugins/ch2-private-item-text/ch2-private-item-text.php*
* the *$content* variable is added to the $atts variable and contains the text (HTML) between
  * [my_shortcode]
  * and [/my_shortcode]
# 56
* The solution of the previous [private text but with styling](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-private-item-text/ch2-private-item-text-v2.php)
# 57
* the first parameter, the handle is usefull when you have to define dependencies (its name must be unique in the Wordpress Site) 
```php
wp_enqueue_style('privateshortcodestyle', plugins_url('stylesheet.css', __FILE__));
```
* More on [plugin_url](https://developer.wordpress.org/reference/functions/plugins_url/)
* More on [wp_enqueue_style](https://developer.wordpress.org/reference/functions/wp_enqueue_style/)
# 58 Writinh Plugins using Object PHP
* same functionality than above but with creating an Object
  * [solution on Github](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-oo-private-item-text/ch2-oo-private-item-text.php)