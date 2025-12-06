# The CORS PROBLEM
* is not on the Client Side
* It is on the the Server Answer, which gives on the Symfony Side
```php
    $jsonContent = $serializer->serialize($diploms, 'json');

    $jsonResponse = new Response($jsonContent, 200, [
            'Access-Control-Allow-Origin' => '*', //Allows all orgins especially my localhost:5173
            'Access-Control-Allow-Methods' => 'GET',
            'Content-Type' => 'application/json',
    ]);

    return $jsonResponse;
```
# PROBLEM formatting on the VueJS Side
* using the Code Debugger aliready in Vue JS on F12
  * to pose a breakpoint and check the variables through the console
```javascript
const fetchUser = (lang) => {
  const url = `http://localhost:8081/diploms/${lang}`
  fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
    },
  })
    .then((response) => {
      console.log(`[then1] Retour d'une réponse pour ${url}`)
      var jsonData = response.json()
      console.log(`[then1] response vaut ${jsonData}`)
      return jsonData
    })
    .then((result) => {
      console.log(`[then2] données result valent ${result}`)
      Object.assign(diploms, result)
      result.forEach((x) => console.log(`${x.schoolName} - ${x.cursusDescription}`))
    })
}
```