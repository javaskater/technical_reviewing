```scala
package com.absile.scala.chap08

object Exo6 extends App{
  abstract class Shape {
    def CenterPoint:(Double,Double)
  }
  class Rectangle(val topLeft:(Double, Double), width:Double, height:Double) extends Shape {
    override def CenterPoint: (Double, Double) = {
      val xCenter:Double = topLeft._1 + width / 2
      val yCenter = topLeft._2 + height /2
      (xCenter, yCenter)
    }
  }

  class Circle(val center:(Double, Double), radius:Double) extends Shape {

    override def CenterPoint: (Double, Double) = center
  }

  val r = new Rectangle((10,10), 100, 50)
  assert(r.CenterPoint == (60, 35))
  val c = new Circle((100,200), 50)
  assert(c.CenterPoint == (100, 200))
}
```
# solution
* [solution to the exercise 6](https://github.com/BasileDuPlessis/scala-for-the-impatient/blob/master/src/main/scala/com/basile/scala/ch08/Ex06.scala)
*  a val can ovveride a def, so for the circle ot gives
```scala
package com.absile.scala.chap08

object Exo6 extends App{
  abstract class Shape {
    def centerPoint:(Double,Double)
  }
  class Rectangle(val topLeft:(Double, Double), width:Double, height:Double) extends Shape {
    override def centerPoint: (Double, Double) = {
      val xCenter:Double = topLeft._1 + width / 2
      val yCenter = topLeft._2 + height /2
      (xCenter, yCenter)
    }
  }

  class Circle(override val centerPoint:(Double, Double), radius:Double) extends Shape //with or without override

  val r = new Rectangle((10,10), 100, 50)
  assert(r.centerPoint == (60, 35))
  val c = new Circle((100,200), 50)
  assert(c.centerPoint == (100, 200))
}
```