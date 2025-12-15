# In this Part2 we are connecting to a Database
## Already installed on my computer
```bash
jmena01@m077-2281091:~$ docker --version
Docker version 27.5.1, build 9f9e405
jmena01@m077-2281091:~$ docker compose version # docker compose also present
Docker Compose version v2.32.4
```
# 189
## Accessing docker without sudo
* [Answer 1501 of this StackExchange post](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo)
* docker group already present
```bash
jmena01@m077-2281091:~$ cat /etc/group | grep -i docker
docker:x:985:
```
* Adding myself to that group
```bash
jmena01@m077-2281091:~$ echo $USER
jmena01
jmena01@m077-2281091:~$ sudo gpasswd -a $USER docker # I am adding mysel to the docker group
Ajout de l''utilisateur jmena01 au groupe docker
jmena01@m077-2281091:~$ cat /etc/group | grep -i docker
docker:x:985:jmena01 # I am in the docker group
```
* restarting the computer !!!!
* testing with a simple Image
```bash
jmena01@m077-2281091:~$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete 
Digest: sha256:d4aaab6242e0cace87e2ec17a2ed3d779d18fbfd03042ea58f2995626396a274
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
* the image hello-world is now in my repository List
```bash
jmena01@m077-2281091:~$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    1b44b5a3e06a   4 months ago   10.1kB
```
## getting and accessing a postgres container
### Getting and starting a container from a postgres image
```bash
# we look for the postgres image and create/start a postgresql container at the same time
jmena01@M077-1840900:~$ docker run -itd -e POSTGRES_USER=packt -e POSTGRES_PASSWORD=packt -p 5432:5432 --name postgresql postgres
Unable to find image 'postgres:latest' locally # We download the latest postgres (official) image
latest: Pulling from library/postgres
af302e5c37e9: Pull complete 
23db180a1f67: Pull complete 
dc59dd9c8eb3: Pull complete 
aec09e638045: Pull complete 
4dd47a683737: Pull complete 
7cebbe7849b3: Pull complete 
dc4330b02129: Pull complete 
498cc40b9fe9: Pull complete 
6d3411bb4696: Pull complete 
8f14f34d54d3: Pull complete 
88d4f7416643: Pull complete 
e91ad5cfb8d0: Pull complete 
e0c4d5055fb9: Pull complete 
254ee626d709: Pull complete 
Digest: sha256:87ec5e0a167dc7d4831729f9e1d2ee7b8597dcc49ccd9e43cc5f89e808d2adae
Status: Downloaded newer image for postgres:latest
8bdf0e12660a7d9bfcc0c34ba3246c5991db0920c1b71c6e221e4c9804f0898d
jmena01@M077-1840900:~$ docker ps # my container postgresql (from image postgres) has just been started
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                       NAMES
8bdf0e12660a   postgres   "docker-entrypoint.s…"   49 seconds ago   Up 12 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   postgresql
```
* the above command is in the [docker create + up command shell](./scripts/docker_postgres_create_up_connect.sh)
* Stopping the container [docker down command shell](./scripts/docker_postgres_down.sh)
  * see [this Baeldung link](https://www.baeldung.com/ops/docker-stop-delete-active-container)
```bash
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/scripts$ ./docker_postgres_down.sh 
postgresql 
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/scripts$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES # no more containers running
jmena01@m077-2281091:~$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
postgres      latest    b5caf683a8bb   6 days ago     456MB # The image is still here and does not need to be reloaded
hello-world   latest    1b44b5a3e06a   4 months ago   10.1kB
```
* to restart the container it does need to bre created again it is the joc ogf [that very simple script using container name](./scripts/docker_postgres_up.sh)
```bash
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/scripts$ ./docker_postgres_up.sh 
postgresql
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/scripts$ docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS         PORTS                    NAMES
20cf43cb22fd   postgres   "docker-entrypoint.s…"   28 minutes ago   Up 9 seconds   0.0.0.0:5432->5432/tcp   postgresql # the conntainer is started
```
### Installing the postgres client on the Host
```bash
jmena01@m077-2281091:~$ apt list --installed | grep postgresql

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

