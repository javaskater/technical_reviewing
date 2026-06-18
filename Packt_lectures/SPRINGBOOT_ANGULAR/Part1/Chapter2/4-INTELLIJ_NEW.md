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
