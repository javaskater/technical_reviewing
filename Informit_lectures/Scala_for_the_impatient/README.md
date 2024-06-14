# installing scala and scalac
## using the command line
* The recommended method is by [using coursier](https://docs.scala-lang.org/getting-started/index.html)
```bash
jpmena@jpmena-ThinkCentre-M710t:~$ whereis scala
scala: /home/jpmena/.local/share/coursier/bin/scala
jpmena@jpmena-ThinkCentre-M710t:~$ whereis scalac
scalac: /home/jpmena/.local/share/coursier/bin/scalac
jpmena@jpmena-ThinkCentre-M710t:~$ scala -version
Scala code runner version 2.12.17 -- Copyright 2002-2022, LAMP/EPFL and Lightbend, Inc.
```
* it is in the path through the _.profile_:
```bash
jpmena@jpmena-ThinkCentre-M710t:~$ tail -3 .profile
# >>> coursier install directory >>>
export PATH="$PATH:/home/jpmena/.local/share/coursier/bin"
# <<< coursier install directory <<<
```
## in IntelliJ
* I use the scala IntelliJ Plugin *2023.3.20* version
* I don't understand what the **Scala Server** is
* I onlys note that in the */home/jpmena/IdeaProjects/ScalaForTheImpatient/build.sbt* file
  * we specify a scala version of 2.13.12 (and not 3.xx.yy) which is the version taught in the book
```sbt
ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.12"

lazy val root = (project in file("."))
  .settings(
    name := "ScalaForTheImpatient"
  )
```
# Origin
## The Book
* There are notes and personal remarks on the Book [Scala For The Impatient 2nd edition](https://www.informit.com/store/scala-for-the-impatient-9780134540566)
  * of __Cay S. Horstmann__
## The Source Code
* It is on the Informit page of the Book when you have bought it (an archive to download)
* There are many GitHub page for the solutions to the exercises here from [Basile Du Plessis](https://github.com/BasileDuPlessis/scala-for-the-impatient)

## Programming in SCALA
### Trough the REPL
* calling it through _scala_ command!
```scala
scala> import scala.beans.BeanProperty
import scala.beans.BeanProperty

scala> class Person {
     | @BeanProperty var name: String = _
     | }
defined class Person
```
### In Itellij Community Edition

* They proposed the [Scala Plugin for IntelliJ](https://plugins.jetbrains.com/plugin/1347-scala/versions/stable)
  * but it was already installed (Settings / Plugins) and ned only an online update (which asks for a restart)
  * because in between IntelliJ has been online-updated to the 2023-2 version
* the plugin is regularly updated (I updated it two times sinc my first use)

# Other Dev environment
## Visual Studio Code
* There is a big [Scala Plugin for Visual Studio Code](https://scalameta.org/metals/docs/editors/vscode/)
* I didn't test it but it must be worth a look
## Eclipse
* seems to be very Old !!! (Eclipse Luna Edition)
