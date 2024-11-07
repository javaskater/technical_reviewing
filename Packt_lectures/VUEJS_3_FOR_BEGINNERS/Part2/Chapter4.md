# 59
## The [VueJS directives](https://vuejs.org/api/built-in-directives.html)
* The [Official documentation on the VueJS directives](https://vuejs.org/api/built-in-directives.html)
  * is very well-done
# p 60
## Loading the new Environment development
* The book proposes git switch instead of git checkout
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap04
Clonage dans 'chap04'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 3.99 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap04/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap04$ git checkout CH04
La branche 'CH04' est paramétrée pour suivre la branche distante 'CH04' depuis 'origin'.
Basculement sur la nouvelle branche 'CH04'
```
* We now have our starting code on *~/CONSULTANT/my_vuejs-3_beginner/chap04*
* getting the libraries adn starting the demo
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap04$ npm i

added 444 packages, and audited 445 packages in 24s

105 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (5 moderate, 4 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap04$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 373 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
## Decomposition
* App.vue calls
```html
<template>
  <TheHeader />

  <RouterView />
</template>
```
* TheHeader is given by *chap04/src/components/organisms/TheHeader.vue* and is static
  * *https://picsum.photos/50/50"* is blocked by My company Firewall
*  RouterView depends on the router configuration file *chap04/src/router/index.js*
  * We can test http://localhost:5173/about 
  * for the Home Page the *chap04/src/views/HomeView.vue* is called
    *  which adds a <main> tag around *chap04/src/components/TheWelcome.vue*
* With CTRL+Enter you can follow the included components in Visual Studio Code.
## v-text and v-html
* Vue directives manipulate directly the DOM
* difference between v-show (visibility:visible/hidden) and v-if (display) is that 
  * the former just hide the element
  * the latter removes the element from the DOM
# 61
* good [examples of v-for in the Vue Official documentation](https://vuejs.org/api/built-in-directives.html#v-for)
* the [v-on official documentation](https://vuejs.org/api/built-in-directives.html#v-on) is worth read
* the book explaination is taken [from the official doc](https://vuejs.org/api/built-in-directives.html#v-bind)
* [another documentation on named slots](https://vuejs.org/guide/components/slots.html#named-slots) which means the use of v-slot
* You can create your own custom directives let them start with *v-*
# 62
* The green link comes from *chap04/src/assets/main.css* which is called by *chap04/src/main.js*
# 63
* Back to the [ref and reactive parameters](https://vuejs.org/guide/essentials/reactivity-fundamentals.html)
  * The following code shows *Welcome JPMENA* in *TheHeader.vue*
```javascript
import { ref } from 'vue';
const username = ref("Zelig880");
username.value = "JPMENA";
```
# 65
* back quotes are used to represent [template litérals on multiline string see answer 466](https://stackoverflow.com/questions/27678052/usage-of-the-backtick-character-in-javascript)
# 67
* using the Firefox DOM Explorer we see that v-vhow does not withdraw the Button from the DOM, instead it sets its display property to none
```html
<div class="SocialPost">
    <div class="header">
      <img class="avatar" src="https://i.pravatar.cc/40">
      <div class="name">Username two</div><div class="userId">usernameId2</div>
    </div>
    <div class="post">This is my second post</div>
    <button style="display: none;"> Show Comments </button>
</div>
```
# 68 v-if
* With v-if the component is not in the DOM, The Firefox DOM Explorer puts a <!--v-if--> HTML comment instead
* A reactive value adds reactivity to the VueJS dom like for *showComments*
# 71 v-for
* the v-for is meant to repeat a spécific HTML Element, so in Figure 4.6 it is not put on the UL (we won't repeat the UL element)
  * but reather on th LI element 
# 72 v-for 
* The Three steps method we follow is an intersting one.
* I added the index in the v-for loop
```html
<template>
    <div>
        <p>Comments:</p>
        <div v-for="co, ic in comments">{{ ic + 1 }}st Comment: {{ co }}</div>
    </div>
  </template>
```
# 73 Your turn
* [an integer is a Number for Javascript/Vue](https://vuejs.org/guide/components/props)