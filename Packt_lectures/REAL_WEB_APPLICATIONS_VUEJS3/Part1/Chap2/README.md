# 14
* Créate a new project
  * with more questions 
# 17
* The isChecked property is bidirectional
  * can be set at initialisation by the parent component
    * (decides which checkbox has to be set active)
* when the checkbox is checked/unchecked that valeur ** changes accordingly 
* here we go to the [link given](https://vuejs.org/guide/essentials/template-syntax.html#shorthand)
* Interesting also [binding multiple attributes at once](https://vuejs.org/guide/essentials/template-syntax.html#dynamically-binding-multiple-attributes)
* [slots](https://vuejs.org/guide/components/slots.html) are interestng
# 20
* key is here the index (see the [v-for loop](https://vuejs.org/guide/essentials/list)) :key is used to uniquely identify in order to keep the changes synchronized
  * it can be easily be shown as index
```html
<template>
    <ul>
        <li :key='key' v-for="(item, key) in listItems">
            <ListItem :is-checked="item.checked">{{ item.title }} - {{key}}</ListItem>
        </li>
    </ul>
</template>
```
* The ListItem property *is-checked* has in *vue-todo-list/src/components/ListItem.vue* a default value of false
  * the title property is the default <slot> value
# 21
* Two words about the class of ListItem
```html
<label :class="{ 'checked': isChecked }">
```
* :class is like :checked a read/write VueJs property linked to the html attributes class, checked
* ref or reactive allows to say the content can be modified 
  * *ref can be used to track primitives and objects* 
* Ref allows Typescript to guess the actual Type
  * *Ref is used to type the value*
* note the *console.log* with string interpolation to show the item that changed:
```typescript
 const toggleItemChecked = (item:Item):void => {
    item.checked = !item.checked
    console.log(`The item ${item.title} has changed its status to ${item.checked?"ON":"OFF"}`)
 }
```

# 23
* the [official link to the v-on directive](https://vuejs.org/api/built-in-directives.html#v-on) does not tell us what to do with the event object
  * on the book we use the *.prevent* modifier to the click event **v-on:click.prevent=**
  * Is it the reason why the checkbox is not checked ? (Tested that the reason)
# 24:
## The 3 dots
* what are the ... for?
  * that is a Javascript property
  * they are useful when you have to join two arrays see [geeks for geeks blog post](https://www.geeksforgeeks.org/what-are-these-triple-dots-in-javascript/)
* Here
```typescript
const sortedList = computed(() =>
    [...listItems.value].sort((a, b) => (a.checked? 1:0) - (b.checked? 1:0))
)
```
* is the almost the same than
```typescript
 const sortedList = computed(() =>
    listItems.value.sort((a, b) => (a.checked? 1:0) - (b.checked? 1:0))
)
```
* because we have only one array 
* but the original array (*listItems.value*) is not modified by the sort (the element themselleves are modified du to reactivity)
## computed reactivity
* What about computed properties reactivity see [this Medium link](https://medium.com/@mslmyrtd/what-the-difference-between-computed-property-and-watcher-d65bcebf37a4)
```
Vue’s reactivity system automatically tracks dependencies for computed properties. This means that if the underlying reactive data changes, the computed property is re-evaluated, ensuring efficiency and avoiding unnecessary recalculations.
```
## defining functions in typescript
* either with {} and return keyword (useful when the function has more the one statement)
```typescript
 const sortedList = computed(() => {
    return [...listItems.value].sort((a, b) => (a.checked? 1:0) - (b.checked? 1:0))
 }
)
```
* or when there are only one statement without {} and no return keyword
```typescript
 const sortedList = computed(() => 
    [...listItems.value].sort((a, b) => (a.checked? 1:0) - (b.checked? 1:0))
)
```