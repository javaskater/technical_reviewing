# Reading all lines of the file
* _in.mkString("\n")_ puts a return line after each character
* _in.mkString_ prints all charaters as it is including the \n at the end of the line
```scala
package com.absile.scala.chap09
import scala.io.Source

object Exo3 extends App{
  val in = Source.fromURL(getClass.getResource("/com/absile/scala/chap09/recettesRFJanvier.csv"))
  println(in.mkString)
  //println(in.getLines.mkString("\n")) //Equivalent to the previous one
}
```
## First way to match words of more than 12 caraters
* with a for loop
```scala
package com.absile.scala.chap09
import scala.io.Source

object Exo3 extends App{
  val in = Source.fromURL(getClass.getResource("/com/absile/scala/chap09/recettesRFJanvier.csv"))
  //println(in.mkString)
  //println(in.getLines.mkString("\n")) //Equivalent to the previous one
  for (w <- """\w{12,}""".r.findAllIn((in.mkString))){
    println(f"word of motre than 12 caracters |$w|")
  }
}
```
## Second way to match words of more than 12 caraters
* map should return a List _println_ returns nothing. The returned map is made of Units
* you have to use a foreach
* you cannot interpolate **_**
```scala
package com.absile.scala.chap09
import scala.io.Source

object Exo3 extends App{
  val in = Source.fromURL(getClass.getResource("/com/absile/scala/chap09/recettesRFJanvier.csv"))
  //println(in.mkString)
  //println(in.getLines.mkString("\n")) //Equivalent to the previous one
  //"""\w{12,}""".r.findAllIn((in.mkString)).map[Unit](w => println(f"word of more than 12 chars $w") ) //prints nothing
  //"""\w{12,}""".r.findAllIn((in.mkString)).foreach(w => println(f"word of more than 12 chars $w"))
  """\w{12,}""".r.findAllIn((in.mkString)).foreach(println(_))
}
```
* if you are using _, the code-block after foreach must be one line long
  * which is not the case if you are using an explicit variable declaration like w 