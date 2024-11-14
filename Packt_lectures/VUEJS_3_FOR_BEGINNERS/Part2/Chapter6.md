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
## Properties
* working on the *chap06/src/components/atoms/TheButton.vue*
* *NOTICE* difference between book's button style and [GitHub 's code of the Chapter 6's solution](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH06-end/src/components/atoms/TheButton.vue)
  * I mix the *size* prop, with the button width *v-binded* parameter 
* The props are by default reactive [props reactivity challenge](https://dev.to/richardevcom/destructuring-vuejs-props-the-reactivity-challenge-5h1i)
* *defineProps(* without *props=defineProps(* makes directly access to the properties in the child component. 
## Native events
* *v-on:change* equals *@change*
* *v-on:click* equals *@click*
# 103
* note the name of the click event associated function name *onWhatTheEventProvokesEvent*
  * it is a Vue Method
# 105
* the figure 6.4 shows the communication from Child Component back to Parent Component
# 106
* defineEmits has two purposes
  * returns a function that can be used to emit events
  * defines (through th call parameters) the custom event names we may emit 
# 107
* I experiment passing parameters to the custom Event
* on the <SocialPost> side
```javascript
const emit = defineEmits(['detruire'])
const onDeleteClick = () => {
  console.log("[SocialPost] On Delete...");
  emit('detruire', props.userId);
}
```
* on the <SocialPosts> side
```html
<template>
  <SocialPost
    v-for="post in posts"
    :username="post.username"
    :userId="post.userId"
    :avatarSrc="post.avatar"
    :post="post.post"
    :comments="post.comments"
    :likes="post.likes"
    :retweets="post.retweets"
    :key="post.userId"
    @detruire="onDelete" <!--Custom detruire event emited from the SocialPost (with no s)-->
  ></SocialPost>
</template>
```
```javascript
const onDelete = (parameter) => {
    posts.splice(0,1);
    console.log(`[SocialPosts] we received the parameter ${parameter}`);
}
```
# 108
* here we do a different choice passing the index on the SocialPosts onFunction
* We don't need to pass a value (through emit) from the SocialPost to socialPosts 
* we transmit the event with no parameter (the first element has always the 0 index because of the reactivity from the posts array)
* * If we pass a index parameter the function does not expect another orgument (the emit's argument)
## To still get the best of the two
* On the SocialPost site (child component)
  * we emit the userIfd with the special evnt *detruire*
```html
<div class="header">
  <img class="avatar" :src="avatarSrc" />
  <div class="name">{{ username }}</div>
  <div class="userId">{{ userId }}</div>
  <IconDelete @click="onDeleteClick" />
</div>
```
```javascript
const emit = defineEmits(['detruire'])
const onDeleteClick = () => {
  console.log("[SocialPost] On Delete...");
  emit('detruire', props.userId); //We add the userId to the event
}
```
* On the SocialPosts site (parent component)
  * We use the special parameter event
```html
<template>
  <SocialPost
    v-for="(post, index) in posts"
    :username="post.username"
    :userId="post.userId"
    :avatarSrc="post.avatar"
    :post="post.post"
    :comments="post.comments"
    :likes="post.likes"
    :retweets="post.retweets"
    :key="post.userId"
    @detruire="onDelete($event, index)"
  ></SocialPost>
</template>
```
```javascript
  const onDelete = (event, postIndex) => {
    posts.splice(postIndex,1);
    console.log(`[SocialPosts] we delete the ${postIndex +1}th element from the list with argument ${event}`);
  }
```