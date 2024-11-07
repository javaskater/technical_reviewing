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
* initializing the project
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
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ npm create vue@latest
Need to install the following packages:
  create-vue@3.11.1
Ok to proceed? (y) y

Vue.js - The Progressive JavaScript Framework

✔ Nom du projet : … vue-for-beginners
✔ Ajouter TypeScript ? … Non / Oui
✔ Ajouter le support de JSX ? … Non / Oui
✔ Ajouter Vue Router pour le développement d'applications _single page_ ? … Non / Oui
✔ Ajouter Pinia pour la gestion de l'état ? … Non / Oui
✔ Ajouter Vitest pour les tests unitaires ? … Non / Oui
✔ Ajouter une solution de test de bout en bout (e2e) ? › Cypress
✔ Ajouter ESLint pour la qualité du code ? … Non / Oui
✔ Ajouter Prettier pour le formatage du code ? … Non / Oui
✔ Ajouter l'extension Vue DevTools 7 pour le débogage ? (expérimental) … Non / Oui

Génération du projet dans /home/jmena01/CONSULTANT/my_vuejs-3_beginner/vue-for-beginners...

Terminé. Exécutez maintenant :

  cd vue-for-beginners
  npm install
  npm run format
  npm run dev
```
## Two projects at the same level
* the project cloned from the [CH03 BLANK](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/tree/CH03) branch using Git
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap03$ git status
Sur la branche CH03
Votre branche est à jour avec 'origin/CH03'. # the project cloned from the Copnion GitHub REPO. The branch is meannt to start the exercises

rien à valider, la copie de travail est propre
```
* the project *vue-for-beginners* created through the command *npm create vue@latest*
```bash
jjmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/vue-for-beginners$ git status
fatal: ni ceci ni aucun de ses répertoires parents n'est un dépôt git : .git
```
* *vue-for-beginners/README.md* reminds you of all the commands (including the test comands) at your disposal 
## App.vue
* *vue-for-beginners/src/App.vue* calls <RouterView />
  * it is a standard component that allow to switch components depending the route
  * its configuration file (route --> Component) is under the router folder at: *vue-for-beginners/src/router/index.js*
    * it gives your two ways to call for a component
* so for the / Path the component *vue-for-beginners/src/views/HomeView.vue* is called
## The tests
* *vue-for-beginners/src/components/__tests__/HelloWorld.spec.js* loads the componnts and unit tests it
* *vue-for-beginners/cypress/e2e/example.cy.js* simulates a navigator to click or look for HTML Elements in the pages.
# 43
* [explanation of the setup keyword with the script tag](https://vuejs.org/api/sfc-script-setup)
# 44
* Te good news is that The SocialPost Component uses SASS (lang="scss")
  * which allows for embedding
# 46 
* What is the D switch for? see  [first answer to that StackOverflow Question](https://stackoverflow.com/questions/23177336/what-does-npm-d-flag-mean)
  * it is a shortcut for *--save-dev* 
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/vue-for-beginners$ npm i -D sass-embedded
```
## Your turn
* [example of a footer in VueJS3](https://dev.to/divewitholeg/a-responsive-and-language-aware-footer-component-for-vue-3-3c5c)
# 47
* defineProps is a comiler macro it compiles the declaration ino actual properties
# 48
* Is is different depending
  * it is a text between HTML Tags: use *{{}}*
  * It is a HTML Tag attribute: replace attrName=xxxxx by *:attrName=variable*
* The component in question is *vue-for-beginners/src/components/molecules/SocialPost.vue*
# 52
* difference between REF and reactive in [this link](https://vuejs.org/api/reactivity-core.html)
  * we define a reactive from a ref variable
# 53
* *&__selected* see [adding suffix in SASS](https://sass-lang.com/documentation/style-rules/parent-selector/#adding-suffixes) 
# 57 Your Turn
* For the WelcomeView or the footer
* If you want to associate a variable to a property prefix the property name with **:** 
* in order  to interpret the assoiated value as a variable
  * also true for the templates