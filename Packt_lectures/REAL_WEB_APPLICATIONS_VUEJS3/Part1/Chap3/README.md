## 
## [TailWind](https://tailwindcss.com/)
* Two interesting links
  * [installation](https://tailwindcss.com/docs/installation)
  * which calls for an [explanation of the configuration](https://tailwindcss.com/docs/configuration)
  ## [WEATHER API](https://www.weatherapi.com/) 
  * [sign up to the weather API](https://www.weatherapi.com/signup.aspx)
    * Go to *My account* to find the *API Key*
  * [Testing Weather API using curl](https://reqbin.com/lib/weather-api/curl/owbduwje/weather-rest-api-example)
```bash
jmena01@M077-1840900:~$ curl https://api.openweathermap.org/data/2.5/weather?appid=79a86148ade14517b54152423241308&q=chicago
[1] 36691
jmena01@M077-1840900:~$ {"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}
```
* Perhaps wait for one day. The Free account expires on the 27 of August !!! 
* this [post StackOverflow](https://stackoverflow.com/questions/72653892/invalid-api-key-in-openweathermap-error-401)
  * *answer 11* tells us it takes 2 hours for Key activation
  * Very interesting the Flutter source Code (the Question)
    * perhaps I can use it as a node app!!!  
* new key generated the 13/08/2024:
  * very important [the url and the quesry parameters are in the official documentation](https://www.weatherapi.com/docs/)
  * don't forget the double quotes otherwise **$q=Chicago** cannot be interpreted.
```bash
jmena01@M077-1840900:~$ curl "http://api.weatherapi.com/v1/current.json?key=cbbee947ff994b1c89b154220241308&q=chicago"
{"location":{"name":"Chicago","region":"Illinois","country":"United States of America","lat":41.85,"lon":-87.65,"tz_id":"America/Chicago","localtime_epoch":1724057115,"localtime":"2024-08-19 03:45"},"current":{"last_updated_epoch":1724057100,"last_updated":"2024-08-19 03:45","temp_c":21.1,"temp_f":70.0,"is_day":0,"condition":{"text":"Partly cloudy","icon":"//cdn.weatherapi.com/weather/64x64/night/116.png","code":1003},"wind_mph":11.9,"wind_kph":19.1,"wind_degree":20,"wind_dir":"NNE","pressure_mb":1016.0,"pressure_in":30.01,"precip_mm":0.0,"precip_in":0.0,"humidity":68,"cloud":75,"feelslike_c":21.1,"feelslike_f":70.0,"windchill_c":20.1,"windchill_f":68.2,"heatindex_c":20.2,"heatindex_f":68.4,"dewpoint_c":14.3,"dewpoint_f":57.7,"vis_km":16.0,"vis_miles":9.0,"uv":1.0,"gust_mph":18.8,"gust_kph":30.3}}
```
# 33:
* *ref* stands for reactive property
  * [Why reactive property](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#why-refs)
  * when the value changes the DOM is updated automatically
* *Ref* to define [more complex types beyond inferring](https://vuejs.org/guide/typescript/composition-api#typing-ref)
* to define an anonymous type which is made of a json with a string
```javascript
error: {message:string}
```
* This in contrast to explicit types like GeoLocation
```javascript
type Geolocation ={
    latitude: number;
    longitude: number;
}
```
* a mix between anonymous and declared datatype:
```javascript
position: {coords:Geolocation}
```
* *navigator.geolocation.getCurrentPosition* takes an Promise or an async as a parameter
  * an async function is a function that returns a Promise
  * because getcurrentPosition waits for an async the function calling it is putting a *await* in front of it
  * it does not returns immediatly so the function calling await is itslef a async !!!
* *http://localhost:5173/*  never returns the position (is it due to the proxy  or is it due to the local server?) 
# 36 -37
* I put mys APIWEATHER key (cbbee947ff994b1c89b154220241308) in the .env at the root of the project
* Explanation of the (I have been looking at before) 
  * url to ask 
  * type WeatherData we take only some infos of the json result (see the curl result above)
    * the key must be the same as in the curl result
* [what is interface ?](https://www.typescriptlang.org/docs/handbook/interfaces.html)
  * it is a contract (like the anonymous types see first example)
  * it only require that you have at least the properties defined by the interface (cooler than a type) 
  * here a key *coords* of props (wihich is the object passed by the calling component here GetLocation) whose value is of type *Coords*
* what is [defineProps](https://dev.to/cn-2k/working-with-props-declaration-in-vue-3-ts-included-4o4f)
 * this component will be called by the GetLocation