# The start and end on GitHub
* [Start of the Recipe 6 on GitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-6/start/football)
  * only the football server code
* [End of the Recipe 6 on gitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-6/end)
  * [football server](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-6/end/football)
  * [album client](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-6/end/albums) 
# 25
* Creating the album application using [spring.io](https://start.spring.io)
```bash
jmena01@M077-1840900:~/Téléchargements$ unzip albums.zip -d ~/CONSULTANT/my_springboot_30_cookbook/
Archive:  albums.zip
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/.gitignore  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/HELP.md  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/.mvn/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/.mvn/wrapper/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/.mvn/wrapper/maven-wrapper.properties  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/.gitattributes  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/test/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/test/java/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/test/java/com/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/test/java/com/packt/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/test/java/com/packt/albums/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/test/java/com/packt/albums/AlbumsApplicationTests.java  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/resources/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/resources/templates/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/resources/static/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/resources/application.properties  
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/com/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/com/packt/
   creating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/com/packt/albums/
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/com/packt/albums/AlbumsApplication.java  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/mvnw.cmd  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/pom.xml  
  inflating: /home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/mvnw
  ```
# 26 
* It is the same Player/Model on the server side and on the client side
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football/src/main/java/com/packt/football/model$ cp -pv Player.java ~/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/com/packt/albums
'Player.java' -> '/home/jmena01/CONSULTANT/my_springboot_30_cookbook/albums/src/main/java/com/packt/albums/Player.java'
```
## ports used in the Application
* The album client (in the Album controller) is addressing the port 8080 see  [yaml Configuration for production](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-6/end/albums/src/main/resources/application.yml)
* the album client app is starting for the Conrolller listening on port 8081 see  end of page 26 bottom
  * in [this Baeldung article](https://www.baeldung.com/spring-boot-change-port) there are many ways to change the listening port of a Spring boot application.
```bash
./mvnw spring-boot:run -Dspring-boot.run.arguments=--server.port=8081 # no blank between the -Dvariable and ist value
```
* At the end of the start
```bash
# the port is 8081 and not 8080
2025-01-15T11:14:01.589+01:00  INFO 48103 --- [albums] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8081 (http) with context path '/'ext path '/'
2025-01-15T11:14:01.613+01:00  INFO 48103 --- [albums] [           main] com.packt.albums.AlbumsApplication       : Started AlbumsApplication in 2.809 seconds (process running for 3.606)
```
* I have to start also the footbal application on port 8080
* It works
```bash
jmena01@M077-1840900:~/Téléchargements$ curl http://localhost:8081/albums/players
[{"id":"325636","jerseyNumber":11,"name":"Alexia PUTELLAS","position":"MidFielder","dateOfBirth":"1994-02-04"},{"id":"396930","jerseyNumber":2,"name":"Ona BATLLE","position":"Defender","dateOfBirth":"1999-06-10"},{"id":"396911","jerseyNumber":15,"name":"Eva NAVARRO","position":"Forward","dateOfBirth":"2001-01-27"},{"id":"420276","jerseyNumber":9,"name":"Esther GONZALEZ","position":"Forward","dateOfBirth":"1992-12-08"},{"id":"396914","jerseyNumber":14,"name":"Laia CODINA","position":"Defender","dateOfBirth":"2000-01-22"},{"id":"467287","jerseyNumber":16,"name":"Maria PEREZ","position":"Midfielder","dateOfBirth":"2001-12-24"},{"id":"387138","jerseyNumber":10,"name":"Jennifer HERMOSO","position":"Forward","dateOfBirth":"1990-05-09"},{"id":"387134","jerseyNumber":8,"name":"Vicky LOSADA","position":"Midfielder","dateOfBirth":"1991-01-01"},{"id":"398088","jerseyNumber":17,"name":"Alba REDONDO","position":"Forward","dateOfBirth":"1996-08-27"},{"id":"413022","jerseyNumber":3,"name":"Teresa ABELLEIRA","position":"Midfielder","dateOfBirth":"2000-01-09"},{"id":"377762","jerseyNumber":6,"name":"Aitana BONMATI","position":"Midfielder","dateOfBirth":"1998-01-18"},{"id":"387133","jerseyNumber":4,"name":"Irene PAREDES","position":"Defender","dateOfBirth":"1998-01-18"},{"id":"377723","jerseyNumber":20,"name":"Rocio GALVEZ","position":"Defender","dateOfBirth":"1997-04-15"},{"id":"420284","jerseyNumber":21,"name":"Claudia ZORNOZA","position":"Midfielder","dateOfBirth":"1990-10-20"},{"id":"415394","jerseyNumber":18,"name":"Salma PARALLUELO","position":"Forward","dateOfBirth":"2003-11-13"},{"id":"420277","jerseyNumber":7,"name":"Irene GUERRERO","position":"Midfielder","dateOfBirth":"1996-12-12"},{"id":"396907","jerseyNumber":23,"name":"Cata COLL","position":"Goalkeeper","dateOfBirth":"2001-04-23"},{"id":"396929","jerseyNumber":12,"name":"Oihane HERNANDEZ","position":"Defender","dateOfBirth":"2000-05-04"},{"id":"467297","jerseyNumber":22,"name":"Athenea DEL CASTILLO","position":"Forward","dateOfBirth":"2000-10-24"},{"id":"1884823","jerseyNumber":5,"name":"Ivana ANDRES","position":"Defender","dateOfBirth":"1994-07-31"},{"id":"398097","jerseyNumber":8,"name":"Mariona CALDENTEY","position":"Forward","dateOfBirth":"1996-03-19"},{"id":"398098","jerseyNumber":1,"name":"Misa RODRIGUEZ","position":"Goalkeeper","dateOfBirth":"1999-07-22"},{"id":"413016","jerseyNumber":19,"name":"Olga CARMONA","position":"Defender","dateOfBirth":"2000-06-12"},{"id":"415396","jerseyNumber":13,"name":"Enith SALON","position":"Goalkeeper","dateOfBirth":"2001-09-24"}]
```
# [Very interesting test class](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-6/end/albums/src/test/java/com/packt/albums/AlbumsControllerTests.java) but not spoken in the book the AlbumsController class
* The Test using the Feigh client again a [WireMock server](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-6/end/albums/src/test/java/com/packt/albums/AlbumsControllerTests.java) listening on port 7079
* the port 7079 is also addressed by the Mvc client through the the [yaml Configuration for test](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-6/end/albums/src/main/resources/application-test.yml)
## Annotations
* [@SpringBootTest](https://reflectoring.io/spring-boot-test/) is useful for integration tests it loooks for the mainconfiguration
* [@ActiveProfiles](https://docs.spring.io/spring-framework/reference/testing/annotations/integration-spring/annotation-activeprofiles.html) makes we will load our configuration from *src/main/resources/application-test.yaml*
* [@SpringBootTest and @AutoConfigureMockMvc](https://openclassrooms.com/fr/courses/6900101-creez-une-application-java-avec-spring-boot/7078023-testez-votre-api-avec-spring-boot) 
  * It is in french. the combination is used for integration tests (see summary/Résumé in french)
### Wiremock and WiremockServer
* it seems [both do the same](https://stackoverflow.com/questions/57422081/difference-between-wiremockserver-vs-mockserverclient)
* [More about WireMock on this Baeldung blog](https://www.baeldung.com/introduction-to-wiremock#overview)