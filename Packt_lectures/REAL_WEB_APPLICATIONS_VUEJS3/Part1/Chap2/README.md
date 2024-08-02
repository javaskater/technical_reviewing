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