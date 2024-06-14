# the private and pravate[this]
* see chapter 5.4 p 60 (83/385) of the book
# the protected constructor
* before the constructor parameters (and their opening parentheses) there must be the _protected_ keyword !!!
# The Scala Code:
```scala
package com.absile.scala.chap08

object Exo10 extends App{
  class Person protected (protected val name:String){ //protected constructor
    def this(n:String, age:Int) = { //public constructor
      this(n) //protected constructor
    }
  }

  class Manager(n:String) extends Person(n)

  val p = new Person(n="MENA", age=30)
  val m = new Manager(n="Super MENA")
}
```