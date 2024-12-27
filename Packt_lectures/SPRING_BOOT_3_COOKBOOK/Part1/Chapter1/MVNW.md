# Whaat is installed
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ ./mvnw -v
HOME MAVEN /home/jmena01/.m2/wrapper/dists/apache-maven-3.9.9/3477a4f1 # I added this echo in the code
Apache Maven 3.9.9 (8e8579a9e76f7d015ee5ec7bfcdc97d260186937)
Maven home: /home/jmena01/.m2/wrapper/dists/apache-maven-3.9.9/3477a4f1
Java version: 17.0.6, vendor: Private Build, runtime: /usr/lib/jvm/java-17-openjdk-amd64
Default locale: fr_FR, platform encoding: UTF-8
OS name: "linux", version: "5.15.0-72-generic", arch: "amd64", family: "unix"
```
* It found java in the path
* it downlaoded Maven from *.mvn/wrapper/maven-wrapper.properties*
```bash
wrapperVersion=3.3.2
distributionType=only-script
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.9/apache-maven-3.9.9-bin.zip
```
* it was using curl to download it and the unzip it
* it creates a hash from the *distributionUrl*
# putting the right settings.xml
```bash
jmena01@M077-1840900:~/.m2/wrapper/dists/apache-maven-3.9.9/3477a4f1/conf$ cp -pv settings.xml settings.xml.bak_$(date '+%d%m%Y_%H%M%S') 
'settings.xml' -> 'settings.xml.bak_27122024_135430'
jmena01@M077-1840900:~/.m2/wrapper/dists/apache-maven-3.9.9/3477a4f1/conf$ cp -pv ~/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/conf/settings.xml . #getting a working settings.xml
'/home/jmena01/atelierjava/eclipse-inst-linux64/outils/construction/maven/apache-maven-3.9.4-DGFiP/conf/settings.xml' -> './settings.xml'
```
* the proxy has not been uncommented but it works
# test it works
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ ./mvnw spring-boot:run
HOME MAVEN /home/jmena01/.m2/wrapper/dists/apache-maven-3.9.9/3477a4f1 # echo that I added in the shell
[INFO] Scanning for projects... # it does nee to download it did it already (when testing trough the Visual Studio Java Maven plugin)
[INFO] 
[INFO] -------------------------< com.packt:football >-------------------------
[INFO] Building football 0.0.1-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] >>> spring-boot:3.4.1:run (default-cli) > test-compile @ football >>>
[INFO] 
[INFO] --- resources:3.3.1:resources (default-resources) @ football ---
[INFO] Copying 1 resource from src/main/resources to target/classes
[INFO] Copying 0 resource from src/main/resources to target/classes
[INFO] 
[INFO] --- compiler:3.13.0:compile (default-compile) @ football ---
[INFO] Nothing to compile - all classes are up to date.
[INFO] 
[INFO] --- resources:3.3.1:testResources (default-testResources) @ football ---
[INFO] skip non existing resourceDirectory /home/jmena01/CONSULTANT/my_springboot_30_cookbook/football/src/test/resources
[INFO] 
[INFO] --- compiler:3.13.0:testCompile (default-testCompile) @ football ---
[INFO] Nothing to compile - all classes are up to date.
[INFO] 
[INFO] <<< spring-boot:3.4.1:run (default-cli) < test-compile @ football <<<
[INFO] 
[INFO] 
[INFO] --- spring-boot:3.4.1:run (default-cli) @ football ---
[INFO] Attaching agents: []

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.4.1)

2024-12-27T13:57:21.874+01:00  INFO 126338 --- [football] [           main] com.packt.football.FootballApplication   : Starting FootballApplication using Java 17.0.6 with PID 126338 (/home/jmena01/CONSULTANT/my_springboot_30_cookbook/football/target/classes started by jmena01 in /home/jmena01/CONSULTANT/my_springboot_30_cookbook/football)
2024-12-27T13:57:21.887+01:00  INFO 126338 --- [football] [           main] com.packt.football.FootballApplication   : No active profile set, falling back to 1 default profile: "default"
2024-12-27T13:57:23.334+01:00  INFO 126338 --- [football] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2024-12-27T13:57:23.360+01:00  INFO 126338 --- [football] [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2024-12-27T13:57:23.361+01:00  INFO 126338 --- [football] [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.34]
2024-12-27T13:57:23.448+01:00  INFO 126338 --- [football] [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2024-12-27T13:57:23.450+01:00  INFO 126338 --- [football] [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1440 ms
2024-12-27T13:57:23.870+01:00  INFO 126338 --- [football] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path '/'
2024-12-27T13:57:23.888+01:00  INFO 126338 --- [football] [           main] com.packt.football.FootballApplication   : Started FootballApplication in 2.686 seconds (process running for 3.362)

# When I call the home page
2024-12-27T14:00:21.196+01:00  INFO 126338 --- [football] [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-12-27T14:00:21.196+01:00  INFO 126338 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-12-27T14:00:21.197+01:00  INFO 126338 --- [football] [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 1 ms
```