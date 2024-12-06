# 178 Technical requirement
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap10
Clonage dans 'chap10'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 6.61 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap10
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap10$ git switch CH10
La branche 'CH10' est paramétrée pour suivre la branche distante 'CH10' depuis 'origin'.
Basculement sur la nouvelle branche 'CH10'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap10$ npm i

added 444 packages, and audited 445 packages in 7s

105 packages are looking for funding
  run `npm fund` for details

10 vulnerabilities (5 moderate, 5 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
```
## use router in src/main.js
* The file *src/main.js* contains:
```javascript
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router' // The router plugin is defined in src/router/index.js

const app = createApp(App) //The app

app.use(createPinia())
app.use(router) //We have to declare that we use the router plugin

app.mount('#app')
```
# 181
* Organisation of our components
  * *Components that are used as routes are stored in a folder called views*
* after having imported StaticTemplate Vetur helps you (autocompletion):
  * to include Statictemplate in your view template
  * to select the right slot when you start with # in you template (insdide the StaticTemplate)  
# 182
* The name of a route is used (name value of privacy in our case) for future programmatic
navigation
# 184
* <a> is fully reloading the page when navigating which is again the philosphy of a SPA application
* so we use <router-link>
* note that the router-link is translated (Firefox Webtools)
```html
<a data-v-efb3f202="" href="/about" class="">About</a>
```
* note that in the template *router-link* is in Kebab Case
  * and in the script section it is imported in Camel Case 
# 188
* It is not clear in the Book but we are creating a [UserProfileView.vue](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH10-end/src/views/UserProfileView.vue)
  * passing to the route a hard encoded userId of *657a3106698992f50c0a5885*
*  TODO: see/pass the curl commands in [Chapter 7 of Part 2](../Part2/Chapter7.md)