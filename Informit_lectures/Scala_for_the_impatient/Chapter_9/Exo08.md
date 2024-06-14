# find all with variables
* Very practical see [Chapter 9_11 notes](./9_11.md)
* Also loading a web page is made in [Notes 4 also in this chapter](./9_4.md)
## testing a source in my intranet
* If I don't call getLines on source, il will loop on every character of the page !!!
```scala
package com.absile.scala.chap09

import scala.io.Source

object Exo8 extends App{
  val source = Source.fromURL("https://example.intranet/", "UTF-8")
  source.getLines().foreach(println(_))
}
```
## Adding the RegExp
* not calling getLines because we want a class that implements _CharSequence_ (a __String__ implements _CharSequence_)
```scala
package com.absile.scala.chap09

import scala.io.Source

object Exo8 extends App{
  val source = Source.fromURL("https://ulysse.dgfip/", "UTF-8")
  val pageHtml = source.mkString //not calling getLines because we wanf a SCharSequence (a String implements CharSequence)
  val htmlImagePattern = """<img([^>]+)src=\"([^\"^\s]+)""".r //^s: to avoid trailing spaces
  for (htmlImagePattern(_, srcUrl) <- htmlImagePattern.findAllIn(pageHtml)){
    println(s"[main][loop] Source of the image |$srcUrl|")
  }
}
```