# Before starting
```bash
# Whe check that the ddev images are present
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ docker image ls
REPOSITORY                        TAG                                  IMAGE ID       CREATED          SIZE
ddev/ddev-webserver               v1.23.5-packt-built                  d509e26d71b2   49 minutes ago   1.61GB
ddev/ddev-dbserver-mariadb-10.4   v1.23.5-packt-built                  266eeb1900ab   49 minutes ago   690MB
ddev/ddev-ssh-agent               v1.23.5-built                        5f8091055da5   23 hours ago     128MB
ddev/ddev-webserver               v1.23.5-tryddevproject-30483-built   05610360930f   24 hours ago     1.58GB
ddev/ddev-webserver               v1.23.5                              aff0bb0fe24e   10 days ago      1.56GB
ddev/ddev-dbserver-mariadb-10.4   v1.23.5                              b68f807ab536   11 days ago      690MB
ddev/ddev-traefik-router          v1.23.5                              da1fc460c87f   11 days ago      210MB
ddev/ddev-ssh-agent               v1.23.5                              bfed6ff7b109   11 days ago      128MB
ddev/ddev-utilities               latest                               09b7b0fddb95   5 weeks ago      68.3MB
node                              18-buster-slim                       f7d0a48c51e6   5 months ago     187MB
busybox                           stable                               6fd955f66c23   17 months ago    4.26MB
node                              16-alpine3.15                        477eb7db0f23   23 months ago    116MB
seleniarm/standalone-chromium     4.1.4-20220429                       11cb7be2ddf7   2 years ago      1.54GB
# We Start ddev (It does not recreate the images)
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev start
Starting packt...
Port 80 is busy, using 33000 instead, see https://ddev.com/s/port-conflict
 Container ddev-ssh-agent  Recreate
 Container ddev-ssh-agent  Recreated
 Container ddev-ssh-agent  Started
ssh-agent container is running: If you want to add authentication to the ssh-agent container, run 'ddev auth ssh' to enable your keys.
time="2024-10-27T15:03:46+01:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.next.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
time="2024-10-27T15:03:46+01:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.selenium-chrome.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
Building project images...
..Project images built in 3s.
 Network ddev-packt_default  Created
 Container ddev-packt-next  Created
 Container ddev-packt-storybook  Created
 Container ddev-packt-db  Created
 Container ddev-packt-selenium-chrome  Created
 Container ddev-packt-web  Created
 Container ddev-packt-storybook  Started
 Container ddev-packt-next  Started
 Container ddev-packt-db  Started
 Container ddev-packt-selenium-chrome  Started
 Container ddev-packt-web  Started
Waiting for containers to become ready: [web db]
Warning: command 'n install 16' run as 'jpmena' failed with exit code 124:
Command 'n install 16' timed out after 30 seconds
Starting ddev-router if necessary...
 Container ddev-router  Created
 Container ddev-router  Started
Waiting 120s for additional project containers [ddev-packt-selenium-chrome ddev-packt-next ddev-packt-storybook] to become ready...
Some components of the project packt were not installed properly.
The project is running anyway, but see the warnings above for details.
If offline, run 'ddev restart' once you are back online.
If online, check your connection and run 'ddev restart' later.
If this seems to be a config issue, update it accordingly.
Successfully started packt
Your project can be reached at https://packt.ddev.site
See 'ddev describe' for alternate URLs.
```
* Go to [https://packt.ddev.site](https://packt.ddev.site)
# If the WebSite is a blank Drupal 10.1 to be installed 
* Which is not my case
* Just pass the **ddev build** command
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev build
Gathering patches for root package.
Installing dependencies from lock file (including require-dev)
Verifying lock file contents can be installed on current platform.
Nothing to install, update or remove
Generating autoload files
94 packages you are using are looking for funding.
Use the `composer fund` command to find out more!
phpstan/extension-installer: Extensions installed
  * Homepage: https://www.drupal.org/project/drupal
  * Support:
    * docs: https://www.drupal.org/docs/user_guide/en/index.html
    * chat: https://www.drupal.org/node/314178
 You are about to:
 * DROP all tables in your 'db' database.

 // Do you want to continue?: yes.

 [notice] Starting Drupal installation. This takes a while.
 [notice] Performed install task: install_select_language
 [notice] Performed install task: install_select_profile
 [notice] Performed install task: install_load_profile
 [notice] Performed install task: install_verify_requirements
 [notice] Performed install task: install_verify_database_ready
 [notice] Performed install task: install_base_system
 [notice] Performed install task: install_bootstrap_full
 [notice] Performed install task: install_config_import_batch
 [notice] Performed install task: install_config_download_translations
 [notice] Performed install task: install_config_revert_install_changes
 [notice] Performed install task: install_import_translations
 [notice] Performed install task: install_configure_form
 [notice] Performed install task: install_finish_translations
 [notice] Performed install task: install_finished
 [success] Installation complete.
>  [notice] Successfully indexed 14 items on Contents.
>  [notice] Message: Successfully indexed 14 items.
>
 [success] Cache rebuild complete.
yarn install v1.22.22
[1/4] Resolving packages...
success Already up-to-date.
Done in 0.09s.
yarn run v1.22.22
$ ls
alps_trips.info.yml  node_modules  package.json  yarn.lock
Done in 0.06s.

> storybook@1.0.0 generate-css
> postcss src/tailwind.css -o public/main.css

Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
``` 
# The https://packt.ddev.site/ website
* The adminsitrator (User 1) 
 * user **admin**
 * passord **admin**
* In the admin mode we have the SEVEN Appearance for example *https://packt.ddev.site/admin/content*
# Useful commands
## ddev describe
* The status and the way to access my containers
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev describe
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Project: packt ~/D10Theming/Modernizing-Drupal-10-Theme-Development https://packt.ddev.site             │
│ Docker platform: wsl2-docker-ce                                                                         │
│ Router: traefik                                                                                         │
├────────────┬──────┬────────────────────────────────────────────────────────────────┬────────────────────┤
│ SERVICE    │ STAT │ URL/PORT                                                       │ INFO               │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ web        │ OK   │ https://packt.ddev.site                                        │ drupal10 PHP8.1    │
│            │      │ InDocker: web:3000,443,80,8025                                 │ nginx-fpm          │
│            │      │ Host: 127.0.0.1:32770,32769                                    │ docroot:'web'      │
│            │      │                                                                │ Perf mode: none    │
│            │      │                                                                │ NodeJS:16          │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ db         │ OK   │ InDocker: db:3306                                              │ mariadb:10.4       │
│            │      │ Host: 127.0.0.1:32768                                          │ User/Pass: 'db/db' │
│            │      │                                                                │ or 'root/root'     │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ next       │ OK   │ https://packt.ddev.site:4001                                   │                    │
│            │      │ InDocker: next:4000                                            │                    │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ selenium-c │ OK   │ https://packt.ddev.site:7900                                   │                    │
│ hrome      │      │ InDocker: selenium-chrome:4444,5900,7900                       │                    │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ storybook  │ OK   │ https://packt.ddev.site:6006                                   │                    │
│            │      │ InDocker: storybook:6006                                       │                    │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ Mailpit    │      │ Mailpit: https://packt.ddev.site:8026                          │                    │
│            │      │ Launch: ddev mailpit                                           │                    │
├────────────┼──────┼────────────────────────────────────────────────────────────────┼────────────────────┤
│ All URLs   │      │ https://packt.ddev.site, https://127.0.0.1:32770,              │                    │
│            │      │ http://packt.ddev.site:33000, http://127.0.0.1:32769           │                    │
└────────────┴──────┴────────────────────────────────────────────────────────────────┴────────────────────┘
```
## ddev ssh 
* To access the Web container
```jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev ssh
jpmena@packt-web:/var/www/html$ ll
bash: ll: command not found
jpmena@packt-web:/var/www/html$ ls -al
total 564
drwxr-xr-x 15 jpmena jpmena   4096 Oct 25 15:05 .
drwxrwxrwx  3 root   root     4096 Oct 16 17:28 ..
drwxr-xr-x 19 jpmena jpmena   4096 Oct 27 15:03 .ddev
-rw-r--r--  1 jpmena jpmena    357 Oct 25 15:05 .editorconfig
drwxr-xr-x  8 jpmena jpmena   4096 Oct 26 14:41 .git
-rw-r--r--  1 jpmena jpmena   4034 Oct 25 15:05 .gitattributes
drwxr-xr-x  3 jpmena jpmena   4096 Oct 25 12:23 .github
-rw-r--r--  1 jpmena jpmena    836 Oct 25 12:23 .gitignore
-rw-r--r--  1 jpmena jpmena   1192 Oct 25 12:23 .gitpod.yml
drwxr-xr-x  2 jpmena jpmena   4096 Oct 25 12:23 .vscode
drwxr-xr-x  2 jpmena jpmena   4096 Oct 25 12:23 ERRATA
-rw-r--r--  1 jpmena jpmena   5285 Oct 25 12:23 ERRATA.md
-rw-r--r--  1 jpmena jpmena    826 Oct 25 12:23 HOW-TO.md
-rw-r--r--  1 jpmena jpmena   1062 Oct 25 12:23 LICENSE
-rw-r--r--  1 jpmena jpmena   3623 Oct 25 12:23 README.md
drwxr-xr-x  2 jpmena jpmena   4096 Oct 25 12:23 assets
-rw-r--r--  1 jpmena jpmena   5483 Oct 25 12:23 composer.json
-rw-r--r--  1 jpmena jpmena 466201 Oct 25 12:23 composer.lock
drwxr-xr-x  3 jpmena jpmena   4096 Oct 25 12:23 config
drwxr-xr-x  2 jpmena jpmena   4096 Oct 27 14:30 logs
drwxr-xr-x  9 jpmena jpmena   4096 Oct 25 15:01 next
drwxr-xr-x  2 jpmena jpmena   4096 Oct 25 12:23 patches
drwxr-xr-x  7 jpmena jpmena   4096 Oct 25 14:54 storybook
drwxr-xr-x 56 jpmena jpmena   4096 Oct 25 15:05 vendor
drwxr-xr-x  8 jpmena jpmena   4096 Oct 25 15:05 web
jpmena@packt-web:/var/www/html$ whoami
jpmena
```
## ddev drush
* to pass a drush command in the web-container
  * for example 
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev drush cr
 [success] Cache rebuild complete.
```
## ddev mysql
* To accees the Mysql Database
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 59
Server version: 10.4.34-MariaDB-1:10.4.34+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```
```sql
MariaDB [db]> SHOW TABLES; -- the case is important
+----------------------------------------------+
| Tables_in_db                                 |
+----------------------------------------------+
| batch                                        |
| block_content                                |
| block_content__body                          |
| block_content__field_cta                     |
| block_content__field_image                   |
| block_content__field_link                    |
| block_content_field_data                     |
| block_content_field_revision                 |
| block_content_revision                       |
| block_content_revision__body                 |
| block_content_revision__field_cta            |
| block_content_revision__field_image          |
| block_content_revision__field_link           |
| cache_bootstrap                              |
| cache_config                                 |
| cache_container                              |
| cache_data                                   |
| cache_default                                |
| cache_discovery                              |
| cache_entity                                 |
| cache_jsonapi_normalizations                 |
| cache_menu                                   |
| cache_rest                                   |
| cache_toolbar                                |
| cachetags                                    |
| config                                       |
| config_snapshot                              |
| consumer                                     |
| consumer__roles                              |
| consumer_field_data                          |
| file_managed                                 |
| file_usage                                   |
| help_search_items                            |
| history                                      |
| key_value                                    |
| key_value_expire                             |
| locale_file                                  |
| locales_location                             |
| locales_source                               |
| locales_target                               |
| media                                        |
| media__field_caption                         |
| media__field_media_image                     |
| media_field_data                             |
| media_field_revision                         |
| media_revision                               |
| media_revision__field_caption                |
| media_revision__field_media_image            |
| menu_link_content                            |
| menu_link_content_data                       |
| menu_link_content_field_revision             |
| menu_link_content_revision                   |
| menu_tree                                    |
| node                                         |
| node__body                                   |
| node__field_contents                         |
| node__field_destination                      |
| node__field_duration                         |
| node__field_lat_lng                          |
| node__field_level                            |
| node__field_new_price                        |
| node__field_old_price                        |
| node__field_origin                           |
| node__field_picture                          |
| node_access                                  |
| node_field_data                              |
| node_field_revision                          |
| node_revision                                |
| node_revision__body                          |
| node_revision__field_contents                |
| node_revision__field_destination             |
| node_revision__field_duration                |
| node_revision__field_lat_lng                 |
| node_revision__field_level                   |
| node_revision__field_new_price               |
| node_revision__field_old_price               |
| node_revision__field_origin                  |
| node_revision__field_picture                 |
| oauth2_token                                 |
| oauth2_token__scopes                         |
| paragraph__field_city                        |
| paragraph__field_contents                    |
| paragraph__field_description                 |
| paragraph__field_picture                     |
| paragraph__field_title                       |
| paragraph__field_trips                       |
| paragraph_revision__field_city               |
| paragraph_revision__field_contents           |
| paragraph_revision__field_description        |
| paragraph_revision__field_picture            |
| paragraph_revision__field_title              |
| paragraph_revision__field_trips              |
| paragraphs_item                              |
| paragraphs_item_field_data                   |
| paragraphs_item_revision                     |
| paragraphs_item_revision_field_data          |
| path_alias                                   |
| path_alias_revision                          |
| queue                                        |
| router                                       |
| search_api_db_contents                       |
| search_api_db_contents_search_api_datasource |
| search_api_db_contents_search_api_language   |
| search_api_db_contents_text                  |
| search_api_item                              |
| search_api_task                              |
| semaphore                                    |
| sequences                                    |
| sessions                                     |
| shortcut                                     |
| shortcut_field_data                          |
| shortcut_set_users                           |
| taxonomy_index                               |
| taxonomy_term__field_equipment               |
| taxonomy_term__field_picture                 |
| taxonomy_term__parent                        |
| taxonomy_term_data                           |
| taxonomy_term_field_data                     |
| taxonomy_term_field_revision                 |
| taxonomy_term_revision                       |
| taxonomy_term_revision__field_equipment      |
| taxonomy_term_revision__field_picture        |
| taxonomy_term_revision__parent               |
| user__roles                                  |
| user__user_picture                           |
| users                                        |
| users_data                                   |
| users_field_data                             |
| watchdog                                     |
+----------------------------------------------+
129 rows in set (0.001 sec)

MariaDB [db]> \q
Bye
```
