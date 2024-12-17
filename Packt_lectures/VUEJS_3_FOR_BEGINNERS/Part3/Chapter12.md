# 224
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap12
Clonage dans 'chap12'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 7.47 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap12
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap12$ git switch CH12 # see page 224
La branche 'CH12' est paramétrée pour suivre la branche distante 'CH12' depuis 'origin'.
Basculement sur la nouvelle branche 'CH12'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap12$ npm i
npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm WARN deprecated @humanwhocodes/config-array@0.11.14: Use @eslint/config-array instead
npm WARN deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm WARN deprecated abab@2.0.6: Use your platform's native atob() and btoa() methods instead
npm WARN deprecated @humanwhocodes/object-schema@2.0.3: Use @eslint/object-schema instead
npm WARN deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm WARN deprecated domexception@4.0.0: Use your platform's native DOMException instead

added 444 packages, and audited 445 packages in 23s

104 packages are looking for funding
  run `npm fund` for details

6 vulnerabilities (2 moderate, 4 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap12$ npm run dev # start the local server

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.5.3  ready in 379 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# 225
* the label can connect to the corresponding input
  * either by the input's id
  * or by wrapping the input field to which it belongs  
# 227
* [see more about autocomplete](https://www.w3schools.com/tags/att_input_autocomplete.asp)
# 228 v-model
* *v-model* is typically used in forms
* from the input value to the correspdonding ref-value
## The complicated
```html
<input value="firstName" @input="firstName = $event.target.value" />
```
* has been simplified to:
```html
<input v-mdel="firstName" />
```
## ref or v-model
* see [this discussion on reddit](https://www.reddit.com/r/vuejs/comments/dntasl/should_you_prefer_to_use_vmodel_or_ref_when/?rdt=40731)
# 229
* If you don't call the line with comment underneath
```javascript
const createPostHandler = (event) => {
    event.preventDefault(); //If you don't have it the pages is reloded and the posts store (Pinia) is reloaded
    addPost(postText); // is accepted like postText.value (which is a cleaner way of doing it)
    console.log(`[CreatePost][createPostHandler] adding a new post with text ${postText.value}`);
}
```
* The page is reloaded and you lose the added post (the Pinia store is resetted)