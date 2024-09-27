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
# 39
* we use on Mounted for the *WeatherReport* component. But it is mounted only when called by the *GetLocation* component
# 40
* [Installation  of tailwind css](https://tailwindcss.com/docs/guides/vite)
  * [Vite](https://vitejs.dev/guide/why.html) is used by Vitest installéd when creating the project p 42
  * I have a file *Chapter3/vue-local-weather/vite.config.ts* at the root of the Weather project...
* [postcss](https://postcss.org/) is not SASS, it only adpats to the browser using  prefixes, polyfills
  * it must use [autoprefixer](https://autoprefixer.github.io/) which add vendor prefixes to the classes
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/Chapter3/vue-local-weather$ npm install -D tailwindcss postcss autoprefixer
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@vue/eslint-config-typescript@13.0.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || >=20.0.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }

added 54 packages, changed 1 package, and audited 393 packages in 10s # we added 54 packages

92 packages are looking for funding
  run `npm fund` for details

1 moderate severity vulnerability

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm notice 
npm notice New major version of npm available! 9.5.1 -> 10.8.3
npm notice Changelog: https://github.com/npm/cli/releases/tag/v10.8.3
npm notice Run npm install -g npm@10.8.3 to update!
npm notice 
```
* [difference between npm and npx](https://www.naukri.com/code360/library/difference-between-npm-and-npx)
  * npx can run/execute a module/package present in the registry without installing it
  * from version 5.4 npm and npx are installed together
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/Chapter3/vue-local-weather$ npx tailwindcss init -p

Created Tailwind CSS config file: tailwind.config.js
Created PostCSS config file: postcss.config.js
```
* we see here that autoprefixer is a plugin of postcss in hte same way than tailwindcss
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/Chapter3/vue-local-weather$ cat postcss.config.js 
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```
* We have to modify the default taiilwind configuration:
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  purge: ['./index.html', './src/**/*.{vue,js,ts;jsx,tsx}'], //removes all unused styles from our production app
  content: ['./src/**/*.{vue,js,ts;jsx,tsx}'], //Where tailwind should be applied
  theme: {
    extend: {},
  },
  plugins: [],
}
```
* exposing utility classes of tailwind to the application
  * is using @Tailwind annotation int a root style.css which is imported int he main.ts file
# 41
* the style.css file is not imported in the traditional sense, it is only an element of the development pipeline
  * it is just the list of all the utility classes used by the tooling system
  * I wonder why ./inndex.html is not in the content
# 42
* as icon in the .index.htm file we don't use a SVG icon but the *Chapter3/vue-local-weather/public/favicon.ico*
* great Advantage of VSCode, the class names in index.html are automatically completed
```
Version: 1.92.2
Commit: fee1edb8d6d72a0ddff41e5f71a671c23ed924b9
Date: 2024-08-14T17:29:30.058Z
Electron: 30.1.2
ElectronBuildId: 9870757
Chromium: 124.0.6367.243
Node.js: 20.14.0
V8: 12.4.254.20-electron.0
OS: Linux x64 5.15.0-72-generic snap
```
* [listing Visual Studio code extensions using the command line](https://code.visualstudio.com/docs/editor/extension-marketplace#_command-line-extension-management)
  * the only Vue  extension is [vue.volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) 
```bash
jmena01@M077-1840900:/var/www/formationDrupal$ code --list-extensions | grep -i vue
vue.volar
```
* I have a problem:
  * nothing in the div/app beacause the *<GetLocation />* does not work !!
    * behind a enterprise proxy there is no position given by the navigator!!! 
    * so I give the coordinates manually for Paris
  ```ts
  const getGeolocation = async(): Promise<void> => {
    /*await navigator.geolocation.getCurrentPosition(
        async (position: {coords:Geolocation}) => {
            coords.value = position.coords;
        },
        (error: {message:string}) => {
            geoLocationBlockedByUser.value = true;
            console.error(error.message);
        }
    );*/
    coords.value = {latitude:48.864716, longitude: 2.349014}; //Paris coordinates
};```
## To debug WeatherReport
* curl it:
```javascript
jmena01@M077-1840900:~$ curl "https://api.weatherapi.com/v1/current.json?key=cbbee947ff994b1c89b154220241308&q=Paris"
{"location":{"name":"Paris","region":"Ile-de-France","country":"France","lat":48.87,"lon":2.33,"tz_id":"Europe/Paris","localtime_epoch":1727269188,"localtime":"2024-09-25 14:59"},"current":{"last_updated_epoch":1727268300,"last_updated":"2024-09-25 14:45","temp_c":16.1,"temp_f":61.0,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.weatherapi.com/weather/64x64/day/302.png","code":1189},"wind_mph":10.7,"wind_kph":17.3,"wind_degree":192,"wind_dir":"SSW","pressure_mb":1004.0,"pressure_in":29.65,"precip_mm":0.12,"precip_in":0.0,"humidity":82,"cloud":50,"feelslike_c":16.1,"feelslike_f":61.0,"windchill_c":16.0,"windchill_f":60.8,"heatindex_c":16.0,"heatindex_f":60.8,"dewpoint_c":13.1,"dewpoint_f":55.5,"vis_km":2.5,"vis_miles":1.0,"uv":4.0,"gust_mph":15.2,"gust_kph":24.4}}
```
* Try the URL of the API using Firefox
* a lot of console.log to be done
```ts
onMounted(async() => {
    const {latitude, longitude} = props.coords;
    console.log("[WeatherApp] on va demander le temps pour latitude:"+latitude+ " et longitude:"+longitude);
    const weatherResponse = await fetchWeather({latitude, longitude});
    data.value = weatherResponse;
    icon_src.value = `http:${data.value.current.condition.icon}`; //must be defined to include to refix wiht http: the cdn url 
    console.log("[WeatherApp] météo:"+data.value.current.condition.text+ "icon:"+icon_src.value);

});
```
* I was obliged to define a *icon_src* as a *ref String* because *data.current.condition.icon* (**//cdn.weatherapi.com/weather/64x64/day/302.png** above see the curl output) does not include the http prfix and my localhost (*npm run dev*) thinks it is a localfile
```ts
const icon_src: Ref<string | undefined> = ref();
```
# 43 formatting a date
* note we can call a function inside *{{}}*
  * it would have been a good way to add http: to the icon url.
```ts
<p>{{ formatDate(data.location.localtime) }}</p>
```
* data.location.localtime is considered in Javascript as a Date object though *2024-09-25 14:59* in the curl output above
* it is the *res.json()* function that does the conversion 
* dateString is only from the Date interface.
* we need a real objetc of type Date to do some work !!!
# 45
* note the parent component passes only the member of the interface defined as property
* I cannot rotate an utf8 icon
* None of the tailwindcss styles has been taken *class="inline-block"* is a tailwind css style
* see [trying to actvate tailwind.css](./PB_TAILWIND.md)
  * solved: I mispelled @utilities (@utilititis) in *Chapter3/vue-local-weather/src/style.css*
  * Vite does not tells you that it cannot find the library   
## For a real project:
* starts the TailWind cli process see [tailwind installation](https://tailwindcss.com/docs/installation)
  * especially
```bash
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```
# p 47
* after having suppressed the directory __test__ created by the default App (inside there is a test for a compoent we did eliminate)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/Chapter3/vue-local-weather$ npm run test:unit

> vue-local-weather@0.0.0 test:unit
> vitest


 DEV  v1.6.0 /home/jmena01/CONSULTANT/my_vue_js/Chapter3/vue-local-weather

 ✓ src/App.spec.ts (1)
   ✓ App (1)
     ✓ renders the GetLocation Component

 Test Files  1 passed (1)
      Tests  1 passed (1)
   Start at  17:42:17
   Duration  1.43s (transform 261ms, setup 1ms, collect 313ms, tests 23ms, environment 520ms, prepare 269ms)


 PASS  Waiting for file changes...
       press h to show help, press q to quit
```
* the text after the *describe* and the *it* appear in the console
  * a practical way to know which test does not pass
* Here we only make the App wrapper dos finds the *GetLocation* component
  * we changed *shallowMount<App>(App);* by *shallowMount<typeof App>(App)* (change suggested by the Vue's official extension [Vue Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar))  
# p 48
* [Vitest globals](https://vitest.dev/config/#globals)
  * is meant to use [Jest API](https://jestjs.io/fr/) in my [Vitest](https://vitest.dev/config/#globals)
> We can make a small modification in our project files that removes the need for manually importing those much used functions.
* So we avoid *import { describe, it, expect} from 'vitest'*
* Erratum: the json test part is not in *Chapter3/vue-local-weather/vite.config.ts* but in *Chapter3/vue-local-weather/vitest.config.ts* 
  * That is where I add the *globals: true*
  * It imports *Chapter3/vue-local-weather/vite.config.ts* 
# 52 Mocking
## Go back to the orginal GetLocation component
* I changed the position of the comments to go back to the navigator position
```ts
const getGeolocation = async(): Promise<void> => {
    await navigator.geolocation.getCurrentPosition(
        async (position: {coords:Geolocation}) => {
            coords.value = position.coords;
        },
        (error: {message:string}) => {
            geoLocationBlockedByUser.value = true;
            console.error(error.message);
        }
    );
    //coords.value = {latitude:48.864716, longitude: 2.349014};
};
```
## First Tests:
* The error message states: *Cannot read properties of undefined (reading 'getCurrentPosition')*
* because jsdom as Virtual navigator does not have the getCurrentPosition() in its API
# p 53
* *global.navigator.geolocation = {* is no accepted by the plugib Vue od Visual Studio Code
  * but the test passes 
## Test with a mock returning values
* The book gives access to the [](https://w3c.github.io/geolocation/#dom-geolocation-getcurrentposition)
  * it is passed a *successCallback* as well as a *errorCallback* function
  * Here we simulate only the *successCallback* function
* [wrapper.wm](https://v1.test-utils.vuejs.org/api/wrapper/#properties) is the Vue Instance
# 54
* The promise of *getCurrentPosition* that we simulate takes [two functions as parameter](https://w3c.github.io/geolocation/#dom-geolocation-getcurrentposition) 
 * we call either the *successcallback* or the *errocallback* as the result of getCurrentPosition 
 * to simulate either a successful result respectively negative result in the **real component**
 * that is all the force of **vi.fn**
 * On that page we simulate a errorCallback by calling it at the end of the mock of getComponent
   * *we are defining and invoking the error Callback*
   * we get only a div (the WeatherReoport component if not called because of a v-if)