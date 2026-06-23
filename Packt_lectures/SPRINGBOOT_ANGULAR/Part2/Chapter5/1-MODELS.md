# 88

- @Data annotation is meant for
  - Getters and Setters
  - toString method

# 89

- The author forgot to tell us that he added
  - in the [pom.xml file on GitHub](https://github.com/PacktPublishing/Spring-Boot-and-Angular/blob/main/Chapter-05/superheroes/pom.xml)

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
```

- I finally added in the pom.xml file (right click + Maven + Synchronize)

```xml
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <optional>true</optional>
    </dependency>
```

## [Lombok in the IntelliJ Spring boot Project](https://medium.com/devdomain/using-lombok-in-spring-boot-simplifying-your-code-c38057894cb8)

- file / Settings / Plugins searching for Lombok
  - Lombok is marked as already installed

# 91

- in the Entity class imports

```java
import jakarta.validation.constraints.NotNull; //comes from spring-boot-starter-validation
import lombok.AllArgsConstructor; //comes from lombok
import lombok.Data; //comes from lombok
import lombok.NoArgsConstructor; //comes from lombok
```

# 92

- very intelligent use of DTO (a DTO is a subset of a Entity objects without all database annotations)
