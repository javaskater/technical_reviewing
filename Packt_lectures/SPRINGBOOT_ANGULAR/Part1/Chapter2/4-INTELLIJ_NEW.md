# The workspace

- **~/Ateliers/intellj/idea-IU-261.25134.95/workspace**
- select Maven not IntelliJ as the builder ...

- File / Project Structure
  - to have the actual JDK
  - The actual Maven is not given here but in File Settings
- it has taken the Maven deliverd with IntelliJ
  - /home/jmena01/Ateliers/intellj/idea-IU-261.25134.95/outils/construction/maven/apache-maven-3.6.1-DGFiP
  - trying to compile it does not find a settings.xml

```bash
/bin/sh /home/jmena01/Ateliers/intellj/idea-IU-261.25134.95/plugins/maven/lib/maven3/bin/mvn -Didea.version=2026.1.3 -Dmaven.ext.class.path=/home/jmena01/Ateliers/intellj/idea-IU-261.25134.95/plugins/maven/lib/intellij.maven.rt/maven-event-listener.jar -Djansi.passthrough=true -Dstyle.color=always -s /home/jmena01/Ateliers/intellj/idea-IU-261.25134.95/outils/construction/maven/conf/settings.xml -Dmaven.repo.local=/home/jmena01/.m2/repository compile
[ERROR] Error executing Maven.
[ERROR] The specified user settings file does not exist: /home/jmena01/Ateliers/intellj/idea-IU-261.25134.95/outils/construction/maven/conf/settings.xml
```

- there is no outils (tools) directory !!!!
- I use the latest corporate MAVEN

```bash
/bin/sh /home/soda/atelierjavaeclipse/outils/construction/maven/apache-maven-3.9.9-DGFiP/bin/mvn -Didea.version=2026.1.3 -Dmaven.ext.class.path=/home/jmena01/Ateliers/intellj/idea-IU-261.25134.95/plugins/maven/lib/intellij.maven.rt/maven-event-listener.jar -Djansi.passthrough=true -Dstyle.color=always -s /home/soda/atelierjavaeclipse/outils/construction/maven/conf/settings.xml -Dmaven.repo.local=/home/soda/atelierjavaeclipse/.m2/repository compile
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------< org.example:Projet2 >-------------------------
[INFO] Building Projet2 1.0-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- resources:3.3.1:resources (default-resources) @ Projet2 ---
[INFO] Copying 0 resource from src/main/resources to target/classes
[INFO]
[INFO] --- compiler:3.13.0:compile (default-compile) @ Projet2 ---
[INFO] Recompiling the module because of changed source code.
[INFO] Compiling 1 source file with javac [debug target 17] to target/classes
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  0.471 s
[INFO] Finished at: 2026-06-19T13:35:00+02:00
[INFO] ------------------------------------------------------------------------
```
