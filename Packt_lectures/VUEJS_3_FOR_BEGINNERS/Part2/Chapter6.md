# 93
* properties are a dynamic way to exchange data from parent to child
* events are a dynamic way to exchange data from child back to parent
  * broadcasting messages to the rest of the App
# 94 
## technical requirements
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap06
Clonage dans 'chap06'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 1.34 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap06
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap06$ git switch CH06 # Go to Chapter 6 before running the Book's chapter
La branche 'CH06' est paramétrée pour suivre la branche distante 'CH06' depuis 'origin'.
Basculement sur la nouvelle branche 'CH06'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap06$ npm i # load librraries

added 444 packages, and audited 445 packages in 10s

105 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (5 moderate, 4 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap06$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 380 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# 95 
## Folder and File changes
* *chap06/src/components/atoms/TheButton.vue* is not use for the moment
  * it has 3 props: *theme* (class) *size* (class) *value* (button's text)
    * to be added to the props 
  * It embarks the classes you can use for it
# 96
* The the class for the icon is defined in the parent component no :class because we give it a string and not a variable
```html
<IconSettings class="settings" />
```
```scss
header {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    grid-column-start: 1;
    grid-column-end: 3;
    padding-bottom:24px;
    border-bottom: solid 1px var(--color-border);

    .span {
        display: flex;
    }
    a{
        font-size: 16px;
        line-height: 24px;
        margin-right:8px;
        font-weight: bolder;
    }
    .settings {
        width: 16px;
        height: 16px;
        fill: var(--color-input-mute);
    }
}
```
# 97
* The [key attribute](https://vuejs.org/guide/essentials/list#maintaining-state-with-key)
  * is meant to give VueJS a hint of each element identity in a v-for loop
  * in order to facilitate in-place replacement for example
  * In the link example we see that the *v-for* directive is at the template level
* In our case we have the *v-for* directive is at the child level <SocialPost
# 99
* default values can be returned by factory functions (functions that accept 0 parameter)
  * especially in the case of arrays *() => []* or objects *() => {}* 
* with a validator with no default value, the property becomes required 
# 100
* working on the *chap06/src/components/atoms/TheButton.vue*