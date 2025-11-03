# 178 Technical requirement
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap10
Clonage dans 'chap10'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 6.61 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap10
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap10$ git switch CH10
La branche 'CH10' est paramétrée pour suivre la branche distante 'CH10' depuis 'origin'.
Basculement sur la nouvelle branche 'CH10'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap10$ npm i

added 444 packages, and audited 445 packages in 7s

105 packages are looking for funding
  run `npm fund` for details

10 vulnerabilities (5 moderate, 5 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
```
## use router in src/main.js
* The file *src/main.js* contains:
```javascript
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router' // The router plugin is defined in src/router/index.js

const app = createApp(App) //The app

app.use(createPinia())
app.use(router) //We have to declare that we use the router plugin

app.mount('#app')
```
# 181
* Organisation of our components
  * *Components that are used as routes are stored in a folder called views*
* after having imported StaticTemplate Vetur helps you (autocompletion):
  * to include Statictemplate in your view template
  * to select the right slot when you start with # in you template (insdide the StaticTemplate)  
# 182
* The name of a route is used (name value of privacy in our case) for future programmatic
navigation
# 184
* <a> is fully reloading the page when navigating which is again the philosphy of a SPA application
* so we use <router-link>
* note that the router-link is translated (Firefox Webtools)
```html
<a data-v-efb3f202="" href="/about" class="">About</a>
```
* note that in the template *router-link* is in Kebab Case
  * and in the script section it is imported in Camel Case 
* note that router-link accepts the path of a route and not the name of a route !!!
# 185
* same thing with event handling *router.push("privacy");* expects a path not the name of a route
# 188
* It is not clear in the Book but we are creating a [UserProfileView.vue](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH10-end/src/views/UserProfileView.vue)
  * passing to the route a hard encoded userId of *657a3106698992f50c0a5885*
*  passing the corresponding CURL command: see/pass the curl commands in [Chapter 7 of Part 2](../Part2/Chapter7.md)
  *  problem there must be a **mistake in the book** as there is no data key (for the posts there was a parent data key)
```bash
jmena01@M077-1840900:~$ curl --header "app-id: 657a3106698992f50c0a5885" https://dummyapi.io/data/v1/user/60d0fe4f5311236168a109ca
{"id":"60d0fe4f5311236168a109ca","title":"ms","firstName":"Sara","lastName":"Andersen","picture":"https://randomuser.me/api/portraits/women/58.jpg","gender":"female","email":"sara.andersen@example.com","dateOfBirth":"1996-04-30T19:26:49.610Z","phone":"92694011","location":{"street":"9614, SÃ¸ndermarksvej","city":"Kongsvinger","state":"Nordjylland","country":"Denmark","timezone":"-9:00"},"registerDate":"2021-06-21T21:02:07.374Z","updatedDate":"2021-06-21T21:02:07.374Z"}
```
* Personnaly I made a big mistake
* I wrote
```html
<script scoped>
  <!-- instead of-->
<script setup>
```
* The variable where not seen!!!
* to check what is given
```javascript
const fetchUser = (userId) => {
    const url = `https://dummyapi.io/data/v1/user/${userId}`;
    fetch(url, {
        "headers":{
            "app-id": "657a3106698992f50c0a5885"
        }
    }).then( response => response.json())
    .then( result => {
        console.debug(result);
        Object.assign(user, result);
        console.log(`[UserProfile] user with title ${user.title} firstname: ${user.firstName}`);
    })
}
```
# 192
* from the emitter (the component/View the redirect to a different Vue) you use *useRouter* to push (go) to the Routed View/
  * here the emitter is *src/components/molecules/SocialPost.vue*
  * here we push navigation, but we could also
    * trigger events before and after redirect
    * dynamically add reoutes
* from the component/Vues that is called for you use useRoute to get the route's parameters
  * here the component called for is *src/views/UserProfileView.vue*
* userRouter is verry practical to use routes by name and not by url
## Second mistake
* as userID we pass to the UserProfileView url the postId
  * I get the following object as *result*
```javascript
{
  "error": "RESOURCE_NOT_FOUND"
}
``` 
I added userId in the template of **src/components/organisms/SocialPosts.vue** with:
```html
<template>
  <SocialPost
    v-for="(post, index) in posts"
    :username="post.owner.firstName"
    :userId="post.owner.id"
    :id="post.id"
    :avatarSrc="post.image"
    :post="post.text"
    :likes="post.likes"
    :key="post.id"
    @delete="onDelete(index)"
  ></SocialPost>
</template>
```
* And in **src/components/molecules/SocialPost.vue** I replaced id by userId
```javascript
const props = defineProps({
  username: String,
  userId: String, //new prop filled by the SocialPosts parent component
  id: String,
  avatarSrc: String,
  post: String,
  likes: Number
});

const router = useRouter();
const navigateToUser = () => {
  router.push({
    name:"user",
    params: {
      userId: props.userId //and no more props.id
    }
  });
}
```
## For errors p 188 and p 192, I created [an issue on the gitHub project](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/issues/5)
# 197-198
* note that a route child has the same format than a main route, there are 3 keys: *name*, *path*, *component*.
  * the *src/router/index.js* says
```javascript
routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about', //main route
      name: 'about',
      component: AboutView
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: PrivacyView
    },
    {
      path:"/user/:userId",
      name: "user",
      redirect: {name: "user-profile"}, // for a redirect we have to say how we access the route here by route-name
      children: [
        {
          path: "profile", //nested or child route same path, name, component keyys
          name: "user-profile",
          component: UserProfileView
        },
        {
          path: "post",
          name: "user-posts",
          component: UserPostsView
        }
      ]
    }
  ]
