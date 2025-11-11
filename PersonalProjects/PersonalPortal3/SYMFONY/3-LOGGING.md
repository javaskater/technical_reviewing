# Documentation about Monolog
[Using Monolog](https://symfony.com/doc/current/logging.html#monolog)
Better than the default Logger
# Installing Monolog
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php composer require symfony/monolog-bundle
The repository at "/app" does not have the correct ownership and git refuses to use it:

fatal: detected dubious ownership in repository at '/app'
To add an exception for this directory, call:

        git config --global --add safe.directory /app

./composer.json has been updated
The repository at "/app" does not have the correct ownership and git refuses to use it:

fatal: detected dubious ownership in repository at '/app'
To add an exception for this directory, call:

        git config --global --add safe.directory /app

Running composer update symfony/monolog-bundle
Loading composer repositories with package information
Restricting packages listed in "symfony/symfony" to "7.3.*"
Updating dependencies
Lock file operations: 3 installs, 0 updates, 0 removals
  - Locking monolog/monolog (3.9.0)
  - Locking symfony/monolog-bridge (v7.3.6)
  - Locking symfony/monolog-bundle (v3.10.0)
Writing lock file
Installing dependencies from lock file (including require-dev)
Package operations: 3 installs, 0 updates, 0 removals
  - Downloading monolog/monolog (3.9.0)
  - Downloading symfony/monolog-bridge (v7.3.6)
  - Downloading symfony/monolog-bundle (v3.10.0)
  - Installing monolog/monolog (3.9.0): Extracting archive
  - Installing symfony/monolog-bridge (v7.3.6): Extracting archive
  - Installing symfony/monolog-bundle (v3.10.0): Extracting archive
Generating autoload files
48 packages you are using are looking for funding.
Use the `composer fund` command to find out more!

Symfony operations: 1 recipe (22cc647fbf853201b90ef022802bbda6)
  - Configuring symfony/monolog-bundle (>=3.7): From github.com/symfony/recipes:main
Executing script cache:clear [OK]
Executing script assets:install public [OK]
              
 What's next? 
              

Some files have been created and/or updated to configure your new packages.
Please review, edit and commit them: these files are yours.

No security vulnerability advisories found.
Using version ^3.10 for symfony/monolog-bundle
```
## Configuring Monolog to write [to a different location](https://symfony.com/doc/current/logging.html#handlers-writing-logs-to-different-locations)
* nothing to do.
  * all environments are taken into account at **config/packages/monolog.yaml**
  * for the prod environment I just added a custom file
```yaml
file_log: # The part I just added
    type: stream
    # log to var/log/(environment).log
    path: "%kernel.logs_dir%/%kernel.environment%.log"
    # log *all* messages (debug is lowest level)
    level: info
main: # That was already there
    type: fingers_crossed
    action_level: error
    handler: file_log # I changed from nested to file_log
    excluded_http_codes: [404, 405]
    channels: ["!deprecation"]
    buffer_size: 50 # How many messages should be saved? Prevent memory leaks
```
# Using the Logger
* seems to be used like the [default Logger](https://symfony.com/doc/current/components/console/logger.html)