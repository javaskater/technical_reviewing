# 15 Managing Errors in a RESTFUL API
## [Resources on github for that RECIPE 1.3](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-3)
* [Starting with RECIPE 1.3](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-3/start/football)
* [Solution of RECIPTE 1.3](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-3/end/football)
# 16
* I don't understand what the function is used for is it only a marker ?
```java
@ResponseStatus(value = HttpStatus.NOT_FOUND, reason = "Not found")
@ExceptionHandler(NotFoundException.class)
public void notFoundHandler() {
}
```