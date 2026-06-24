# 99

## Through Intellij

- Right Click on the repostory package / New ... / Spring Component (java)
  - I constructs the Rest Controller class automatically !!!!
- withour no further code, we have

```bash
jmena01@m077-2281091:~$ curl http://localhost:8080/api/v1/anti-heroes
{"timestamp":"2026-06-23T11:09:31.735Z","status":404,"error":"Not Found","path":"/api/v1/anti-heroes"}
```

# 100

## creating a mapper between dto and Entity

- [the latest version of ModelMapper is th 3.2.6](https://mvnrepository.com/artifact/org.modelmapper/modelmapper)
  - The book uses the 2.3.9 version
- I don't specify the 3.2.6 version
  - File / settings / Build / BuildTools /Maven

### to access the Maven dependecies see [the Maven tool window](https://www.jetbrains.com/help/idea/maven-projects-tool-window.html)

- accessible by **View | Tool Windows | Maven** (Folder _Dependencies_)

## The @Configuration

- is meant to contain only @Bean methods
- each such method returns an object available in the application context ...

## the DTO

- it is the controller and not the service that needs the DTO class !!!

# 101

- in 3 lines of code we do a lot of things

```java
    @GetMapping("/{id}")
    public AntiHeroDto getAntiHeroById(@PathVariable("id")UUID id){
        return convertToDto(service.findAntiHeroById(id));
    }

    private AntiHeroDto convertToDto(AntiHeroEntity entity){
        return mapper.map(entity, AntiHeroDto.class);
    }
```

- I still have a bad request

## At Startup automatic creation of the table

```bash
jmena01@m077-2281091:~$ psql -h localhost -p 5434 -U postgres -d SpringDevDb
Mot de passe pour l'utilisateur postgres :
psql (17.2 (Ubuntu 17.2-1.pgdg24.04+1), serveur 18.1 (Debian 18.1-1.pgdg13+2))
ATTENTION : psql version majeure 17, version majeure du serveur 18.
         Certaines fonctionnalités de psql pourraient ne pas fonctionner.
Saisissez « help » pour l'aide.

SpringDevDb=# \d packt.* # I did not have had to create it manually
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
```

## I tested the PostCommand using PostMan

- POST request
- URL http://localhost:8080/api/v1/antiheroes
- Body / Raw / JSON Format (select list at the very right)

```json
{
  "firstName": "JEan-Pierre",
  "lastName": "MENA",
  "house": "Neuilly Plaisance",
  "knownAs": "jpm"
}
```

- the answer is the same as the body with th id in more

```json
{
  "firstName": "JEan-Pierre",
  "house": "Neuilly Plaisance",
  "id": "e95f5f5b-cb1a-48af-ac6c-ee181a14740b", //What the response brings is the object with the UUID
  "knownAs": "jpm",
  "lastName": "MENA"
}
```

- The id is not 1 but _e95f5f5b-cb1a-48af-ac6c-ee181a14740b_
  - That is why my GET Request was malformed 1 is not a Java UUID

### The Equivalent curl command

- given by POSTMAN

```bash
curl --location --request POST 'http://localhost:8080/api/v1/antiheroes' \
--header 'Content-Type: application/json' \
--data-raw '{
    "firstName":"JEan-Pierre",
    "lastName": "MENA",
    "house": "Neuilly Plaisance",
    "knownAs": "jpm"
}'
```

### in the database springDevDb

- We have now an entry !!!

```sql
SpringDevDb=# select * from packt.anti_hero_entity;
                  id                  |        created_at         | first_name  |       house       | known_as | last_name
--------------------------------------+---------------------------+-------------+-------------------+----------+-----------
 e95f5f5b-cb1a-48af-ac6c-ee181a14740b | 23-06-02026 14:40:37 CEST | JEan-Pierre | Neuilly Plaisance | jpm      | MENA
(1 ligne)
```

### The Get Command with the good UUID

```bash
jmena01@m077-2281091:~$ curl -v --location --request GET 'http://localhost:8080/api/v1/antiheroes/e95f5f5b-cb1a-48af-ac6c-ee181a14740b'
Note: Unnecessary use of -X or --request, GET is already inferred.
* Uses proxy env variable no_proxy == 'localhost,127.0.0.1,.dgfip,.impots,172.16.32.15,10.154.53.200,.rie.gouv.fr'
* Host localhost:8080 was resolved.
* IPv6: ::1
* IPv4: 127.0.0.1
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080
> GET /api/v1/antiheroes/e95f5f5b-cb1a-48af-ac6c-ee181a14740b HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 200 # OK
< Content-Type: application/json
< Content-Length: 133
< Date: Tue, 23 Jun 2026 12:56:53 GMT
<
* Connection #0 to host localhost left intact
{"firstName":"JEan-Pierre","house":"Neuilly Plaisance","id":"e95f5f5b-cb1a-48af-ac6c-ee181a14740b","knownAs":"jpm","lastName":"MENA"}
```

- If I change a a letter from the UUID I get a 500 error and a Stacktrace in the output console of the server
  - It is because the exception is not caught to return a 404 Code

```bash
com.example.springbootsuperheroes.superheroes.antiHero.exception.NotFoundException: Anti-hero By Id: e95f5f5b-cb1a-48af-ac6c-ee181a14740c was not found # My Runtime Excption
	at com.example.springbootsuperheroes.superheroes.antiHero.service.AntiHeroService.lambda$findOrThrow$0(AntiHeroService.java:43) ~[classes/:na]
	at java.base/java.util.Optional.orElseThrow(Optional.java:403) ~[na:na]
	at com.example.springbootsuperheroes.superheroes.antiHero.service.AntiHeroService.findOrThrow(AntiHeroService.java:42) ~[classes/:na]
	at com.example.springbootsuperheroes.superheroes.antiHero.service.AntiHeroService.findAntiHeroById(AntiHeroService.java:23) ~[classes/:na]
	at com.example.springbootsuperheroes.superheroes.antiHero.controller.AntHeroController.getAntiHeroById(AntHeroController.java:23)
```

- the next method PUT shows us how to return an error Response Code

# 102

## PUT Method

- the function signature is the Get function signature + the Post function Signature
  - the request translated by POSTMAN

```bash
curl --location --request PUT 'http://localhost:8080/api/v1/antiheroes/e95f5f5b-cb1a-48af-ac6c-ee181a14740b' \
--header 'Content-Type: application/json' \
--data-raw '{
    "firstName":"JEan-Pierre",
    "lastName": "MENA",
    "house": "Neuilly Plaisance",
    "knownAs": "jpm",
    "id": "e95f5f5b-cb1a-48af-ac6c-ee181a14740b"
}'
```

- when the 2 Ids do not match We don't see the message _ids do not match_ in the result

```json
{
  "timestamp": "2026-06-23T13:43:49.228Z",
  "status": 400,
  "error": "Bad Request",
  "path": "/api/v1/antiheroes/e95f5f5b-cb1a-48af-ac6c-ee181a14740c"
}
```

- When update 200 OK (I changed the house field)

```sql
SpringDevDb=# select * from packt.anti_hero_entity;  -- before the update
                  id                  |        created_at         | first_name  |       house       | known_as | last_name
--------------------------------------+---------------------------+-------------+-------------------+----------+-----------
 e95f5f5b-cb1a-48af-ac6c-ee181a14740b | 23-06-02026 15:38:13 CEST | JEan-Pierre | Neuilly Plaisance | jpm      | MENA
(1 ligne)

SpringDevDb=# select * from packt.anti_hero_entity; -- after the update
                  id                  |        created_at         | first_name  |  house  | known_as | last_name
--------------------------------------+---------------------------+-------------+---------+----------+-----------
 e95f5f5b-cb1a-48af-ac6c-ee181a14740b | 23-06-02026 15:48:34 CEST | JEan-Pierre | Guilers | jpm      | MENA
(1 ligne)
```

# 102

## DELETE

```java
    @DeleteMapping("/{id}")
    public void deleteAntiHeroById(@PathVariable("id") UUID id){
        service.removeAntiHeroById(id);
    }
```

- the request

```bash
curl --location --request DELETE 'http://localhost:8080/api/v1/antiheroes/e95f5f5b-cb1a-48af-ac6c-ee181a14740b'
```

- after calling that method, the entry is not present in the Database

## making the GET Request catch the NotFoundException

- useful after we deleted the Entry
- Code taken from the PUT command

```java
    @GetMapping("/{id}")
    public AntiHeroDto getAntiHeroById(@PathVariable("id") UUID id){
        try
        {
            var entity = service.findAntiHeroById(id);
            return convertToDto(entity);
        } catch (NotFoundException nex)
        {
            throw new ResponseStatusException(
                HttpStatus.NOT_FOUND, "id does not match with an existing Hero"
            );
        }

    }
```

# 1O3

## Get all AntiHeroes

- be careful no / at the end of the URL (otherwise it is 404 Not Found)

```bash
jmena01@m077-2281091:~$ curl --location --request GET 'http://localhost:8080/api/v1/antiheroes'
[]
```

## StreamSupport

- [more on the SplitITerator](https://medium.com/unibench/java-spliterator-examine-how-arraylist-gets-converted-to-a-stream-3d1b23e31fab) when the second parameter is set to false it means we split the Steam not in parallel but in serial !!!!
- [Official documentation of a splitIterator](https://docs.oracle.com/javase/8/docs/api/java/util/Spliterator.html)
- an ierable ha s splitIterator
- I don't especially understand the split operator

```java
    @GetMapping
    public List<AntiHeroDto> getAntiHeroes(){
        var antiHeroEntityList = StreamSupport.stream(service.findAllAntiHeroes().spliterator(), false).collect(Collectors.toList());
        return antiHeroEntityList.stream().map(e -> convertToDto(e)).collect(Collectors.toList());
    }
```

- After two POST requests it gives

```bash
jmena01@m077-2281091:~$ curl --location --request GET 'http://localhost:8080/api/v1/antiheroes'
[{"firstName":"JEan-Pierre","house":"Neuilly Plaisance","id":"58554ea4-a75c-4030-93f7-6cd78c5bbe67","knownAs":"jpm","lastName":"MENA"},{"firstName":"Liliane","house":"Guilers","id":"803739e7-f55a-4ed3-a8e0-c74cc21dff61","knownAs":"lq","lastName":"QUERRE"}]
```

- and in the database

```sql
SpringDevDb=# select * from packt.anti_hero_entity;
                  id                  |        created_at         | first_name  |       house       | known_as | last_name
--------------------------------------+---------------------------+-------------+-------------------+----------+-----------
 58554ea4-a75c-4030-93f7-6cd78c5bbe67 | 24-06-02026 10:00:34 CEST | JEan-Pierre | Neuilly Plaisance | jpm      | MENA
 803739e7-f55a-4ed3-a8e0-c74cc21dff61 | 24-06-02026 10:01:06 CEST | Liliane     | Guilers           | lq       | QUERRE
(2 lignes)
```
