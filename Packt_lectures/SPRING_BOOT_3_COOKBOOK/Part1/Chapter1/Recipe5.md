# Solution on GitHub
* we start from the [Recipe 5 start on Github](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-5/start/football)
* the expected result is on [Recipe 5 end on Github](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-5/end/football)
# 23
* What about the extension version ?
  * The book has been written in 2024 (see page ii)
  * we are the 14 of january 2025
```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.2.0</version>
</dependency>
```
## When I test the *OpenAPI/ local URLs* I get a great stacktrace
* reason the [2.2.0 version is of August 2023](https://mvnrepository.com/artifact/org.springdoc/springdoc-openapi-starter-webmvc-ui)
* I try the [latest stable version and it works](https://mvnrepository.com/artifact/org.springdoc/springdoc-openapi-starter-webmvc-ui)
  * even the Spring-boot version of the book (parent tag in the [pom.xml](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-5/end/football/pom.xml)) is old mine 3.4.1 has been given by the 
  * a version is mandatory in the pom.xml, that gives:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>3.4.1</version> <!--the Book version 3.2.2 is too old-->
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.packt</groupId>
	<artifactId>football</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>football</name>
	<description>Demo project for Spring 3 CookBook</description>
	<url/>
	<licenses>
		<license/>
	</licenses>
	<developers>
		<developer/>
	</developers>
	<scm>
		<connection/>
		<developerConnection/>
		<tag/>
		<url/>
	</scm>
	<properties>
		<java.version>17</java.version> <!--I only have JAVA 17-->
	</properties>
	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springdoc</groupId>
			<artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
			<version>2.8.3</version> <!--last version availabe the 14/01/2025-->
		</dependency>
```
## Access SWAGGER URL
* The raw version http://localhost:8080/v3/api-docs
### The raw version is a json one
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/v3/api-docs -H "Accept: application/json" > swagger.jso
jmena01@M077-1840900:~$ node -e "console.log(JSON.stringify(JSON.parse(require('fs').readFileSync(process.argv[1])), null, 4));"  swagger.json > swaggerFmt.json
```
* The [JSON formatted SWAGGER document](./swaggerFmt.json) is very interesting (usually it is a yaml doc)
# 24
* I call the *endpoints/REST Controllers* using the SWAGGER/UI
## the API enriched version http://localhost:8080/swagger-ui/index.html#/ 
* That version allows to use for each operation the **Try It Out button** // Followed by the **Execute** button to test the request
* It gives you the CURL request that is passed and of course rhe response
  * you can copy or download the response
#### I test a put command
* [SWAGGER UI](http://localhost:8080/swagger-ui/index.html#/) tells us that it is passing the following command
```bash
curl -X 'PUT' \
  'http://localhost:8080/players' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "325636",
  "jerseyNumber": 11,
  "name": "MENA Jean-Pierre",
  "position": "unknow,",
  "dateOfBirth": "1967-08-08"
}'
```
* it tells us that the corresponding response is
```javascript
{
  "id": "325636",
  "jerseyNumber": 11,
  "name": "MENA Jean-Pierre",
  "position": "unknow,",
  "dateOfBirth": "1967-08-08"
}
```
* After that command I [pass a GET command through the SWAGGER API](http://localhost:8080/swagger-ui/index.html#/player-controller/listPlayers)
 * and I find the informations of the player whose id is *325636* as modified by the PUT command
   * (I did a download of the response) Advantage it is formatted JSON and the modified user appears at the beginning of the list
   * The modified user appears only one (no duplicate)