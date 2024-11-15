# 379
## From the first part
* We created the default shopping-cart application in [the First Part of the paragraph on Vue.JS](../Chap13_1/README.md)
## Installing mdBootstrap
* in the *shopping-cart/src/shims-vue.d.ts* I added
```typescript
declare module 'mdb-ui-kit/js/mdb.es.min.js'; //It adds an es to the module name
```
## Note
* the created *shopping-cart/src/App.vue* is already using the OptionAPI
# 381
* for the App.vue to avoid any VisualCodeStudio error you have
  * [what is the use of the question mark in TypeScript](https://blog.logrocket.com/understanding-exclamation-mark-typescript/)
```ts
export default class App extends Vue {
  cartItems!: CartCollection; //Must define the property as we assert it never will be null see ShoppingCart p 383 
  data(){
    return {
      cartItems: shoppingCartItems
    }
  }
}
``` 
## don't forget
* to test the page do a **npm run serve** under the project root
```bash
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT/shopping-cart$ npm run serve

> shopping-cart@0.1.0 serve
> vue-cli-service serve

 INFO  Starting development server...


 DONE  Compiled successfully in 3422ms                                                                                                                  17:32:51


  App running at:
  - Local:   http://localhost:8080/ 
  - Network: http://10.156.7.60:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.

Issues checking in progress...
No issues found.
```