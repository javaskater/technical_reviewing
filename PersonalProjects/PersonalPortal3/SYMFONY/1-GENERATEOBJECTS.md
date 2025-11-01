# to make an DTO object creation from a database
* see [doctrine documentation on Symfony WebSite](https://symfony.com/doc/current/doctrine.html)
## prerequisite 
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php composer req --dev symfony/maker-bundle
```
* see [passing composer commands directly from the host](./0-Composer.md)
* now at the very end of *composer.json* (file located at the project root) I have
```javascript
    "require-dev": {
        "symfony/maker-bundle": "^1.64"
    }
```
## Génératiing a Diplom object
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php bin/console make:entity
##################"""
 updated: src/Entity/Diplom.php

 Add another property? Enter the property name (or press <return> to stop adding fields):
 > 


           
  Success! 
           

 Next: When you're ready, create a migration with php bin/console make:migration
```
*  preparing the migration
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php bin/console make:migration
 created: migrations/Version20251101143254.php

           
  Success! 
           

 Review the new migration then run it with php bin/console doctrine:migrations:migrate
 See https://symfony.com/doc/current/bundles/DoctrineMigrationsBundle/index.html
 ```
 * on the php container at *migrations/Version20251101143254.php* (date time of the make:migration command)
   * the SQL Code in the php up method
```php
    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TABLE diplom (id INT AUTO_INCREMENT NOT NULL, school_name VARCHAR(255) NOT NULL, url VARCHAR(255) DEFAULT NULL, begin_date DATE NOT NULL, end_date DATE DEFAULT NULL, language VARCHAR(15) NOT NULL, content VARCHAR(500) DEFAULT NULL, PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('DROP TABLE Persons'); // it sees my existing tables
        $this->addSql('DROP TABLE jpm_diplomas');
    }
```
* the down method does the opposite
### Running the migration
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec php bin/console doctrine:migration:migrate

 WARNING! You are about to execute a migration in database "app" that could result in schema changes and data loss. Are you sure you wish to continue? (yes/no) [yes]:
 > # it asks for confirmation

[notice] Migrating up to DoctrineMigrations\Version20251101143254
[notice] finished in 113.9ms, used 12M memory, 1 migrations executed, 3 sql queries
                                                                                                                        
 [OK] Successfully migrated to version: DoctrineMigrations\Version20251101143254                                        *
 ```
 ## Conclusion
* I have 2 tables in my mysql8 database
  * accessing from the WSL host through the *mysql --host=127.0.0.1 --user=app --port=33066 --password='!ChangeMe!' app* command
```sql
mysql> SHOW TABLES;
+-----------------------------+
| Tables_in_app               |
+-----------------------------+
| doctrine_migration_versions |
| jpm_diplom                  |
+-----------------------------+
2 rows in set (0.00 sec)

mysql> select * from doctrine_migration_versions;
+------------------------------------------+---------------------+----------------+
| version                                  | executed_at         | execution_time |
+------------------------------------------+---------------------+----------------+
| DoctrineMigrations\Version20251101153911 | 2025-11-01 15:40:28 |             28 |
+------------------------------------------+---------------------+----------------+
1 row in set (0.00 sec)

mysql> SHOW COLUMNS FROM jpm_diplom;
+--------------------+---------------+------+-----+---------+----------------+
| Field              | Type          | Null | Key | Default | Extra          |
+--------------------+---------------+------+-----+---------+----------------+
| id                 | int           | NO   | PRI | NULL    | auto_increment |
| school_name        | varchar(255)  | NO   |     | NULL    |                |
| url                | varchar(300)  | YES  |     | NULL    |                |
| begin_date         | date          | NO   |     | NULL    |                |
| end_date           | date          | YES  |     | NULL    |                |
| cursus_description | varchar(1000) | YES  |     | NULL    |                |
+--------------------+---------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)
```