# Resource
* Good resource about [regular expressions in Scala](https://docs.scala-lang.org/tour/regular-expression-patterns.html)
* I check the regular expression to find Double numbers in the [solution](https://github.com/BasileDuPlessis/scala-for-the-impatient/blob/master/src/main/scala/com/basile/scala/ch09/Ex07.scala)
```scala
scala> val r = """^(\d+)?\.\d+$""".r
val r: scala.util.matching.Regex = ^(\d+)?\.\d+$

scala> r.findFirstIn("10")
val res8: Option[String] = None

scala> r.findFirstIn(".10")
val res9: Option[String] = Some(.10)

scala> r.findFirstIn("12.10")
val res10: Option[String] = Some(12.10)
```
## How to split a line
```scala
scala> """Hello 12.31    JP MENA""".split("""\s+""")
val res11: Array[String] = Array(Hello, 12.31, JP, MENA)

scala> """Hello 12.31    JP MENA""".split("\\s+")
val res12: Array[String] = Array(Hello, 12.31, JP, MENA)
```
## Combining the two
* firstfindIn does the Job because we start at the beginning of the String ^ and go to the end of the string $
```scala
scala> """Hello 12.31    JP MENA""".split("\\s+").filter("""^(\d+)?\.\d+$""".r.findFirstIn(_) == None)
val res13: Array[String] = Array(Hello, JP, MENA)
```
## Read the text file
* TODO see previous exercise