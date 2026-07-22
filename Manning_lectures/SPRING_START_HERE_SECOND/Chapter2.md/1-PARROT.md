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
