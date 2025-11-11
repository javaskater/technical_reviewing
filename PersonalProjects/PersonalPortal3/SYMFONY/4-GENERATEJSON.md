[See The JSON Serializer](https://symfony.com/doc/current/serializer.html)
* How to serialize an Controller Exception (todo)
* The example is very interesting (with  Model Class of Person)
## Test API using Curl from the Host in WSL
* Calling the Controller in insecure mode 
  * Using Curl with -k (or --insecure) switch
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl -k https://localhost
OK
```
* [How to pretty print JSON In Javascript](https://www.geeksforgeeks.org/javascript/how-to-pretty-print-json-string-in-javascript/)
## Installing the Serializer
* it is present only int the composer.lock as a require-dev dependency
* Command to pass from the Host
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ docker compose exec php composer require symfony/serializer-pack
```
* todo [Folloxw the Example](https://symfony.com/doc/current/serializer.html)
  * with your **src/Entity/JpmDiplom.php**
  * does it work with all the annotations or do I have to create a DTO Object ? (todo)