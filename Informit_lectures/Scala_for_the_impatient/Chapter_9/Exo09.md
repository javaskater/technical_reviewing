# using the walk
* see [Notes on the chapter 9.7](./9_7.md)
# Using the findfirst
* Because each line correspond of a unique pass we need only to match _.class_
  * see the [Notes on chapter 9.10](./9_10.md) it gives an Option so don't forget the _getOrElse_
* We find a lot of class file in _~/IdeaProjects/testScala_ see the find command underneath:
```bash
jmena01@M077-1840900:~/IdeaProjects/testScala$ find . -name *.class | wc -l
137
```
* My program
```scala
package com.absile.scala.chap09
import java.nio.file.{Files, Paths}
object Exo09 extends App{
  val classPathRegExp = """^[^\s]+\.class$""".r
  var nbClassfiles = 0
  Files.walk(Paths.get("/home/jmena01/IdeaProjects/testScala")).map(_.toAbsolutePath.toString).forEach(p =>{
    val pReg  = classPathRegExp.findFirstIn(p).getOrElse("")
    if (pReg.length > 0) {
      println(f"[main][loop] class path: |$pReg|")
      nbClassfiles += 1
    }
  })
  println(f"[main] total number of class files ${nbClassfiles}")
}
```
## [The solution](https://github.com/BasileDuPlessis/scala-for-the-impatient/blob/master/src/main/scala/com/basile/scala/ch09/Ex09.scala)
* uses sum to sum up he results on the different directories _
* uses listDir and no walk to manage by itself the recursivity!
  * some tests of listDir and toString on java.io.File objects using scala REPL
```scala
scala> import java.io.File
import java.io.File

scala> val dir = new File("/home/jmena01/IdeaProjects/testScala")
val dir: java.io.File = /home/jmena01/IdeaProjects/testScala

scala> dir.isFile
val res3: Boolean = false

scala> dir.isDirectory
val res4: Boolean = true

scala> val liste = dir.listFiles
val liste: Array[java.io.File] = Array(/home/jmena01/IdeaProjects/testScala/src, /home/jmena01/IdeaProjects/testScala/.idea, /home/jmena01/IdeaProjects/testScala/project, /home/jmena01/IdeaProjects/testScala/.bsp, /home/jmena01/IdeaProjects/testScala/build.sbt, /home/jmena01/IdeaProjects/testScala/target)

scala> liste.map(_.toString)
val res1: Array[String] = Array(/home/jmena01/IdeaProjects/testScala/src, /home/jmena01/IdeaProjects/testScala/.idea, /home/jmena01/IdeaProjects/testScala/project, /home/jmena01/IdeaProjects/testScala/.bsp, /home/jmena01/IdeaProjects/testScala/build.sbt, /home/jmena01/IdeaProjects/testScala/target)

scala> liste.filter(_.isDirectory).map(_.toString)
val res2: Array[String] = Array(/home/jmena01/IdeaProjects/testScala/src, /home/jmena01/IdeaProjects/testScala/.idea, /home/jmena01/IdeaProjects/testScala/project, /home/jmena01/IdeaProjects/testScala/.bsp, /home/jmena01/IdeaProjects/testScala/target) //There is not the .sbt file

```
### the program
* the parameter of countClassFiles has to be a directory
```scala
package com.absile.scala.chap09

import java.io.File

object Exo09_Solution extends App{
  def countclassFiles(dir:File):Int = {
    val dirFiles = dir.listFiles
    dirFiles.filter(_.toString.endsWith(".class")).length + dirFiles.filter(_.isDirectory).map(countclassFiles(_)).sum
  }
  println(f"[main] total number of class files ${countclassFiles(new File("/home/jmena01/IdeaProjects/testScala"))}")
}
```
* The directory part brings 0 whe there anre no subdirectories in the directory I am in
* sum on en empty list is 0
```scala
scala> val ia = List(1,2,3,4).filter(_ > 4).map(_*2).sum
val ia: Int = 0

scala> val ia = List(1,2,3,4).filter(_ > 4).map(_*2)
val ia: List[Int] = List()
```