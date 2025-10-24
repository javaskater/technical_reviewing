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
# 144 
* the commad to install Cypress is missing the *-D* (in the development libraries) switch it shoud be
```bash
npm install -D cypress
```
# 147
```bash
jmena01@m077-2281091:~/CONSULTANT/chap08$ npx cypress open
It looks like this is your first time using Cypress: 13.3.0

✔  Verified Cypress! /home/jmena01/.cache/Cypress/13.3.0/Cypress
```
* Ask the interface to create a *cypress.config.js* at the root of the project which contains
```javascript
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    specPattern: 'cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}',
    baseUrl: 'http://localhost:4173'
  }
})
```
* I access mys file through http://localhost:4173/__/#/specs
  * the file is located at *cypress/e2e/homepage.cy.js*
# 148
then only package.json command that works is
```javascript
    "test:e2e": "start-server-and-test preview http://localhost:4173 'cypress run --e2e'", //KO does not open the cypress configuration window
    "test:e2e:dev": "start-server-and-test 'vite dev --port 4173' http://localhost:4173 'cypress open --e2e'", //OK does open the cypress configuration window
```
* A typical example of a Cypress file is given in the [Chapter 8 solution](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH08-END/cypress/e2e/homepage.cy.js)
* it is played through http://localhost:4173/__/#/specs/runner?file=cypress/e2e/homepage.cy.js
# 150 
* be.visible is one of the assertions brought by the Intellisense plugin (autocompletion through the VSCode Intellisense plugin ?)
```javascript
cy.get('h1').should('be.visible');
```
* Cypress' get is a selector with a syntax very similar to the JQuery selectors ...
  * for example querying a css class
# 152
* The interesting thing is that on the [left pane of the Firefox windows of Cypress](http://localhost:4173/__/#/specs/runner?file=cypress/e2e/homepage.cy.js)
  * You have all XHR requests/responses
## When we call
```javascript
cy.get('[data-cy="showCommentButton"]').first().click();
```
* we see appearing the comment on [the middle pane of the Firefox windows of Cypress](http://localhost:4173/__/#/specs/runner?file=cypress/e2e/homepage.cy.js)
  * for the first Post that is
```html
<div class="SocialPostComments"><p>There are no comments for this post!</p></div>
```
* At this point, on the entire page there is only one element with a parent *.SocialPostComment* class that contains the 
# 153 
* Same thing for the last, but in that case we have a 4 comments with a *.comment* class 
```javascript
describe('Homepage', () => {
    it('default journey', () =>{
        cy.visit("/");
        cy.get('h1').should('contain.text', 'Companion app');
        cy.get('.SocialPost').should('have.length', 5);
        cy.get('[data-cy="showCommentButton"]').first().click();
        cy.get('.SocialPostComments').should('have.length', 1); // the only SocialPostComment in the DOM
        cy.get('.SocialPostComments').should('contain.text', 'There are no comments for this post!');
        cy.get('[data-cy="showCommentButton"]').last().click();
        cy.get('.SocialPostComments').last().should('not.contain.text', 'There are no comments for this post!');// there are two SocialPostComment parent elements in the DOM
    });
});
```