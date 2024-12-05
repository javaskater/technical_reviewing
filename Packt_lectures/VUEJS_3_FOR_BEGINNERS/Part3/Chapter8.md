# 134 Technical requirements
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap08
Clonage dans 'chap08'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 2.86 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap08/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap08$ git switch CH08 #on passe sur la branche CH08 (début du chapitre)
La branche 'CH08' est paramétrée pour suivre la branche distante 'CH08' depuis 'origin'.
Basculement sur la nouvelle branche 'CH08'
```
# 139
* Vitur helps giving the imported library after I declare the module
  * example *vitest for expect*
# 140
* Given => describe
* When => describe
* Then => it
```javascript
import { expect, describe, it } from "vitest";
import { mount } from "@vue/test-utils";
import component from '../atoms/TheButton.vue'

describe( 'TheButton vue', () =>{
    describe('When Mounted', () => {
        it('renders properly', () => {
            expect(true).toBe(true);; //always true
        });
    });
});
```
* Be careful expect has a very specific syntax
  * it is not like *assert* in Java
# 143
* I test your turn using the [passing properties to a mounted component in Vue Test](https://test-utils.vuejs.org/guide/essentials/passing-data)
* * other link of interest [all the possible expectations in ViTest](https://vitest.dev/api/expect)
```javascript
describe( 'TheButton vue', () =>{
    describe('When Mounted', () => {
        it('renders properly', () => {
            const wrapper = mount(component, {});
            expect(wrapper.html()).toContain('button');
            //expect(false).toBe(true);
        });
        it ('default to light theme', () => {
            const wrapper = mount(component, {});
            expect(wrapper.classes()).toContain('light');
        });
        /**
         * Your turn
         */
        it ('can be set to ddark theme when mounted', () => { 
            const wrapper = mount(component,{
                props: {
                    theme: 'dark'
                }
            });
            expect(wrapper.classes()).toContain('dark');
        });
        it ('can be set to dark theme after initialization', async () => {
            const wrapper = mount(component);
            await wrapper.setProps({theme: 'dark'});
            expect(wrapper.classes()).toContain('dark');
        });
    
        it ('cannot be set to atheme other thant light or dark', () => {
            const wrapper = mount(component,{
                props: {
                    theme: 'yellow'
                }
            });
            expect(wrapper.classes()).toContain('yellow'); //The test is OK the validator does not act
        });
    });
});
```
# 150 Cypress does not access the site
* I put the [issue 4 on the Packt Github Site](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/issues/4)