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
The repository at "/app" does not have the correct ownership and git refuses to use it:

fatal: detected dubious ownership in repository at '/app'
To add an exception for this directory, call:

        git config --global --add safe.directory /app

./composer.json has been updated
########################################################
########################################################
Found 1 security vulnerability advisory affecting 1 package.
Run "composer audit" for a full list of advisories.
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_symfony_vue$ grep -in serializer composer.json 
27:        "symfony/serializer": "7.3.*", # check OK
```
## [Folloxw the Example](https://symfony.com/doc/current/serializer.html)
  * with your **src/Entity/JpmDiplom.php**
  * does it work with all the annotations or do I have to create a DTO Object ?
* no I did
```php
#[Route('/', name: 'app_j_p_m')]
    public function index(Request $request, SerializerInterface $serializer): Response
    {
        $this->phpLogger->debug("[main Controller] Calling jpm");
        
        /*return $this->render('jpm/index.html.twig', [
         #   'nom' => "Jean-Pierre MENA",
			
        ]);*/

        $format = 'd/m/Y';
        $begin_date_str = '01/09/1988';
        $end_date_str = '01/09/1991';

        $diplom = new JpmDiplom();
        $diplom->setSchoolName("Ecole Centrale de Lille");
        $diplom->setUrl("https://centralelille.fr/");
        $diplom->setBeginDate(DateTime::createFromFormat($format, $begin_date_str));
        $diplom->setEndDate(DateTime::createFromFormat($format, $end_date_str));
        $diplom->setCursusDescription("Ecole Généraliste, fait partie du groupe des Ecoles Centrales");

        $jsonContent = $serializer->serialize($diplom, 'json');

        return JsonResponse::fromJsonString($jsonContent);
    }
```
* and it works
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl -H "Accept: application/json" -k https://localhost # -k or --insecure
{"id":null,"schoolName":"Ecole Centrale de Lille","url":"https:\/\/centralelille.fr\/","beginDate":"1988-09-01T15:52:04+00:00","endDate":"1991-09-01T15:52:04+00:00","cursusDescription":"Ecole G\u00e9n\u00e9raliste, fait partie du groupe des Ecoles Centrales","language":null}
```
* now getting the diplom from the DATABASE / see [calling Doctrine](./5-CALLINGDOCTRINE.md)
# [How to pretty print JSON In Javascript](https://www.geeksforgeeks.org/javascript/how-to-pretty-print-json-string-in-javascript/)
* I wrote that [NODEJS script](./prettifyJSONCurl.js) to show and write a prettify version of a curl command
  * I need NodeJS installed on my WSL/Ubuntu24 see [Installing Node JS for Vue Development](../VUEJS/0-INSTALLINGNODEJS.md)
