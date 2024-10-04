# 18 Reactvity
* I cannot test the code in the node.js REPL
* I have to create a vue project
# 19 The Lifecycle
* Three main stp
  * creating the component's HTML
  * gathering all the dynamic values
  * displayng these values (with the HTML) in the DOM
# p 20 The diagram
* Figure 2.3 see also [option Lifecycle official page](https://vuejs.org/api/options-lifecycle)
# 21
* before-mount means the template has already been compiled. It is about to be appended to the DOM
# 22
* [beforeUpdate](https://vuejs.org/api/options-lifecycle#beforeupdate): clearly explained. concerns the Ref values which depends on a values that is to be changed, the value is changed the DOM has still not been changed
  * You don't need theses lifecylces as VueJs rovides other features like computed values and watchers 
* [beforeUnmount](https://vuejs.org/api/options-lifecycle#beforeunmount) the component is still functional
  * ideal for unsubscribing to events for performance reasons (do not let subscribers when the event source does not exist anymore)
# 25
* Figure 2.5 intersting fr differentiating between *Composition API* and *Option API*
* *Props*, *Data*, *Methods* are all options
* On the other hand, a feature is linked to a technical output
# 28
* The exemple does not say how to create the project skeleton for this ATOM
* No Appendix in that book
* I create a project using [the npm method](https://vuejs.org/guide/quick-start)
  * I respond No to all questions
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ npm create vue@latest

Vue.js - The Progressive JavaScript Framework

✔ Nom du projet : … Atom
✔ Nom du package : … atom
✔ Ajouter TypeScript ? … Non / Oui
✔ Ajouter le support de JSX ? … Non / Oui
✔ Ajouter Vue Router pour le développement d'applications _single page_ ? … Non / Oui
✔ Ajouter Pinia pour la gestion de l'état ? … Non / Oui
✔ Ajouter Vitest pour les tests unitaires ? … Non / Oui
✔ Ajouter une solution de test de bout en bout (e2e) ? › Non
✔ Ajouter ESLint pour la qualité du code ? … Non / Oui
✔ Ajouter l'extension Vue DevTools 7 pour le débogage ? (expérimental) … Non / Oui

Génération du projet dans /home/jmena01/CONSULTANT/my_vuejs-3_beginner/Atom...

Terminé. Exécutez maintenant :

  cd Atom
  npm install
  npm run dev
``` 
## My option project
* More on the [option API in the VueJS inrduction](https://vuejs.org/guide/introduction.html#options-api)
* There is an icon in *Atom/src/assets/logo.svg*
* I put the code in *Atom/src/App.vue*
* Two difficulties:
  * The path to the Logo Image it is not *./assets/logo.svg* but *./src/assets/logo.svg*
  * the @click function: it has to be decalred in a methods part of the script tag
* the App.vue
```javascript
<template>
  <vfpIcon size="large" name="logo" @click="notifie" />
</template>

<script>
import vfpIcon from'./components/MyIcon.vue';
export default{
  components: {vfpIcon},
  methods:{
    notifie: function (event){
      var message = "Hello World";
      console.log("le messsage est:"+message);
      alert(message)
    }
  }
};
</script>
```
* the components/MyIcon.vue
```javascript
<template>
  <img :src="iconPath" :class="sizeClass" />
</template>
<script setup>
import { computed } from 'vue';

  const props = defineProps({
    size: String,
    name: String
  });
  const iconPath = computed(() => {
      return `./src/assets/${this.name}.svg`;
    });
  const sizeClass = computed(() => {
      return `${this.size}-ic);on`;
    }
function notifie(event){
  message = "Hello World";
  console.log("le messsage est:"+message);
  alert(message)
}
</script>
<style scoped>
  .small-icon {
    width: 16px;
    height: 16px;
  }
  .medium-icon {
    width: 32px;
    height: 32px;
  }
  .large-icon {
    width: 48px;
    height: 48px;
  }
</style>
```
# 29
* a property can have validation rule
* computed values are dynamic properties
## Composition API
* More on the [Composition API in the VueJS introduction](https://vuejs.org/guide/introduction.html#composition-api)
### for the component
* this is replaced by props
* the computed values are defined using anonymous functions passed to the computed function (which is imported)
* script has the setup keyword in the same way that style has the scoped keyword
* I couldn't use defineComponent to give another name (different from the file name) to the component
```javascript
<template>
  <img :src="iconPath" :class="sizeClass" @click="notifie" />
</template>
<script setup>
import { computed } from 'vue';

const props = defineProps({
size: String,
name: String
});

const iconPath = computed(() => {
  return `src/assets/${props.name}.svg`;
});

const sizeClass = computed(() => {
  return `${props.size}-icon`;
});

function notifie(event){
  var message = "Hello World";
  console.log("le messsage est:"+message);
  alert(message)
}
</script>
<style scoped>
  .small-icon {
    width: 16px;
    height: 16px;
  }
  .medium-icon {
    width: 32px;
    height: 32px;
  }
  .large-icon {
    width: 48px;
    height: 48px;
  }
</style>
```
### for the App
* You have to declare the components to make them active
* export default is prohibited when script has the setup keyword
  * it pushes an error otherwise ... 
* defineComponent is mandatory in App
```javascript
<template>
  <MyIcon size="large" name="logo" />
</template>

<script setup>
import { defineComponent } from 'vue'
import MyIcon from'./components/MyIcon.vue';

defineComponent({
  name: 'App',
  components: {
    MyIcon
  }
});
</script>
```