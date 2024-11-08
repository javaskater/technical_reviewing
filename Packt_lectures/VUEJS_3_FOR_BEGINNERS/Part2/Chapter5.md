# 76
## Techical requirments
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap04$ cd .. # We keep Chapter 05
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git chap05 # We add a Chap05 directory
Clonage dans 'chap05'... 
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 4.77 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner$ cd chap05/
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap05$ git switch CH05 #inside chap05 we switch to branch CH05
La branche 'CH05' est paramétrée pour suivre la branche distante 'CH05' depuis 'origin'.
Basculement sur la nouvelle branche 'CH05'
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap05$ npm i # We have to reload all the librairies

added 444 packages, and audited 445 packages in 11s

105 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (5 moderate, 4 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/my_vuejs-3_beginner/chap05$ npm run dev # We restart the local Web Server

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 380 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help

```
# 78
* See the figure 5.1 to get the way we access Ref and Reactive variables
  * and explanation starting at p 79 
# 80
* functions are very practical especially when you want to Log
  * see [embedded expressions in that documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Text_formatting)
  * With the Back Ticks that gives 
  * *\[Component\]\[method\] text of the log*
```javascript
onMounted(() => {
  var nbComments = 0;
  var nbPosts = 0;
  console.log("[TheWelcome][onMounted] Component mounted");
  posts.forEach(post => { //The forEach mehtod has been proposed by Visual Studio Code
    nbComments += post.comments.length;
    nbPosts += 1;
  });
  console.log(`[TheWelcome][onMounted] we have ${nbPosts} posts and a total of ${nbComments} comments`);  
});
``` 
## Computed properties
* there are kind of reactive functions
  * for example *formatting a date*
# 81
* The author uses Dtring interpolation with backticks to create a *fullName* computed value.
# 82
* To add tweets and likes see [The Welcome.vue solution of chapter 5](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH05-end/src/components/TheWelcome.vue)
  * I always have them in [The Welcome.vue I am using at the start of Chapter 5](https://github.com/PacktPublishing/Vue.js-3-for-Beginners/blob/CH05/src/components/TheWelcome.vue) 
* SocialPost does not control the type of its properties (Typescript would do)
  * that I assign comments do :retweets is accpeted
```javascript
const interactions = computed(() => {
  const commentsNb= props.comments.length
  return commentsNb + props.retweets + props.likes
});
onMounted( () => { //computed are like ref. You have to call their .value method
  console.log(`[SocialPost][onMounted] user ${props.username} likes ${props.likes} tweets ${props.retweets} total interactions ${interactions.value}`);
});
```
# 88
## Your turn
```javascript
const welcomeMessage = computed(() => {
    return `Welcome <span>${username.value}</span>` //I can put html code in the computed property (useful when formatting)
});
onMounted(() => {
    console.log(`[TheHeader][onMounted] message ${welcomeMessage.value}`);
});
```
## Methods vs computed properties
* Figure 5.5 has an error the left header should not be <del>*Ref*</del> but **Method**
# 90 computed or method
* In the code sample (the answer) we see a use of fetch (side effect: conect an external API)