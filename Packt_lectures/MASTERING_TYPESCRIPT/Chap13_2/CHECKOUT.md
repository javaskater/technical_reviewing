# 388 The Checkout component
* very interesting 
```html
<div v-if="isCheckingOut">
```
* to mask/unmask entire part of the screen
* The price of the item is to be found in the items list at *shopping-cart/src/CartIems.ts* 
* *scope="col"* and *scope="row"* are typical array elements [here a demo in french](https://www.accede-web.com/notices/html-et-css/tableaux/utiliser-lattribut-scope-pour-associer-les-cellules-aux-entetes-des-tableaux-de-donnees-simples/)
* in the *shopping-cart/src/components/ShoppingCart.vue* component, I forgot to declare the ChecoutComponent
```javascript
  components: {
    ItemView,
    CheckoutView
  } 
```
* so the  *<CheckoutView* was not replaced by its template...
# 390
* *right-aligned-text* is not seen as a css property by the Firefox explorer