libobasis7.2-postgresql-sdbc/inconnu,now 7.2.7.2-2 amd64  [installé]
postgresql-client-17/noble-pgdg,now 17.2-1.pgdg24.04+1 amd64  [installé] # I alread installed it for profesional tests
postgresql-client-common/noble-pgdg,now 267.pgdg24.04+1 all  [installé]
```
* test the installed client
```bash
jmena01@m077-2281091:~$ psql --version
psql (PostgreSQL) 17.2 (Ubuntu 17.2-1.pgdg24.04+1)
```
### Accessing the Postgres server from the Host
* don't forget the *-h localhost* otherwise it tries to access through a socket
```bash
jmena01@M077-1840900:~$ psql -h localhost -U packt 
Password for user packt: # enter packt 
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
Type "help" for help.

packt=# \q

jmena01@M077-1840900:~$ psql -U packt # if I forget the -h localhost it tries to connect through a local socket
psql: error: la connexion au serveur sur le socket « /var/run/postgresql/.s.PGSQL.5432 » a échoué : Aucun fichier ou dossier de ce type
	Le serveur est-il actif localement et accepte-t-il les connexions sur ce socket ?
```
### Entering datas in the Database
* We are using 
  * the [script for creating the database and 2 tables: teams and players](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-1/start/sql/db-creation.sql)
    * I downloaded the script in [the creation](./sql_docker/insert-data.sql)
    * in the [Data insertion](./sql_docker/insert-data.sql)
    * note that after we have created the database we connect to it in order to place the tables inside it
```sql
CREATE DATABASE football
    WITH
    OWNER = packt
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

\c football --we connect to that database so that the tables are connected inside it

CREATE TABLE IF NOT EXISTS teams
(
    id integer GENERATED BY DEFAULT AS IDENTITY,
    name character varying(255),
    CONSTRAINT teams_pkey PRIMARY KEY (id)
);
``` 
  * the [script for entering datas into those 2 tables](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-1/start/sql/insert-data.sql)
    * note the first order in that script
```sql
\c football --we connect to the newly created database, so we are sure the
``` 
* I pass the 2 scripts using my host's postgres client (psql):
```bash
# football database creation
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/Spring-Boot-3.0-Cookbook/chapter5/recipe5-1/start/sql$ psql -h localhost -U packt -f db-creation.sql # football database creation 
Password for user packt: 
CREATE DATABASE
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17. # my client is old (postgres 12 On Ubuntu 20.04) and the server:latest at that date (17/01/2025) is postgresql 17
         Some psql features might not work.
You are now connected to database "football" as user "packt".
CREATE TABLE # teams table creation
CREATE TABLE # players table creation
# Adding a lot of datas to teams and players tables
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/Spring-Boot-3.0-Cookbook/chapter5/recipe5-1/start/sql$ psql -h localhost -U packt -f insert-data.sql 
Password for user packt: 
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
You are now connected to database "football" as user "packt".
psql:insert-data.sql:4: ERROR:  relation "albums" does not exist
LIGNE 1 : INSERT INTO albums # small mistake from a previous version of the book onlys teams and players tables have been previously created
                      ^
INSERT 0 1
INSERT 0 23
# ...............................................
INSERT 0 1
INSERT 0 23
```
### Testing the data entered
* Through psql
```bash
jmena01@M077-1840900:~$ psql -h localhost -U packt -d football # we directly connect to the football database
Password for user packt: 
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
Type "help" for help.

football=# select * from teams LIMIT 10;
   id    |    name    
---------+------------
 1884881 | Argentina
 1882891 | Australia
 1882881 | Brazil
 1883718 | Canada
 1882892 | China PR
 1885035 | Colombia
 1884880 | Costa Rica
 1883719 | Denmark
 1883720 | England
 1884761 | France
