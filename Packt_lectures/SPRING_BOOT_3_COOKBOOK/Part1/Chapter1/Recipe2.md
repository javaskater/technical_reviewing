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
## For the second Controller function
```bash
jmena01@M077-1840900:~$ curl http://localhost:8080/players/415396 -H "Accept: application/json" # a player id that exists see just above
{"id":"415396","jerseyNumber":13,"name":"Enith SALON","position":"Goalkeeper","dateOfBirth":"2001-09-24"}jmena01@M077-1840900:~$ 
jmena01@M077-1840900:~$ curl http://localhost:8080/players/9999 -H "Accept: application/json" # a player that does not exist
{"timestamp":"2025-01-09T16:14:35.533+00:00","status":500,"error":"Internal Server Error","path":"/players/9999"}
```
* In case of a non existent player the Embedded Tomcat Console tells us
```bash
2025-01-09T17:14:35.530+01:00 ERROR 147960 --- [football] [nio-8080-exec-6] o.a.c.c.C.[.[.[/].[dispatcherServlet]    : Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed: com.packt.football.exceptions.NotFoundException: Player not Found!!!] with root cause

com.packt.football.exceptions.NotFoundException: Player not Found!!!
        at com.packt.football.services.FootballService.getPlayer(FootballService.java:50) ~[classes/:na]
```
## For the Third Controller function (POST)
```bash
# We POST a new player
jmena01@M077-1840900:~$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request POST --data '{"id":"9999", "jerseyNumber": 0, "name": "JP MENA", "position": "All", "dateOfBirth": "0967-08-08"}}'  http://localhost:8080/players
# We chack that that user exists
jmena01@M077-1840900:~$ curl http://localhost:8080/players/9999 -H "Accept: application/json"
{"id":"9999","jerseyNumber":0,"name":"JP MENA","position":"All","dateOfBirth":"0967-08-08"}
```
## For the Fourth Controller action (PUT)
* The id in the controller is no use (the service uses player.id). We skip it
```bash
# I create the user (myself)
jmena01@M077-1840900:~$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request POST --data '{"id":"9999", "jerseyNumber": 0, "name": "JP MENA", "position": "All", "dateOfBirth": "0967-08-08"}'  http://localhost:8080/players
## I check that I exist
jmena01@M077-1840900:~$ curl http://localhost:8080/players/9999 -H "Accept: application/json"
{"id":"9999","jerseyNumber":0,"name":"JP MENA","position":"All","dateOfBirth":"0967-08-08"} 
# I correct the date of birth 0967 to 1967
jmena01@M077-1840900:~$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request PUT --data '{"id":"9999", "jerseyNumber": 0, "name": "JP MENA", "position": "All", "dateOfBirth": "1967-08-08"}'  http://localhost:8080/players
{"id":"9999","jerseyNumber":0,"name":"JP MENA","position":"All","dateOfBirth":"1967-08-08"} # the PUT returns the added Player object in JSON format
## I check that my date of birth has been corrected
jmena01@M077-1840900:~$ curl http://localhost:8080/players/9999 -H "Accept: application/json"
{"id":"9999","jerseyNumber":0,"name":"JP MENA","position":"All","dateOfBirth":"1967-08-08"}
```
## For the Fifth Controller action (DELETE)
* I changed the DELETE service for 
  * (the id and no more a whole Player object as parameter)
  * I don't return void but the removed player
```java
       public Player deletePlayer(String id){
        if (!players.containsKey(id)){
            throw new NotFoundException(String.format("[FootballService][deletePlayer]The Player of id %s is not present in the Map of players", id).toString()); // nothing to return the code after this line is not reachable
        } else {
            return players.remove(id);
        }
    }
```
### Tests
```bash
# I add myseld
jmena01@M077-1840900:~$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request POST --data '{"id":"9999", "jerseyNumber": 0, "name": "JP MENA", "position": "All", "dateOfBirth": "0967-08-08"}'  http://localhost:8080/players
jmena01@M077-1840900:~$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request DELETE http://localhost:8080/players/9999 # I delete myself
{"id":"9999","jerseyNumber":0,"name":"JP MENA","position":"All","dateOfBirth":"0967-08-08"} # my delete action returns the deleted player
jmena01@M077-1840900:~$ curl http://localhost:8080/players/9999 -H "Accept: application/json"
{"timestamp":"2025-01-09T16:56:08.586+00:00","status":500,"error":"Internal Server Error","path":"/players/9999"} # I don't exist anymore (Exception thrown see the server logs/Console)
```

