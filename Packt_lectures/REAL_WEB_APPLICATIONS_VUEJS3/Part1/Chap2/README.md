# 14
* Créate a new project
  * with more questions 
# 15
* I need the solution Code
```bash
jmena01@m077-2281091:~/CONSULTANT/REALVUEJS$ git clone https://github.com/PacktPublishing/Building-Real-world-Web-Applications-with-Vue.js-3.git
Clonage dans 'Building-Real-world-Web-Applications-with-Vue.js-3'...
remote: Enumerating objects: 746, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 746 (delta 36), reused 24 (delta 24), pack-reused 694 (from 2)
Réception d''objets: 100% (746/746), 1.72 Mio | 673.00 Kio/s, fait.
Résolution des deltas: 100% (294/294), fait.
```
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
## I added 2 console.log in the TodoList.vue
```typescript
onst updateItem = (item:Item):void => {
    const updatedItem = findItemInList(item)
    console.log(`[TODOLIST][updateItem] item found ${updatedItem?.title}`) //first console.log
    if (updatedItem){
        toggleItemChecked(updatedItem)
    }
}

const findItemInList = (item: Item): Item | undefined => {
    return listItems.value.find(
        (itemInList: Item) => itemInList.title === item.title
    )
}

const toggleItemChecked = (item:Item): void => {
    item.checked = !item.checked
    console.log(`[TODOLIST][toggleItemChecked] I just chnaged ${item.title} to ${item.checked}`) //second console.log
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
    [...listItems.value].sort((a, b) => (a.checked? 1:0) - (b.checked? 1:0)) //It is a new Array oes not change the organization of he initial Array
)
```
# 25:
* wee will use a [VueJS Lifecycle hook](https://vuejs.org/api/composition-api-lifecycle.html#composition-api-lifecycle-hooks)
* We don't use listItems as the reactive variable why we do need another reactve variable which takes the *listItems* as value 
  * p 25/end  and 26/begins duplication of code
```typescript
import { ref, computed, onMounted } from 'vue';
import type { Ref } from 'vue';
import ListItem from './ListItem.vue';
type Item = {
    title: string,
    checked?: boolean
}
/*const listItems: Ref<Item[]> = ref([
    {title: 'Make a todo list app', checked: true},
    {title: 'Predict the weather', checked: false},
    {title: 'Play some tunes', checked: false},
    {title: 'Let\'s get cooking', checked: false},
    {title: 'Pump some iron', checked:false},
    {title: 'Learn a new language', checked:false},
    {title: 'Publish my work'}
])*/
 const storageItems: Ref<Item[]> = ref([])
 const updateItem = (item: Item): void => {
    const updatedItem = findItemInList(item)
    if (updatedItem){
        toggleItemChecked(updatedItem)
        setToStorage(storageItems.value)
    }
 }
 
 const findItemInList = (item:Item) : Item | undefined => {
    return storageItems.value.find(
        (itemInList:Item) => itemInList.title == item.title
    )
 }

 const toggleItemChecked = (item:Item):void => {
    item.checked = !item.checked
    console.log(`The item ${item.title} has changed its status to ${item.checked?"ON":"OFF"}`)
 }

 const sortedList = computed(() => 
    [...storageItems.value].sort((a, b) => (a.checked? 1:0) - (b.checked? 1:0))
)

const setToStorage = (items:Item[]):void => {
    localStorage.setItem('list-items', JSON.stringify(items))
}

const getFromStorage = ():Item[]|[] => {
    const stored = localStorage.getItem('list-items') // returns a String
    if (stored){
        return JSON.parse(stored)
    }
    return []
}

const initListItems = (): void => {
    if (storageItems.value?.length === 0){ //It simulate getting the Data from a server
        const listItems =[
            {title: 'Make a todo list app', checked: true},
            {title: 'Predict the weather', checked: false},
            {title: 'Play some tunes', checked: false},
            {title: 'Let\'s get cooking', checked: false},
            {title: 'Pump some iron', checked:false},
            {title: 'Learn a new language', checked:false},
            {title: 'Publish my work'}
        ]
        setToStorage(listItems)
        //storageItems.value = listItems //Can work without because onMounted already fills storageItems.value
    }
}
onMounted(() => {
    initListItems()
    storageItems.value = getFromStorage() //Cannot work without because we reload from the updated List storageItems.value
})
```
## Typescript default return
* If you are using the {} you must have an explicit return instruction
```typescript
const sortedList = computed(() => {
        var sortedItems = [...storageItems.value].sort((a,b) => (a.checked ? 1: 0) - (b.checked ? 1: 0))
        return sortedItems
    }
)
```
* otherwise online methods don't need {} and in that case no return instruction
```typescript
const sortedList = computed(() => 
    [...storageItems.value].sort((a,b) => (a.checked ? 1: 0) - (b.checked ? 1: 0))
)
```
# 27
* [VueJsDevTools](https://vuejs.org/guide/scaling-up/tooling.html#browser-devtools) was introduced page 7 
  * I runs on firefox or Chromium
  * *CTRL + SHIFT + I* To Get the DEV ENV of Firefox
  *  watch [the video](https://vueschool.io/lessons/using-vue-dev-tools-with-vuejs-3?friend=vuejs)
  * viewed on my smartphone (the Entreprise Firewall did not allow for the Youtube flow) 