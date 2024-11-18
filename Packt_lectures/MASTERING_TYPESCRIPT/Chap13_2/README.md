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
# 384
* How to use @Option props just this.props
> Note that the collection prop that is exposed by the component has the same
> name as the internal state property named collection
* I can different names
```ts
@Options({
  props: {
    collection: CartCollection
  },
  components: {
    ItemView
  }
})
export default class ShoppingCart extends Vue {
  collection!: CartCollection; //The property must be declared
  collectionData!: CartCollection; //The sensitive data must be declared in the same way as the prop
  isCheckingOut!:boolean;
  data() {
    return {
      collectionData: this.collection,
      isCheckingOut: false
    } 
  }
```
* in the template above I address the data and not the props
```html
<div v-bind:key="item.id" v-for="item in collectionData.items"> <!--I address the data not the props-->
  <ItemView :item="item" @onRemove="onItemRemoved">
  </ItemView>
</div>
```
# 386
* in order to place correctly the label respective to the input
  * we have to use  a bit of Javascript *mdb.Input(inputBts).init()* with mdb from *mdb-ui-kit/js/mdb.min.js*
```ts
    mounted(){
        let inputBts = this.$refs.inpuAmount;
        let inputMdb = new mdb.Input(inputBts);
        inputMdb.init;
    }
```
# 388
## Emits a remove event from the ItemVue
```ts
    onItemRemove(){
        let myId = this.itemData.id
        console.log(`[ItemView][onItemRewove] for the item of id: ${myId}`)
        this.$emit("onRemove", myId)
    }
```
* we pass the id of the element to remove
## The parent Element ShoppingCart receives th onRemove event
```html
<ItemView :item="item" @onRemove="onItemRemoved">
</ItemView>
```
* and the ShoppingCart's *onItemRemoved* function
```ts
  onItemRemoved(id:number){ //The id passed with the onRemove event (by the ItemView child element)
    const index = this.collectionData.items.findIndex((item) => item.id === id);
    this.collectionData.items.splice(index, 1);
    console.log(`[ShoppingCart][onItemRemoved] I removed the item if id ${id} which correspond to the index ${index} of the collectionData state`);
  }
```
* We just update the state (data()) and the template will be updated automatically!!!
## Just a mystery
* *shopping-cart/src/components/ItemView.vue* and *shopping-cart/src/shims-vue.d.ts* must call the same library
* *declare module 'mdb-ui-kit/js/mdb.min.js';* does not exist anymore. the new are at *shopping-cart/node_modules/mdb-ui-kit/js*
  * and is replaced by *declare module 'mdb-ui-kit/js/mdb.es.min.js';* the other  mdb.umd.min.js does not accept the **Input** method
* the label does not align very well perhaps an incompatibility between
  * the library called in  *Mastering-TypeScript-Fourth-Edition/ch13/shopping-cart/public/index.html* are the 3.0.0 version
```html
<script
type="text/javascript"
src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.0.0/mdb.min.js">
</script>

<link
href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.0.0/mdb.min.css"
rel="stylesheet"
/>
```
* And the one I call in my code are (see *shopping-cart/package-lock.json*) the
```js
"dependencies": {
        "@fortawesome/fontawesome-free": "^6.6.0",
        "bootstrap": "^5.3.3",
        "mdb-ui-kit": "^8.0.0", //there are the 8.0.0 version
        "vue": "^3.2.13",
        "vue-class-component": "^8.0.0-0"
      },
``` 
* in the example code there are in  [package-lock.json for the chapter 13 on GitHub](https://github.com/PacktPublishing/Mastering-TypeScript-Fourth-Edition/blob/main/ch13/shopping-cart/package-lock.json)
```js
    "mdb-ui-kit": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/mdb-ui-kit/-/mdb-ui-kit-3.0.0.tgz",
      "integrity": "sha512-4Hr6u2qnWxd5Od+fsF+oB2MePU9HUubsOn6+rE7F6bTU5eDDtgpqPoo4/DrOJx68+2vp0hrA8i/2/zo4lCTvoQ=="
    },
```
* I changed *shopping-cart/public/index.html* for:
```html
    <!--<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/8.0.0/mdb.es.min.js">
    </script>--> <!--Decalaration may not be at the top-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/8.0.0/mdb.min.css">
  </head>
```
* plus in *shopping-cart/src/components/ItemView.vue* placing the label after the input
```html
<div class="form-outline" ref="inputAmount">
    <input type="number"
    class="form-control"
    v-model="itemData.amount">
    <label class="form-label">No of Switches</label>
</div>
```
* The label is now very well placed
## For the complexity ot ItemWiewTemplate mixing rows and columns
* when you close a div just comment the opening div it belongs to
```html
<template>
    <div>
        <div class="container-sm">
            <div class="row"><h4>Item#{{ itemData.id }} - {{ item.name }} ({{ item.type }})</h4></div>
            <br />
            <div class="row">
                <div class="col-sm-2">
                    <img :src="imageSource" class="img-thumbnail image-small">
                </div>

                <div class="col-sm-10">
                    <div class="row">
                        <div class="col-sm-5">
                            <div class="form-outline" ref="inputAmount">
                                <input type="number"
                                class="form-control"
                                v-model="itemData.amount">
                                <label class="form-label">No of Switches</label>
                            </div>
                        </div> <!--col-sm-5-->
                    </div> <!--row-->
                    <div class="row">&nbsp;</div>
                    <div class="row">
                        <div class="col-sm-6">
                            <button class="btn btn-primary" v-on:click="onItemRemove">
                                <i class="fas fa-times-circle"></i>&nbsp;Delete
                            </button>
                        </div> <!--col-sm-6---->
                    </div> <!--row-->
                </div> <!--col-sm-10-->
            </div> <!--row---->
        </div> <!--container-sm-->
    </div>
</template>
```