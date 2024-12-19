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
* If you don't call the line with comment underneath in *src/components/molecules/CreatePost.vue*
```javascript
const createPostHandler = (event) => {
    event.preventDefault(); //If you don't have it the pages is reloded and the posts store (Pinia) is reloaded
    addPost(postText); // is accepted like postText.value (which is a cleaner way of doing it)
    console.log(`[CreatePost][createPostHandler] adding a new post with text ${postText.value}`);
}
```
* The page is reloaded and you lose the added post (the Pinia store is resetted)
* The v-model is linked to a Ref variable (const because the enveloppe does not change) 
> Behind the scenes, v-model assigns the value on the first load and then automatically updates it
> every time the input field emits a change event
# 230
* *@submit* replaced by *@submit.prevent* to avoid to have to call event.preventDefault in the event handler.
# 231
* adding *vee-validate* I add the -s flag to install action of npm
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap12$ npm i vee-validate -s
```
* now in the *package.json*:
```javascript
  "dependencies": {
    "pinia": "^2.1.6",
    "vee-validate": "^4.14.7", //Newly added in prod dependencies
    "vue": "^3.4.27",
    "vue-router": "^4.2.4"
  },
```
# 232
* The field name must be the same as the parameter name on the @submit handle function
  * the parameters' order does not matter
  * no @submit.prevent (it is not even accepted) 
* *<Field* is by default an *<input type=text* to have other types of input use the **as** key!
# 233
* The field name is also used to connect the field with the error message
# 235
* returning an error message is like returning false for the validation's rule
* *defineRule* defines a validation rule it can be repeated like:
```javascript
  defineRule('required', value => {
    if(!value || !value.length){
      return 'this field is required';
    }
    return true;
  })
  defineRule('mon10chars', value => {
    if(!value || value.length < 10){
      return 'this field must have 10 characters min';
    }
    return true;
  })
```
# 236
* the name of the field must be the same as the Error's name
  * Remember: it is used as the name of the parameter in the submit handler function
# 237
* [the website for the predefined vee validation rules](https://vee-validate.logaretm.com/v4/guide/global-validators#vee-validaterules) 
  * is very interesting
* Adding the package
  * don't forget the -s switch as it adds the entry in the package.json and  package-lock.json files
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap12$ npm i @vee-validate/rules -s
```
* which added in *package.json*
```javascript
 "dependencies": {
    "@vee-validate/rules": "^4.14.7", //package added
    "pinia": "^2.1.6",
    "vee-validate": "^4.14.7",
    "vue": "^3.4.27",
    "vue-router": "^4.2.4"
  },
```
* and also added in the *package-lock.json* file
```javascript
  "packages": {
    "": {
      "name": "vue.js-for-beginners",
      "version": "0.0.0",
      "dependencies": {
        "@vee-validate/rules": "^4.14.7", //just added and locked
        "pinia": "^2.1.6",
        "vee-validate": "^4.14.7",
        "vue": "^3.4.27",
        "vue-router": "^4.2.4"
      },
```
* the [regex rule](https://vee-validate.logaretm.com/v4/guide/global-validators#regex) could be very interesting
# 238
* To have more than one parameter to your rule see the [between global rule](https://vee-validate.logaretm.com/v4/guide/global-validators#between)
* Their error message are very poor *email2 is not valid* is one of them
# 239
* be careful to use *:rules* when you pass an object (don't forget the :)
```html
<Form @submit="handleSubmit">
    <label for="email">Email</label>
    <Field id="email" type="email" rules="stdrequired|stdemail" placeholder="Enter here your email" name="email2"></Field> <!--pass a string-->
    <ErrorMessage as="div" class="error" name="email2" />
    <label for="message">Message</label>
    <Field id="message" as="textarea" :rules="{stdrequired:true,stdmin:100}" name="message2"></Field>  <!--pass an object-->
    <ErrorMessage as="div" class="error" name="message2" />
    <TheButton>Send</TheButton>
</form>
```
## small exercise
* [making post or get requests with fetch](https://www.topcoder.com/thrive/articles/fetch-api-javascript-how-to-make-get-and-post-requests)
* doing a [dummyapi.io dummy post request](https://dummyapi.io/docs/post)
  * I get the Post Create Content on [that models link](https://dummyapi.io/docs/models) 
```bash
curl -H "app-id: 657a3106698992f50c0a5885" -H 'Content-Type: application/json' \
 -d '{"text": "Hello everybody", "image": "https://img.dummyapi.io/photo-1581804928342-4e3405e39c91.jpg", "likes": 0, "tags": ["animal","dog","golden retriever"], "owner": "60d0fe4f5311236168a109d5"}' \
 -X POST https://dummyapi.io/data/v1/post/create
```
* which gives
```bash
jmena01@M077-1840900:~$ curl -H "app-id: 657a3106698992f50c0a5885" -H 'Content-Type: application/json'  -d '{"text": "Hello everybody", "image": "https://img.dummyapi.io/photo-1581804928342-4e3405e39c91.jpg", "likes": 0, "tags": ["animal","dog","golden retriever"], "owner": "60d0fe4f5311236168a109d5"}'  -X POST https://dummyapi.io/data/v1/post/create # the request
{"id":"67644d65b75039f2595c14ec","image":"https://img.dummyapi.io/photo-1581804928342-4e3405e39c91.jpg","likes":0,"link":"","tags":["animal","dog","golden retriever"],"text":"Hello everybody","publishDate":"2024-12-19T16:44:21.376Z","updatedDate":"2024-12-19T16:44:21.376Z","owner":{"id":"60d0fe4f5311236168a109d5","title":"mrs","firstName":"Sibylle","lastName":"Leibold","picture":"https://randomuser.me/api/portraits/med/women/89.jpg"}}
```
### TODO makes the post request
* see [making post or get requests with fetch](https://www.topcoder.com/thrive/articles/fetch-api-javascript-how-to-make-get-and-post-requests)
* see *src/stores/posts.js*