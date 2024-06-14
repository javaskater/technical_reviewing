```scala
package com.absile.scala.chap08

object Exo5 extends App {
  class Point(val x:Double, val y:Double)

  class LabeledPoint(val label:String, x:Double, y:Double) extends Point(x,y)

  val lp = new LabeledPoint("Black Thursday", 1929, 230.07)

  assert(lp.label == "Black Thursday")
  assert(lp.x == 1929)
  assert(lp.y == 230.07)
}
```
* Note that in the x and y are already defined as val in the parent class
* if I define one of them as val in the child class I get an error, I have to add the overrode qualifier
```scala
package com.absile.scala.chap08

object Exo5 extends App {
  class Point(val x:Double, val y:Double){
    def getX:Double = x
  }

  class LabeledPoint(val label:String, override val x:Double, y:Double) extends Point(x,y){
    def getParentx:Double = super.getX //it has put the son value int the parent one
  }

  val lp = new LabeledPoint("Black Thursday", 1929, 230.07)

  assert(lp.label == "Black Thursday")
  assert(lp.x == 1929)
  assert(lp.y == 230.07)
  val parentx = lp.getParentx
  println(f"parent x ${parentx}")
}
```