(10 rows)

football=# select * from players LIMIT 10;
   id   | jersey_number |         name         |  position  | date_of_birth | team_id 
--------+---------------+----------------------+------------+---------------+---------
 357669 |             2 | Adriana SACHS        | Defender   | 1993-12-25    | 1884881
 420326 |            10 | Dalila IPPOLITO      | Midfielder | 2002-03-24    | 1884881
 420324 |             8 | Daiana FALFAN        | Midfielder | 2000-10-14    | 1884881
 357671 |            17 | Camila GOMEZ ARES    | Midfielder | 1994-10-26    | 1884881
 417317 |            11 | Yamila RODRIGUEZ     | Forward    | 1998-01-24    | 1884881
 420334 |             3 | Eliana STABILE       | Defender   | 1993-11-26    | 1884881
 277423 |             5 | Vanesa SANTANA       | Midfielder | 1990-09-03    | 1884881
 420328 |            14 | Miriam MAYORGA       | Defender   | 1989-11-20    | 1884881
 357674 |            15 | Florencia BONSEGUNDO | Midfielder | 1993-07-14    | 1884881
 461591 |             4 | Julieta CRUZ         | Defender   | 1996-06-04    | 1884881
(10 rows)

football=# 
```
* Other way to do it
```bash
jmena01@M077-1840900:~$ psql -h localhost -U packt
Password for user packt: 
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
Type "help" for help.

packt=# select * from players LIMIT 10;
ERROR:  relation "players" does not exist
LIGNE 1 : select * from players LIMIT 10; # players and teams do not exit in the main database
                        ^
packt=# \c football # we connect to the right database
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
You are now connected to database "football" as user "packt".
football=# select * from players LIMIT 10;
   id   | jersey_number |         name         |  position  | date_of_birth | team_id 
--------+---------------+----------------------+------------+---------------+---------
 357669 |             2 | Adriana SACHS        | Defender   | 1993-12-25    | 1884881
 420326 |            10 | Dalila IPPOLITO      | Midfielder | 2002-03-24    | 1884881
 420324 |             8 | Daiana FALFAN        | Midfielder | 2000-10-14    | 1884881
 357671 |            17 | Camila GOMEZ ARES    | Midfielder | 1994-10-26    | 1884881
 417317 |            11 | Yamila RODRIGUEZ     | Forward    | 1998-01-24    | 1884881
 420334 |             3 | Eliana STABILE       | Defender   | 1993-11-26    | 1884881
 277423 |             5 | Vanesa SANTANA       | Midfielder | 1990-09-03    | 1884881
 420328 |            14 | Miriam MAYORGA       | Defender   | 1989-11-20    | 1884881
 357674 |            15 | Florencia BONSEGUNDO | Midfielder | 1993-07-14    | 1884881
 461591 |             4 | Julieta CRUZ         | Defender   | 1996-06-04    | 1884881
(10 rows)

