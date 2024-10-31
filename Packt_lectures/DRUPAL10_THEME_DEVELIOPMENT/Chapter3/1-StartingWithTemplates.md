# 50
## Intalling and activating [drupal:webprofiler](https://www.drupal.org/project/webprofiler)
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev composer require drupal/webprofiler
./composer.json has been updated
Running composer update drupal/webprofiler
Gathering patches for root package.
Loading composer repositories with package information
Updating dependencies
Lock file operations: 11 installs, 0 updates, 0 removals
  - Locking doctrine/common (3.4.5)
  - Locking doctrine/event-manager (2.0.1)
  - Locking doctrine/persistence (3.4.0)
  - Locking drupal/devel (5.2.0)
  - Locking drupal/tracer (1.0.4)
  - Locking drupal/webprofiler (10.1.3)
  - Locking league/commonmark (2.5.3)
  - Locking league/config (v1.2.0)
  - Locking nette/php-generator (v4.1.6)
  - Locking nette/schema (v1.3.2)
  - Locking nette/utils (v4.0.5)
Writing lock file
Installing dependencies from lock file (including require-dev)
Package operations: 11 installs, 0 updates, 0 removals
  - Downloading doctrine/event-manager (2.0.1)
  - Downloading doctrine/persistence (3.4.0)
  - Downloading doctrine/common (3.4.5)
  - Downloading nette/utils (v4.0.5)
  - Downloading nette/php-generator (v4.1.6)
  - Downloading nette/schema (v1.3.2)
  - Downloading league/config (v1.2.0)
  - Downloading league/commonmark (2.5.3)
  - Downloading drupal/tracer (1.0.4)
  - Downloading drupal/devel (5.2.0)
  - Downloading drupal/webprofiler (10.1.3)
Gathering patches for root package.
Gathering patches for dependencies. This might take a minute.
  - Installing doctrine/event-manager (2.0.1): Extracting archive
  - Installing doctrine/persistence (3.4.0): Extracting archive
  - Installing doctrine/common (3.4.5): Extracting archive
  - Installing nette/utils (v4.0.5): Extracting archive
  - Installing nette/php-generator (v4.1.6): Extracting archive
  - Installing nette/schema (v1.3.2): Extracting archive
  - Installing league/config (v1.2.0): Extracting archive
  - Installing league/commonmark (2.5.3): Extracting archive
  - Installing drupal/tracer (1.0.4): Extracting archive
  - Installing drupal/devel (5.2.0): Extracting archive # Version 5.2.0 for drupal/devel
  - Installing drupal/webprofiler (10.1.3): Extracting archive # version 10.1.13 for drupal/webprofiler
1 package suggestions were added by new dependencies, use `composer suggest` to see details.
Generating autoload files
99 packages you are using are looking for funding.
Use the `composer fund` command to find out more!
phpstan/extension-installer: Extensions installed
Found 9 security vulnerability advisories affecting 4 packages.
Run composer audit for a full list of advisories.
Using version ^10.1 for drupal/webprofiler 
```
* The module has been downloaded at *web/modules/contrib/webprofiler* though id depends on *web/modules/contrib/devel*
* The versions indicated on the [project's page](https://www.drupal.org/project/webprofiler) don't match the installed version
* The activation command *(pm enable)* is interesting
### But I have an error
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev drush pm:enable webprofiler
The following module(s) will be enabled: webprofiler, devel, tracer

 Do you want to continue? (yes/no) [yes]:
 > yes


In PreExistingConfigException.php line 65:

  Configuration objects (system.menu.devel) provided by devel already exist in active configuration


Failed to run drush pm:enable webprofiler: exit status 1
```
* Following [this issue](https://www.drupal.org/project/devel/issues/2764325) I go on to the container and pass the following code
```bash
jpmena@packt-web:/var/www/html/web$ ../vendor/bin/drush php:cli
Psy Shell v0.11.18 (PHP 8.1.30 — cli) by Justin Hileman
Alps Trips (Drupal 10.1.1)
> $devel_menu = \Drupal\system\Entity\Menu::load('devel');
= Drupal\system\Entity\Menu {#7560
    #uuid: "180b83a6-3ddb-452a-ad9d-5404bf82f066",
    #langcode: "en",
    #status: true,
    #dependencies: [
      "enforced" => [
        "module" => [
          "devel",
        ],
      ],
    ],
    #_core: [
      "default_config_hash" => "3V-l1uuTcyirYOGLPZV5HWaDfr02uEbWZJIwc8Byz-c",
    ],
    #id: "devel",
    #label: "Development",
    #description: "Links related to Devel module.",
    #locked: true,
  }

> $devel_menu->delete();
= null
```
* I still have [another error](https://github.com/drush-ops/drush/issues/5941)
```bash
jpmena@packt-web:/var/www/html/web$ ../vendor/bin/drush pm:enable webprofiler
The following module(s) will be enabled: webprofiler, devel, tracer

 Do you want to continue? (yes/no) [yes]:
 > yes

> PHP Fatal error:  Trait "Drush\Commands\AutowireTrait" not found in /var/www/html/web/modules/contrib/devel/src/Drush/Commands/DevelCommands.php on line 25
>  [warning] Drush command terminated abnormally.

In ProcessBase.php line 171:

  Unable to decode output into JSON: Syntax error

  Fatal error: Trait "Drush\Commands\AutowireTrait" not found in /var/www/html/web/modules/contrib/devel/src/Drush/Commands/DevelCommands.php on line 25
```
* My drush version is too low
```bash
jpmena@packt-web:/var/www/html/web$ ../vendor/bin/drush --version
Drush Commandline Tool 11.6.0
```
### Installing the modules manually
* but going to [Admin/extends](https://packt.ddev.site/admin/modules) I check
  * Devel
  * Tracer
  * WebProfiler
* And I get the bar installed
* The [WebProfiler settings](https://packt.ddev.site/admin/config/development/devel/webprofiler?destination=/admin/modules) like on *Extension/WebProfiler/Configure*
  * checking the Theme Checkbox adds a very interesting new icon...
# 53
* associative (dictionaries in Python) versus index arrays (Lists in Python)
* Scalar by opposition to objects 
# 55 
* Dot notation adpats as weel to arrays as to objects
  * see the order of research for array element / property / getter
# 56
* the tilde operator in twig is used to concatenate strings