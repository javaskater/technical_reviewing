# Difference between List and Array in Scala 
* this [site (link)](https://users.scala-lang.org/t/when-to-use-array-and-when-to-use-list/8101) does not recommend to use an Array, use List instead 
```scala
package com.absile.scala.chap09

import scala.io.Source

object Exo4 extends App{
  val in = Source.fromURL(getClass.getResource("/com/absile/scala/chap09/doubles.txt"))
  val double_list = """[0-9\.]+""".r.findAllIn((in.mkString)).map(_.toDouble).toList
  double_list.foreach(println(_))
  List(
    f"Sum of all doubles: ${double_list.sum}%.2f",
    f"Mean on all doubles: ${double_list.sum/double_list.length}%.2f",
    f"Min of all doubles: ${double_list.min}%.2f",
    f"Max of all doubles: ${double_list.max}%.2f"
  ).foreach(println(_))
}
```