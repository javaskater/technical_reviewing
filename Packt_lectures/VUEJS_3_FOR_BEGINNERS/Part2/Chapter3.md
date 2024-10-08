# 36
* Vite from the french: rapid and leaner development for modern web (not only VueJS)
* *npm create vue@latest* asks the first time if you want to include create-vue npm package
* the next time it does not ask! 
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch$ npm create vue@latest

Vue.js - The Progressive JavaScript Framework

✔ Nom du projet : … vue.js-for-beginners
✔ Ajouter TypeScript ? … Non / Oui
✔ Ajouter le support de JSX ? … Non / Oui
✔ Ajouter Vue Router pour le développement d'applications _single page_ ? … Non / Oui
✔ Ajouter Pinia pour la gestion de l'état ? … Non / Oui
✔ Ajouter Vitest pour les tests unitaires ? … Non / Oui
✔ Ajouter une solution de test de bout en bout (e2e) ? › Cypress
✔ Ajouter ESLint pour la qualité du code ? … Non / Oui
✔ Ajouter Prettier pour le formatage du code ? … Non / Oui
✔ Ajouter l'extension Vue DevTools 7 pour le débogage ? (expérimental) … Non / Oui

Génération du projet dans /home/jmena01/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/vue.js-for-beginners...

Terminé. Exécutez maintenant :

  cd vue.js-for-beginners
  npm install
  npm run format
  npm run dev
```
* I pass the 4 commands recomended (no high vulnerabilities - I don't have a package-lock.json)
  * *npm run format* lists all the files I check for formatting 
  * *npm run dev* takes a new port to run the application if a previous *run dev* has been started before
  * with devtools installed we have now 2 URLs at our disposal
    * http://localhost:5174/ 
    * http://localhost:5174/__devtools__/
* I put my innstallation very deep:
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/vue.js-for-beginners$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v5.4.8  ready in 3117 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  Vue DevTools: Open http://localhost:5173/__devtools__/ as a separate window
  ➜  Vue DevTools: Press Alt(⌥)+Shift(⇧)+D in App to toggle the Vue DevTools

  ➜  press h + enter to show help
```
* The [devTools Vue](http://localhost:5173/__devtools__/)
  * has a very interesting right Toolbar (see [the offical page](https://devtools.vuejs.org/))
  * that brings more information than the [Vue DevTools Firefox Plugin](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
    * which tells us nothing
  * especially the graph icon (very weel done)
# p 40
* no more dist folder
# p 41
* note that for the unit tests there is a **__tests__** folder inside the *src/vomponents* folder
* There is also teh [cypress testing Framework](https://docs.cypress.io/guides/component-testing/vue/overview)
  * whose files are in a *cypress* folder at the root of the project
* link between the two ?
* src/main.js is the root of the application, it is called from the index.html
```html
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
``` 
## the src folder
* src/main.js calls for App.vue
```javascript
import './assets/main.css' //We get the css for the entire app (../index.html)

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue' //Aour parent/main component
import router from './router'
const app = createApp(App) //Instanciate App.vue

app.use(createPinia())
app.use(router)

app.mount('#app')
```
* router has two exemples of route
* store stores only a counter (ands the associated computed value and methods)
# p 42
## src folder
* in the views folder we have real pages the ons called by the router
  * the use parts defined in the components folder
# starting the project [CH03 BLANK](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/tree/CH03)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git
Clonage dans 'Vue.js-3-for-Beginners'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 6.36 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch$ cd Vue.js-3-for-Beginners/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/Vue.js-3-for-Beginners$ git branch 
* CH11
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/Vue.js-3-for-Beginners$ git checkout -b CH03
Basculement sur la nouvelle branche 'CH03'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/Vue.js-3-for-Beginners$ git branch 
* CH03
  CH11
```
* j'intialise le projet
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/Vue.js-3-for-Beginners$ npm i

added 444 packages, and audited 445 packages in 9s

105 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (5 moderate, 4 high) # since the writing of the book some compoenets are a bit old

To address all issues, run:
  npm audit fix

Run `npm audit` for details.

```
* Is is not the right place to start (there are already components)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch$ npm create vue@latest

Vue.js - The Progressive JavaScript Framework

✔ Nom du projet : … vue-ch03
✔ Ajouter TypeScript ? … Non / Oui
✔ Ajouter le support de JSX ? … Non / Oui
✔ Ajouter Vue Router pour le développement d'applications _single page_ ? … Non / Oui
✔ Ajouter Pinia pour la gestion de l'état ? … Non / Oui
✔ Ajouter Vitest pour les tests unitaires ? … Non / Oui
✔ Ajouter une solution de test de bout en bout (e2e) ? › Cypress
✔ Ajouter ESLint pour la qualité du code ? … Non / Oui
✔ Ajouter Prettier pour le formatage du code ? … Non / Oui
✔ Ajouter l'extension Vue DevTools 7 pour le débogage ? (expérimental) … Non / Oui

Génération du projet dans /home/jmena01/CONSULTANT/my_vuejs-3_beginner/ch03_from_scratch/vue-ch03...

Terminé. Exécutez maintenant :

  cd vue-ch03
  npm install
  npm run format
  npm run dev
```