football=# 
```
* Through PGADMIN4
  * Register server
  * localhost
  * Maintenance Database / User / Password: all **packt**
* PGADMIN 4 works partially
  * some commands give a 500 error (My PGADMIN has version 6.14 the current version is 8.14)
    * perhaps version 8.14 would more be adapted to Postgres 17
    * version 6.14 works well with Postgres 12
  * I can use the Query Editor when the focus is on football (schéma by default: *public*) 
  * Right click on Football Database and select **Generate ERD**
    * You will have figure 5.1
# Restarting the container the other Day
## The image
```bash
jmena01@M077-1840900:~$ docker image ls | grep postgres
postgres                     latest                9a0ce6be5dd4   2 months ago    435MB # The used image
wodby/postgres               14                    f2a839d99b85   5 months ago    250MB
postgres                     12                    f671527fc54a   11 months ago   419MB # an older one from another experiment
```
## The container
### the container is still present but not active/started: 
```bash
# Exception the container does not need to be re-created from the image postgres:latest
jmena01@M077-1840900:~$ docker run -itd -e POSTGRES_USER=packt -e POSTGRES_PASSWORD=packt -p 5432:5432 --name postgresql postgres
docker: Error response from daemon: Conflict. The container name "/postgresql" is already in use by container "8bdf0e12660a7d9bfcc0c34ba3246c5991db0920c1b71c6e221e4c9804f0898d". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
# The postgresql container is there and stopped 
jmena01@M077-1840900:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                    PORTS     NAMES
8bdf0e12660a   postgres      "docker-entrypoint.s…"   4 days ago     Exited (0) 3 days ago               postgresql
ff33c96207f7   hello-world   "/hello"                 7 months ago   Exited (0) 7 months ago             quirky_rhodes
a92bf72552c4   postgres:12   "docker-entrypoint.s…"   9 months ago   Exited (0) 9 months ago             postgresCont
```
### Just start it:
* docker start does the job
```bash
jmena01@M077-1840900:~$ docker start postgresql
postgresql
# the conainer is well started with port translation
jmena01@M077-1840900:~$ docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED      STATUS         PORTS                                       NAMES
8bdf0e12660a   postgres   "docker-entrypoint.s…"   4 days ago   Up 4 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   postgresql
```
* to start the container once it is created just use [this simple script](./scripts/docker_postgres_up.sh)
* see [the simple script](./scripts/docker_postgres_up.sh)
### check the database Volume is maintained
```bash
jmena01@M077-1840900:~$ psql -h localhost -U packt -d football # We directly connect to the football database
Password for user packt: 
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
Type "help" for help.

football=# select * from teams LIMIT 10; # it is the public schema no prefix/schema for the table name
   id    |    name    
---------+------------
 1884881 | Argentina
 1882891 | Australia
 1882881 | Brazil
 1883718 | Canada
 1882892 | China PR
 1885035 | Colombia
 1884880 | Costa Rica
 1883719 | Denmark
 1883720 | England
 1884761 | France
(10 rows)

football=# select * from players LIMIT 10; # it is the public schema no prefix/schema for the table name
   id   | jersey_number |         name         |  position  | date_of_birth | team_id 
--------+---------------+----------------------+------------+---------------+---------
 357669 |             2 | Adriana SACHS        | Defender   | 1993-12-25    | 1884881
 420326 |            10 | Dalila IPPOLITO      | Midfielder | 2002-03-24    | 1884881
 420324 |             8 | Daiana FALFAN        | Midfielder | 2000-10-14    | 1884881
 357671 |            17 | Camila GOMEZ ARES    | Midfielder | 1994-10-26    | 1884881
 417317 |            11 | Yamila RODRIGUEZ     | Forward    | 1998-01-24    | 1884881
 420334 |             3 | Eliana STABILE       | Defender   | 1993-11-26    | 1884881
 277423 |             5 | Vanesa SANTANA       | Midfielder | 1990-09-03    | 1884881
 420328 |            14 | Miriam MAYORGA       | Defender   | 1989-11-20    | 1884881
 357674 |            15 | Florencia BONSEGUNDO | Midfielder | 1993-07-14    | 1884881
 461591 |             4 | Julieta CRUZ         | Defender   | 1996-06-04    | 1884881
(10 rows)

football=# \q
```
## stopping the container
* just call **docker stop container_name** 
  * command of [this simple script](./scripts/docker_postgres_down.sh)
```bash
jmena01@M077-1840900:~$ docker stop postgresql
postgresql
jmena01@M077-1840900:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                     PORTS     NAMES
8bdf0e12660a   postgres      "docker-entrypoint.s…"   4 days ago     Exited (0) 9 seconds ago             postgresql # The conainer just stopped
ff33c96207f7   hello-world   "/hello"                 7 months ago   Exited (0) 7 months ago              quirky_rhodes
a92bf72552c4   postgres:12   "docker-entrypoint.s…"   9 months ago   Exited (0) 9 months ago              postgresCont
```