* [how to create a class with many constructors](https://alvinalexander.com/scala/how-to-create-multiple-class-constructors-in-scala-alternate-constructors/)
* [constructing a Rectangle](https://www.tabnine.com/code/java/methods/java.awt.Rectangle/%3Cinit%3E)
  * [The new Rectangle class in Java 17](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)
  * all the coordinates and lengthes are Int 
```scala
package com.absile.scala.chap08

object Exo7 extends App {
  class Square(topLeft:(Int,Int), width:Int) extends java.awt.Rectangle(topLeft._1, topLeft._2, width, width){
    def this(widthOnly:Int) = this((0, 0), widthOnly)
    def this() = this(0)
  }

  val sq1 = new Square()
  assert(sq1.x == 0)
  assert(sq1.width == 0)

  val sq2 = new Square(156)
  assert(sq2.x == 0)
  assert(sq2.width == 156)
  assert(sq2.height == 156)
}
```
* Don't put any val or var in any contructor
 * because the variables have already been created in the Rectangle constructor !!!!
 * see _assert(sq2.height == 156)_