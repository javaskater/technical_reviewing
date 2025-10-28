# 157-158
```bash
# rget the project in a new directory
jmena01@m077-2281091:~/CONSULTANT$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap09
Clonage dans 'chap09'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (83/83), done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 321 (delta 66), reused 52 (delta 52), pack-reused 238 (from 1)
Réception d''objets: 100% (321/321), 176.63 Kio | 4.77 Mio/s, fait.
Résolution des deltas: 100% (136/136), fait.
jmena01@m077-2281091:~/CONSULTANT$ cd chap09/
# we swith to the branch for starting chapter 9
jmena01@m077-2281091:~/CONSULTANT/chap09$ git switch CH09
la branche 'CH09' est paramétrée pour suivre 'origin/CH09'.
Basculement sur la nouvelle branche 'CH09'
# installation of the npm libraries that the project needs
jmena01@m077-2281091:~/CONSULTANT/chap09$ npm i

added 444 packages, and audited 445 packages in 2s

105 packages are looking for funding
  run `npm fund` for details

16 vulnerabilities (2 low, 4 moderate, 8 high, 2 critical)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.6.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.6.2
npm notice To update run: npm install -g npm@11.6.2
npm notice
# we start the local server
jmena01@m077-2281091:~/CONSULTANT/chap09$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 185 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# 160
* Slots can accept HTML and other Vue Components
# 163
* If the unique slot like Button il filled by callling the button the the HTML between the opening and closing Tag.
* for named slots like the StaticTemplate you need to define a template tag ith the slotname prexiex with **#**
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
# 168
* To get the value of the ref textAreaRef call 2 times value
```javascript
const createPost = (event) => {
    event.preventDefault();
    if (createPostForm.value.reportValidity()){
        console.debug(textareaRef.value) //tells US that it is a HTM%Element with value as the text
        console.log('Le entered text: '+textareaRef.value.value)
    } else {
        console.log("I don't approve !!!")
    }
}
```
# 170
tne v-if directive asks for a v-else directive otherwise the template does not appear
# 171 Lifecycle
* class=*sidebar_icon* has been added to the svg because the template tag produces no HTML element
# 172
* [Why the ampersand and why not in Sass](https://css-tricks.com/the-sass-ampersand/)
* *position:relative* of the <aside> enclosing element
  * is mandatory to allow the Icons inside it to have a *position:absolute*
  * it seems that svg behaves like a div (block)  
* apply the sidebar__closed class if the condition is met (here closed is true) don't forget the : before the class keyword
  * otherwise then class value won't be linked tot the closed ref
```
:class="{ 'sidebar__closed': closed}
```
* note on SASS
```scss
aside {
    display: flex;
    flex-direction: column;
    &.sidebar__closed{ //The & address the aside itself not its descendant
        width: 40px;
    }
    .sidebar__icon{ // Without the & we are looking for a descendant that has the sidebar__icon class
        position: absolute;
        right: 12px;
        top: 22px;
        cursor: pointer;
    }
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