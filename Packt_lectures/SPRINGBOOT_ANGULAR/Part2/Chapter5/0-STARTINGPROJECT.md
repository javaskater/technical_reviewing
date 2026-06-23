# 80

## Missing dependency in the page

- see [the expected pom.xml](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-05/superheroes/pom.xml)

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

- It proposed me the **spring-boot-starter-webmvc** instead !!!
- without that dependency we don't have the

```bash
jmena01@m077-2281091:~/Ateliers/intellj/idea-IU-261.25134.95/workspace/superheroes/src/main/resources$ ll
total 20
drwxr-xr-x 4 jmena01 domain users 4096 juin  23 09:06 ./
drwxr-xr-x 4 jmena01 domain users 4096 juin  23 09:06 ../
-rw-r--r-- 1 jmena01 domain users   36 juin  23 09:06 application.properties
drwxr-xr-x 2 jmena01 domain users 4096 juin  23 09:06 static/ # comes with the starter-web
drwxr-xr-x 2 jmena01 domain users 4096 juin  23 09:06 templates/ # comes with the starter-web
```

# 81

- in my case the properties are
  - I don't know what the {{databasename}} are for in a .properties file

```bash
spring.datasource.url=jdbc:postgresql://localhost:5434/springdb?currentSchema=packt
spring.datasource.username=postgres
spring.datasource.password=pass

spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.properties.hibernate.format_sql=true
```

## Access on my local database

- on the command line start the postgres docker container:

```bash
# Start the conainer
jmena01@m077-2281091:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                    PORTS     NAMES
72bd3c9897d1   postgres      "docker-entrypoint.s…"   3 days ago     Exited (0) 16 hours ago             postgresql-container # my postgres container
34bb178b1496   hello-world   "/hello"                 13 days ago    Exited (0) 13 days ago              mystifying_lalande
20cf43cb22fd   postgres      "docker-entrypoint.s…"   6 months ago   Exited (0) 6 months ago             postgresql # a old 6 months postgres container
6dc856820a00   hello-world   "/hello"                 6 months ago   Exited (0) 6 months ago             reverent_joliot
jmena01@m077-2281091:~$ docker start postgresql-container # I start my recent postgres contianuer
postgresql-container
# Access the postgres database using the potgres client
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres -d springdb
Mot de passe pour l''utilisateur postgres :
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l''aide.

springdb=#
# Access the database
```

- we check we have our previous table in the Database

```sql
springdb=# \d packt.*
                            Table « packt.blog »
 Colonne |          Type          | Collationnement | NULL-able | Par défaut
---------+------------------------+-----------------+-----------+------------
 id      | integer                |                 |           |
 title   | character varying(255) |                 |           |
 author  | character varying(255) |                 |           |
 body    | character varying(255) |                 |           |

                            Séquence « packt.uuid »
  Type  | Début | Minimum |       Maximum       | Incrément | Cycles ? | Cache
--------+-------+---------+---------------------+-----------+----------+-------
 bigint |     1 |       1 | 9223372036854775807 |        50 | no       |     1

 springdb=# select * from packt.blog;
 id |        title         |      author       |               body
----+----------------------+-------------------+----------------------------------
  1 | Awesome Java Project | Seiji Villafranca | This is an awesome blog for java
(1 ligne)
```

## we can access it using PGADMIN

- I create srpingDevDb and inside a packt schema
- I test it using the psql command line tool

```bash
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres -d SpringDevDb
Mot de passe pour l''utilisateur postgres :
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l''aide.
SpringDevDb=# \d packt.*
Aucune relation nommée « packt.* » n'a été trouvée.
SpringDevDb=#
```

# 84

- near > Run adn debug icon on the upper bar there is an icon with 3 vertical dots
  - click on it then on edit ...
  - we ha already the registered Run configuration
