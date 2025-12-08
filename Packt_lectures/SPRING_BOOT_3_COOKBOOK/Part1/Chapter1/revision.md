# The Book
* From PACKT [Spring Boot 3.0 Cookbook: Proven recipes for building modern and robust Java web applications with Spring Boot ](https://www.packtpub.com/en-us/product/spring-boot-30-cookbook-9781835089491)
## The reason
* At my company we are migrating from an old Java Framework to *Spring Boot Rest* (Backend) / *VueJS* (Frontend)

# 22 SwaggerUI
* The library propsed in the book is too old (In my pom.xml I have at minimum the 3.5.8 Spring Boot version)
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.5.8</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```
## Actual Swagger Library
* You have to install the [right Boot/OpenAPI doc like on the official documentation](https://springdoc.org/#getting-started)
* the pom extension becomes:
```xml
 <dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId> <!--It changed from the book-->
    <version>2.8.14</version> <!--A more recent version as of the book-->
</dependency>
```
* Starting the SpringBoot application gives
```bash
2025-12-08T10:55:23.794+01:00[0;39m [33m WARN[0;39m [35m94192[0;39m [2m--- [football] [           main] [0;39m[36mo.s.core.events.SpringDocAppInitializer [0;39m [2m:[0;39m SpringDoc /v3/api-docs endpoint is enabled by default. To disable it in production, set the property 'springdoc.api-docs.enabled=false'
[2m2025-12-08T10:55:23.795+01:00[0;39m [33m WARN[0;39m [35m94192[0;39m [2m--- [football] [           main] [0;39m[36mo.s.core.events.SpringDocAppInitializer [0;39m [2m:[0;39m SpringDoc /swagger-ui.html endpoint is enabled by default. To disable it in production, set the property 'springdoc.swagger-ui.enabled=false'
```
* This Eclipse output indicates that the swagger endpoint is http://localhost:8080/v3/api-docs which points to http://localhost:8080/swagger-ui/index.html
* Swagger let you test the requests and gives you the curl equivalent expression like 
```bash
curl -X 'GET' \
  'http://localhost:8080/players/1884823' \
  -H 'accept: */*'
```
* I can test a not Found expression
# 25 Creating a client application
## Changing the default SpringBoot Port
* See this [Baeldung Resource](https://www.baeldung.com/spring-boot-change-port) for the different ways of specifing the Tomcat Port
* See also that [](https://www.baeldung.com/spring-profiles) to chnage the port only on a specfici profile
* That gives in ou case a new **albums/src/main/resources/application-dev.properties** that contains
```bash
server.port=8081
```
* to select the dev profile on startup 
  * go to the *Boot DashBoard*
  * Right click on the *albums* project
  * *Open Config* menu
    * *Arguments* Tab 
      * in the *VM Arguments* Text Area just add **-Dspring.profiles.active=dev**
# 27
* To test it you have to start 2 Applications (I use the Spring Boot Dashboard)
## Server application (port 8080)
* http://localhost:8080/players works
* http://localhost/players/325636 works
## Client Web App (port 8081)
* http://localhost:8081/albums/players works
* http://localhost:8081/albums/players/325636 404 (method not programmed on the Feign client)
# 29 Restclient
## Parametrized Type Reference
* More on [the use of ParameterizedTypeReference<List<Player>>()](https://www.baeldung.com/spring-parameterized-type-reference)
## Player class forgotten
* like in the Feign client we have to define a Player Record see [Player Record in the solution](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-7/end/albums/src/main/java/com/packt/albums/Player.java)
## Configuration Bean
* it has to be placed at the root of the application *albums/AlbumsConfiguration.java*
  * otherwise the Service Bean does not see the restClient bean (defined in that configuration Bean)
## For the RestClient Bas URL
* note the Java notation
  * baseUri will be http://localhost:8080 unless another url is defined in the properties for the **football.api.url** key
```java
@Value("${football.api.url:http://localhost:8080}")
String baseUri;
```
## For the Port
* same thing as for the feign client above
* here whe put in the *albums/src/main/resources/application.properties* directly (without defining profiles)
```bash
server.port=8081
```
# 31
* There is no recipe1-8 on the [Bootk's Github website](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main)
  * instead the [*albums/src/test/java/com/packt/albums/FootballClientServiceTests.java* of the solution of RECIPE 1.7](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-7/end/albums/src/test/java/com/packt/albums/FootballClientServiceTests.java) gives the expected solution.
  * At 4 p.m. the 08/12/2025 I cannot work anymore the corporate maven repository seems to be not working ...
    * 5 minutes later it worked again
# 32
* The SpringBootTest annotation at the beginning of [*albums/src/test/java/com/packt/albums/FootballClientServiceTests.java*](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-7/end/albums/src/test/java/com/packt/albums/FootballClientServiceTests.java)
```java
@SpringBootTest(properties = {"football.api.url=http://localhost:7979"}) § // replaces Spring Boot's football.api.url property
public class FootballClientServiceTests
{
```
* is meant to give a configuration to the [*albums/src/main/java/com/packt/albums/AlbumsConfiguration.java*](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-7/end/albums/src/main/java/com/packt/albums/AlbumsConfiguration.java) rest client configuration
```java
@Configuration
public class AlbumsConfiguration {

    @Value("${football.api.url:http://localhost:8080}") //is replaced by http://localhost:7979
    String baseURI;

    @Bean
    RestClient restClient() {
        return RestClient.create(baseURI);
    }
}
```
* see [use of WireMok in JUnit](https://www.baeldung.com/introduction-to-wiremock#managed)
 * I don't understand why using starting the instance (with the port) 
   * and after configuring using the class 
   * stubFor is also a class method (the instance is only there to start a thread in the WireMock Server)
   * [WireMock default configuration](https://wiremock.org/docs/java-usage/)
     * speaking to many instances see [wiremock configuration](https://wiremock.org/docs/java-usage/#newing-up)
# 33
* note that in *albums/src/test/java/com/packt/albums/FootballClientServiceTests.java* when comparing two arrays
  * the order of elements is important
```java
assertArrayEquals(exceptedPlayers.toArray(), players.toArray());
```
* http://wiremock.io is the product website proposing Cloud Solution
* but for a day to day Java use the page is https://wiremock.org/docs/java-usage/#newing-up
