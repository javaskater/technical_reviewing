# preparation
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap13
Clonage dans 'chap13'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 5.20 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap13/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap13$ git switch CH12-end
La branche 'CH12-end' est paramétrée pour suivre la branche distante 'CH12-end' depuis 'origin'.
Basculement sur la nouvelle branche 'CH12-end'

npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm WARN deprecated @humanwhocodes/config-array@0.11.14: Use @eslint/config-array instead
npm WARN deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm WARN deprecated abab@2.0.6: Use your platform's native atob() and btoa() methods instead
npm WARN deprecated @humanwhocodes/object-schema@2.0.3: Use @eslint/object-schema instead
npm WARN deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm WARN deprecated domexception@4.0.0: Use your platform's native DOMException instead

added 447 packages, and audited 448 packages in 9s

105 packages are looking for funding
  run `npm fund` for details

6 vulnerabilities (2 moderate, 4 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap13$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.5.3  ready in 673 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# 244
* [VueJs Dev Tool for Firefox](https://addons.mozilla.org/fr/firefox/addon/vue-js-devtools/)
* restart Firefox to see the Vue Extension in the F12 Firefox debug console
# 245
* pin Vue devtools to the Toolbar on Firefox
# 252
## Timeline
* To make the Timeline in **My Firefox 140.3.0esr** You have to activate the Events you want to appear
  * Right click on a section (left panel) / select activate
  * click on the red circle to start Recording
  * **restart Firefox**
* What is very interesting is the component section
# 254
* I don't see how you get the recorded events
## Time line
* in order to see te detail Vue of Each event you must be in recording active mode
  * when you provok e another event you see alo all the events before
# 257
* I don't know how to install Vue DevTools plugin,
 * or are they present when You use them in you Vue App see *package.json*
```javascript
  "dependencies": {
    "@vee-validate/rules": "^4.12.6",
    "pinia": "^2.1.6", //also in Vue DevTools
    "vee-validate": "^4.12.6",
    "vue": "^3.4.27",
    "vue-router": "^4.2.4" //also in Vue DevTools
  },
```
