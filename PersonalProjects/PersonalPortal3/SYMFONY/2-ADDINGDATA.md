# [Working with fixtures](https://symfony.com/bundles/DoctrineFixturesBundle/current/index.html#installation)
* [This podcst is very interesting](https://symfonycasts.com/screencast/symfony-doctrine/persisting-fixtures)
* usually for testing, but in my case used for loading my personal datas
## [installing fixtures](https://symfony.com/bundles/DoctrineFixturesBundle/current/index.html#installation)
* only for DEV not on production
* installed from the host using *docker compose exec php {the command to be passed in the docker-compose's php service}*
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php composer require --dev doctrine/doctrine-fixtures-bundle
###############################################
#############################################
No security vulnerability advisories found.
Using version ^4.3 for doctrine/doctrine-fixtures-bundle
```
* we have a new File in the php container (*src/DataFixtures/AppFixtures.php*) which is a Feature example
  * My first feature **src/DataFixtures/DiplomsFixtures.php**
## Loading the fixture
* see [loading the just created fixture](https://symfony.com/bundles/DoctrineFixturesBundle/current/index.html#loading-fixtures)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php bin/console doctrine:fixtures:load --help
Description:
  Load data fixtures to your database

Usage:
  doctrine:fixtures:load [options]

##############################################""
  
    php bin/console doctrine:fixtures:load --dry-run
```
* Why is my Fixture not applied ? (todo)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php bin/console doctrine:fixtures:load --dry-run
   (dry-run)
   > purging database
   > loading App\DataFixtures\AppFixtures # not my fixture
```
* REASON: The Class Name was DiplomFixtures the Filename was DimplomsFixtures (with two s)
  * The class was not seen by Symfony AutoWire
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php bin/console doctrine:fixtures:load --dry-run
   (dry-run)
   > purging database
   > loading App\DataFixtures\AppFixtures
   > loading App\DataFixtures\DiplomFixtures
```
* Now I have (after I ran the Fixture:load with no dry run) with mysql client on the Host
```sql
mysql> select id, school_name, language, url from jpm_diplom;
+----+-------------------------+----------+------------------------------+
| id | school_name             | language | url                          |
+----+-------------------------+----------+------------------------------+
|  4 | Ecole Centrale de Lille | fr_FR    | 'https://centralelille.fr/   |
|  5 | Ecole Centrale de Lille | en_EN    | https://centralelille.fr/en/ |
|  6 | Ecole Centrale de Lille | de_DE    | https://centralelille.fr/en/ |
+----+-------------------------+----------+------------------------------+
3 rows in set (0.00 sec)
```
* or without Mysql Client on the Host:
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php bin/console dbal:run-sql "select id, school_name, language, url from jpm_diplom"
 ---- ------------------------- ---------- ------------------------------ 
  id   school_name               language   url                           
 ---- ------------------------- ---------- ------------------------------ 
  4    Ecole Centrale de Lille   fr_FR      'https://centralelille.fr/    
  5    Ecole Centrale de Lille   en_EN      https://centralelille.fr/en/  
  6    Ecole Centrale de Lille   de_DE      https://centralelille.fr/en/  
 ---- ------------------------- ---------- ------------------------------
 ```
 ## TO CHECK
 * when restarting the docker mysql container, will the data be still present ? answer yes (mysql volume)

## New Data in my fixture
* After adding new Diploms in [Diplom Fixture](https://github.com/javaskater/jpm_pages_symfony_vue/blob/main/src/DataFixtures/DiplomFixtures.php)
* One command to load the new Data
  * it truncates the actual datas before running the Fixtures
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php bin/console doctrine:fixtures:load

 Careful, database "app" will be purged. Do you want to continue? (yes/no) [no]: # It will empty the table
 > yes

   > purging database
   > loading App\DataFixtures\AppFixtures
   > loading App\DataFixtures\DiplomFixtures
# To check if my datas are present
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php bin/console dbal:run-sql "select id, school_name, language, url from jpm_diplom"
 ---- ------------------------- ---------- ------------------------------- 
  id   school_name               language   url                            
 ---- ------------------------- ---------- ------------------------------- 
  7    Ecole Centrale de Lille   fr_FR      https://centralelille.fr/      
  8    Ecole Centrale de Lille   en_EN      https://centralelille.fr/en/   
  9    Ecole Centrale de Lille   de_DE      https://centralelille.fr/en/   
  10   Université Lille 1        fr_FR      https://www.univ-lille.fr/     
  11   University of Lille       en_EN      https://www.univ-lille.fr/en/  
  12   Lille Universität         de_DE      https://www.univ-lille.fr/en/  
 ---- ------------------------- ---------- ------------------------------- 
 ```