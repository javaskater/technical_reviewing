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