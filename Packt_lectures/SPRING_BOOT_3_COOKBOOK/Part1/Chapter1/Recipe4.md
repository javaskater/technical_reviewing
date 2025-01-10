# [Source Code on GitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-4)
* [Where to start from](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-4/start/football)
* [Where to end to](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-4/end/football)
# 19
* contrary to Eclipse, Visual Studio Code does not automatically import the classes you use
* We want the footballService to return only two players and not the entire Database
```java
given(footballService.listPlayers()).willReturn(players); //We reduce it
```
* more on the JSON Path in [this Baeldung Blog](https://www.baeldung.com/guide-to-jayway-jsonpath#syntax)
* andReturn() makes you cna get the result in a variable