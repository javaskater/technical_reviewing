# Postgres Database creation ussing Docker
* and the official Postgres Image
* see [The README file of this Part 2](../README.md)
# 191
## Create a [new project through Spring IO](https://start.spring.io/)
* Group *com.packt*
* Artifact *footballpg*
* dependencies (use the *Add Depedencies / search Bar*)
  * Spring Web
  * Spring Data JPA
  * PostgreSQL Driver
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
  ### In the pom.xml there are the 3 dependencies:
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
  * For the runtime keyword see [answer 181 of this StackOverflow Post](https://stackoverflow.com/questions/12272499/maven-what-is-the-runtime-scope-purpose)
## After completing [Service](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-1/end/footballpg/src/main/java/com/packt/footballpg/service/TeamsService.java) and [controller](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-1/end/footballpg/src/main/java/com/packt/footballpg/controller/TeamsController.java)
* don't forget to complete the database access by Spring JDBC
* It is in the file [*src/main/resources/application.yml*](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-1/end/footballpg/src/main/resources/application.yml)

# 192
* Sarting the embedded server *./mvnw  spring-boot:run*
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/footballpg$ ./mvnw  spring-boot:run
[INFO] Scanning for projects...
[INFO] 
[INFO] ------------------------< com.packt:footballpg >------------------------
[INFO] Building footballpg 0.0.1-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] >>> spring-boot:3.4.1:run (default-cli) > test-compile @ footballpg >>
#.........................
2025-01-17T14:45:40.551+01:00  INFO 145440 --- [footballpg] [           main] org.hibernate.orm.connections.pooling    : HHH10001005: Database info:
        Database JDBC URL [Connecting through datasource 'HikariDataSource (HikariPool-1)']
        Database driver: undefined/unknown
        Database version: 17.2
        Autocommit mode: undefined/unknown
        Isolation level: undefined/unknown
        Minimum pool size: undefined/unknown
        Maximum pool size: undefined/unknown
#............................

2025-01-17T14:45:41.414+01:00  INFO 145440 --- [footballpg] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path '/'
# ..........................................;
```
## From the client using curl
```bash
jmena01@M077-1840900:~/Téléchargements$ curl http://localhost:8080/teams/count -H "Accept: application/json"
32
# We verify directly on the database itself
jmena01@M077-1840900:~/Téléchargements$ psql -h localhost -U packt -d football -c "select count(*) from teams" 
Password for user packt: 
 count 
-------
    32
(1 row)
```
# 192
* *@GetMapping("/"* does not work (404) use *@GetMapping* instead
## Test of the *ublic List<Team> getTeams()* service function
```bash
jmena01@M077-1840900:~/Téléchargements$ curl http://localhost:8080/teams -H "Accept: application/json"
[{"id":1884881,"name":"Argentina"},{"id":1882891,"name":"Australia"},{"id":1882881,"name":"Brazil"},{"id":1883718,"name":"Canada"},{"id":1882892,"name":"China PR"},{"id":1885035,"name":"Colombia"},{"id":1884880,"name":"Costa Rica"},{"id":1883719,"name":"Denmark"},{"id":1883720,"name":"England"},{"id":1884761,"name":"France"},{"id":1882879,"name":"Germany"},{"id":1885012,"name":"Haiti"},{"id":1883722,"name":"Italy"},{"id":1885011,"name":"Jamaica"},{"id":1883723,"name":"Japan"},{"id":1885010,"name":"Korea Republic"},{"id":1884821,"name":"Morocco"},{"id":1884883,"name":"Netherlands"},{"id":1883725,"name":"New Zealand"},{"id":1882893,"name":"Nigeria"},{"id":1882882,"name":"Norway"},{"id":1889512,"name":"Panama"},{"id":1885027,"name":"Philippines"},{"id":1884822,"name":"Portugal"},{"id":1884884,"name":"Republic of Ireland"},{"id":1885031,"name":"South Africa"},{"id":1884823,"name":"Spain"},{"id":1882883,"name":"Sweden"},{"id":1884203,"name":"Switzerland"},{"id":1882884,"name":"USA"},{"id":1886308,"name":"Vietnam"},{"id":1885017,"name":"Zambia"}]
```
## Test of the single Team
* [following that Blog](https://mkyong.com/spring/spring-jdbctemplate-querying-examples/) I explicily define the rowMapper this time!!!
* I don't want to use *BeanPropertyRowMapper<>(Team.class)* which infers the row mapping !!!!
  * new Code for the *src/main/java/com/packt/footballpg/service/TeamsService.java* Service:
```java
    private class TeamRowMapper implements RowMapper<Team> {

        @Override
        public Team mapRow(ResultSet rs, int rowNum) throws SQLException {
    
            Team team = new Team();
            team.setId(rs.getInt("id"));
            team.setName(rs.getString("name"));
            return team;
    
        }
    }

    public Team getTeam(Integer id){
        return jdbcTemplate.queryForObject("Select * from teams where id=?", new Object[]{id}, new TeamRowMapper());
    }
```
* I test 
```bash
jmena01@M077-1840900:~/Téléchargements$ curl http://localhost:8080/teams/1882883 -H "Accept: application/json"
{"id":1882883,"name":"Sweden"}
```
# Test part that is not in the book 
* but on the [GitHub solution](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-1/end/footballpg/src/test/java/com/packt/footballpg/TeamsServiceTests.java)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/footballpg$ ./mvnw  test
```
* I have problem with assertTrue and assertEquals be careful there are static methods, so the imports are static too:
```java
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;
```
## My test class is working
```java
package com.packt.footballpg;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.beans.factory.annotation.Autowired;

import com.packt.footballpg.service.TeamsService;
import com.packt.footballpg.entities.Team;

@SpringBootTest
public class TeamsServiceTests {
    
    @Autowired
    private TeamsService teamsService;

    @Test
    public void testGetTeamCount(){
        int count = teamsService.getTeamCount();
        assertTrue(count > 0);
    }

    @Test
    public void testGetTeams(){
        int count = teamsService.getTeams().size();
        assertTrue(count > 0);
    }

    @Test
    public void testASpecificTeam(){
        Team maTeam = teamsService.getTeam(1882883);
        assertEquals(maTeam.getName(), "Sweden");
    }
}
```