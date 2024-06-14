# Exo4
* [Solution to the Exo4 exercise](https://github.com/BasileDuPlessis/scala-for-the-impatient/blob/master/src/main/scala/com/basile/scala/ch08/Ex04.scala)
## foldLeft
* a good [introcduction to **foldLeft**](https://blog.lunatech.com/posts/2022-07-11-foldleft-introduction-fr)
* exemple in the REPL
```scala
/**
* Int is the return type
* z is the initial value
* op is the left operation applied it is a function (=>) with on the left the accumulator and on the right the value to be added
*/
scala> val s = numbers.foldLeft[Int](z = 0)(op = (accumulator, number) => accumulator + number)
val s: Int = 10
/*
* The return type is calculated from the initial value 0
* the (op)eration adds to the left (accumulator) _ the actual value _ and returns the accumulator 
*/
scala> val s2 = numbers.foldLeft(0)(_+_)
val s2: Int = 10
```
## The Scala ArrayBuffer
```bash
scala> import scala.collection.mutable.ArrayBuffer
 
 val numbers = ArrayBuffer[Double](1,2,3,4)
import scala.collection.mutable.ArrayBuffer

scala> 
scala> val numbers: scala.collection.mutable.ArrayBuffer[Double] = ArrayBuffer(1.0, 2.0, 3.0, 4.0)

scala> numbers += 10.0
val res26: numbers.type = ArrayBuffer(1.0, 2.0, 3.0, 4.0, 10.0)
```
## With the map method

```scala
package com.absile.scala.chap08

import scala.collection.mutable.ArrayBuffer

object Exo04 extends App {
  abstract class Item {
    def price:Double
    def description:String
  }

  class SimpleItem(val price:Double, val description:String)  extends Item

  class Bundle() extends Item {
    private val items = ArrayBuffer[Item]()
    def addItem(i:Item):Unit= items += i
    def price:Double = items.foldLeft[Double](z=0)(op=(acc,item) => acc+item.price)
    def description:String = items.map[String](f = (i:Item) => i.description).mkString(",")
  }


  val si1 = new SimpleItem(4.5, "ring")
  val si2 = new SimpleItem(6.5, "necklace")

  assert(si1.description == "ring")
  assert(si2.price == 6.5)

  val b = new Bundle()
  b.addItem(si1)
  b.addItem(si2)
  assert(b.price == si1.price + si2.price)
  assert(b.description == f"${si1.description},${si2.description}")

}
```