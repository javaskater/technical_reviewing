# Using Spring6 Rest Client instead of FeighClient
* No more extra dependency ?
# Resources
## start
* [How to start the application](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-7/start/football)
* only the football server (no albums client)
## end
* [What is expected](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-7/end)
# 28
## Starting a new albums application
```bash
# backup of the feign album application
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook$ mv albums albums_feign
```
* Starting using [SPRING_IO](https://start.spring.io)
  * only the SpringWeb dependency 
  * (makes both the client *org.springframework.web.client.RestClient* and the server *org.springframework.web.bind.annotation.RestController;*) 
  * group *com.packt* artifact *albums*
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook$ unzip ~/Téléchargements/albums.zip -d .
Archive:  /home/jmena01/Téléchargements/albums.zip
   creating: ./albums/
  inflating: ./albums/.gitignore     
  inflating: ./albums/HELP.md        
   creating: ./albums/.mvn/
   creating: ./albums/.mvn/wrapper/
  inflating: ./albums/.mvn/wrapper/maven-wrapper.properties  
  inflating: ./albums/.gitattributes  
   creating: ./albums/src/
   creating: ./albums/src/test/
   creating: ./albums/src/test/java/
   creating: ./albums/src/test/java/com/
   creating: ./albums/src/test/java/com/packt/
   creating: ./albums/src/test/java/com/packt/albums/
  inflating: ./albums/src/test/java/com/packt/albums/AlbumsApplicationTests.java  
   creating: ./albums/src/main/
   creating: ./albums/src/main/resources/
   creating: ./albums/src/main/resources/templates/
   creating: ./albums/src/main/resources/static/
  inflating: ./albums/src/main/resources/application.properties  
   creating: ./albums/src/main/java/
   creating: ./albums/src/main/java/com/
   creating: ./albums/src/main/java/com/packt/
   creating: ./albums/src/main/java/com/packt/albums/
  inflating: ./albums/src/main/java/com/packt/albums/AlbumsApplication.java  
  inflating: ./albums/mvnw.cmd       
  inflating: ./albums/pom.xml        
  inflating: ./albums/mvnw         
```  
## The configuration class
```java
import org.springframework.beans.factory.annotation.Value;
//..................................
@Value("${football.api.url:http://localhost:8080}")
String baseURI;

```
* If the property *football.api.url* is not defined, the *baseURI* variable takes the value: *http://localhost:8080* 
  * it takes the value from configuration files or environment variables
  * there could be for example a *src/main/resources/application.yml* with the following content:
```yaml
football:
  api:
    url: http://locahost:8080
```
  * or the *src/main/resources/application.properties* with the following content
```bash
football.api.url=http://localhost:8080
```
* *src/main/java/com/packt/albums/AlbumsConfiguration.java* is the configuration bean definition whose target is to definee and configure another Bean (RestClient)
# 29
## The [client](https://www.baeldung.com/spring-boot-restclient) in the Service class
* the body and bodyTo  are two methods used to deserialize the JSON response Body
  * see [this Baeldung Post](https://www.baeldung.com/spring-boot-restclient)
* the restClient get allows to pass also headers (see [answers 9 and 0 of this StackOverflow Post](https://stackoverflow.com/questions/77692831/how-to-add-multiple-headers-to-restclient-for-spring-boot-3-2))
  * the header/headers have to be set before the *retrieve/exchange* method
* The uri accepts paramtrized Strings
* the exchange expects a lambda expression, I don't need to put the types of request ant response in the imports
# 30
## Running the football server and the albums client
* See [prededing Recipe p26](./Recipe6.md)
### Starting the Football application/microservice
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ ./mvnw spring-boot:run
```
### Starting the Albums application/microservice
```bash
# We change the port to 8081 because 6060 is already used (by default) by the football application
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/albums$ ./mvnw spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
############################
2025-01-16T15:10:32.346+01:00  INFO 158981 --- [albums] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8081 (http) with context path '/' # It started on the right port
```
### Testing with curl
* getting the list of Players
```bash
jmena01@M077-1840900:~$ curl http://localhost:8081/albums/players
[{"id":"325636","jerseyNumber":11,"name":"Alexia PUTELLAS","position":"MidFielder","dateOfBirth":"1994-02-04"},{"id":"396930","jerseyNumber":2,"name":"Ona BATLLE","position":"Defender","dateOfBirth":"1999-06-10"},{"id":"396911","jerseyNumber":15,"name":"Eva NAVARRO","position":"Forward","dateOfBirth":"2001-01-27"},{"id":"420276","jerseyNumber":9,"name":"Esther GONZALEZ","position":"Forward","dateOfBirth":"1992-12-08"},{"id":"396914","jerseyNumber":14,"name":"Laia CODINA","position":"Defender","dateOfBirth":"2000-01-22"},{"id":"467287","jerseyNumber":16,"name":"Maria PEREZ","position":"Midfielder","dateOfBirth":"2001-12-24"},{"id":"387138","jerseyNumber":10,"name":"Jennifer HERMOSO","position":"Forward","dateOfBirth":"1990-05-09"},{"id":"387134","jerseyNumber":8,"name":"Vicky LOSADA","position":"Midfielder","dateOfBirth":"1991-01-01"},{"id":"398088","jerseyNumber":17,"name":"Alba REDONDO","position":"Forward","dateOfBirth":"1996-08-27"},{"id":"413022","jerseyNumber":3,"name":"Teresa ABELLEIRA","position":"Midfielder","dateOfBirth":"2000-01-09"},{"id":"377762","jerseyNumber":6,"name":"Aitana BONMATI","position":"Midfielder","dateOfBirth":"1998-01-18"},{"id":"387133","jerseyNumber":4,"name":"Irene PAREDES","position":"Defender","dateOfBirth":"1998-01-18"},{"id":"377723","jerseyNumber":20,"name":"Rocio GALVEZ","position":"Defender","dateOfBirth":"1997-04-15"},{"id":"420284","jerseyNumber":21,"name":"Claudia ZORNOZA","position":"Midfielder","dateOfBirth":"1990-10-20"},{"id":"415394","jerseyNumber":18,"name":"Salma PARALLUELO","position":"Forward","dateOfBirth":"2003-11-13"},{"id":"420277","jerseyNumber":7,"name":"Irene GUERRERO","position":"Midfielder","dateOfBirth":"1996-12-12"},{"id":"396907","jerseyNumber":23,"name":"Cata COLL","position":"Goalkeeper","dateOfBirth":"2001-04-23"},{"id":"396929","jerseyNumber":12,"name":"Oihane HERNANDEZ","position":"Defender","dateOfBirth":"2000-05-04"},{"id":"467297","jerseyNumber":22,"name":"Athenea DEL CASTILLO","position":"Forward","dateOfBirth":"2000-10-24"},{"id":"398097","jerseyNumber":8,"name":"Mariona CALDENTEY","position":"Forward","dateOfBirth":"1996-03-19"},{"id":"1884823","jerseyNumber":5,"name":"Ivana ANDRES","position":"Defender","dateOfBirth":"1994-07-31"},{"id":"398098","jerseyNumber":1,"name":"Misa RODRIGUEZ","position":"Goalkeeper","dateOfBirth":"1999-07-22"},{"id":"413016","jerseyNumber":19,"name":"Olga CARMONA","position":"Defender","dateOfBirth":"2000-06-12"},{"id":"415396","jerseyNumber":13,"name":"Enith SALON","position":"Goalkeeper","dateOfBirth":"2001-09-24"}]j
```
* getting a specific player out of the List above
```bash
curl http://localhost:8081/albums/player/413016
null
```
* there is a mistake on the client it should call */players/{id}* on the football server and not */player/{id}*
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/players/413016 #what we should call from the src/main/java/com/packt/albums/FootballClientService.java
{"id":"413016","jerseyNumber":19,"name":"Olga CARMONA","position":"Defender","dateOfBirth":"2000-06-12"}
jmena01@M077-1840900:~$ curl http://localhost:8080/player/413016 # What we actually call
{"timestamp":"2025-01-16T14:19:34.351+00:00","status":404,"error":"Not Found","path":"/player/413016"}
```
* now I have the right answer:
```bash
jmena01@M077-1840900:~$ curl http://localhost:8081/albums/player/413016
{"id":"413016","jerseyNumber":19,"name":"Olga CARMONA","position":"Defender","dateOfBirth":"2000-06-12"}
```
# Test not in the Book but in the [solution on GitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-7/end/albums/src/test/java/com/packt/albums/FootballClientServiceTests.java)
* I take the *src/test/java/com/packt/albums/AlbumsControllerTests.java* from the [previous RECIPE](./Recipe6.md)
## Simpler than the [previous Recipe](./Recipe6.md)
* because we don't send request directly but let footballclientService does it for us 
  * in the [Preceding RECIPE](./Recipe6.md) it was not intersting to instantiate footballClient (since it came from an interface)
  * two différent ways to test (between [RECIPE6](./Recipe6.md) and here)
* after giving the environment/property variable *football.api.url* the value *http://localhost:7979"*
## Don't forget to add the wiremok dependency in the *pom.xml*
```xml
  <!-- Using standalone version as there is an incompatibility with Spring Boot 3.2.1 - See: https://github.com/wiremock/wiremock/issues/2395 -->
  <dependency>
    <groupId>com.github.tomakehurst</groupId>
    <artifactId>wiremock-standalone</artifactId>
    <version>3.0.1</version>
    <scope>test</scope>
  </dependency>
```
## running the tests
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/albums$ ./mvnw test
```
### Case of a single player
* The URL to the football web service has to be the exact one to match with the clientService
* In that case I don't return an array but a single JSON Object representing the correpsonding player
```java
WireMock.stubFor(WireMock.get(WireMock.urlEqualTo("/players/396930")) //The called url has tobe changed to wht I will call
							.willReturn(WireMock.aResponse()
								.withHeader("content-Type", "application/json")
								.withBody( // I don't return an array buta single element
									"""
									{
											"id": "396930",
											"jerseyNumber": 2,
											"name": "Ona BATLLE",
											"position": "Defender",
											"dateOfBirth": "1999-06-10"
									}
									"""
								)
							)
		);
```