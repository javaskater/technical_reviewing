```bash
jmena01@m077-2281091:~/CONSULTANT/Spring-Boot-and-Angular/Chapter-07$ cp -pvr superheroes ~/Ateliers/intellj/idea-IU-261.25134.95/workspace/
```

- just start the Postgresql container

```bash
jmena01@m077-2281091:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                    PORTS     NAMES
72bd3c9897d1   postgres      "docker-entrypoint.s…"   9 days ago     Exited (0) 2 days ago               postgresql-container #our container
34bb178b1496   hello-world   "/hello"                 2 weeks ago    Exited (0) 2 weeks ago              mystifying_lalande
20cf43cb22fd   postgres      "docker-entrypoint.s…"   6 months ago   Exited (0) 6 months ago             postgresql
6dc856820a00   hello-world   "/hello"                 6 months ago   Exited (0) 6 months ago             reverent_joliot
jmena01@m077-2281091:~$ docker start postgresql-container # starting our container
```

- and adapt the datasource.url in the [application.properties](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-07/superheroes/src/main/resources/application.properties)
  - port 5434
  - database name
  - currentSchema

```bash
spring.datasource.url=jdbc:postgresql://localhost:5434/SpringDevDb?currentSchema=packt
```

# After starting th project solution

- we have in the database

```sql
SpringDevDb=# \d packt.*
                        Table « packt.anti_hero_entity »
  Colonne   |          Type          | Collationnement | NULL-able | Par défaut
------------+------------------------+-----------------+-----------+------------
 id         | uuid                   |                 | not null  |
 created_at | character varying(255) |                 |           |
 first_name | character varying(255) |                 | not null  |
 house      | character varying(255) |                 |           |
 known_as   | character varying(255) |                 |           |
 last_name  | character varying(255) |                 |           |
Index :
    "anti_hero_entity_pkey" PRIMARY KEY, btree (id)

Index « packt.anti_hero_entity_pkey »
 Colonne | Type | Clé ? | Définition
---------+------+-------+------------
 id      | uuid | oui   | id
clé primaire, btree, pour la table « packt.anti_hero_entity »

     Index « packt.uk_4xad1enskw4j1t2866f7sodrx »
 Colonne |          Type          | Clé ? | Définition
---------+------------------------+-------+------------
 email   | character varying(255) | oui   | email
unique , btree, pour la table « packt.user_entity »

                            Table « packt.user_entity »
    Colonne    |          Type          | Collationnement | NULL-able | Par défaut
---------------+------------------------+-----------------+-----------+------------
 id            | uuid                   |                 | not null  |
 email         | character varying(255) |                 |           |
 mobile_number | character varying(255) |                 |           |
 stored_hash   | bytea                  |                 |           |
 stored_salt   | bytea                  |                 |           |
Index :
    "user_entity_pkey" PRIMARY KEY, btree (id)
    "uk_4xad1enskw4j1t2866f7sodrx" UNIQUE CONSTRAINT, btree (email)

  Index « packt.user_entity_pkey »
 Colonne | Type | Clé ? | Définition
---------+------+-------+------------
 id      | uuid | oui   | id
clé primaire, btree, pour la table « packt.user_entity »
```

- no user for the moment

```sql
SpringDevDb=# select * from packt.anti_hero_entity; --we didn't lose our entities
                  id                  |        created_at         | first_name |  house  |  known_as   | last_name
--------------------------------------+---------------------------+------------+---------+-------------+-----------
 803739e7-f55a-4ed3-a8e0-c74cc21dff61 | 24-06-02026 10:01:06 CEST | Liliane    | Guilers | lq          | QUERRE
 8b24c68f-ac8f-4b8e-9844-b280164287b8 | 26-06-2026 15:05:19 CEST  | Nicolas    | PARIS   | super_nb    | Bérend
 d081b084-e90d-4025-85b9-eeb81658b898 | 26-06-2026 15:13:18 CEST  | Michael    | ISOLA   | super_micha | Reiter
(3 lignes)

SpringDevDb=# select * from packt.user_entity; --no entered user
 id | email | mobile_number | stored_hash | stored_salt
----+-------+---------------+-------------+-------------
(0 ligne)
```
