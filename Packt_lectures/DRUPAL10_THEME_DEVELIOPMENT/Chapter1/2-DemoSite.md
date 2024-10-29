# 15
* I we log in as admin/admin we can access **https://packt.ddev.site/admin/structure**
  * with the normal admin/Seven/design
## ddev stop and tomorrow docker image ls and ddev start
# 16
* A field ia the minimal piece of information in Drupal
* It has
  * a Widget (for entering data)
  * a formatter (for displaying that piece of data)
* A *geographical coordinate field type* can have two HTML Inputs (two Widget)
* The formatter for a *geographical coordinate field type* can be a marker on a Map
# 17 
## Paragraphs
* The [paragraphs project](https://www.drupal.org/project/paragraphs) is a contibuted module (not in the Core)
  * It is a big module preinstalled by the [GitHub project Composer.json](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/composer.json) 
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development/web/modules/contrib/paragraphs$ ll
total 164
drwxr-xr-x 11 jpmena jpmena  4096 Aug 25  2022 ./
drwxr-xr-x 23 jpmena jpmena  4096 Oct 25 15:05 ../
-rw-r--r--  1 jpmena jpmena 18092 Nov 17  2016 LICENSE.txt
-rw-r--r--  1 jpmena jpmena  2828 Aug 25  2022 README.txt
-rw-r--r--  1 jpmena jpmena   683 Aug 25  2022 composer.json
drwxr-xr-x  4 jpmena jpmena  4096 Aug 25  2022 config/
drwxr-xr-x  2 jpmena jpmena  4096 Aug 25  2022 css/
drwxr-xr-x  2 jpmena jpmena  4096 Aug 25  2022 icons/
drwxr-xr-x  2 jpmena jpmena  4096 Aug 25  2022 js/
drwxr-xr-x  2 jpmena jpmena  4096 Aug 25  2022 migrations/
drwxr-xr-x  5 jpmena jpmena  4096 Aug 25  2022 modules/
-rw-r--r--  1 jpmena jpmena  1695 Aug 25  2022 paragraphs.api.php
-rw-r--r--  1 jpmena jpmena   568 Aug 25  2022 paragraphs.info.yml
-rw-r--r--  1 jpmena jpmena 17094 Aug 25  2022 paragraphs.install
-rw-r--r--  1 jpmena jpmena  1841 Aug 25  2022 paragraphs.libraries.yml
-rw-r--r--  1 jpmena jpmena   141 Aug 25  2022 paragraphs.links.action.yml
-rw-r--r--  1 jpmena jpmena   469 Aug 25  2022 paragraphs.links.menu.yml
-rw-r--r--  1 jpmena jpmena   290 Aug 25  2022 paragraphs.links.task.yml
-rw-r--r--  1 jpmena jpmena 20249 Aug 25  2022 paragraphs.module
-rw-r--r--  1 jpmena jpmena   608 Aug 25  2022 paragraphs.permissions.yml
-rw-r--r--  1 jpmena jpmena   226 Aug 25  2022 paragraphs.plugin_type.yml
-rw-r--r--  1 jpmena jpmena 11523 Aug 25  2022 paragraphs.post_update.php
-rw-r--r--  1 jpmena jpmena  1167 Aug 25  2022 paragraphs.routing.yml
-rw-r--r--  1 jpmena jpmena   403 Aug 25  2022 paragraphs.services.yml
drwxr-xr-x 10 jpmena jpmena  4096 Aug 25  2022 src/
drwxr-xr-x  2 jpmena jpmena  4096 Aug 25  2022 templates/
drwxr-xr-x  5 jpmena jpmena  4096 Aug 25  2022 tests/
``` 
* Paragraphs are a collection of fields
## Content types
* The different content types have each an URL to access all content built on that content type
* An instance of a content type is a **Node** in Drupal
## Vocabulary
* A tag is useful to categorize content or to aggregate it in one way
* Taxonomy system to manage the vocabulary of terms/tags
## Block
* to add contextual content around the main content
* the blocs have visibility Rules they are not related to a particular URL
  * but on nodes of a particular content type
  * but on user of a particular role
# 18
## Views
## Menus
* Every webpage in Drupal is a mix of Node, View, and blocs
* A menu is a tree and every leaf is a (Label, Url)
* Many Menus for a site (Main, USer, Footer)
# 19
## How to uncompress the csss/js and removes the cache
* The variable **IS_DDEV_PROJECT** is set to true
  * It has been set in every _./.ddev/.ddev-docker-compose*.yaml_ file
  * if we access the web container we see
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev ssh # accessing the Web Container
jpmena@packt-web:/var/www/html$ echo $IS_DDEV_PROJECT
true
```
* The *web/sites/development.services.yml* is a services configuration file
  * that defines parameters to be used by others services (defined in service definition files) 
  * here debug (Twig) true and cache (false)
# Summary
* If you don't remember of your WebSite *ddev describe* is your friend.
* *https://packt.ddev.site/* seemed to be OffLine on Chromen [ERR_CONN_RESET](https://kinsta.com/fr/base-de-connaissances/err_connection_reset/)
  * On Chrome I go to the vertical ... (at the upper right) And *Suppress Recent History* (All)
    * And it seems to work again
  * I opened it on Firefox and everything worked OK
* Using F12 I can access all the CSS Files uncompressed
* I see in Debug the Javascript Code
* Looking for the Page Source Code wee see in green the Template suggestions
