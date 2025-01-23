# the target
* Using an ORM
# The resource
* Only resource on GitHub: [End of the Recipe](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter5/recipe5-3/end)
# A new Database
* Before dropping the database stop the spring server
```bash
jmena01@M077-1840900:~/ERICA/E2025_01/ERI_03.25.01_06022025/source/SQL/scripts$ psql -h localhost -U packt -c "drop database football"
Password for user packt: 
ERROR:  database "football" is being accessed by other users
DÉTAIL : There are 10 other sessions using the database.
# After having stopped the local Spring server
jmena01@M077-1840900:~/ERICA/E2025_01/ERI_03.25.01_06022025/source/SQL/scripts$ psql -h localhost -U packt -c "drop database football"
Password for user packt: 
DROP DATABASE
```
* replay the creation and the insertion scripts
```bash
# creating the football database and its 2 tables
jmena01@M077-1840900:~/Documents/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/sql_docker$ psql -h localhost -U packt -f db-creation.sql 
Password for user packt: 
CREATE DATABASE
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
You are now connected to database "football" as user "packt".
CREATE TABLE
CREATE TABLE
# inserting data in the tables
jmena01@M077-1840900:~/Documents/CONSULTANT/technical_reviewing/Packt_lectures/SPRING_BOOT_3_COOKBOOK/Part2/sql_docker$ psql -h localhost -U packt -f insert-data.sql 
Password for user packt: 
##..............................
INSERT 0 1
INSERT 0 23
```
# A new project
* saving the old sql version
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook$ mv footballpg footballpg_sql
```
## starting a new project using [SpringIO](https://start.spring.io)
* That is Why there is no start folder/section in the [GitHub Ressources](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter5/recipe5-3)
* 3 dependecies added in [Spring IO](https://start.spring.io/) this time
    * *Spring Web*
    * *PostgreSQL Driver*
    * *Spring Data JPA* **NEW**
```bash
jmena01@M077-1840900:~/Téléchargements$ unzip footballpg.zip -d ~/CONSULTANT/my_springboot_30_cookbook/
Archive:  footballpg.zip
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/.gitignore  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/HELP.md  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/.mvn/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/.mvn/wrapper/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/.mvn/wrapper/maven-wrapper.properties  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/.gitattributes  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/test/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/test/java/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/test/java/com/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/test/java/com/packt/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/test/java/com/packt/footballpg/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/test/java/com/packt/footballpg/FootballpgApplicationTests.java  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/resources/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/resources/templates/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/resources/static/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/resources/application.properties  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/java/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/java/com/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/java/com/packt/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/java/com/packt/footballpg/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/src/main/java/com/packt/footballpg/FootballpgApplication.java  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/mvnw.cmd  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/pom.xml  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/footballpg/mvnw
```
* The project's *pom.xml* file contains:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <scope>runtime</scope>
</dependency>
```
# 196
* no use of int for the id, use Integer for a mapped value!
* It is important to make a distinction between the @Entity types
  * and their corresponding DTO (defined here as records) 
## mappedBy
* in TeamEntity (ManyToOne) refers to the field on the other side of the relation (here in PlayerEntity) used to make the association
* On the side of the ManyToOne I need to specify the Foreign Key *@Joincolumn(name="team_id")*
* For all the other fields, in the absence of the *@Column* annotation, the column name is calculated by passing
  * from the *Camel Case* variable notation
  * to the *Snake Case* column notation