```
* !!! be careful, only the children paths do no start with /
## 198
* the redirect could be a complex object with params like in *src/components/molecules/SocialPost.vue*
```javascript
const navigateToUser = () => {
  router.push({ //complex object with params
    name:"user",
    params: {
      userId: props.userId
    }
  });
```
## aliases
* There are pathes so if
  * parent paths: they have to start with /
  * children paths: they start without /
# 199 Summary
## More
* I want that the two children routes point to Vue with template like *src/views/PrivacyView.vue*
* I chages the template of *src/views/UserProfileView.vue* for:
```html
<template>
    <StaticTemplate>
        <template #heading>
            User Profile Page for {{ user.firstName }}
        </template>
        <template #default>
            <section>
                <h2>User Information</h2>
                <template v-for="key in valuesToDisplay">
                    <label v-if="user[key]">
                        {{ key }}
                        <input type="text"
                            disabled
                            :value="user[key]" />
                    </label>
                </template>
            </section>
        </template>
    </StaticTemplate>
</template>
```
* Of course in the Javascript you have import **StaticTemplate**
* From the *src/views/UserPostsView.vue* I want to go back to the *src/views/UserProfileView.vue*
  * see [passing parameters to a router-link](https://v3.router.vuejs.org/api/#router-link-props)
* so we have in the template of the *src/views/UserPostsView.vue*:
```html
<template>
  <StaticTemplate>
      <template #heading>
          Page of the posts for User of ID <router-link :to="{ name: 'user-profile'}">{{userId}}</router-link>
      </template>
      <template #default>
        <SocialPost
          v-for="(post, index) in posts"
          :username="post.owner.firstName"
          :userId="post.owner.id"
          :id="post.id"
          :avatarSrc="post.image"
          :post="post.text"
          :likes="post.likes"
          :key="post.id"
          @delete="onDelete(index)"
        ></SocialPost>
    </template>
  </StaticTemplate>
</template>
```
* we don't need the params part because it is already in the parent URL 
* see in the Script part
```javascript
const userId = route.params.userId //It is aliready here throught the parent route
```
* repeat: in *src/router/index.js* we have:
```javascript
{
  path:"/user/:userId",
  name: "user",
  redirect: {name: "user-posts"},
  children: [
    {
      path: "profile",
      name: "user-profile",
      component: UserProfileView
    },
    {
      path: "posts",
      name: "user-posts",
      component: UserPostsView
    }
  ]
}
```
* the profile subroute has the same **route.params.userId** value
## Whe could give a param value
* see [router-link page](https://v3.router.vuejs.org/api/#router-link-props)
```html
<!-- named route -->
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
>