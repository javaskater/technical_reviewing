# 66

- I skip the direct Windows installation for Docker

```bash
jmena01@m077-2281091:~$ docker run --name postgresql-container -p 5434:5432 -e POSTGRES_PASSWORD=pass -d postgres
72bd3c9897d1fe1c19b6941dee260fbf372da2016374652f9e8feb93e476e4b5
jmena01@m077-2281091:~$ docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                    NAMES
72bd3c9897d1   postgres   "docker-entrypoint.s…"   11 seconds ago   Up 10 seconds   0.0.0.0:5434->5432/tcp   postgresql-container
```

- Mistake in the book it does a **-p 5434:5434** instead of **-p 5434:5432**
- test from my psql client

```bash
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres
Mot de passe pour l''utilisateur postgres : # enter pass
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l'aide.
```

## I don't know if the datas will be persistent !!!!

```sql
postgres=# CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);
CREATE TABLE
postgres=# \d
         Liste des relations
 Schéma | Nom  | Type  | Propriétaire
--------+------+-------+--------------
 public | cars | table | postgres
(1 ligne)
```

- stop and restart the container

```bash
jmena01@m077-2281091:~$ docker stop 72bd3c9897d1
72bd3c9897d1
jmena01@m077-2281091:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
jmena01@m077-2281091:~$ docker start 72bd3c9897d1
72bd3c9897d1
jmena01@m077-2281091:~$ docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS         PORTS                    NAMES
72bd3c9897d1   postgres   "docker-entrypoint.s…"   26 minutes ago   Up 4 seconds   0.0.0.0:5434->5432/tcp   postgresql-container
```

- I still connect and have the cars table...

## I stopped an restarted my computer

- I still have accedd to the container
  - and the mysql car table is still present !!!

```bash
jmena01@m077-2281091:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
jmena01@m077-2281091:~$ docker start 72bd3c9897d1
72bd3c9897d1
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres
Mot de passe pour l''utilisateur postgres :
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l''aide.

postgres=# \d
         Liste des relations
 Schéma | Nom  | Type  | Propriétaire
--------+------+-------+--------------
 public | cars | table | postgres
(1 ligne)

postgres=#
```

# 69

