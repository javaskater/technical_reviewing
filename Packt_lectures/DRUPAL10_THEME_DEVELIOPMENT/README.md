# This is my lecture of the [Modernizing Drupal 10 Theme Development from Packt](https://www.packtpub.com/en-fr/product/modernizing-drupal-10-theme-development-9781803249025)
* This Book has only one author
## [Source Code for the book](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development)
* Like for almost any [Packt Source Code on Github](https://github.com/PacktPublishing/) there is a [GitHub Repo for Modernizing Drupal Theme Development](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development)
## DDEV
* The author use [DDEV](https://ddev.com/get-started/) like for the [Drupal 10 Development CookBok of Packt](../DRUPAL10_DEVELOPMENT_COOKBOOK/README.md) 
  * (I installed ddev there)
* More on the [DDEV insitialization with on issue when also using DockerDesktop](./DDEV.md)
## very important page the [ERRATA page on the GitHub repository](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/ERRATA.md)
# Note drush not working anymore
* Note that since the manual actvation of the DEVEL Module (WEB PROFILER p 50) drush returns an error
  * it did work earlier on 
```bash
jpmena@packt-web:/var/www/html/web$ ../vendor/bin/drush
PHP Fatal error:  Trait "Drush\Commands\AutowireTrait" not found in /var/www/html/web/modules/contrib/devel/src/Drush/Commands/DevelCommands.php on line 25
jpmena@packt-web:/var/www/html/web$ ../vendor/bin/drush -- # The only working command
Drush Commandline Tool 11.6.0
```