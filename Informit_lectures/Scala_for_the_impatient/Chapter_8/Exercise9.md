```scala
package com.absile.scala.chap08

object Exo09 extends App{
  class Creature {
    def range: Int = 10
    val env:Array[Int] = new Array[Int](range)
    println(s"[Creature] range vaut ${range}")
  }
  println("[main] premier assert")
  assert(new Creature().env.size == 10)

  //def range is defined before primary cnostructor call
  class AntA extends Creature{
    override def range: Int = 2
    println(s"[AntA] range vaut ${range}")
  }
  println("[main] second assert")
  assert(new AntA().env.size == 2)

  //val range is defined after primary cnostructor call
  class AntB extends Creature{
    println(s"[AntA] Before range vaut ${range}")
    override val range: Int = 5
    println(s"[AntA] After range vaut ${range}")
  }
  println("[main] 3ème assert")
  assert(new AntB().env.size == 0)
}
```
* The val is called after the primary constructor of _AntB_ 
  * which calls the primary constructor of _Creature_
  * as it overrides the _def range_ range has at that time no value because the overriden value is not given