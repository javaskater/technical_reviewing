# Running composer from the Host
* see [All the docker commands available through this project](../DOCKER/COMMANDS.md)
* [From the docs](https://github.com/dunglas/symfony-docker/blob/main/README.md) 
*   * especially the doc for [Using a Database (Mysql in mys case)](https://github.com/dunglas/symfony-docker/blob/main/docs/mysql.md)
* The remote compose command installing the orm vendor dependency, also modifies the docker - compose file to add the Mysql image ...
> The Docker configuration of this repository is extensible thanks to Flex recipes. By default, the recipe installs PostgreSQL
```bash
docker compose exec php composer req symfony/orm-pack # symfony/orm-pack includes a recipe
```
* To be able to generate object from a mysql database I need the following
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php composer req --dev symfony/maker-bundle
fatal: detected dubious ownership in repository at '/app'
To add an exception for this directory, call:

        git config --global --add safe.directory /app

Running composer update symfony/maker-bundle
Loading composer repositories with package information
Restricting packages listed in "symfony/symfony" to "7.3.*"
Updating dependencies
Lock file operations: 3 installs, 0 updates, 0 removals
  - Locking nikic/php-parser (v5.6.2)
  - Locking symfony/maker-bundle (v1.64.0)
  - Locking symfony/process (v7.3.4)
Writing lock file
Installing dependencies from lock file (including require-dev)
Package operations: 3 installs, 0 updates, 0 removals
  - Downloading symfony/process (v7.3.4)
  - Downloading nikic/php-parser (v5.6.2)
  - Downloading symfony/maker-bundle (v1.64.0)
  - Installing symfony/process (v7.3.4): Extracting archive
  - Installing nikic/php-parser (v5.6.2): Extracting archive
  - Installing symfony/maker-bundle (v1.64.0): Extracting archive
Generating autoload files
43 packages you are using are looking for funding.
Use the `composer fund` command to find out more!

Symfony operations: 1 recipe (9d41628288aa2a1f150deb3a28d7b7f6)
  - Configuring symfony/maker-bundle (>=1.0): From github.com/symfony/recipes:main
Executing script cache:clear [OK]
Executing script assets:install public [OK]
              
 What's next? 
              

Some files have been created and/or updated to configure your new packages.
Please review, edit and commit them: these files are yours.

No security vulnerability advisories found.
Using version ^1.64 for symfony/maker-bundle
```