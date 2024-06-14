# The Source Code of this Chapter
* It is an [entire project on GitHub]()
* There is [Scala Code](https://github.com/jgperrin/net.jgp.books.spark.ch01/blob/master/src/main/scala/net/jgp/books/spark/ch01/lab100_csv_to_dataframe/CsvToDataframeScalaApp.scala) with its [sbt constructor](https://github.com/jgperrin/net.jgp.books.spark.ch01/blob/master/build.sbt)
* There is [Java Code](https://github.com/jgperrin/net.jgp.books.spark.ch01/blob/master/src/main/java/net/jgp/books/spark/ch01/lab100_csv_to_dataframe/CsvToDataframeApp.java) with its [Maven Pom file](https://github.com/jgperrin/net.jgp.books.spark.ch01/blob/master/pom.xml )
* There is [Python Code](https://github.com/jgperrin/net.jgp.books.spark.ch01/blob/master/src/main/python/lab100_csv_to_dataframe/csvToDataframeApp.py)
## Problem When running sbt in Intellij
### SBT Problem
* I have the message _java.lang.RuntimeException: /packages cannot be represented as URI_
  * whe see that it starts the __embedded sbt__
```bash
/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java -server -Xmx1536M -Dsbt.supershell=false -Didea.managed=true -Dfile.encoding=UTF-8 -Didea.installation.dir=/home/jmena01/Ateliers/idea-IC-233.14015.106 -Didea.runid=2023.3.2 -jar /home/jmena01/.local/share/JetBrains/IdeaIC2023.3/Scala/launcher/sbt-launch.jar "; set ideaPort in Global := 44017 ; idea-shell"
WARNING: A terminally deprecated method in java.lang.System has been called
WARNING: System::setSecurityManager has been called by sbt.TrapExit$ (file:/home/jmena01/.sbt/boot/scala-2.12.4/org.scala-sbt/sbt/1.0.3/run_2.12-1.0.3.jar)
WARNING: Please consider reporting this to the maintainers of sbt.TrapExit$
WARNING: System::setSecurityManager will be removed in a future release
error: error while loading String, class file '/modules/java.base/java/lang/String.class' is broken
(class java.lang.NullPointerException/Cannot invoke "scala.tools.nsc.Global$Run.typerPhase()" because the return value of "scala.tools.nsc.Global.currentRun()" is null)
[error] java.io.IOError: java.lang.RuntimeException: /packages cannot be represented as URI
[error] 	at java.base/jdk.internal.jrtfs.JrtPath.toUri(JrtPath.java:175)
```
* the [answer 11 to this Stack Overflow post](https://stackoverflow.com/questions/60308229/scala-packages-cannot-be-represented-as-uri) should solve the problem
### Problem of Scala SDK
* [post Stack](https://stackoverflow.com/questions/4773784/module-sdk-for-scala-in-intellij-idea) cela ajoute 
### Problem of the Java JDK used
* The scala SDK is OK (__External libraries__ down left)
* The Java SDK is still the jdk 17, it should be the 8
  * how [to change the Project java](https://www.baeldung.com/intellij-change-java-version) 
### Problem SârkSession is not seen 
* I dobled clicked on the habber icon (left bar down lower part) see the JetBrain help[](https://www.jetbrains.com/help/idea/sbt-support.html#sbt_structure)
* Note under *Settings / Build Execution Deployment / sbt*
  * JRE is 1.8
  * sbt Project is set by default to _net.jpg.books.spark.ch01_
* After that:
  * the terms in the build.sbt file are no more in red
  * the SparkSession from the main Scala File is no more in Red
  * I have the red Arrow 
    * on the object with the main method
    * on the main method
## Success
* I can run the programm
* I can step by step it !!!

* *File / Project Settings / libraries* I see all the dependencies
* I can test some expressions from the [spark sql programming guide](https://spark.apache.org/docs/2.2.1/sql-programming-guide.html)