# 2 ways of getting a file
## From the resources
* I have to put the recettesRFJanvier.csv at the same place than the Exo1.scala file
  *  / indicates the root of the classpath
* Explanation for [the Resources position](https://www.baeldung.com/java-class-vs-classloader-getresource   ) 
```scala
package com.absile.scala.chap09
import java.net.URL
import scala.io.Source

object Exo1 extends App{
  val url:URL = getClass.getResource("/com/absile/scala/chap09/recettesRFJanvier.csv")
  val in:Source = Source.fromURL(url)
  var lines_reversed = in.getLines().toArray.reverse
  println(f"number of lines found ${lines_reversed.size}")
  println(lines_reversed.mkString("\n"))
}
```
## From the file (with an absolute Path)
```scala
package com.absile.scala.chap09
import java.net.URL
import scala.io.Source

object Exo1 extends App{
  //val url:URL = getClass.getResource("/com/absile/scala/chap09/recettesRFJanvier.csv")
  //val in:Source = Source.fromURL(url)
  val in = Source.fromFile("/home/jmena01/ERICA/TOPAD/TOPAD-Cible/recettesRFJanvier.csv")
  var lines_reversed = in.getLines().toArray.reverse
  println(f"number of lines found ${lines_reversed.size}")
  println(lines_reversed.mkString("\n"))
}
```