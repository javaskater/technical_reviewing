# Get the code for starting Chapter 7
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap07
Clonage dans 'chap07'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d'objets: 100% (321/321), 171.75 Kio | 9.04 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git branch -a
fatal: ni ceci ni aucun de ses répertoires parents n'est un dépôt git : .git
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap07/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ git switch CH07
La branche 'CH07' est paramétrée pour suivre la branche distante 'CH07' depuis 'origin'.
Basculement sur la nouvelle branche 'CH07'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ npm i

added 444 packages, and audited 445 packages in 11s

105 packages are looking for funding
  run `npm fund` for details

10 vulnerabilities (5 moderate, 5 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 566 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
## Accessing the WebService
* I cannot sigh up for the WEB-Service be it frm work or on My Mobile Device
### Accessing the SocialPosts
* [in the SocialPosts organism for the solution](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH07-end/src/components/organisms/SocialPosts.vue)
* We get the apid
```javascript
const fetchPosts = (page = 0) => {
    const baseUrl = "https://dummyapi.io/data/v1";
    fetch(`${baseUrl}/post?limit=5&page=${page}`, {
      "headers": {
        "app-id": "657a3106698992f50c0a5885"
      }
    })
      .then( response => response.json())
      .then( result => {
        posts.push(...result.data);
      })
  }
```
* I try without the header
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ curl https://dummyapi.io/data/v1/post?limit=5&page=1
[1] 25152
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ {"error":"APP_ID_MISSING"} # The error message is clear
[1]+  Fini                    curl https://dummyapi.io/data/v1/post?limit=5
```
* I try with the header
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ curl --header "app-id: 657a3106698992f50c0a5885" https://dummyapi.io/data/v1/post?limit=5&page=1
[1] 25382 # it is asynchronous
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ {"data":[{"id":"60d21b4667d0d8992e610c85","image":"https://img.dummyapi.io/photo-1564694202779-bc908c327862.jpg","likes":43,"tags":["animal","dog","golden retriever"],"text":"adult Labrador retriever","publishDate":"2020-05-24T14:53:17.598Z","owner":{"id":"60d0fe4f5311236168a109ca","title":"ms","firstName":"Sara","lastName":"Andersen","picture":"https://randomuser.me/api/portraits/women/58.jpg"}},{"id":"60d21b4967d0d8992e610c90","image":"https://img.dummyapi.io/photo-1510414696678-2415ad8474aa.jpg","likes":31,"tags":["snow","ice","mountain"],"text":"ice caves in the wild landscape photo of ice near ...","publishDate":"2020-05-24T07:44:17.738Z","owner":{"id":"60d0fe4f5311236168a10a0b","title":"miss","firstName":"Margarita","lastName":"Vicente","picture":"https://randomuser.me/api/portraits/med/women/5.jpg"}},{"id":"60d21b8667d0d8992e610d3f","image":"https://img.dummyapi.io/photo-1515376721779-7db6951da88d.jpg","likes":16,"tags":["dog","pet","canine"],"text":"@adventure.yuki frozen grass short-coated black do...","publishDate":"2020-05-24T05:44:55.297Z","owner":{"id":"60d0fe4f5311236168a109ed","title":"miss","firstName":"Kayla","lastName":"Bredesen","picture":"https://randomuser.me/api/portraits/med/women/13.jpg"}},{"id":"60d21b3a67d0d8992e610c60","image":"https://img.dummyapi.io/photo-1581804928342-4e3405e39c91.jpg","likes":7,"tags":["canine","pet","mammal"],"text":"Hiking with my dog in the woods. black labrador re...","publishDate":"2020-05-23T22:56:11.424Z","owner":{"id":"60d0fe4f5311236168a109d5","title":"mrs","firstName":"Sibylle","lastName":"Leibold","picture":"https://randomuser.me/api/portraits/med/women/89.jpg"}},{"id":"60d21bf967d0d8992e610e9b","image":"https://img.dummyapi.io/photo-1574457547512-5b1646994eea.jpg","likes":28,"tags":["dog","human","animal"],"text":"Two boys hug their dogs in a leaf pile in the fall...","publishDate":"2020-05-23T18:52:32.613Z","owner":{"id":"60d0fe4f5311236168a109f7","title":"mrs","firstName":"Jolanda","lastName":"Lacroix","picture":"https://randomuser.me/api/portraits/med/women/32.jpg"}}],"total":873,"page":0,"limit":5}
[1]+  Fini                    curl --header "app-id: 657a3106698992f50c0a5885" https://dummyapi.io/data/v1/post?limit=5
```
### Accessing the comments
* We are using the same key [Social Post's Comments in the Chapter 7 solution](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH07-end/src/components/molecules/SocialPostComments.vue)
  * don't confuse the postid with the owner id (see bash result above)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ curl --header "app-id: 657a3106698992f50c0a5885" https://dummyapi.io/data/v1/post/60d21b4967d0d8992e610c90/comment?limit=5
{"data":[],"total":0,"page":0,"limit":5} # I have to test many post'ids to find one with comments
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap07$ curl --header "app-id: 657a3106698992f50c0a5885" https://dummyapi.io/data/v1/post/60d21bf967d0d8992e610e9b/comment?limit=5
{"data":[{"id":"60d2237267d0d8992e6118d7","message":"Handsome shot","owner":{"id":"60d0fe4f5311236168a10a19","title":"miss","firstName":"Debbie","lastName":"Garcia","picture":"https://randomuser.me/api/portraits/med/women/86.jpg"},"post":"60d21bf967d0d8992e610e9b","publishDate":"2019-12-12T18:57:30.941Z"}],"total":1,"page":0,"limit":5}
```
# 113
* the two then pass the result of the first to the second
  * the last is the return statement 
* test of the [spread operator](https://howtodoinjava.com/typescript/spread-operator/) 
```javascript
> posts = [1,2,3]
[ 1, 2, 3 ]
> posts.push(4,5,6)
6
> posts
[ 1, 2, 3, 4, 5, 6 ]
```
* Test of javascript anonymous function. Example of [javascript map function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
```javascript
> const array1 = [1, 4, 9, 16];
undefined
> const map1 = array1.map((x) => x * 2); //The return is not mandatory because it is only one instruction
undefined
> console.log(map1)
[ 2, 8, 18, 32 ]
> const array3 = [1, 4, 9, 16];
undefined
> const map3 = array3.map((x) => {var a = x; return a * 2;}); //without return the result is undefined
undefined
> console.log(map3)
[ 2, 8, 18, 32 ]
```
## posts.push
* result has a data key (see the above curl output). 
  * That has nothing to do with a reactive posts variable...
```javascript
.then( result => {
      posts.push(...result.data);
    })
```
# 114
* I added a then to the fetch to be sure I retrieve the datas
```javascript
const fetchPosts = () => {
    const baseUrl = "https://dummyapi.io/data/v1";
    fetch(`${baseUrl}/post?limit=5`,{
      "headers":{
        "app-id": "657a3106698992f50c0a5885" //see the solution on GitHub to that chanpter 7
      }
    }).then(response => response.json())
    .then( result => {
      posts.push(...result.data);
      return posts; //I return the posts to be pass to the next then
    }).then( postsToShow => {
      postsToShow.forEach(element => { //Just display posts in the console
        console.log(`${element.id} - ${element.image}`);
      });
    })
  }
  ```
  # 116
  * Here the [solution of chapter 7 for the SocialPost molecule component](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH07-end/src/components/molecules/SocialPost.vue) does not take some SocialPost props/computed values
# 117
* does well explain what it does not take from the Chapter 6 solution (Which is the base for chapter 7). That comprises
  * computed property *interactions*
  * comments Atoms (wait or calling the comments for a specific post - see curl outputs above)
# 119
* What is the key *post-id* (kebab case) in the SocialPost (case insensitive) template
  * becomes a *postId* property in the SocialPostComments component. see 119/end
# 120
* fetching comments for a specific post I added a lot of traces
```javascript
const fetchComments = (postId) => {
    const baseUrl = "https://dummyapi.io/data/v1";
    fetch(`${baseUrl}/post/${postId}/comment?limit=5`,{
      "headers":{
        "app-id": "657a3106698992f50c0a5885"
      }
    }).then(response => response.json())
    .then( result => {
      comments.push(...result.data);
      //Object.assign(comments, result.data)
      return comments;
    }).then( commentsToShow => {
      console.log(`[SocialPostcomments] We found ${commentsToShow.length} comments`)
      commentsToShow.forEach(element => {
        console.log(`[SocialPostcomments]+ ${element.id} - ${element.owner.picture}`);
      });
    })
  };
  fetchComments(props.postId);
```
* The remarks/warning in Yellow in the Firefox / Ouput / Console are also important for debugging unattended behaviours 
# 122 
* The template element supports v-if, v-else directives without adding any HTML Tag to he DOM.
*  power of v-for
  * we can either have comment is the entire *{"id":"60d2237267d0d8992e6118d7","message":"Handsome shot","owner":{"id":"60d0fe4f5311236168a10a19","title":"miss","firstName":"Debbie","lastName":"Garcia","picture":"https://randomuser.me/api/portraits/med/women/86.jpg"},"post":"60d21bf967d0d8992e610e9b","publishDate":"2019-12-12T18:57:30.941Z"}]*
```html
<div v-for="(comment, index) in comments" class="comment">
``` 
* or we can extract speific values associated with specidic keys
  * in that case parenthesises () are replaced by curly braces {} it is a kind of destructuration
```html
<div v-for="{message, owner} in comments" class="comment">
```
# 124
* we use both red and reactive variable in the same *SocialPosts* component
  * [that page](https://vuejsdevelopers.com/2022/06/01/ref-vs-reactive/) does well explain the difference between the two
# 125
* Watch; when less than 4 posts are in the SocialPosts Vue, il recalls fetchPosts and the then logs all the posts including the old ones.
* From the console.log, I removed all the warnings by correcting SocialPost.vue
# 127
* await takes a Promise as a parameter that is why fetcComments must return the last then result
# 129
* With the fallback message we have an example of a slot. The [offical link](https://vuejs.org/guide/components/slots) explains that for the client of my Element (parent template of the BaseLayout template) with slots:
```html
<BaseLayout>
  <template v-slot:header>
    <!-- content for the header slot -->
  </template>
</BaseLayout>
```
* is the same than
```html
<BaseLayout>
  <template #header>
    <!-- content for the header slot -->
  </template>
</BaseLayout>
```
* The parent Layout is then
```html
<BaseLayout>
  <template #header>
    <h1>Here might be a page title</h1>
  </template>

  <template #default>
    <p>A paragraph for the main content.</p>
    <p>And another one.</p>
  </template>

  <template #footer>
    <p>Here's some contact info</p>
  </template>
</BaseLayout>
```
* The BaseLayout template
```html
<template>
  <div class="card">
    <div v-if="$slots.header" class="card-header">
      <slot name="header" />
    </div>
    
    <div v-if="$slots.default" class="card-content">
      <slot />
    </div>
    
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer" />
    </div>
  </div>
</template>
```