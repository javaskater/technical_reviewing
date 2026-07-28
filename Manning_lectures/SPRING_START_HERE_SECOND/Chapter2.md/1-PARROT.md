# 38

- two ways to get the managed bean from the Configuration Object

```java
public class Main {
    static void main() {
        var context = new AnnotationConfigApplicationContext(ProjectConfig.class);

        Parrot p = context.getBean(Parrot.class); // first way using the class name
        System.out.println(p);
        System.out.println(String.format("The Parrot is named: %s", p.getName()));

        String hello = context.getBean(String.class);
        System.out.println(hello);

        int ten = context.getBean(Integer.class);
        context.getBean(String.class);
        System.out.println(ten);

        Parrot p2 = (Parrot) context.getBean("parrot"); // The second way using the method in the configuration clas
        System.out.println(String.format("The other Parrot is named: %s", p2.getName()));
    }
}
```

- you ca test it with unit tests

## see [parrot in unit tests](https://github.com/Spring-Start-Here/Spring-Start-Here/blob/main/ssh_ch2_ex2/src/test/java/com/example/AppTests.java)

- They use here the Bean method name tho retrive the Managed Bean from the context !!!
- **import org.springframework.test.context.junit.jupiter.SpringExtension;** brings the automatic declaration of beans
  - the bean name is the name of the method in the configuration

# Testing the PArros

- [The code on the WebSite is too advanced id does not work](https://github.com/Spring-Start-Here/Spring-Start-Here/blob/main/ssh_ch2_ex2/src/test/java/com/example/AppTests.java)

# I have a problem

- with the File structure in the IntelliJ project
- it does copnsider srr and test the source of my packages not rsrc/java nor test.java
  - **TODO** To correct
- Goto Project file
  - mark src/java as Source Root File (Right click / mark directory as ...)
  - mark test/java as Test Source File

## Running the Spring Config

- The method getBean

```java
 Parrot p = context.getBean("parrot",Parrot.class);
```

- can be used with one parameter (the class)
  - only in the case of only one Parrot instance in the whole Spring configuration
- otherwhise you must specify a name
  - which is the method name in the Configuration class.

```java
@Configuration // This annotation tells that it is a configuration class
public class ProjectConfig
{
    @Bean // The method name undereath that annotation gives the bean name in the Spring context
    Parrot parrot(){
        var p = new Parrot();
        p.setName("Kiki");
        return p;
    }
```

# 43

> By default, Spring uses the names of the methods annotated with
> @Bean as the beans’ names themselves

# 46

- Component and ComponenetScan see [Exercice 5 of Chapter 2](https://github.com/Spring-Start-Here/Spring-Start-Here/tree/main/ssh_ch2_ex5)
