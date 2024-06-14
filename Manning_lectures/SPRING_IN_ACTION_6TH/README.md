## The books code
* The code of the book is on the [GitHub Project](https://github.com/habuma/spring-in-action-6-samples)
## Spring's doc
* [Spring's guides](https://spring.io/guides)
* [StackOverflow's questions about Spring](https://stackoverflow.com/questions/tagged/spring-boot)

## MAVEN configuration in STS

* the __mvnw__ the maven wrapper does not how to find the packages (DNS not found)
* in between I Use the project run menu of STS Maven
  * goal: I enter __spring-boot:run__
  * user settings: it prefills with the value by default _/home/jpmena/.m2/settings.xml_

### Already defined in the configuration
* Windows/Preferences/Maven
  * UserSettings
    * It tells us that
    * UserSettings is /home/jpmena/.m2/settings.xml
        * that I already changed to add
        * the corporate proxy
        * the corporate mirror of central
  * Installations:
    * it tells us we are using the EMBEDDED 3.8.6 version

* Windows/Preferences/General
  * Network connections
    * is set to native
    * the screen has all the parameters defined in /etc/environment

## STS can with diffculty handle hml/thymeleaf code
* Eventhough I migrated to the latest [SpringSTS version](https://spring.io/tools)
  * the 4.20.1 at the time of this writing
* it is very hard to write _html/thymeleaf_ files
* I propose to use Visual Studio Code with the [Spring Boot Extension Pack](https://marketplace.visualstudio.com/items?itemName=vmware.vscode-boot-dev-pack)
