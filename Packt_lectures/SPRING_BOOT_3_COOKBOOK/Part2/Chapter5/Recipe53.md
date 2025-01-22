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