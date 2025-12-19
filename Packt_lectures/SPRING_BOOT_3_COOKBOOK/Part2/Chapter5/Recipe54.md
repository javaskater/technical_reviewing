# Créating the new Database football2
* Starting the PostgreSql Container grâceh au script [Postgres Docker Container UP](../scripts/docker_postgres_up.sh)
```bash
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/scripts$ ./docker_postgres_up.sh 
postgresql
```
## From the Ubuntu Host we pass the following commands
* Accessing Postgres from the Host
```bash
jmena01@m077-2281091:~$ psql -h localhost -U packt
Mot de passe pour l''utilisateur packt : 
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l''aide.

packt=#
```
* passing the Database creation command
```sql
packt=# CREATE DATABASE football2;
CREATE DATABASE
```
# With the two new configurations in the application.yml
* It creates the tables and the 2 sequences for the corresponding **id** field
```sql
football2=# \d+
                                             Liste des relations
 Schéma |      Nom       |   Type   | Propriétaire | Persistence | Méthode d''accès |   Taille   | Description 
--------+----------------+----------+--------------+-------------+-----------------+------------+-------------
 public | players        | table    | packt        | permanent   | heap            | 8192 bytes | 
 public | players_id_seq | séquence | packt        | permanent   |                 | 8192 bytes | 
 public | teams          | table    | packt        | permanent   | heap            | 0 bytes    | 
 public | teams_id_seq   | séquence | packt        | permanent   |                 | 8192 bytes | 
(4 lignes)
football2=# select * from players;
 id | date_of_birth | jersey_number | name | position | team_id 
----+---------------+---------------+------+----------+---------
(0 ligne)

football2=# select * from teams;
 id | name 
----+------
(0 ligne)
```
* no sql file created ...
```bash
jmena01@m077-2281091:/home/soda/atelierjavaeclipse/workspace/footballpg$ find . -name *.sql -type f
```
## Loading the [data.sql file provided on the GitHub Code Repository](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-4/end/footballpg/src/main/resources/data.sql)
```bash
jmena01@m077-2281091:~/CONSULTANT/Spring-Boot-3.0-Cookbook/chapter5/recipe5-5/start/footballpg/src/main/resources$ psql -d football2 -h localhost -U packt -f data.sql
########################################################################"
INSERT 0 1
INSERT 0 23
```
* now we have
```sql
football2=# select count(*) from players;
 count 
-------
   736
(1 ligne)

football2=# select count(*) from teams;
 count 
-------
    32
(1 ligne)
```
