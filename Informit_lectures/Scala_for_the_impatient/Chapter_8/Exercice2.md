# Exo2, calls Ex01 classes
* We can call the BankAccount of the other object of the same package
```scala
package com.absile.scala.chap08

import com.absile.scala.chap08.Ex01.BankAccount

object Exo02 extends App {
  class SavingsAccount(val initialBalance:Double)  extends Ex01.BankAccount(initialBalance){
    var deposits = 0

    def charge(): Unit = {
      deposits += 1 //must be before and not after
      if (deposits > 3) balance -= 1
    }

    def earnMonthlyInterest(rate:Double = 0.01): Unit = {
      balance += balance * rate
      deposits = 0
    }

    override def deposit(amount: Double): Double = {
      charge
      super.deposit(amount)
    }

    override def withdraw(amount: Double): Double = {
      charge
      super.withdraw(amount)
    }
  }

  val myAccount = new SavingsAccount(100)

  myAccount.deposit(10)
  myAccount.withdraw(20)
  myAccount.deposit(10)
  assert(myAccount.currentBalance == 100)

  myAccount.deposit(10)
  assert(myAccount.currentBalance == 109)


}
```