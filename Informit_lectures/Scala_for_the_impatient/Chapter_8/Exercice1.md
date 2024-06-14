* We can use the assert method to ckeck very simply
```scala
package com.absile.scala.chap08

object Ex01 extends App {
  class BankAccount(initialBalance: Double) {
      protected var balance = initialBalance
      def currentBalance = balance
      def deposit(amount: Double) = { balance += amount; balance }
      def withdraw(amount: Double) = { balance -= amount; balance }
  }

  class CheckingAccount(initialBalance: Double) extends BankAccount(initialBalance){
    private def charge() = balance -= 1

    override def deposit(amount: Double): Double = {
      charge
      super.deposit(amount)
    }

    override def withdraw(amount: Double): Double = {
      charge
      super.withdraw(amount)
    }
  }
  val account = new CheckingAccount(100)
  account.deposit(10)
  assert(account.currentBalance == 109)
  //assert(account.currentBalance == 110)
}
```