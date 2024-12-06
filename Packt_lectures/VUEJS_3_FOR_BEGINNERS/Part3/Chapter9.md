# 158
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git ch09
Clonage dans 'ch09'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d objets: 100% (321/321), 171.75 Kio | 3.50 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd ch09/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch09$ git switch CH09
La branche 'CH09' est paramétrée pour suivre la branche distante 'CH09' depuis 'origin'.
Basculement sur la nouvelle branche 'CH09'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch09$ npm i

added 444 packages, and audited 445 packages in 8s

105 packages are looking for funding
  run `npm fund` for details

10 vulnerabilities (5 moderate, 5 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
```
# 160
* Slots can accept HTML and other Vue Components
# 164
* [scoped slots](https://www.w3schools.com/vue/vue_scoped-slots.php) are not explained in this book
# 166
* There must be the same name between html template
```html
<textarea rows="4" cols="20" ref="textareaRef"></textarea>
```
* and the script part of the component
```javascript
const textareaRef = ref(null);
onMounted(() => { //The component must be mounted to access textArea part
    textareaRef.value.focus();
});
```
* Refs should not be used more than five times
  * If it is the case it means we are mis-using others Vue features 
# 171 Lifecycle
* class=*sidebar_icon* has been added to the svg because the template tag produces no HTML element
# 172
* [Why the ampersand and why not in Sass](https://css-tricks.com/the-sass-ampersand/)
* *position:relative* of the <aside> enclosing element
  * is mandatory to allow the Icons inside it to have a *position:absolute*
  * it seems that svg behaves like a div (block)  
* apply the sidebar__closed class if the condition is met (here closed is true)
```
:class="{ 'sidebar__closed': closed}
```
* the **:** are here for v-bind
# 173
* The Lifecycle is to be found in Figure 2.3 on page *20* at the [Chapter 2 of the book](../Part1/Chapter2.md)
* **onBeforeMount**: *This will trigger just before the component is rendered but after all the methods and Refs have been initialized*
  * but it has still *to create and insert DOM Nodes* see figure 2.3 
# 174
* We can see the local storage in the FireFow / F12 Web Console
  * tab storage
  * on the left click to local storage
* we can see the sidebar value to switch between true and false (all strings) when clickin on the Icon Arrows