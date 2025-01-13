# [Source Code on GitHub](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-4)
* [Where to start from](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-4/start/football)
* [Where to end to](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/tree/main/chapter1/recipe1-4/end/football)
# 19
* contrary to Eclipse, Visual Studio Code does not automatically import the classes you use
* We want the footballService to return only two players and not the entire Database
```java
given(footballService.listPlayers()).willReturn(players); //We reduce it
```
## III
* more on the JSON Path in [this Baeldung Blog](https://www.baeldung.com/guide-to-jayway-jsonpath#syntax)
* andReturn() makes you can get the result in a variable
## IIII
```java
//From MvcResult to String
String json = result.getResponse().getContentAsString();
```
* [JavaTimeModule](https://access.redhat.com/webassets/avalon/d/red-hat-jboss-enterprise-application-platform/7.1.beta/javadocs/com/fasterxml/jackson/datatype/jsr310/JavaTimeModule.html)
> serializing java.time objects with the Jackson core
* It is meant to deserialize *dateOfBirth* in the depth of the Player Record
```java
public record Player(String id, int jerseyNumber, String name, String position, LocalDate dateOfBirth) {
} 
```
* for the use of Jackson deserialization
```java
ObjectMapper mapper = new ObjectMapper();
mapper.registerModule(new JavaTimeModule());
List<Player> returnedPlayers = mapper.readValue(json, mapper.getTypeFactory().constructCollectionType(List.class, Player.class));
```
* see the third possibility of [this Baeldung Chapter](https://www.baeldung.com/jackson-collection-array#to-collection)
# 20
## I
```bash
jmena01@M077-1840900:~/CONSULTANT/my_springboot_30_cookbook/football$ ./mvnw test
```
* Many errors du to the lack of autocompletion in *Visual Studio Code* (Eclipse is better for that matter).
### Error 1 hasSize(2) hasSize not found
* see [Answer 329 of this StackOverflow Post](https://stackoverflow.com/questions/13745332/how-to-count-members-with-jsonpath)
* I have to add the following import
  * static because hasSize is a static method !!!
```java
import static org.hamcrest.Matchers.*;
```
* Others links of interest:
  * [testing with MVC](https://codingnomads.com/api-testing-mockmvc-jsonpath-example)
    * see hasSize, status, jsonPath
  * [a full example of testing](https://mkyong.com/spring-boot/spring-test-how-to-test-a-json-array-in-jsonpath/)
    * we see that jsonPath, status comes from also static import
```java
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
```
### Error 2 assertArrayEquals not found
* I forgot the following static import
```java
import static org.junit.jupiter.api.Assertions.assertArrayEquals; //The import I forgot
import static org.junit.jupiter.api.Assertions.assertEquals; //Important for future tests
```
* And I forgot the *toArray()* when calling the comparaison between two lists:
```java
assertArrayEquals(players.toArray(), returnedPlayers.toArray());
```
### Error 3 status is not found
* [a full example of testing](https://mkyong.com/spring-boot/spring-test-how-to-test-a-json-array-in-jsonpath/)
  * we see that jsonPath, status also come from static import
```java
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status; //To be added to my test class
```
#### ERRAYUM ? This import seems to have been forgotten 
* in [the solution]()
  * it is line 7
```java
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
```
  * together with line 20
```java
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
```
## It works!!!!
* It downloaded every library for testing (and java commons) from our intranet maven repositories.
# 21
* Other test in [the solution on gitHub Only](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-4/end/football/src/test/java/com/packt/football/PlayerControllerTest.java)
## get a specific player
```java
	@Test
	public void testReadPlayer_exists() throws Exception {
		String id = "1884823";
		Player player1 = new Player("1884823", 5, "Ivana ANDRES", "Defender", LocalDate.of(1994, 07, 31));
		given(footballService.getPlayer(id)).willReturn(player1);
		MvcResult result = mvc.perform(MockMvcRequestBuilders.get("/players/"+id).accept(MediaType.APPLICATION_JSON))
		.andExpect(status().isOk())
		.andReturn();
		String json = result.getResponse().getContentAsString();
		ObjectMapper mapper = new ObjectMapper();
		mapper.registerModule(new JavaTimeModule());
		Player returnedPlayer = mapper.readValue(json, Player.class);
	}
    @Test
	public void testReadPlayer_doesnt_exist() throws Exception {
		String id = "1884823";
		given(footballService.getPlayer(id)).willThrow(new NotFoundException("Player not Found!!!"));
		mvc.perform(MockMvcRequestBuilders.get("/players/"+id).accept(MediaType.APPLICATION_JSON)).andExpect(status().isNotFound());
	}
```
## add a specific Player
### the Player does not already exist
* see [Service in the gitHub solution](https://github.com/PacktPublishing/Spring-Boot-3.0-Cookbook/blob/main/chapter1/recipe1-4/end/football/src/main/java/com/packt/football/services/FootballService.java)
```java
    public Player addPlayer(Player player) {
        if (players.containsKey(player.id())) {
            throw new AlreadyExistsException("The player already exists");
        } else {
            players.put(player.id(), player);
            return player; //What we want tot test
        }
    }
```
* Solution be care ful to post call */players* not **/players/** (no end slash)
  * otherwise it searches for a ressource id like */players/{id?}*
```java
@Test
    @Test
    public void testCreatePlayer_exists() throws Exception {
		Player player = new Player("1884823", 5, "Ivana ANDRES", "Defender", LocalDate.of(1994, 07, 31));
		given(footballService.addPlayer(player)).willReturn(player);
		ObjectMapper mapper = new ObjectMapper();
		mapper.registerModule(new JavaTimeModule());
		String playerJson = mapper.writeValueAsString(player);
		System.out.println(String.format("[testCreatePlayer_exists] our player |%s|", playerJson));
		MvcResult result = mvc.perform(MockMvcRequestBuilders.post("/players").content(playerJson)
		.accept(MediaType.APPLICATION_JSON)
		.contentType(MediaType.APPLICATION_JSON))
		.andExpect(status().isOk()).andReturn();
		String json = result.getResponse().getContentAsString();
		System.out.println(String.format("[testCreatePlayer_exists] the the response object  |%s|", result.getResponse()));
		System.out.println(String.format("[testCreatePlayer_exists] the json return after palyer addition |%s|", json));
		Player returnedPlayer = mapper.readValue(json, Player.class);
		assertEquals(player, returnedPlayer);
	}
```
### Problem the POST does not retunr anything
* I added [MockMvcResultHandlers](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/servlet/result/MockMvcResultHandlers.html) to get the static print method 
```java
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.*;
```
* to be able to print the POST response see [Response 0 of this StackOverflow Post](https://stackoverflow.com/questions/62174152/java-getting-empty-mockhttpservletresponse-body-however-its-200)
* It changed to
```java
MvcResult result = mvc.perform(MockMvcRequestBuilders.post("/players").content(playerJson)
		.accept(MediaType.APPLICATION_JSON)
		.contentType(MediaType.APPLICATION_JSON))
		.andExpect(status().isOk()).andDo(print()).andReturn(); //I added .andDo(print())
```
* If I go to my controller
```java
    @PostMapping
    public void createPlayer(@RequestBody Player player) {
        this.footballService.addPlayer(player);
    }
```
* I don't return anything !!!