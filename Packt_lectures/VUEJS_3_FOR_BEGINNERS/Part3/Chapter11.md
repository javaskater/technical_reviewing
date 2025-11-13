# 202
## Technical requirements
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git ch11
Clonage dans 'ch11'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 2.45 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd ch11
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch11$ git switch CH11
Déjà sur 'CH11'
Votre branche est à jour avec 'origin/CH11'.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch11$ npm i

added 444 packages, and audited 445 packages in 9s

105 packages are looking for funding
  run `npm fund` for details

11 vulnerabilities (1 low, 5 moderate, 5 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/ch11$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 373 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# 206
* *src/stores/counter.js* is created by the VueCli as an example of a Store
  * it is the one described in the [official documentation](https://pinia.vuejs.org/core-concepts/)
* the name proertie is only a storeId used by VueDevTools
  * if you want to use it use [the exported variable after having imported the js file](https://pinia.vuejs.org/core-concepts/#Using-the-store) 
# 207
* you can declare the store content (properites/state, computed/getters, methods/actions)
  * either using the Option API (the book use the OptionAPI) and the [Option Stores in the official documentation](https://pinia.vuejs.org/core-concepts/#Option-Stores)
  * state here is the same as defineState in the OptionAPI used for components
  * either using the composition API [Setting up the Store in the official documentation](https://pinia.vuejs.org/core-concepts/#Setup-Stores)
* I prefer the [Option API setting up the store](https://pinia.vuejs.org/core-concepts/#Option-Stores)
  * inside the store a state element can be accessed using **this** 
* *useCounterStore* is the name of the exported function... we call using the parentheses *const counter = useCounterStore()* (after having imported it)  
  * the getter are *computed properties* there are called without () parentheses like the state objects
# 209
* to define the SidebarStore we use the Option API
* state is a [javascript anonymous functions](https://www.javascripttutorial.net/javascript-anonymous-functions/)
```javascript
state: () => ({}),
```
* for the second term you can use () or not:
```javascript
> let add = (a, b) => a+b;
undefined
> add(2,3)
5
> let add2 = (a, b) => (a+b);
undefined
> add2(3,4)
7
```
# 210
* we have left the getters/computed empty for that first part
* ===  hase priority over the =
```javascript
> a = true
true
> b = true
true
> b = a === false
false
> b
false
> 
```
* so
```javascript
this.closed = closed === 'true' //is a way to translate from the string 'true' or 'false' to the boolean true or false
```
## to use the store, first use it in the component it is foreseen for, here SideBar.vue
* replace method with actions
* replace redf with state! 
# 211
* onBeforeMount, the last line should no be striked through so that we have [see also the solution on GitHub](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH11-end/src/components/organisms/SideBar.vue)
```javascript
onBeforeMount( async () => {
    sidebarStore.loadSidebarFroLocalStorage();
});
```
# 212
* Be careful when the sideBar is closed not only
  * we do put its width to 40px through aside's class binding
  * but also we change its content through <template v-if and <template v-else 
* in the store replace all closed.value with this.closed
  * the console.log and the F12 warnings help to undestand where the problem is 
# 213
```html
<IconFullScreen class="icon" @click="sidebarStore.toggleSidebar" />
```
* is enough to let drive the sidebar from the Header. the book says
> All instances of the store will work as one, allowing us to use and modify states from different parts of the application.
# 214
* a getter is a function with the state parameter as the first parameter (the only mandatory)
* it is supposed not to produce any side effect like calling an API or logging
* but if state.closed changes friendly will change (see computed properties)
# 215
* With the managment of Posts inside a Pinia store (including fetching posts from the API) 
  * we approach what is done inside the company I work for 
 # 216
* all methods related to the post array are in *src/components/organisms/SocialPosts.vue*
  * this is where we fetch posts 
  * *src/components/molecules/SocialPost.vue* uses only one postData comming from the previous component 
* the Stores Fetch post is meant to work 
  * for the fetchData in onMount
  * for the fetchData in watch (when there are less that 4 post call the next page of posts) 
* the [posts store in the solution on gitHub](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH11-end/src/stores/posts.js)
# 218
* we played with destructuration to avoid the use of usePostsStore
```javascript
  const postsStore = usePostsStore();
  const { posts } = storeToRefs(postsStore); //posts is now a ref value and no more a reactive (post.value is reactive)
  const {fetchPosts, removePost} = postsStore;
```
# 219
* We are now adding a post as a Pinia store is a good place to store it without event bubbling and props drilling
* [unshift (offcial doc)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) adds to the beginning of an array
```javascript
> const a1 = [1,2,3];
undefined
> a1.unshift(4,5,6)
6
> a1
[ 4, 5, 6, 1, 2, 3 ]
```
* The function *generatePostStructure* is lef to the user see [solution on GitHub](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH11-end/src/stores/posts.js)
# 220
* the first value is to get the content of a [ref element](https://blog.logrocket.com/understanding-vue-refs/). We access the textArea element reactive properties
* and the second value is to get the text content of the textArea, like we would do with an HTML5 INPUT 
```javascript
const createPostHandler = (event) => {
    event.preventDefault();
    if(createPostForm.value.reportValidity()){
        addPost(textareaRef.value.value);
    };
}
```
# TODO create your own store element to toggle from the sideBar the Visibility orf the CreatePost part
* Nothing in [the solution part of Chapter 11](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/tree/CH11-end)
## the store *src/stores/create.js*
```javascript
import { defineStore } from "pinia";

export const useCreatePostStateStore = defineStore('createPost',{
    state: () => ({closed:true}),
    getters: {
        friendlyState(state){
            return state.closed? "closed":"open";
        },
    },
    actions: {
        toggleCreatePost() { //call that function when you push the button in order to store the data in windows'storage
            this.closed = !this.closed;
            localStorage.setItem("createPost", this.closed);
        },
        loadCreatePostFromLocalStorage() { //To be called before the HomeView be mounted
            const closed = localStorage.getItem("createPost"); //It gives us a string 'true' or 'false'
            this.closed = closed === 'true';
            console.log(`[useCreatePostStore][loadCreatePostFromLocalStorage] closed state is now ${this.closed}`);
        }
    }
})
```
## the sideBar Button *src/components/organisms/SideBar.vue*
```html
<template>
    <aside :class="{ 'sidebar__closed': sidebarStore.closed}">
        <template v-if="sidebarStore.closed">
            <IconRightArrow class="sidebar__icon" @click="sidebarStore.toggleSidebar" />
        </template>
        <template v-else>
            <h2>Sidebar</h2>
            <IconLeftArrow class="sidebar__icon" @click="sidebarStore.toggleSidebar" />
            <TheButton>Create post</TheButton>
            <div>
                Current time: {{currentTime}}
            </div>
            <TheButton @click="onUpdateTimeClick">Update Time</TheButton>
            <router-link to="privacy">Privacy</router-link>
            <router-link to="about">About</router-link>
            <a @click="navigateToPrivacy">Programmatic to privacy</a>
            <a @click="toggleCreatePost">Display / Hide the create post's form</a>
        </template>
    </aside>
</template>
<script setup>
import { ref, onBeforeMount } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import TheButton  from '../atoms/TheButton.vue'
import IconLeftArrow from '../icons/IconLeftArrow.vue'
import IconRightArrow from '../icons/IconRightArrow.vue'
import { useSidebarStore } from '../../stores/sidebar';
import { useCreatePostStateStore } from '../../stores/create';
const currentTime = ref(new Date().toLocaleTimeString());
//const closed = ref(false);
const sidebarStore = useSidebarStore();
const createPostState = useCreatePostStateStore();
const router = useRouter();

/*const toggleSidebar = () => {
    closed.value = !closed.value;
    window.localStorage.setItem("sidebar", closed.value);
}*/
const onUpdateTimeClick = () => {
    currentTime.value = new Date().toLocaleTimeString();
};
const navigateToPrivacy = (event) => {
    event.preventDefault();
    console.log("[SideBar.vue][navigateToPrivacy] programmatically go to the privacy page");
    router.push("privacy");
}

const toggleCreatePost = (event) => {
    event.preventDefault();
    createPostState.toggleCreatePost() //don't do just createPostState.clodes = !createPostState.closed as it does not store in Navigators local storage
    console.log(`[SideBar.vue][toggleCreatePost] The State of the createPostform has been set to ${createPostState.friendlyState}`);
}

onBeforeMount( async () => {
    /*const sidebarState = window.localStorage.getItem("sidebar");
    closed.value = sidebarState === "true";*/
    sidebarStore.loadSidebarFromLocalStorage(); //The same logic applied to HomeView makes the same as th content above
});
</script>
<style scoped>
aside {
    display: flex;
    flex-direction: column;
    position: relative;
    &.sidebar__closed{
        width: 40px;
    }
    .sidebar__icon{
        position: absolute;
        right: 12px;
        top: 22px;
        cursor: pointer;
    }
}
</style>
```
## The HomeView *src/views/HomeView.vue*
```html
<script setup>
import SocialPosts from '../components/organisms/SocialPosts.vue'
import CreatePost from '../components/molecules/CreatePost.vue'
import SideBar from '../components/organisms/SideBar.vue'
import TheHeader from '../components/organisms/TheHeader.vue'
import { useCreatePostStateStore } from '../stores/create'
import { storeToRefs } from 'pinia'
import { onBeforeMount } from 'vue'
const createPostState = useCreatePostStateStore();
const { closed } = storeToRefs(createPostState); //closed has to be a reference to the Pinial states closed, not a copy
const { loadCreatePostFromLocalStorage } = useCreatePostStateStore() //The function we export from the Pinia
onBeforeMount( async () => { //same thing as for sideBar.vue
    loadCreatePostFromLocalStorage(); //Get the stored value of clodes and gives it to Pinial in case we reload the entire page which is not what SPA are about
});
</script>

<template>
  <TheHeader/>
  <SideBar />
  <main>
    <template v-if="!closed"> <!--New we use the ref Pinia state-->
      <CreatePost />
    </template>
    <SocialPosts />
  </main>
</template>
<style>
@import '../assets/base.css';
aside { 
  border-right: 1px solid var(--color-border);
  padding: 16px 32px;
}
main {
  padding: 16px 32px;
}
</style>
```
# More on Pinia
* [$reset for gonig back to the default values](https://pinia.vuejs.org/core-concepts/state.html#Resetting-the-state)
* [$patch](https://pinia.vuejs.org/core-concepts/state.html#Replacing-the-state)
  * we cannot change the state by hand