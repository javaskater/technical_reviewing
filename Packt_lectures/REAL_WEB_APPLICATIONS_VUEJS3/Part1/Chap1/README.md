# page 5
* node 18 minimum is required:
```bash
jmena01@M077-1840900:~/Documents/CONSULTANT/technical_reviewing$ node -v
v18.16.0
```
* [StackBlitz](https://stackblitz.com/) is a very inseresting environment to test Javascript projects
  * independently of the framework
* it is reommended to access the [Vue documentation](https://vuejs.org/guide/introduction.html) for a more in depth unnderstanding of all he conepts
# page 6:
* There are 4 extensions to be added to Visual Studio Code !
  * I replaced the two extensions named after Volar with the Official VueJS
# page 7:
* The [Vue Dev Tools](https://vuejs.org/guide/scaling-up/tooling.html#browser-devtools) is available on all major web browsers no more only o Chrome.
 * For mys Firefox it is the [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
# page 8
* the create pject is called through *npm init vue@latest*
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/Chapter1$ npm init vue@latest
Need to install the following packages:
  create-vue@3.10.4
Ok to proceed? (y) y

Vue.js - The Progressive JavaScript Framework

✔ Nom du projet : … my-first-vue
✔ Ajouter TypeScript ? … Non / Oui
✔ Ajouter le support de JSX ? … Non / Oui
✔ Ajouter Vue Router pour le développement d'applications _single page_ ? … Non / Oui
✔ Ajouter Pinia pour la gestion de l'état ? … Non / Oui
✔ Ajouter Vitest pour les tests unitaires ? … Non / Oui
✔ Ajouter une solution de test de bout en bout (e2e) ? › Non
✔ Ajouter l'extension Vue DevTools 7 pour le débogage ? (expérimental) … Non / Oui

Génération du projet dans /home/jmena01/CONSULTANT/my_vue_js/Chapter1/my-first-vue...

Terminé. Exécutez maintenant :

  cd my-first-vue
  npm install
  npm run format
  npm run dev
```
* I check the commands
  * npm i is the longuest and the more problematic (it warns us of the age of our node.js)
  * *npm run format* calls *prettier --write src/*
# page 11
* test of the simplified template:
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/Chapter1/my-first-vue$ npm run dev

> my-first-vue@0.0.0 dev
> vite


  VITE v5.3.2  ready in 1310 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```
* in the prevoius console you also see the errors (VSCode helps)