# Goals and resources
* the goal is to escape special chars in a scala RegExp
* Writing in a file PrintWriter from java.io does the job like explained in the [Chapter 9.6 Notes](./9_6.md)
* it takes elements of [Exercice 4](./Exo4.md) for the call to the regular expression's find all
## the code
```scala
package com.absile.scala.chap09

import java.io.PrintWriter

object Exo6 extends  App {
  val out = new PrintWriter("/home/jmena01/ERICA/TOPAD/TOPAD-Cible/special_chars.log", "UTF-8")
  """\\\"""".r.findAllIn(("""Hello \"Basile\" how are you?""".mkString))foreach(out.println(_))
  out.close()
}
```