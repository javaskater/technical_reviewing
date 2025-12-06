# Why working with NO_HTTPS
## I need it 
* because the [basic OVH Offer (Perso)](https://www.ovhcloud.com/fr/web-hosting/) does not HTTPS Certificates
* the http works with difficulty using on the Vue Side the [default Javascript http client](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) 
```javascript
const fetchUser = (lang) => {
  const url = `http://localhost:8081/diploms/${lang}`
  fetch(url, {})
    .then((response) => response.json())
    .then((result) => {
      Object.assign(diploms, result.data)
      diploms.data.map((x) => console.log(`${x.schoolName} - ${x.cursusDescription}`))
    })
}
```
## Script
* [see this answer](https://github.com/dunglas/symfony-docker/discussions/645)
```bash
 SERVER_NAME=:80 HTTP_PORT=8081 docker compose up -d
```
* Creating two scripts 
  * *jpm_pages_symfony_vue/up.sh*
    * don't forget the two export in the script
  * *jpm_pages_symfony_vue/down.sh*
## Tests:
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl --location --request GET 'localhost:8081/diploms/de_DE' --header 'Accept: application/json'
[{"id":6,"schoolName":"Ecole Centrale de Lille","url":"https:\/\/centralelille.fr\/en\/","beginDate":"1988-09-01T00:00:00+00:00","endDate":"1991-09-01T00:00:00+00:00","cursusDescription":"Ingenieur Hochschule sogennante <i>Grande Ecole<\/i> f\u00fbr allgemeine Ingenieur Asubildiung","language":"de_DE"}]
jpmena@LAPTOP-E2MJK1UO:~$ curl --location --request GET 'localhost:8081/diploms/fr_FR' --header 'Accept: application/json'
[{"id":4,"schoolName":"Ecole Centrale de Lille","url":"'https:\/\/centralelille.fr\/","beginDate":"1988-09-01T00:00:00+00:00","endDate":"1991-09-01T00:00:00+00:00","cursusDescription":"Ecole d'ing\u00e9nieurs G\u00e9n\u00e9raliste du Concours Centrale anciennement IDN","language":"fr_FR"}]
jpmena@LAPTOP-E2MJK1UO:~$ curl --location --request GET 'localhost:8081/diploms/en_EN' --header 'Accept: application/json'
[{"id":5,"schoolName":"Ecole Centrale de Lille","url":"https:\/\/centralelille.fr\/en\/","beginDate":"1988-09-01T00:00:00+00:00","endDate":"1991-09-01T00:00:00+00:00","cursusDescription":"General Enginnering School training top level engineers accessible though competitive exam after two years highscool","language":"en_EN"}]
```
* If I call that URL with a non existing language I get a 404 (HTTP not found) error
  * the message is the one foressen by the [Symfony Diplom Controller Action](https://github.com/javaskater/jpm_pages_symfony_vue/blob/main/src/Controller/DiplomController.php)
    * The Stack trace is very long it is not reproduced here
```javascript
{
    "type": "https://tools.ietf.org/html/rfc2616#section-10",
    "title": "An error occurred",
    "status": 404,
    "detail": "No diplom found for language zh",
    "class": "Symfony\\Component\\HttpKernel\\Exception\\NotFoundHttpException",
    "trace": [
```
* Is linked to the Controller php Code
```php
if (!$diploms) {
    throw $this->createNotFoundException(
        'No diplom found for language '.$lang
    );
}
```