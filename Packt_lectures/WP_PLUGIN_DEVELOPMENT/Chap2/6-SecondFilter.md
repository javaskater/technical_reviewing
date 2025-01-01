# 35
* [email filter solution](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-email-page-link/ch2-email-page-link.php)
* [the_content filter](https://developer.wordpress.org/reference/hooks/the_content/) concerns the content of a post
* if after the function name there is no paramters:
  * 10 by default is the priority of the filter (the less the number the higher the priority)
  * 1 by default is the number of parameters (here one parameter is the content of a post)` 
## Creating the structure
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/wp-content/plugins$ mkdir ch2-email-page-link && touch ch2-email-page-link/ch2-email-page-link.php
```
## Getting the emailIcon
* [Getting the emailIcon from the solution](https://github.com/PacktPublishing/WordPress-Plugin-Development-Cookbook-Third-Edition/blob/main/ch2/ch2-email-page-link/mailicon.png)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/Packt_lectures/WP_PLUGIN_DEVELOPMENT/Chap1/Docker/wordpress/wp-content/plugins/ch2-email-page-link$ explorer.exe .
```
### Which opens The *Windows Explorer* 
* At the following address *\\wsl.localhost\Ubuntu\home\jpmena\CONSULTANT\technical_reviewing\Packt_lectures\WP_PLUGIN_DEVELOPMENT\Chap1\Docker\wordpress\wp-content\plugins\ch2-email-page-link*
# 36
* It is the **href** which is very long, it contains:
  * the mailto
  * the subject 
  * the body (&body) (very long with article permalink)
    * **%0A** means newLine 