## The annotations concern 
* the private fields
* not the Getters/Setters
## Difference with the sql previos recipes
* PlayerEntity does not have a *teamId* integer attribute, but directly points to the corresponding Team (hrough the *team_id* field of the *players* table)... 
## Regularly do
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/footballpg$ ./mvnw compile
```
# 197
* [Crud Repository](https://www.baeldung.com/spring-data-crud-repository-save) gives you come methods like save
* [JpaRepository](https://www.baeldung.com/the-persistence-layer-with-spring-data-jpa#1-automatic-custom-queries) allows you to declare/define some methods just by giving them a namefollowing a specific naming convention
  * You can specify the [Query attached to the method name](https://www.baeldung.com/the-persistence-layer-with-spring-data-jpa#2-manual-custom-queries)
## The service class
* the chapter 6 and after concern *src/main/java/com/packt/footballpg/FootballService.java*
* you have to stream a list in order to map it and after calling toList to the new stream created bay the map
  * see the [Java8 examples in that Post Blog](https://mkyong.com/java8/java-8-streams-map-examples/)
    * especially the *3.3 Java 8 example*
* *stream.toList()* is the same than *stream.collect(Collectors.toList())*. The latter ids Java8
* as the map has only one expression, it is that expression that is returned
## for each defined service function
* I immediatly get the corresponding [controller function](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-3/end/footballpg/src/main/java/com/packt/footballpg/FootballController.java) (I could have done a unit test)
### dont' forget page 199
* Chapter 11: setting parameters for connecting with Postgres database
* don't forget to start the database
```bash
jmena01@M077-1840900:~$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS                    PORTS     NAMES
8bdf0e12660a   postgres      "docker-entrypoint.s…"   6 days ago     Exited (0) 21 hours ago             postgresql # stopped
ff33c96207f7   hello-world   "/hello"                 7 months ago   Exited (0) 7 months ago             quirky_rhodes
a92bf72552c4   postgres:12   "docker-entrypoint.s…"   9 months ago   Exited (0) 9 months ago             postgresCont
jmena01@M077-1840900:~$ docker start postgresql # start the continer
postgresql
jmena01@M077-1840900:~$ psql -h localhost -U packt -d football # connect to the Database from the host
Password for user packt: 
psql (12.14 (Ubuntu 12.14-0ubuntu0.20.04.1), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 12, server major version 17.
         Some psql features might not work.
Type "help" for help.

football=# 
```
* the file *src/main/resources/application.yaml* is enough to create the link with the JPA
```yaml
spring:
    jpa:
        database-platform: org.hibernate.dialect.PostgreSQLDialect #no sS only S in PostgreSQLDialect
        open-in-view: false
    datasource:
        url: jdbc:postgresql://localhost:5432/football
        username: packt
        password: packt
```
### curl test
* Just take the second curl request from [the shell](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-3/end/scripts/requests.sh)
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/football/players?search=HER > byName.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   661    0   661    0     0  50846      0 --:--:-- --:--:-- --:--:-- 55083
jmena01@M077-1840900:~$ node -e "console.log(JSON.stringify(JSON.parse(require('fs').readFileSync(process.argv[1])), null, 4));" byName.json | tee byNameFmt.json
[
    {
        "name": "Kailen SHERIDAN",
        "jerseyNumber": 1,
        "position": "Goalkeeper",
        "dateOfBirth": "1995-07-16"
    },
    {
        "name": "Melissa HERRERA",
        "jerseyNumber": 7,
        "position": "Midfielder",
        "dateOfBirth": "1996-10-10"
    },
    {
        "name": "Sophia KLEINHERNE",
        "jerseyNumber": 4,
        "position": "Defender",
        "dateOfBirth": "2000-04-12"
    },
    {
        "name": "Erika HERNANDEZ",
        "jerseyNumber": 18,
        "position": "Forward",
        "dateOfBirth": "1999-03-17"
    },
    {
        "name": "Jennifer HERMOSO",
        "jerseyNumber": 10,
        "position": "Forward",
        "dateOfBirth": "1990-05-09"
    },
    {
        "name": "Oihane HERNANDEZ",
        "jerseyNumber": 12,
        "position": "Defender",
        "dateOfBirth": "2000-05-04"
    },
    {
        "name": "Alyssa NAEHER",
        "jerseyNumber": 1,
        "position": "Goalkeeper",
        "dateOfBirth": "1988-04-20"
    }
]
```
## searchPlayersByBirthDate
* In the controller I profit from the fact to pass from *@RequestParam* (?search=HER) to *@PathVariable* */players/birth/{date}*
  * the parameter name in the controller method must correspond especially if you have many *@PathVariable*
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/football/players/birth/2000-06-12 > byBirthDate.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   184    0   184    0     0    488      0 --:--:-- --:--:-- --:--:--   486
jmena01@M077-1840900:~$ node -e "console.log(JSON.stringify(JSON.parse(require('fs').readFileSync(process.argv[1])), null, 4));" byBirthDate.json | tee byBirthDateFmt.json
[
    {
        "name": "Zineb REDOUANI",
        "jerseyNumber": 2,
        "position": "Defender",
        "dateOfBirth": "2000-06-12"
    },
    {
        "name": "Olga CARMONA",
        "jerseyNumber": 19,
        "position": "Defender",
        "dateOfBirth": "2000-06-12"
    }
]
```
* In the database
```sql
football=# select * from players where date_of_birth = '06/12/2000'; --date in american format
   id   | jersey_number |      name      | position | date_of_birth | team_id 
--------+---------------+----------------+----------+---------------+---------
 467262 |             2 | Zineb REDOUANI | Defender | 2000-06-12    | 1884821
 413016 |            19 | Olga CARMONA   | Defender | 2000-06-12    | 1884823
(2 rows)
```
# 198
## 7 getTeam
* also here the stream().map(xxxxxxxxxx).toList() is only to return a list of Player from a list of PlayerEntitiy
  * this list of Player is the 3rd parameter of the Team record (the record not the TeamEntity).
*  we are reading not wrtiting so the @Transactional(readonly=true)
### curl
* see first curl command in the [request shell in the solution](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-3/end/scripts/requests.sh)
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/football/teams/1884823 > OneTeam.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2172    0  2172    0     0  98727      0 --:--:-- --:--:-- --:--:-- 98727
jmena01@M077-1840900:~$ node -e "console.log(JSON.stringify(JSON.parse(require('fs').readFileSync(process.argv[1])), null, 4));" OneTeam.json | tee OneTeamFmt.json
{
    "id": 1884823,
    "name": "Spain",
    "players": [
        {
            "name": "Alexia PUTELLAS",
            "jerseyNumber": 11,
            "position": "Midfielder",
            "dateOfBirth": "1994-02-04"
        },
        {
            "name": "Enith SALON",
            "jerseyNumber": 13,
            "position": "Goalkeeper",
            "dateOfBirth": "2001-09-24"
        },
################################ And many others ########################################
        {
              "name": "Rocio GALVEZ",
              "jerseyNumber": 20,
              "position": "Defender",
              "dateOfBirth": "1997-04-15"
          }
    ]
}
```
## create a new Team
* do we need to set the ID or will it be set in the save method 
  * see *src/main/java/com/packt/footballpg/TeamEntity.java*
```java
@Entity
@Table(name="teams")
public class TeamEntity {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY) //Auto generated id
    private Integer id;
```
### ERRATUM don't set the Entity ID before saving
```java
public Team createTeam(String name){
    Random random = new Random(); //No use
    TeamEntity teamE = new TeamEntity();
    Integer randomId = random.nextInt(); //No use
    while (randomId < 0){ //No use
        randomId = random.nextInt(); //No use
    }
    System.out.println(String.format("[createTeam/Service] team Is avant insertion %d", randomId));
    //teamE.setId(randomId); //don't set the ID
    teamE.setName(name);
    teamE = teamRepository.save(teamE);
    Team team = new Team(teamE.getId(), teamE.getName(), List.of());
    System.out.println(String.format("[createTeam/Service] team record created: %s", team));
    return team;
}
```
* I want to see the team in the above code:
```java
public record Team(Integer id, String name, List<Player> players) {
    public String toString(){
        return String.format("[Team] id:%d, name:%s, number of payers:%d", id, name, players.size());
    }
}
```
### Curl test
```bash
jmena01@M077-1840900:~$ curl --request POST -H "Content-Type: application/text" -d 'Antarctica' http://localhost:8080/football/teams
{"id":2,"name":"Antarctica","players":[]}
```
* in the Spring server output console
```bash
[createTeam/Service] team Is avant insertion 2069888608
[createTeam/Service] team record created: [Team] id:2, name:Antarctica, number of payers:0
```
* in the Postgres's Database:
```sql
football=# select * from teams where name ~ 'Antarctica';
 id |    name    
----+------------
  2 | Antarctica
(1 row)
```
## updatePlayerPosition
* the playerRepository (JpaRepository) has all the mehods od the CrudRepository
* in particular findById and save see (in the footballService):
  * *playerRepository.findById(id).orElse(null)*
  * *playerE = playerRepository.save(playerE);*
### The controller with many annotations
```java
@PutMapping("/player/{id}/position")
public Player updatePositionPlayer(@PathVariable Integer id, @RequestBody String position ){
    return this.footballService.updatePlayer(id, position);
}
```
### Curling
* Before the update of player **377762**
```sql
football=# select * from players where id = 377762;
   id   | jersey_number |      name      |  position  | date_of_birth | team_id 
--------+---------------+----------------+------------+---------------+---------
 377762 |             6 | Aitana BONMATI | Midfielder | 1998-01-18    | 1884823
(1 row)

football=# select distinct position from players;
  position  
------------
 Defender
 Goalkeeper
 Midfielder
 Forward
(4 rows)
```
* passing it from *Midfielder* to **Goalkeeper** using the WebService
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text"  --request PUT --data 'Goalkeeper' http://localhost:8080/football/player/377762/position
{"name":"Aitana BONMATI","jerseyNumber":6,"position":"Goalkeeper","dateOfBirth":"1998-01-18"}
```
* after the PUT command, we have in Database
```sql
football=# select * from players where id = 377762;
   id   | jersey_number |      name      |  position  | date_of_birth | team_id 
--------+---------------+----------------+------------+---------------+---------
 377762 |             6 | Aitana BONMATI | Goalkeeper | 1998-01-18    | 1884823
(1 row)

football=# select distinct position from players;
  position  
------------
 Defender
 Goalkeeper
 Midfielder
 Forward
(4 rows)
```
# 200
* The JPARepository queries by name are described in this [official link](https://docs.spring.io/spring-data/jpa/reference/jpa/query-methods.html)
# 201
> By creating a session or a transaction while you are retrieving the data, including the lazy
> relations. This is the approach followed in this recipe
>
> That is the reason to create a Service class and not return Entities directly in the RESTful API.
* A restController cannot accept Transactional methods