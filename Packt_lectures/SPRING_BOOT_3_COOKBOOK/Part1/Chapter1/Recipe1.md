# 4
## VSCode proposed extension packs
### [Java extension pack for VSCode](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
* an intersting link is how to [define project jdks](https://marketplace.visualstudio.com/items?itemName=redhat.java#project-jdks)
* by default it uses the Java in the Path if there is no JDK_HOME nor JAVA_HOME variable set.
  * on my computer I have
```bash
jmena01@M077-1840900:~/Documents/Livres/Packt$ java --version
openjdk 17.0.6 2023-01-17
OpenJDK Runtime Environment (build 17.0.6+10-Ubuntu-0ubuntu120.04.1)
OpenJDK 64-Bit Server VM (build 17.0.6+10-Ubuntu-0ubuntu120.04.1, mixed mode, sharing)
```
* this extension pack includes [Maven extension for VSCode](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-maven)
  * In the  *settings cog wheel / settings Menu* you get to a page where you can give the mvn executable Path 
  * on my office computer that gives
```bash
jmena01@M077-1840900:~/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/bin$ ll
total 40
drwxr-xr-x 2 jmena01 domain users 4096 janv. 31  2024 ./
drwxr-xr-x 6 jmena01 domain users 4096 janv. 31  2024 ../
-rw-r--r-- 1 jmena01 domain users  327 janv. 31  2024 m2.conf
-rwxr-xr-x 1 jmena01 domain users 5883 janv. 31  2024 mvn*
-rw-r--r-- 1 jmena01 domain users 6324 janv. 31  2024 mvn.cmd
-rwxr-xr-x 1 jmena01 domain users 1684 janv. 31  2024 mvnDebug*
-rw-r--r-- 1 jmena01 domain users 2169 janv. 31  2024 mvnDebug.cmd
-rwxr-xr-x 1 jmena01 domain users 1611 janv. 31  2024 mvnyjp*
jmena01@M077-1840900:~/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/bin$ pwd
/home/jmena01/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/bin
```
### Related [Springboot extension](https://marketplace.visualstudio.com/items?itemName=vmware.vscode-boot-dev-pack)
* It is a pack and includes 
  * Spring boot Dashboard
  * Spring Boot Tools
  * Spring Initializr Java support 
# 5
* going to the [spring initializer on the web](https://start.spring.io)
  * I only add the Spring Web dependency
# 6
* the generated archive file
```bash
jmena01@M077-1840900:~/Téléchargements$ unzip -l football.zip 
Archive:  football.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2024-12-26 16:38   football/
      395  2024-12-26 16:38   football/.gitignore
     1243  2024-12-26 16:38   football/HELP.md
        0  2024-12-26 16:38   football/.mvn/
        0  2024-12-26 16:38   football/.mvn/wrapper/
      951  2024-12-26 16:38   football/.mvn/wrapper/maven-wrapper.properties
       38  2024-12-26 16:38   football/.gitattributes
        0  2024-12-26 16:38   football/src/
        0  2024-12-26 16:38   football/src/test/
        0  2024-12-26 16:38   football/src/test/java/
        0  2024-12-26 16:38   football/src/test/java/com/
        0  2024-12-26 16:38   football/src/test/java/com/packt/
        0  2024-12-26 16:38   football/src/test/java/com/packt/football/
      212  2024-12-26 16:38   football/src/test/java/com/packt/football/FootballApplicationTests.java
        0  2024-12-26 16:38   football/src/main/
        0  2024-12-26 16:38   football/src/main/resources/
        0  2024-12-26 16:38   football/src/main/resources/templates/
        0  2024-12-26 16:38   football/src/main/resources/static/
       33  2024-12-26 16:38   football/src/main/resources/application.properties
        0  2024-12-26 16:38   football/src/main/java/
        0  2024-12-26 16:38   football/src/main/java/com/
        0  2024-12-26 16:38   football/src/main/java/com/packt/
        0  2024-12-26 16:38   football/src/main/java/com/packt/football/
      315  2024-12-26 16:38   football/src/main/java/com/packt/football/FootballApplication.java
     6912  2024-12-26 16:38   football/mvnw.cmd
     1402  2024-12-26 16:38   football/pom.xml
    10665  2024-12-26 16:38   football/mvnw
---------                     -------
```
## preparing the source code
* What we have generated
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook$ unzip ~/Téléchargements/football.zip -d .
Archive:  /home/jmena01/Téléchargements/football.zip
   creating: ./football/
  inflating: ./football/.gitignore   
  inflating: ./football/HELP.md      
   creating: ./football/.mvn/
   creating: ./football/.mvn/wrapper/
  inflating: ./football/.mvn/wrapper/maven-wrapper.properties  
  inflating: ./football/.gitattributes  
   creating: ./football/src/
   creating: ./football/src/test/
   creating: ./football/src/test/java/
   creating: ./football/src/test/java/com/
   creating: ./football/src/test/java/com/packt/
   creating: ./football/src/test/java/com/packt/football/
  inflating: ./football/src/test/java/com/packt/football/FootballApplicationTests.java  
   creating: ./football/src/main/
   creating: ./football/src/main/resources/
   creating: ./football/src/main/resources/templates/
   creating: ./football/src/main/resources/static/
  inflating: ./football/src/main/resources/application.properties  
   creating: ./football/src/main/java/
   creating: ./football/src/main/java/com/
   creating: ./football/src/main/java/com/packt/
   creating: ./football/src/main/java/com/packt/football/
  inflating: ./football/src/main/java/com/packt/football/FootballApplication.java  
  inflating: ./football/mvnw.cmd     
  inflating: ./football/pom.xml      
  inflating: ./football/mvnw
```
* The [exercises/solutions on gitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook$ git clone https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook.git
Clonage dans 'Spring-Boot-3.0-Cookbook'...
remote: Enumerating objects: 5643, done.
remote: Counting objects: 100% (718/718), done.
remote: Compressing objects: 100% (337/337), done.
remote: Total 5643 (delta 242), reused 619 (delta 176), pack-reused 4925 (from 1)
Réception d''objets: 100% (5643/5643), 1.87 Mio | 9.23 Mio/s, fait.
Résolution des deltas: 100% (2196/2196), fait.
```
* Adding the 2 directory to the VSCode workspace
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook$ ls -ltr
total 8
drwxr-xr-x  4 jmena01 domain users 4096 déc.  26 16:38 football
drwxr-xr-x 12 jmena01 domain users 4096 déc.  26 16:53 Spring-Boot-3.0-Cookbook
```
## TODO hos to tell to mvnw that the mvn path
* is */home/jmena01/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/bin*
* [How to tell mvnw to java download behind a proxy](https://github.com/pmd/pmd/issues/498)
  * the mvnw wrapper (*mvnw*) tries to download maven using java 
## running Maven
### Using the Maven of VSCode
* go left bottom
* open the Maven Tab
* On football right click / Run Maven Command / custom ...
* on the input box above enter *spring-boot:run*
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ "/home/jmena01/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/bin" spring-boot:run -f "/home/jmena01/CONSULTANT/my_springboot_30_cookbook/football/pom.xml"
bash: /home/jmena01/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/bin : est un dossier
```
* I appended **mvn** in the Maven Extension Settings for VSCode (maven absolute path)
```bash
[INFO] Attaching agents: []

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.4.1)

2024-12-26T17:36:02.255+01:00  INFO 124073 --- [football] [           main] com.packt.football.FootballApplication   : Starting FootballApplication using Java 17.0.6 with PID 124073 (/home/jmena01/CONSULTANT/my_springboot_30_cookbook/football/target/classes started by jmena01 in /home/jmena01/CONSULTANT/my_springboot_30_cookbook/football)
2024-12-26T17:36:02.259+01:00  INFO 124073 --- [football] [           main] com.packt.football.FootballApplication   : No active profile set, falling back to 1 default profile: "default"
2024-12-26T17:36:03.699+01:00  INFO 124073 --- [football] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2024-12-26T17:36:03.733+01:00  INFO 124073 --- [football] [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2024-12-26T17:36:03.736+01:00  INFO 124073 --- [football] [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.34]
2024-12-26T17:36:03.811+01:00  INFO 124073 --- [football] [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2024-12-26T17:36:03.822+01:00  INFO 124073 --- [football] [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1482 ms
2024-12-26T17:36:04.244+01:00  INFO 124073 --- [football] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path '/'
2024-12-26T17:36:04.260+01:00  INFO 124073 --- [football] [           main] com.packt.football.FootballApplication   : Started FootballApplication in 2.701 seconds (process running for 3.213)
2024-12-26T17:37:47.052+01:00  INFO 124073 --- [football] [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-12-26T17:37:47.053+01:00  INFO 124073 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-12-26T17:37:47.054+01:00  INFO 124073 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 1 ms
```
* When I go to *http://localhost:8080/* I have no mapping so the error fallback page 
# 7
* running the book's command
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ ./mvnw spring-boot:run
[INFO] Scanning for projects...
Downloading from central: https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/3.4.1/spring-boot-starter-parent-3.4.1.pom
[ERROR] [ERROR] Some problems were encountered while processing the POMs:
[FATAL] Non-resolvable parent POM for com.packt:football:0.0.1-SNAPSHOT: The following artifacts could not be resolved: org.springframework.boot:spring-boot-starter-parent:pom:3.4.1 (absent): Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:3.4.1 from/to central (https://repo.maven.apache.org/maven2): repo.maven.apache.org: Nom ou service inconnu and 'parent.relativePath' points at no local POM @ line 5, column 10
 @ 
[ERROR] The build could not read 1 project -> [Help 1]
[ERROR]   
[ERROR]   The project com.packt:football:0.0.1-SNAPSHOT (/home/jmena01/CONSULTANT/my_springboot_30_cookbook/football/pom.xml) has 1 error
[ERROR]     Non-resolvable parent POM for com.packt:football:0.0.1-SNAPSHOT: The following artifacts could not be resolved: org.springframework.boot:spring-boot-starter-parent:pom:3.4.1 (absent): Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:3.4.1 from/to central (https://repo.maven.apache.org/maven2): repo.maven.apache.org: Nom ou service inconnu and 'parent.relativePath' points at no local POM @ line 5, column 10: Unknown host repo.maven.apache.org: Nom ou service inconnu -> [Help 2]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
[ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
```
* **TODO**: see why idt does not download the parent pom perhaps [Java does not pass through the proxy in *mvnw*](https://github.com/pmd/pmd/issues/498) solution in the [Mavenwrapper documentation page](./MVNW.md)
# 6
## VSCode problem
* It accepted the package *com.packt.football* 
  * for *src/main/java/com/packt/football/FootballApplication.java*
  * but not for *src/main/java/com/packt/football/PlayerController.java*
* no problem when running *./mvnw spring-boot:run*
## Just a mistake in the *import org.springframework.web.bind.annotation.*;* 
* I forgot the a
* *./mvnw spring-boot:run* told me it cannot find the @GetMapping annotation compilation failure
# 7
* The GET verb does work !!!
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/players
["Ivana ANDRES","Alexia PUTELLAS"]
jmena01@M077-1840900:~$ curl http://localhost:8080/players -H "Accept: application/json"
["Ivana ANDRES","Alexia PUTELLAS"] # a JSON array
```
* The POST verb does work
  * the curl test is given page 8 above
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" --request POST --data 'Itana BONMATI' http://localhost:8080/players
Player Itana BONMATI created
```
* in the Visual Studio output console
```bash
2024-12-27T14:36:12.241+01:00  INFO 152386 --- [football] [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-12-27T14:36:12.241+01:00  INFO 152386 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-12-27T14:36:12.242+01:00  INFO 152386 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 1 ms
```
* the Get of a specific one player
  * note the @PathVariable annotation
* test at the top of page 9
  * two ways of specifying headers (-H or --header) 
```bash
mena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/Ivana%20ANDRES
Ivana ANDRES
```
* The output console
```bash
2024-12-27T14:44:08.079+01:00  INFO 157585 --- [football] [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-12-27T14:44:08.079+01:00  INFO 157585 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-12-27T14:44:08.080+01:00  INFO 157585 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 1 ms
```
## The PUT verb
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request PUT --data 'Itiana Andres'  http://localhost:8080/players/Ivana%20ANDRES
Player Ivana ANDRES renamed to Itiana Andres
```
## Note for the path parameter
* If the condition (see comment) is not met no answer is produced
```java
  @GetMapping("/{name}") //the name of the path variable must be the same that the correponding method parameter
  public String readPlayer(@PathVariable String name){
      return name;
  }
  @PutMapping("/{oldname}") //the name of the path variable must be the same that the correponding method parameter
  public String updatePlayer(@PathVariable String oldname, @RequestBody String newname){
      return String.format("Player %s renamed to %s", oldname, newname);
  }
```
## The DELETE verb
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request DELETE  http://localhost:8080/players/Ivana%20ANDRES
Player Ivana ANDRES deleted!!!
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request DELETE  http://localhost:8080/players/Jean-Pierre%20MENA
Player Jean-Pierre MENA deleted!!!
```
# 9
## Adding RequestHeader
* see [Official Spring doc](https://docs.spring.io/spring-framework/reference/web/webflux/controller/ann-methods/requestheader.html)
* The code
```java
  @GetMapping("/{name}")
  public String readPlayer(@PathVariable String name, @RequestHeader("jpm-header") String monHeader){
      if (monHeader != null && monHeader.length() > 0){
          return String.format("Header %s ajouté au paramètre du path %s", monHeader, name);
      }
      return name; //Isn't useful because the header is mandatory and may not be blank
  }
```
* Tests
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" -H "jpm-header: annonce de JPM" --request GET  http://localhost:8080/players/Ivana%20ANDRES
Header annonce de JPM ajouté au paramètre du path Ivana ANDRES
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/Ivana%20ANDRES # No answer the jpm-header is mandatory and mya not be blank
```
* the Header is mandatory is is confirmed in the Java output console
```bash
2024-12-27T15:33:06.743+01:00  WARN 185546 --- [football] [nio-8080-exec-8] .w.s.m.s.DefaultHandlerExceptionResolver : Resolved [org.springframework.web.bind.MissingRequestHeaderException: Required request header 'jpm-header' for method parameter type String is not present]
```
* Solution make two methods:
  * one with the mandatory header
  * one without the header
## Request param
* see the [official Spring documentation](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-methods/requestparam.html)
* Java
```java

```
* Test
```bash
mena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/Ivana%20ANDRES #no answer the q request param is mandatory
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/Ivana%20ANDRES?q=Ma%20Question
query parameter Ma Question added to path variable Ivana ANDRES
```
* Solution make two methods:
  * one with the mandatory query
  * one without the quesry
* but the methods must be attached to two different paths
* Java
```java
  @GetMapping("/header/{name}")
  public String readPlayer(@PathVariable String name, @RequestHeader("jpm-header") String monHeader){
      if (monHeader != null && monHeader.length() > 0){
          return String.format("Header %s ajouté au paramètre du path %s", monHeader, name);
      }
      return name;
  }
  @GetMapping("/query/{name}")
  public String readPlayerWithRequestParame(@PathVariable String name, @RequestParam("q") String myquery){
      if (myquery != null && myquery.length() > 0){
          return String.format("query parameter %s added to path variable %s", myquery, name);
      }
      return name;
  }
```
* Test
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" -H "jpm-header: annonce de JPM" --request GET  http://localhost:8080/players/header/Ivana%20ANDRES
Header annonce de JPM ajouté au paramètre du path Ivana ANDRES 
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/query/Ivana%20ANDRES #no answer ?q is mandatory see output console
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/query/Ivana%20ANDRES?q=My%20Query
query parameter My Query added to path variable Ivana ANDRES
``` 
## The result code
```bash
jmena01@M077-1840900:~$ curl --header "Content-Type: application/text" -H "Accept: application/text" --request GET  http://localhost:8080/players/query/Ivana%20ANDRES?q=My%20Query -vvv
Note: Unnecessary use of -X or --request, GET is already inferred.
* Uses proxy env variable no_proxy == 'localhost,127.0.0.1,.dgfip,.impots,172.16.32.15,10.154.53.200,.rie.gouv.fr'
*   Trying ::1:8080...
* TCP_NODELAY set
* Connected to localhost (::1) port 8080 (#0)
> GET /players/query/Ivana%20ANDRES?q=My%20Query HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.68.0
> Content-Type: application/text
> Accept: application/text
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 #The result code
< Content-Type: application/text;charset=UTF-8
< Content-Length: 60
< Date: Fri, 27 Dec 2024 15:21:27 GMT
< 
* Connection #0 to host localhost left intact
query parameter My Query added to path variable Ivana ANDRES
```