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
* **TODO**: see why idt does not download the parent pom perhaps [Java does not pass through the proxy in *mvnw*](https://github.com/pmd/pmd/issues/498)