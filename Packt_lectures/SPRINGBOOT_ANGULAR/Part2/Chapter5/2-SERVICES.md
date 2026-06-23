# 93

- There is a repository package (previously DAO package)
  - This package is mainly used by the service package

## Use directly the repository Intellij Menu

- Right Click on the repostory package / New ... / Spring Component (java)
  - I constructs the repository class automatically !!!!
  - the Entity class has to be made public

# 94

- the list of methods propsed by the repository is interesting
- we vreate a service package and the the [service class](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-05/superheroes/src/main/java/com/example/springbootsuperheroes/superheroes/antiHero/service/AntiHeroService.java)
- Right Click on the repostory package / New ... / Spring Component (java)
  - I constructs the service class automatically !!!!
  - but does not add the repo automatically to it !!!
    - the repo interface has to be made public !!!

# 98

- it is in the book but not in [the GitHub Code](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-05/superheroes/src/main/java/com/example/springbootsuperheroes/superheroes/antiHero/service/AntiHeroService.java)

```java
    public void removeAntiHeroById(UUID id){
        findOrThrow(id); //Not on Github but suggested by the book
        repo.deleteById(id);
    }
```

## Note

- At that point (the service layer) we don't use the DTO but only the Entity Objects !!!!
