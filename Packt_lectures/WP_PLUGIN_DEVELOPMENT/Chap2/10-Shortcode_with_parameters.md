# [Solution on Github](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/tree/main/ch2/ch2-twitter-embed)
* this Recipe number 10 correspond to [twitter embed](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/tree/main/ch2/ch2-twitter-embed) shortcode with params
# 51
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/wp-content/plugins$ mkdir ch2-twitter-embed && touch ch2-twitter-embed/ch2-twitter-embed.php
```
# 52
* A [good extract tutorial](https://www.w3schools.com/php/func_array_extract.asp) 
  * from the key makes a variable whose name is the key
  * whose value is the value associated to the key.
* for shortcode_atts the [code of the function](https://developer.wordpress.org/reference/functions/shortcode_atts/) speaks by itself
  * we get a key value pair with the key 'username', the value $atts['username'] if present otherwise 'ylefebvre'  
* Through extract the key username becomes $username
# 53
* for the script *//platform.twitter.com/widgets.js* I suppose it looks for the <a> links whose class is *twitter-timeline* it takes from the href value where to take the posts