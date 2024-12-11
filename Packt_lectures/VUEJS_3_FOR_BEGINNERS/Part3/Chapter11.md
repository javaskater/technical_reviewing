# 202
## Technical requirements
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git ch11
Clonage dans 'ch11'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 2.45 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd ch11
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch11$ git switch CH11
Déjà sur 'CH11'
Votre branche est à jour avec 'origin/CH11'.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch11$ npm i

added 444 packages, and audited 445 packages in 9s

105 packages are looking for funding
  run `npm fund` for details

11 vulnerabilities (1 low, 5 moderate, 5 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch11$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 373 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# 206
* *src/stores/counter.js* is created by the VueCli as an example of a Store
  * it is the one described in the [official documentation](https://pinia.vuejs.org/core-concepts/)
* the name proertie is only a storeId used by VueDevTools
  * if you want to use it use [the exported variable after having imported the js file](https://pinia.vuejs.org/core-concepts/#Using-the-store) 
# 207
* you can declare the store content (properites/state, computed/getters, methods/actions)
  * either using the Option API (the book use the OptionAPI) and the [Option Stores in the official documentation](https://pinia.vuejs.org/core-concepts/#Option-Stores)
  * state here is the same as defineState in the OptionAPI used for components
  * either using the composition API [Setting up the Store in the official documentation](https://pinia.vuejs.org/core-concepts/#Setup-Stores)
* I prefer the [Option API setting up the store](https://pinia.vuejs.org/core-concepts/#Option-Stores)
  * inside the store a state element can be accessed using **this** 
* *useCounterStore* is the name of the exported function... we call using the parentheses *const counter = useCounterStore()* (after having imported it)  
  * the getter are *computed properties* there are called without () parentheses like the state objects
# 209
* to define the SidebarStore we use the Option API
* state is a [javascript anonymous functions](https://www.javascripttutorial.net/javascript-anonymous-functions/)
```javascript
state: () => ({}),
```
* for the second term you can use () or not:
```javascript
> let add = (a, b) => a+b;
undefined
> add(2,3)
5
> let add2 = (a, b) => (a+b);
undefined
> add2(3,4)
7
```
# 210
* we have left the getters/computed empty for that first part
## to use the store, first use it in the component it is foreseen for, here SideBar.vue
* replace method with actions
* replace redf with state! 
# 212
* Be careful when the sideBar is closed not only
  * we do put its width to 40px through aside's class binding
  * but also we change its content through <template v-if and <template v-else 
* in the store replace all closed.value with this.closed
  * the console.log and the F12 warnings help to undestand where the problem is 
# 213
```html
<IconFullScreen class="icon" @click="sidebarStore.toggleSidebar" />
```
* is enough to let drive the sidebar from the Header. the book says
> All instances of the store will work as one, allowing us to use and modify states from different parts of the application.
# 214
* a getter is a function with the state parameter as the first parameter (the only mandatory)
* it is supposed not to produce any side effect like calling an API or logging
* but if state.closed changes friendly will change (see computed properties)
# 215
* With the managment of Posts inside a Pinia store (including fetching posts from the API) 
  * we approach what is done inside the company I work for 
 # 216
* all methods related to the post array are in *src/components/organisms/SocialPosts.vue*
  * this is where we fetch posts 
  * *src/components/molecules/SocialPost.vue* uses only one postData comming from the previous component 
* the Stores Fetch post is meant to work 
  * for the fetchData in onMount
  * for the fetchData in watch (when there are less that 4 post call the next page of posts) 
* the [posts store in the solution on gitHub](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH11-end/src/stores/posts.js)