# Getting one spectic item see [Official Doctrine Documentation](https://symfony.com/doc/current/doctrine.html#fetching-objects-from-the-database)
* In the controller, we make another route */diplom/{id}*
* the controller new action
```php
    #[Route('/diplom/{id}', name: 'diplom_j_p_m')]
    public function getDiplom(SerializerInterface $serializer, EntityManagerInterface $entityManager, int $id): Response
    {
        $this->phpLogger->debug("[diplom Controller] Calling diplom with ID:".$id);
        
        $diplom =  $entityManager->getRepository(JpmDiplom::class)->find($id);

        if (!$diplom) {
            throw $this->createNotFoundException(
                'No diplom found for id '.$id
            );
        }

        $jsonContent = $serializer->serialize($diplom, 'json');

        return JsonResponse::fromJsonString($jsonContent);
    }
```
* the command to call that controller's action
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl -H "Accept: application/json" -k https://localhost/diplom/4
{"id":4,"schoolName":"Ecole Centrale de Lille","url":"'https:\/\/centralelille.fr\/","beginDate":"1988-09-01T00:00:00+00:00","endDate":"1991-09-01T00:00:00+00:00","cursusDescription":"Ecole d'ing\u00e9nieurs G\u00e9n\u00e9raliste du Concours Centrale anciennement IDN","language":"fr_FR"}
```
* the log in the php container
```bash
root@41133e368aa7:/app# cd var/log/
root@41133e368aa7:/app/var/log# tail -2 dev.log
[2025-11-15T16:27:35.147698+00:00] php.DEBUG: [diplom Controller] Calling diplom with ID:4 [] []
[2025-11-15T16:27:35.147868+00:00] doctrine.DEBUG: Executing statement: SELECT t0.id AS id_1, t0.school_name AS school_name_2, t0.url AS url_3, t0.begin_date AS begin_date_4, t0.end_date AS end_date_5, t0.cursus_description AS cursus_description_6, t0.language AS language_7 FROM jpm_diplom t0 WHERE t0.id = ? (parameters: array{"1":4}, types: array{"1":1}) {"sql":"SELECT t0.id AS id_1, t0.school_name AS school_name_2, t0.url AS url_3, t0.begin_date AS begin_date_4, t0.end_date AS end_date_5, t0.cursus_description AS cursus_description_6, t0.language AS language_7 FROM jpm_diplom t0 WHERE t0.id = ?","params":{"1":4},"types":{"1":1}} []
```
* the log if no diplom found
```bash
root@41133e368aa7:/app/var/log# tail -2 dev.log
[2025-11-15T16:37:27.328030+00:00] doctrine.DEBUG: Executing statement: SELECT t0.id AS id_1, t0.school_name AS school_name_2, t0.url AS url_3, t0.begin_date AS begin_date_4, t0.end_date AS end_date_5, t0.cursus_description AS cursus_description_6, t0.language AS language_7 FROM jpm_diplom t0 WHERE t0.id = ? (parameters: array{"1":1}, types: array{"1":1}) {"sql":"SELECT t0.id AS id_1, t0.school_name AS school_name_2, t0.url AS url_3, t0.begin_date AS begin_date_4, t0.end_date AS end_date_5, t0.cursus_description AS cursus_description_6, t0.language AS language_7 FROM jpm_diplom t0 WHERE t0.id = ?","params":{"1":1},"types":{"1":1}} []
[2025-11-15T16:37:27.330716+00:00] request.ERROR: Uncaught PHP Exception Symfony\Component\HttpKernel\Exception\NotFoundHttpException: "No diplom found for id 1" at AbstractController.php line 325 {"exception":"[object] (Symfony\\Component\\HttpKernel\\Exception\\NotFoundHttpException(code: 0): No diplom found for id 1 at /app/vendor/symfony/framework-bundle/Controller/AbstractController.php:325)"} []
```
##  Using the [JSON Prettifyer](./prettifyJSONCurl.js) see [GENERATING JSON](./4-GENERATEJSON.md)
```bash
$ curl -H "Accept: application/json" -k https://localhost/diplom/4 -o ~/CONSULTANT/diplom4.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   288  100   288    0     0   2184      0 --:--:-- --:--:-- --:--:--  2198
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/PersonalProjects/PersonalPortal3/SYMFONY$ node prettifyJSONCurl.js "/home/jpmena/CONSULTANT/diplom4.json"
filename:|/home/jpmena/CONSULTANT/diplom4.json|
OK I read diplom4.json
file: diplom4.json read
{
    "id": 4,
    "schoolName": "Ecole Centrale de Lille",
    "url": "'https://centralelille.fr/",
    "beginDate": "1988-09-01T00:00:00+00:00",
    "endDate": "1991-09-01T00:00:00+00:00",
    "cursusDescription": "Ecole d'ingénieurs Généraliste du Concours Centrale anciennement IDN",
    "language": "fr_FR"
}
```
## What if I get an error
* I get a JSON Stacktrace
```javascript
{
    "type": "https://tools.ietf.org/html/rfc2616#section-10",
    "title": "An error occurred",
    "status": 404,
    "detail": "No diplom found for id 1",
    "class": "Symfony\\Component\\HttpKernel\\Exception\\NotFoundHttpException",
    "trace": [
        {
            "namespace": "",
            "short_class": "",
            "class": "",
            "type": "",
            "function": "",
            "file": "/app/vendor/symfony/framework-bundle/Controller/AbstractController.php",
            "line": 325,
            "args": []
        },
        {
            "namespace": "Symfony\\Bundle\\FrameworkBundle\\Controller",
            "short_class": "AbstractController",
            "class": "Symfony\\Bundle\\FrameworkBundle\\Controller\\AbstractController",
            "type": "->",
            "function": "createNotFoundException",
            "file": "/app/src/Controller/JPMController.php",
            "line": 62,
            "args": [
                [
                    "string",
                    "No diplom found for id 1"
                ]
            ]
        },
        {
            "namespace": "App\\Controller",
            "short_class": "JPMController",
            "class": "App\\Controller\\JPMController",
            "type": "->",
            "function": "getDiplom",
            "file": "/app/vendor/symfony/http-kernel/HttpKernel.php",
            "line": 183,
            "args": [
                [
                    "object",
                    "Symfony\\Component\\Serializer\\Serializer"
                ],
                [
                    "object",
                    "Doctrine\\ORM\\EntityManager"
                ],
                [
                    "integer",
                    1
                ]
            ]
        },
        {
            "namespace": "Symfony\\Component\\HttpKernel",
            "short_class": "HttpKernel",
            "class": "Symfony\\Component\\HttpKernel\\HttpKernel",
            "type": "->",
            "function": "handleRaw",
            "file": "/app/vendor/symfony/http-kernel/HttpKernel.php",
            "line": 76,
            "args": [
                [
                    "object",
                    "Symfony\\Component\\HttpFoundation\\Request"
                ],
                [
                    "integer",
                    1
                ]
            ]
        },
        {
            "namespace": "Symfony\\Component\\HttpKernel",
            "short_class": "HttpKernel",
            "class": "Symfony\\Component\\HttpKernel\\HttpKernel",
            "type": "->",
            "function": "handle",
            "file": "/app/vendor/symfony/http-kernel/Kernel.php",
            "line": 182,
            "args": [
                [
                    "object",
                    "Symfony\\Component\\HttpFoundation\\Request"
                ],
                [
                    "integer",
                    1
                ],
                [
                    "boolean",
                    true
                ]
            ]
        },
        {
            "namespace": "Symfony\\Component\\HttpKernel",
            "short_class": "Kernel",
            "class": "Symfony\\Component\\HttpKernel\\Kernel",
            "type": "->",
            "function": "handle",
            "file": "/app/vendor/runtime/frankenphp-symfony/src/Runner.php",
            "line": 38,
            "args": [
                [
                    "object",
                    "Symfony\\Component\\HttpFoundation\\Request"
                ]
            ]
        },
        {
            "namespace": "Runtime\\FrankenPhpSymfony",
            "short_class": "Runner",
            "class": "Runtime\\FrankenPhpSymfony\\Runner",
            "type": "->",
            "function": "{closure:Runtime\\FrankenPhpSymfony\\Runner::run():33}",
            "file": null,
            "line": null,
            "args": []
        },
        {
            "namespace": "",
            "short_class": "",
            "class": "",
            "type": "",
            "function": "frankenphp_handle_request",
            "file": "/app/vendor/runtime/frankenphp-symfony/src/Runner.php",
            "line": 45,
            "args": [
                [
                    "object",
                    "Closure"
                ]
            ]
        },
        {
            "namespace": "Runtime\\FrankenPhpSymfony",
            "short_class": "Runner",
            "class": "Runtime\\FrankenPhpSymfony\\Runner",
            "type": "->",
            "function": "run",
            "file": "/app/vendor/autoload_runtime.php",
            "line": 29,
            "args": []
        },
        {
            "namespace": "",
            "short_class": "",
            "class": "",
            "type": "",
            "function": "require_once",
            "file": "/app/public/index.php",
            "line": 5,
            "args": [
                [
                    "string",
                    "/app/vendor/autoload_runtime.php"
                ]
            ]
        }
    ]
}
```

# Getting an array of objects from the Database
* [during the Entity / Mysql Table generation](./1-GENERATEOBJECTS.md) Symfony console not only created
  * [JpmDiplom Entity](https://github.com/javaskater/jpm_pages_symfony_vue/blob/main/src/Entity/JpmDiplom.php)
  * but also a repository [JpmDiplom Repository](https://github.com/javaskater/jpm_pages_symfony_vue/blob/main/src/Repository/JpmDiplomRepository.php) for that Entity with the possibility to pass more complex Database Requests
    * in the generated code they commented an example of such a complex request
* very interesting [Doctrine ressource (in french)](https://zestedesavoir.com/tutoriels/1713/doctrine-2-a-lassaut-de-lorm-phare-de-php/exploiter-une-base-de-donnees-avec-doctrine-2/a-la-rencontre-du-querybuilder-1/#recherche-dun-utilisateur)
  * CloudFlare does not work this 18/11/2025 p.m. so I have no access to the official Symfony or Doctrine pages
## The result
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl -H "Accept: application/json" -k https://localhost/diploms/fr_FR
[{"id":4,"schoolName":"Ecole Centrale de Lille","url":"'https:\/\/centralelille.fr\/","beginDate":"1988-09-01T00:00:00+00:00","endDate":"1991-09-01T00:00:00+00:00","cursusDescription":"Ecole d'ing\u00e9nieurs G\u00e9n\u00e9raliste du Concours Centrale anciennement IDN","language":"fr_FR"}]
jpmena@LAPTOP-E2MJK1UO:~$ curl -H "Accept: application/json" -k https://localhost/diploms/de_DE
[{"id":6,"schoolName":"Ecole Centrale de Lille","url":"https:\/\/centralelille.fr\/en\/","beginDate":"1988-09-01T00:00:00+00:00","endDate":"1991-09-01T00:00:00+00:00","cursusDescription":"Ingenieur Hochschule sogennante <i>Grande Ecole<\/i> f\u00fbr allgemeine Ingenieur Asubildiung","language":"de_DE"}]
```
* no answer
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl -H "Accept: application/json" -k https://localhost/diploms/zh_ZH -o CONSULTANT/diploms_err.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2855  100  2855    0     0   114k      0 --:--:-- --:--:-- --:--:--  116k
## Prettyfying it
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/technical_reviewing/PersonalProjects/PersonalPortal3/SYMFONY$ node prettifyJSONCurl.js /home/jpmena/CONSULTANT/diploms_err.json 
input full path:|/home/jpmena/CONSULTANT/diploms_err.json|
file: diploms_err.json read
{
    "type": "https://tools.ietf.org/html/rfc2616#section-10",
    "title": "An error occurred",
    "status": 404,
    "detail": "No diplom found for language zh_ZH",
    "class": "Symfony\\Component\\HttpKernel\\Exception\\NotFoundHttpException",
    "trace": [
        ###########################################
```
