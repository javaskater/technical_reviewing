# [new Pom](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-5/end/footballpg/pom.xml)
# 206
* that code just creates and starts a container with a configured *football* database
```java
static PostgreSQLContainer<?> postgreSQLContainer = new PostgreSQLContainer<>("postgres:latest")
        .withDatabaseName("football")
        .withUsername("football")
        .withPassword("football");
```
# 207
* The embedded static Initializer class onlys simpulates an application.yaml file (only for those tests)
  * The following annotation initilizes it to start with a test application.yml
```java
@ContextConfiguration(initializers = FootballServiceTest.Initializer.class)
```
* I asks you to implements
```java
    static class Initializer implements ApplicationContextInitializer<ConfigurableApplicationContext>{ //needs to implements the following method

        @Override
        public void initialize(ConfigurableApplicationContext applicationContext)
        {
                TestPropertyValues.of(
                    "spring.datasource.url = "+ postgreSQLContainer.getJdbcUrl(),
                    "spring.datasource.username =" + postgreSQLContainer.getUsername(),
                    "spring.datasource.password = " + postgreSQLContainer.getPassword()
                    ).applyTo(applicationContext.getEnvironment());
        }
        
    }
```
* *applicationContext.getEnvironment()* loads the data in the simulated application.yml
* use of *TestPropertyValues.of* see [answer 13 of that StackOverflow Post](https://stackoverflow.com/questions/54718995/appropriate-usage-of-testpropertyvalues-in-spring-boot-tests)
## [is tests equality of two objects](https://www.baeldung.com/hamcrest-core-matchers#is-matchers)
* it is an equal to attribute by attribute ...
## Running one test
* Right click on the Test Java File *footballpg/src/test/java/com/packt/footballpg/FootballServiceTest.java* / Run As / Junit Test (that menu only appears if we have at least one @Test annotation)
```bash
09:47:45.907 [main] INFO org.testcontainers.DockerClientFactory -- Docker host IP address is localhost
09:47:45.916 [main] INFO org.testcontainers.DockerClientFactory -- Connected to docker: 
  Server Version: 27.5.1
  API Version: 1.47
  Operating System: Ubuntu 24.04.2 LTS
  Total Memory: 31765 MB
09:47:45.932 [main] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling docker image: testcontainers/ryuk:0.12.0. Please be patient; this may take some time but only needs to be done once.
09:47:45.935 [main] INFO org.testcontainers.utility.RegistryAuthLocator -- Failure when attempting to lookup auth config. Please ignore if you don''t have images in an authenticated registry. Details: (dockerImageName: testcontainers/ryuk:latest, configFile: /home/jmena01/.docker/config.json, configEnv: DOCKER_AUTH_CONFIG). Falling back to docker-java default behaviour. Exception message: Status 404: No config supplied. Checked in order: /home/jmena01/.docker/config.json (file not found), DOCKER_AUTH_CONFIG (not set)
09:47:47.515 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Starting to pull image ## Docker pulls the image the first time
09:47:47.527 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  0 pending,  0 downloaded,  0 extracted, (0 bytes/0 bytes)
09:47:49.058 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  2 pending,  1 downloaded,  0 extracted, (4 MB/? MB)
09:47:49.105 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  1 pending,  2 downloaded,  0 extracted, (4 MB/? MB)
09:47:51.162 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  0 pending,  3 downloaded,  0 extracted, (7 MB/11 MB)
09:47:51.308 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  0 pending,  3 downloaded,  1 extracted, (7 MB/11 MB)
09:47:51.416 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  0 pending,  3 downloaded,  2 extracted, (8 MB/11 MB)
09:47:51.494 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pulling image layers:  0 pending,  3 downloaded,  3 extracted, (11 MB/11 MB)
09:47:51.550 [docker-java-stream--1931961954] INFO tc.testcontainers/ryuk:0.12.0 -- Pull complete. 3 layers, pulled in 4s (downloaded 11 MB at 2 MB/s) # it is very fast
09:47:51.550 [main] INFO tc.testcontainers/ryuk:0.12.0 -- Image testcontainers/ryuk:0.12.0 pull took PT5.617667142S
09:47:51.575 [main] INFO tc.testcontainers/ryuk:0.12.0 -- Creating container for image: testcontainers/ryuk:0.12.0
09:47:51.713 [main] INFO tc.testcontainers/ryuk:0.12.0 -- Container testcontainers/ryuk:0.12.0 is starting: b9d4e3dc412ac95a4daba2c2c1e362cac3481747baaaf745caea05aa68212c78
09:47:52.175 [main] INFO tc.testcontainers/ryuk:0.12.0 -- Container testcontainers/ryuk:0.12.0 started in PT0.599805226S
09:47:52.178 [main] INFO org.testcontainers.utility.RyukResourceReaper -- Ryuk started - will monitor and terminate Testcontainers containers on JVM exit
09:47:52.178 [main] INFO org.testcontainers.DockerClientFactory -- Checking the system...
09:47:52.178 [main] INFO org.testcontainers.DockerClientFactory -- ✔︎ Docker server version should be at least 1.6.0
09:47:52.178 [main] INFO tc.postgres:latest -- Creating container for image: postgres:latest
09:47:52.281 [main] INFO tc.postgres:latest -- Container postgres:latest is starting: e1ef476c67816db77612c8358e154383f919b063e994dd232352d822cc8d1cf3
09:47:53.810 [main] INFO tc.postgres:latest -- Container postgres:latest started in PT1.632004012S
09:47:53.811 [main] INFO tc.postgres:latest -- Container is started (JDBC URL: jdbc:postgresql://localhost:32769/football?loggerLevel=OFF) # Our simulated application.yml

 
 :: Spring Boot ::                (v3.5.8)

2025-12-18T09:47:53.994+01:00  INFO 52440 --- [footballpg] [           main] c.packt.footballpg.FootballServiceTest   : Starting FootballServiceTest using Java 17.0.14 with PID 52440 (started by jmena01 in /home/soda/atelierjavaeclipse/workspace/footballpg)
2025-12-18T09:47:53.995+01:00  INFO 52440 --- [footballpg] [           main] c.packt.footballpg.FootballServiceTest   : No active profile set, falling back to 1 default profile: "default"
2025-12-18T09:47:54.322+01:00  INFO 52440 --- [footballpg] [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
2025-12-18T09:47:54.353+01:00  INFO 52440 --- [footballpg] [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 25 ms. Found 2 JPA repository interfaces.
2025-12-18T09:47:54.545+01:00  INFO 52440 --- [footballpg] [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2025-12-18T09:47:54.672+01:00  INFO 52440 --- [footballpg] [           main] com.zaxxer.hikari.pool.HikariPool        : HikariPool-1 - Added connection org.postgresql.jdbc.PgConnection@19faedcc
2025-12-18T09:47:54.673+01:00  INFO 52440 --- [footballpg] [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2025-12-18T09:47:54.699+01:00  INFO 52440 --- [footballpg] [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2025-12-18T09:47:54.733+01:00  INFO 52440 --- [footballpg] [           main] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 6.6.36.Final
2025-12-18T09:47:54.757+01:00  INFO 52440 --- [footballpg] [           main] o.h.c.internal.RegionFactoryInitiator    : HHH000026: Second-level cache disabled
2025-12-18T09:47:54.905+01:00  INFO 52440 --- [footballpg] [           main] o.s.o.j.p.SpringPersistenceUnitInfo      : No LoadTimeWeaver setup: ignoring JPA class transformer
2025-12-18T09:47:54.938+01:00  WARN 52440 --- [footballpg] [           main] org.hibernate.orm.deprecation            : HHH90000025: PostgreSQLDialect does not need to be specified explicitly using 'hibernate.dialect' (remove the property setting and it will be selected by default)
2025-12-18T09:47:54.950+01:00  INFO 52440 --- [footballpg] [           main] org.hibernate.orm.connections.pooling    : HHH10001005: Database info:
	Database JDBC URL [Connecting through datasource 'HikariDataSource (HikariPool-1)']
	Database driver: undefined/unknown
	Database version: 18.1
	Autocommit mode: undefined/unknown
	Isolation level: undefined/unknown
	Minimum pool size: undefined/unknown
	Maximum pool size: undefined/unknown
2025-12-18T09:47:55.365+01:00  INFO 52440 --- [footballpg] [           main] o.h.e.t.j.p.i.JtaPlatformInitiator       : HHH000489: No JTA platform available (set 'hibernate.transaction.jta.platform' to enable JTA platform integration)
2025-12-18T09:47:55.398+01:00  INFO 52440 --- [footballpg] [           main] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
2025-12-18T09:47:55.859+01:00  INFO 52440 --- [footballpg] [           main] c.packt.footballpg.FootballServiceTest   : Started FootballServiceTest in 2.022 seconds(process running for 10.716) # th only test we run
OpenJDK 64-Bit Server VM warning: Sharing is only supported for boot loader classes because bootstrap classpath has been appended
2025-12-18T09:47:56.230+01:00  INFO 52440 --- [footballpg] [ionShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2025-12-18T09:47:56.233+01:00  INFO 52440 --- [footballpg] [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown initiated...
2025-12-18T09:47:56.235+01:00  INFO 52440 --- [footballpg] [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown completed.
```
* our test image is now present on our host
  * last line of our listing below
```bash
jmena01@m077-2281091:~$ docker image ls
REPOSITORY            TAG       IMAGE ID       CREATED        SIZE
postgres              latest    b5caf683a8bb   9 days ago     456MB # The Postgres image used all along the book
hello-world           latest    1b44b5a3e06a   4 months ago   10.1kB # The image to test Docker
testcontainers/ryuk   0.12.0    a926383422af   6 months ago   15.8MB # The Postgres image used only for our test
# The container has been removed
jmena01@m077-2281091:~$ docker container ls -a # no container from the testcontainers/ryuk image
CONTAINER ID   IMAGE         COMMAND                  CREATED      STATUS                    PORTS     NAMES
20cf43cb22fd   postgres      "docker-entrypoint.s…"   3 days ago   Exited (0) 18 hours ago             postgresql
6dc856820a00   hello-world   "/hello"                 3 days ago   Exited (0) 3 days ago               reverent_joliot
```
## Remarks
* Container / Configuration decalred as static because shared between all tests (a test is not static)
* in the [solution](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter5/recipe5-5/end/footballpg/src/test/java/com/packt/footballpg/FootballServiceTest.java)
  * There are two other tests
## Be Carefull 
* to the package of the imported Assetion Classes
```java
import static org.hamcrest.core.IsNull.nullValue;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.Is.is;
import static org.hamcrest.core.IsNull.notNullValue;
```