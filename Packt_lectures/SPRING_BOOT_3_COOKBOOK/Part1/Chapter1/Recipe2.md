# 10 
* Starting from the [corresponding GitHub Code](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-2/start/football)
* Note that there is a [nice Test Class](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-2/start/football/src/test/java/com/packt/football/PlayerControllerTest.java) (perhaphs for later) 
* The [Playercontroller (REST)](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-2/start/football/src/main/java/com/packt/football/PlayerController.java) has been resetted to the en of the previous recipe
# 11
* The [record is a simplification for data carriers](https://www.codementor.io/@noelkamphoa/use-records-to-simplify-your-java-code-2j9tv56b64)
  * they were introduced with the JDK 16
  * only getters
  * [use of it](https://www.codementor.io/@noelkamphoa/use-records-to-simplify-your-java-code-2j9tv56b64#4-definition)
* For the service class see [the Solution](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-2/end/football/src/main/java/com/packt/football/services/FootballService.java)
  * especially because VSCode does not help importing Spring's annotations 
## architecture
* In this recipe we have a good separation between 
  * DTO (there is the DAO part missing)
  * Service (using exceptions)
  * Controllers
## The Service
* I entered the 2 first players manually (like in the book) but copied the rest from the [solution Service](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-2/end/football/src/main/java/com/packt/football/services/FootballService.java)
# 12
## ListPlayers
* [good examples of what Map.values() returns](https://www.geeksforgeeks.org/map-values-method-in-java-with-examples/)
  * It returns a collection not a list
  * but you can directly iterate over
## getPlayer
## putPlayer
* updating a value in a map (test jshell)
```java
jshell> import java.util.Map;
jshell> Map<Integer, String> noms = Map.ofEntries(Map.entry(1,"Jean"), Map.entry(2,"Pierre"));
noms ==> {2=Pierre, 1=Jean} //Problem is is immutable
jshell> Map<Integer, String> noms = new HashMap<Integer, String>(Map.ofEntries(Map.entry(1,"Jean"), Map.entry(2,"Pierre")));
noms ==> {1=Jean, 2=Pierre} //HashMap to make it mutable

jshell> noms.put(3, "Nicole"); //Otherwise I cannot add a new member (POST)
$6 ==> null

jshell> noms.put(1, "Jean sans terre"); //Otherwise I cannot update a member (PUT)
$7 ==> "Jean"

jshell> noms
noms ==> {1=Jean sans terre, 2=Pierre, 3=Nicole}
```
* **ERRATUM** The book at the end of page 11 has an error, it forgotted the HasMap to make the players' map mutable [the solution on GitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-2/end/football/src/main/java/com/packt/football/services/FootballService.java) is OK

# 13
## Delete a player
* test in jshell
```java
jshell> noms
noms ==> {1=Jean sans terre, 2=Pierre, 3=Nicole}

jshell> noms.remove(2)
$10 ==> "Pierre"

jshell> noms
noms ==> {1=Jean sans terre, 3=Nicole}

jshell> var supprime=noms.remove(3)
supprime ==> "Nicole" //It returns the removed value

jshell> noms
noms ==> {1=Jean sans terre}
```
# 13
* footballService is already decalred as a service @Service it can be injected anywhere
* After correcting som Bugs especially in the Service
## remember how we compile and start the embedded Tomcat (.jar) 
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ ./mvnw spring-boot:run
```
## We get for the first request (List<Player>)
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/players -H "Accept: application/json" > players.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2561    0  2561    0     0   625k      0 --:--:-- --:--:-- --:--:--  625k
jmena01@M077-1840900:~$ node -e "console.log(JSON.stringify(JSON.parse(require('fs').readFileSync(process.argv[1])), null, 4));"  players.json | tee playersFmt.json
jmena01@M077-1840900:~$ tail -10 playersFmt.json
        "dateOfBirth": "2000-06-12"
    },
    {
        "id": "415396",
        "jerseyNumber": 13,
        "name": "Enith SALON",
        "position": "Goalkeeper",
        "dateOfBirth": "2001-09-24"
    }
]
```