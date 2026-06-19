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
