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
# When starting the node dev I also have the devTools
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ npm run dev

> jpm_pages_client@0.0.0 dev
> vite


  VITE v7.2.2  ready in 1355 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  Vue DevTools: Open http://localhost:5173/__devtools__/ as a separate window # no need of browser vue extension
  ➜  Vue DevTools: Press Alt(⌥)+Shift(⇧)+D in App to toggle the Vue DevTools
  ➜  press h + enter to show help
```
* I don't know How to use /__devtools__/ page when I am not on /home
* Prefer using the browsers extensions
  * [Chrome VueJs DevTool](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=fr)
  * [Firefox VueJS Extension](https://addons.mozilla.org/fr/firefox/addon/vue-js-devtools/)
    * for that last extension see [Chapter 13 of the Packt Book (VueJS for Beginners)](../../../Packt_lectures/VUEJS_3_FOR_BEGINNERS/Part4/Chapter13.md)