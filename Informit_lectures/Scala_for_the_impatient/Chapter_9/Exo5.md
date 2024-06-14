# power of 2
* more on the [power function](https://alvinalexander.com/scala/scala-math-power-exponent-exponentiation-function/)
* About the [ranges in Scala](https://www.scala-lang.org/api/2.12.9/scala/collection/immutable/Range.html)
```scala
scala> import scala.math._
import scala.math._

scala> val l = (1 until 20).map(pow(2,_))
val l: IndexedSeq[Double] = Vector(2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 131072.0, 262144.0, 524288.0)

scala> l.length
val res0: Int = 19

scala> val l = (1 until 21).map(pow(2,_).toInt)
val l: IndexedSeq[Int] = Vector(2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576)

scala> l.length
val res1: Int = 20
```
* Writing in a file PrintWriter from java.io does the job like explained in the [Chapter 9.6 Notes](./9_6.md)
* The third way of doing it is by using the for loop (not = but **<-**)
* Test of the for loop for three variables
```scala

scala> for(i<- 1 to 2; j <- 'a' to 'b'; k <- 1 to 10 by 5) {
     | println(f"i=$i , j=$j, k=$k")
     | }
```
## The program with the 3 ways of doing it
```scala
package com.absile.scala.chap09
import java.io.PrintWriter
import scala.math._
object Exo5 extends  App{
  val out = new PrintWriter("/home/jmena01/ERICA/TOPAD/TOPAD-Cible/powers.log", "UTF-8")
  (1 until 21).map(pow(2,_)).foreach(i => out.println(f"${i.toInt}%10d     ${1/i}%.10f"))
  (1 to 20).map(pow(2,_)).foreach(i => out.println(f"${i.toInt}%10d     ${1/i}%.10f"))
  for(v <- 1 to 20; i = pow(2,v)) out.println(f"${i.toInt}%10d     ${1/i}%.10f")
  out.close()
}
```