- testing a Villain class !!!!
  - see [Answer 6 of this StackOverflow post](https://stackoverflow.com/questions/48307487/setting-up-spring-boot-jpa-postgresql)

# 76

## remember palying with the Postgres container

```bash
jmena01@m077-2281091:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                    PORTS     NAMES
72bd3c9897d1   postgres      "docker-entrypoint.s…"   2 days ago     Exited (0) 2 days ago               postgresql-container # the container I restart
34bb178b1496   hello-world   "/hello"                 12 days ago    Exited (0) 12 days ago              mystifying_lalande
20cf43cb22fd   postgres      "docker-entrypoint.s…"   6 months ago   Exited (0) 6 months ago             postgresql
6dc856820a00   hello-world   "/hello"                 6 months ago   Exited (0) 6 months ago             reverent_joliot
# restarting the container
jmena01@m077-2281091:~$ docker start 72bd3c9897d1
72bd3c9897d1
# other way to start it (using the conainer name)
jmena01@m077-2281091:~$ docker start postgresql-container
postgresql-container
```

- accessing Postgres

```bash
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres
Mot de passe pour l''utilisateur postgres :
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l''aide.

postgres=# \d
         Liste des relations
 Schéma | Nom  | Type  | Propriétaire
--------+------+-------+--------------
 public | cars | table | postgres
(1 ligne)
# We create the asked fo Database
postgres=# CREATE DATABASE springDB;
CREATE DATABASE
# be careful all database nmes are in lowcase letters
postgres=# \l # it is recarded as springdb and not springDB
                                                          Liste des bases de données
    Nom    | Propriétaire | Encodage | Fournisseur de locale | Collationnement | Type caract. | Locale | Règles ICU : |    Droits d'accès
-----------+--------------+----------+-----------------------+-----------------+--------------+--------+--------------+-----------------------
 postgres  | postgres     | UTF8     | libc                  | en_US.utf8      | en_US.utf8   |        |              |
 springdb  | postgres     | UTF8     | libc                  | en_US.utf8      | en_US.utf8   |        |              |
 template0 | postgres     | UTF8     | libc                  | en_US.utf8      | en_US.utf8   |        |              | =c/postgres          +
           |              |          |                       |                 |              |        |              | postgres=CTc/postgres
 template1 | postgres     | UTF8     | libc                  | en_US.utf8      | en_US.utf8   |        |              | =c/postgres          +
           |              |          |                       |                 |              |        |              | postgres=CTc/postgres
(4 lignes)
```

- connecting directly to the database

```bash
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres -d springdb
Mot de passe pour l''utilisateur postgres :
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l''aide.

springdb=# -- I am already in the springdb database in the public schema
```

- I create a schema to be like at work

```sql
springdb=# CREATE SCHEMA IF NOT EXISTS packt AUTHORIZATION postgres;
CREATE SCHEMA
```

## entering the parameters

- In the demoJpa/src/main/resources/application.properties file I added:

```bash
spring.datasource.url=jdbc:postgresql://localhost:5434/springdb?currentSchema=packt
spring.datasource.username=postgres
spring.datasource.password=pass
```

- Maven / Run / compile now work ...

# 77

- creating the blog table for the book example

```sql
springdb=# SHOW SEARCH_PATH;
   search_path
-----------------
 "$user", public
(1 ligne)

springdb=# SET search_path TO packt; --all the operations (table creation for example) will happen in this schema
SET
springdb=# SHOW SEARCH_PATH;
 search_path
-------------
 packt
(1 ligne)
springdb=# CREATE TABLE blog (
  title VARCHAR(255),
  author VARCHAR(255),
  body text
);
CREATE TABLE
springdb=# select * from packt.blog; --test ...
 title | author | body
-------+--------+------
(0 ligne)
```

## The run command does not work

- instead use [Running script on startup](https://www.baeldung.com/running-setup-logic-on-startup-in-spring)
  - I chose the [Post Construct Annotation](https://www.baeldung.com/running-setup-logic-on-startup-in-spring#1-the-postconstruct-annotation)

```java
package org.example.demojpa.startup;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

@Component
public class PostConstructExampleBean
{
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @PostConstruct
    public void init(){
        String sql = "INSERT INTO blog (title, author, body) VALUES ('Awesome Java Project', 'Seiji Villafranca', 'This is an wesome blog for java')";
        int rows = jdbcTemplate.update(sql);
        System.out.println(String.format("On Startup number of rows created %d", rows));

    }
}
```

- the starter class

```bash
2026-06-22T14:33:57.418+02:00  INFO 199282 --- [demoJpa] [           main] org.hibernate.orm.connections.pooling    : HHH10001005: Database info:
	Database JDBC URL [jdbc:postgresql://localhost:5434/springdb?currentSchema=packt] # It does see well my PostgreSQL Database
	Database driver: PostgreSQL JDBC Driver
	Database dialect: PostgreSQLDialect
	Database version: 18.1 # The Postgres version in the container
	Default catalog/schema: springdb/packt # Database/Schema name
	Autocommit mode: undefined/unknown
	Isolation level: READ_COMMITTED [default READ_COMMITTED]
	JDBC fetch size: none
	Pool: DataSourceConnectionProvider
	Minimum pool size: undefined/unknown
	Maximum pool size: undefined/unknown
2026-06-22T14:33:57.594+02:00  INFO 199282 --- [demoJpa] [           main] org.hibernate.orm.core                   : HHH000489: No JTA platform available (set 'hibernate.transaction.jta.platform' to enable JTA platform integration)
2026-06-22T14:33:57.597+02:00  INFO 199282 --- [demoJpa] [           main] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
On Startup number of rows created 1 # The ouput on the console on @Postconstruct
2026-06-22T14:33:57.688+02:00  INFO 199282 --- [demoJpa] [           main] org.example.demojpa.DemoJpaApplication   : Started DemoJpaApplication in 1.069 seconds (process running for 1.294)
2026-06-22T14:33:57.695+02:00  INFO 199282 --- [demoJpa] [ionShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2026-06-22T14:33:57.697+02:00  INFO 199282 --- [demoJpa] [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown initiated...
2026-06-22T14:33:57.699+02:00  INFO 199282 --- [demoJpa] [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown completed.

Process finished with exit code 0
```

- in the Postgres Database

```sql
springdb=# select * from packt.blog; -- I called the main Java Code 2 times
        title         |      author       |              body
----------------------+-------------------+---------------------------------
 Awesome Java Project | Seiji Villafranca | This is an wesome blog for java
 Awesome Java Project | Seiji Villafranca | This is an wesome blog for java
(2 lignes)
```

# 78

## JPA Repository

- I add a id key at the blog table

```sql
springdb=# drop table blog;
DROP TABLE
springdb=# create table packt.blog (
id INTEGER,
title VARCHAR(255),
author VARCHAR(255),
body text
);
CREATE TABLE
springdb=# \d blog
                            Table « packt.blog »
 Colonne |          Type          | Collationnement | NULL-able | Par défaut
---------+------------------------+-----------------+-----------+------------
 id      | integer                |                 |           |
 title   | character varying(255) |                 |           |
 author  | character varying(255) |                 |           |
 body    | text                   |                 |           |
```

### The JavaCode

- The Blog Entity
  - There is an error in the book use **GenerationType.AUTO** and not <s>GenerationType.IDENTITY</s>

```java
package org.example.demojpa.beans;

import jakarta.persistence.*;

@Entity
@Table(name="blog")
public class Blog
{
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO, generator="UUID") //and not GenerationType.IDENTITY
    private Integer id;

    private String title;
    private String author;
    private String body;
    // Getters and setters for all private fields
```

- The repository (An interface is enough)

```java
package org.example.demojpa.repositories;

import org.example.demojpa.beans.Blog;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BlogRepository extends JpaRepository<Blog, Integer>
{
}
```

- The controller

```java
import org.example.demojpa.repositories.BlogRepository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/blogs")
public class EntitiesController
{
    BlogRepository blogRepository;

    public EntitiesController(BlogRepository blogRepository)
    {
        this.blogRepository = blogRepository;
    }

    @GetMapping("/new")
    public Blog saveBlogPost(){
        Blog b = new Blog();
        b.setTitle("Awesome Java Project");
        b.setAuthor("Seiji Villafranca");
        b.setBody("This is an awesome blog for java");

        Blog bsaved = blogRepository.save(b);
        System.out.println(String.format("On Startup Blog creates %d", bsaved.getId()));
        return bsaved;
    }
}
```

### The curl command

```bash
jmena01@m077-2281091:~$ curl http://localhost:8080/api/blogs/new
{"author":"Seiji Villafranca","body":"This is an awesome blog for java","id":1,"title":"Awesome Java Project"}
```

### In the Database

```sql
-- before running the curl command
springdb=# select * from packt.blog;
 id | title | author | body
----+-------+--------+------
(0 ligne)
-- After running the curl
springdb=# select * from packt.blog;
 id |        title         |      author       |               body
----+----------------------+-------------------+----------------------------------
  1 | Awesome Java Project | Seiji Villafranca | This is an awesome blog for java
(1 ligne)
```

# TODO

- make a POST REQUEST with a all Blog Fields from a POST Body !!!!
- using REST Client Extension of VSCode
