# Source
* J'avais dans le [README.md](README.md) de ce chapitre donné un chemin pour [les solutions aux exercices sur Github](https://github.com/BasileDuPlessis/scala-for-the-impatient/tree/master/src/main/scala/com/basile/scala/ch06)
# Ex01
* defining an object with no attribute is like defining functions in python (we only add the Object name to call them)
# Ex02
* we can define a class inside Main (even an abstract class)
* assert is very practical for testinng results (like in Python)
# Ex03
```scala
package eu.jpmena.chp06

object Ex03 extends App{
  object Origin extends java.awt.Point {
    this.translate(2,2)
    this.translate(1,3)
    def goto(x:Int, y:Int)={
      this.translate(x,y)
    }
  }
  Origin.translate(10,12)
  println(Origin)
}
```
* It works, but how to initilize with values ?
# Ex04
```scala
package eu.jpmena.chp06

object Ex04 extends App{
  class Point (val x:Int, val y: Int) {
    /*override def translate(dx:Int, dy:Int) = {
      super.translate(dx,dy)
    }*/
    def to_string ={
      s"coordonnes ${x} et ${y}"
    }
  }
  //class Point(val x:Int, val y:Int)
  object Point {
    def apply(x:Int, y:Int): Point = new Point(x,y)
  }
  var p = Point(3,4)
  assert(p.x == 3)
  //p.translate(2,3)
  println(p.to_string)
```
* but I don't know how to call the Constructor of _java.awt.Point_