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
## Test
* I now get a 404 instead of a 500 (Internal Server Error)
```bash
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl http://localhost:8080/players/9999 -H "Accept: application/json"
{"timestamp":"2025-01-10T12:12:45.478+00:00","status":404,"error":"Not Found","path":"/players/9999"}
```
* No Stacktrace in the Server's console's output / Tomcat Log
  * The Exception has been caught into a 404 / not found error
* I now test the AlredyExistsException
```bash
# I don't exist I create a new User
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request POST --data '{"id":"9999", "jerseyNumber": 0, "name": "JP MENA", "position": "All", "dateOfBirth": "0967-08-08"}'  http://localhost:8080/players
# I check that I exist
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl http://localhost:8080/players/9999 -H "Accept: application/json"
{"id":"9999","jerseyNumber":0,"name":"JP MENA","position":"All","dateOfBirth":"0967-08-08"}
# I exist I try to cerate myself again
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" -H "Accept: application/json" --request POST --data '{"id":"9999", "jerseyNumber": 0, "name": "JP MENA", "position": "All", "dateOfBirth": "0967-08-08"}'  http://localhost:8080/players
{"timestamp":"2025-01-10T12:55:20.184+00:00","status":400,"error":"Bad Request","path":"/players"} # I get the 400 eror
```
* No Stack Trace, the 400 Error catches the Exception
# 17
* playing with the bash to check for Already existing Data
* The --data=$data does not work!!! I must give it manually
```bash
# I put the --data manually
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data '{"id": "8888", "jerseyNumber":6, "name":"Cata COLL", "position":"Goalkeeper", "dateOfBirth": "2001-04-23"}'  http://localhost:8080/players
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data '{"id": "8888", "jerseyNumber":6, "name":"Cata COLL", "position":"Goalkeeper", "dateOfBirth": "2001-04-23"}'  http://localhost:8080/players
{"timestamp":"2025-01-10T13:23:52.962+00:00","status":400,"error":"Bad Request","path":"/players"}j # It already exists 
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl http://localhost:8080/players/8888 -H "Accept: application/json"
{"id":"8888","jerseyNumber":6,"name":"Cata COLL","position":"Goalkeeper","dateOfBirth":"2001-04-23"} # I can find it 
```
## TO PUST AS ERRATUM
* To use a variablesee the [answer 6 of this stackExchange Post](https://askubuntu.com/questions/1162945/how-to-send-json-as-variable-with-bash-curl)
* That gives:
```bash
jmena01@M077-1840900:~/Documents/Livres/Packt$ data='{"id": "8888", "jerseyNumber":6, "name":"Cata COLL",'
jmena01@M077-1840900:~/Documents/Livres/Packt$ data=${data}' "position":"Goalkeeper", '
jmena01@M077-1840900:~/Documents/Livres/Packt$ data=${data}' "dateOfBirth": "2001-04-23"}'
jmena01@M077-1840900:~/Documents/Livres/Packt$ echo $data
{"id": "8888", "jerseyNumber":6, "name":"Cata COLL", "position":"Goalkeeper", "dateOfBirth": "2001-04-23"} # Each field in the variable must be between " and not '"
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data "$data"   http://localhost:8080/players # No error message
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl http://localhost:8080/players/8888 -H "Accept: application/json"
{"id":"8888","jerseyNumber":6,"name":"Cata COLL","position":"Goalkeeper","dateOfBirth":"2001-04-23"} # It has well been registered
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data "$data"   http://localhost:8080/players
{"timestamp":"2025-01-10T13:47:35.097+00:00","status":400,"error":"Bad Request","path":"/players"} #already exists
```
* the Tocalt/console tells us
```bash
2025-01-10T14:44:18.977+01:00  WARN 93538 --- [football] [nio-8080-exec-1] .w.s.m.s.DefaultHandlerExceptionResolver : Resolved [org.springframework.http.converter.HttpMessageNotReadableException: JSON parse error: Unexpected character (''' (code 39)): was expecting double-quote to start field name]
```
# 18
* I test the Global (for all Controller classes) Exception Handler
* the global class
```java
package com.packt.football;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.packt.football.exceptions.NotFoundException;
import com.packt.football.exceptions.AlreadyExistsException;

@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<String> notFoundGlobalHandler(NotFoundException ex){
        return new ResponseEntity<String>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }

    @ExceptionHandler(AlreadyExistsException.class)
    public ResponseEntity<String> alreadyExistsGlobalHandler(AlreadyExistsException ex){
        return new ResponseEntity<String>(ex.getMessage(), HttpStatus.BAD_REQUEST);
    }
}
```
* the tests
```bash
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data "$data"   http://localhost:8080/players
# I control that it exists
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl http://localhost:8080/players/8888 -H "Accept: application/json"
{"id":"8888","jerseyNumber":6,"name":"Cata COLL","position":"Goalkeeper","dateOfBirth":"2001-04-23"}jmena01@M077-1840900:~/Documents/Livres/Packt$ 
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data "$data"   http://localhost:8080/players
[FootballService][addPlayer]The Player of id 8888 is already present in the Map of players # I return a String in the Response Body (not a JSON/Java Object) 
jmena01@M077-1840900:~/Documents/Livres/Packt$ curl --header "Content-Type: application/json" --request POST --data "$data"   http://localhost:8080/players -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
* Uses proxy env variable no_proxy == 'localhost,127.0.0.1,.dgfip,.impots,172.16.32.15,10.154.53.200,.rie.gouv.fr'
*   Trying ::1:8080...
* TCP_NODELAY set
* Connected to localhost (::1) port 8080 (#0)
> POST /players HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.68.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 113
> 
* upload completely sent off: 113 out of 113 bytes
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 # The Answer code is well 400
< Content-Type: text/plain;charset=UTF-8
< Content-Length: 90
< Date: Fri, 10 Jan 2025 14:12:17 GMT
< Connection: close
< 
* Closing connection 0
[FootballService][addPlayer]The Player of id 8888 is already present in the Map of players
```