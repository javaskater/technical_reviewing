* After renaming project vendor does not work anymore
  * needs to stop containers before moving vendor (because in use)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ sudo mv -v vendor vendor.bak_$(date '+%d%m%Y')
[sudo] password for jpmena: 
renamed 'vendor' -> 'vendor.bak_10112025'
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ sudo mv -v composer.lock  composer.lock.bak_$(date '+%d%m%Y')
renamed 'composer.lock' -> 'composer.lock.bak_10112025'
```
# Reload all libraries
* see [Composer basic usage](https://getcomposer.org/doc/01-basic-usage.md)
* restart the containers
* recreate all composer dependencies
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php composer update
Loading composer repositories with package information
Restricting packages listed in "symfony/symfony" to "7.3.*"
Updating dependencies
Nothing to modify in lock file
Writing lock file
Installing dependencies from lock file (including require-dev)
Nothing to install, update or remove
Generating autoload files
45 packages you are using are looking for funding.
Use the `composer fund` command to find out more!

Run composer recipes at any time to see the status of your Symfony recipes.

Executing script cache:clear [OK]
Executing script assets:install public [OK]

No security vulnerability advisories found.
Bumping dependencies
./composer.json has been updated (5 changes).
```
## No need of all that 
* Just [restart Visual Studio Code see link](https://developercommunity.visualstudio.com/t/intellisense-stops-working-after-renaming-class/1003988)
# Push project to my GitHub
* on the container side I Need to be able to create the .git directory
```bash
root@c868bf654f2c:/app# chmod 777 .
```
* on the host side
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git remote add origin git@github.com:javaskater/jpm_pages_symfony_vue.git
fatal: detected dubious ownership in repository at '/home/jpmena/CONSULTANT/jpm_pages_symfony_vue'
To add an exception for this directory, call:

        git config --global --add safe.directory /home/jpmena/CONSULTANT/jpm_pages_symfony_vue
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git config --global --add safe.directory /home/jpmena/CONSULTANT/jpm_pages_symfony_vue
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git remote -v # nothing
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git remote add origin git@github.com:javaskater/jpm_pages_symfony_vue.git
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git remote -v
origin  git@github.com:javaskater/jpm_pages_symfony_vue.git (fetch)
origin  git@github.com:javaskater/jpm_pages_symfony_vue.git (push)
```
* again on the contaier side
```bash
root@c868bf654f2c:/app# chmod 755 .
root@c868bf654f2c:/app# chmod 777 .git # I want the Hot to write int the .git directory
```
## Commit
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git add *
The following paths are ignored by one of your .gitignore files:
var
vendor
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
# for the moment i take the .env and .ev.dev files with me
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git add .editorconfig .env .env.dev .gitattributes .gitignore
pmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git commit -m "first version of my Peronal webSite"
[master (root-commit) a3f0fbf] first version of my Peronal webSite
 59 files changed, 10906 insertions(+)
 create mode 100644 .dockerignore
 create mode 100644 .editorconfig
 create mode 100644 .env
 create mode 100644 .env.dev
 create mode 100644 .gitattributes
 create mode 100644 .gitignore
 create mode 100644 Dockerfile
 create mode 100644 Dockerfile_back_11102025
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100755 bin/console
 create mode 100644 compose.override.yaml
 create mode 100644 compose.override.yaml_back_11102025
 create mode 100644 compose.prod.yaml
 create mode 100644 compose.yaml
 create mode 100644 composer.json
 create mode 100644 composer.lock
 create mode 100644 composer.lock.bak_10112025
 create mode 100644 config/bundles.php
 create mode 100644 config/packages/cache.yaml
 create mode 100644 config/packages/doctrine.yaml
 create mode 100644 config/packages/doctrine_migrations.yaml
 create mode 100644 config/packages/framework.yaml
 create mode 100644 config/packages/routing.yaml
 create mode 100644 config/preload.php
 create mode 100644 config/routes.yaml
 create mode 100644 config/routes/framework.yaml
 create mode 100644 config/services.yaml
 create mode 100644 docs/alpine.md
 create mode 100644 docs/digitalocean-dns.png
 create mode 100644 docs/digitalocean-droplet.png
 create mode 100644 docs/existing-project.md
 create mode 100644 docs/extra-services.md
 create mode 100644 docs/makefile.md
 create mode 100644 docs/mysql.md
 create mode 100644 docs/options.md
 create mode 100644 docs/production.md
 create mode 100644 docs/tls.md
 create mode 100644 docs/troubleshooting.md
 create mode 100644 docs/updating.md
 create mode 100644 docs/xdebug.md
 create mode 100644 frankenphp/Caddyfile
 create mode 100644 frankenphp/conf.d/10-app.ini
 create mode 100644 frankenphp/conf.d/20-app.dev.ini
 create mode 100644 frankenphp/conf.d/20-app.prod.ini
 create mode 100755 frankenphp/docker-entrypoint.sh
 create mode 100644 migrations/.gitignore
 create mode 100644 migrations/Version20251101153911.php
 create mode 100644 public/index.php
 create mode 100644 src/Controller/.gitignore
 create mode 100644 src/Controller/JPMController.php
 create mode 100644 src/DataFixtures/AppFixtures.php
 create mode 100644 src/DataFixtures/DiplomsFixtures.php
 create mode 100644 src/Entity/.gitignore
 create mode 100644 src/Entity/JpmDiplom.php
 create mode 100644 src/Kernel.php
 create mode 100644 src/Repository/.gitignore
 create mode 100644 src/Repository/JpmDiplomRepository.php
 create mode 100644 symfony.lock
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git branch -M main # oupps I forgot it
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ git push origin main # I does not need a password as my ssh Pub Key has been uploaded on GitHub
Enumerating objects: 72, done.
Counting objects: 100% (72/72), done.
Delta compression using up to 8 threads
Compressing objects: 100% (68/68), done.
Writing objects: 100% (72/72), 287.78 KiB | 1.96 MiB/s, done.
Total 72 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To github.com:javaskater/jpm_pages_symfony_vue.git
 * [new branch]      main -> main
```