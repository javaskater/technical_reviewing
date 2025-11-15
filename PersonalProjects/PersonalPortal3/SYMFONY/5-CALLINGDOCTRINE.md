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

# Getting an array of objects from the Database
* [during the Entity / Mysql Table generation](./1-GENERATEOBJECTS.md) Symfony console not only created
  * [JpmDiplom Entity](https://github.com/javaskater/jpm_pages_symfony_vue/blob/main/src/Entity/JpmDiplom.php)
  * but also a repository [JpmDiplom Repository](https://github.com/javaskater/jpm_pages_symfony_vue/blob/main/src/Repository/JpmDiplomRepository.php) for that Entity with the possibility to pass more complex Database Requests
    * in the generated code they commented an example of such a complex request