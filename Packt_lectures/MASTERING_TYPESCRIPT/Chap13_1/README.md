# 362
# Introduction to Vue / Vue Setup
```bash
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT$ npm i -g @vue/cli
npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and #######################################################################################"" lot of download
added 831 packages in 46s # 831 packages globally

75 packages are looking for funding
  run `npm fund` for details
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT$ vue -V
@vue/cli 5.0.8 #in the book it is the 4.5.9 version
```
# 363
## Créating the Shopping Cart Project
* The first Menu: don't choose a specific Vue version, but choose Manual Component selection
  * the Space bar is there to select individual options
  * The rest is well detailed in the Book 
```bash
mena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT$ vue create shopping-cart
 ERROR  Failed to get response from https://registry.npmjs.org/vue-cli-version-marker


Vue CLI v5.0.8
Failed to check for updates
? Please pick a preset: Manually select features
? Check the features needed for your project: TS
? Choose a version of Vue.js that you want to start the project with 3.x
? Use class-style component syntax? Yes
? Use Babel alongside TypeScript (required for modern mode, auto-detected polyfills, transpiling JSX)? No
? Where do you prefer placing config for Babel, ESLint, etc.? In dedicated config files
? Save this as a preset for future projects? No


Vue CLI v5.0.8
Failed to check for updates
✨  Creating project in /home/jmena01/CONSULTANT/MY_MASTERING_TYPESCRIPT/shopping-cart.
🗃  Initializing git repository...
⚙️  Installing CLI plugins. This might take a while...


added 686 packages, and audited 687 packages in 30s

94 packages are looking for funding
  run `npm fund` for details

4 moderate severity vulnerabilities

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
🚀  Invoking generators...
📦  Installing additional dependencies...


added 16 packages, and audited 703 packages in 4s

95 packages are looking for funding
  run `npm fund` for details

4 moderate severity vulnerabilities

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
⚓  Running completion hooks...

📄  Generating README.md...

🎉  Successfully created project shopping-cart.
👉  Get started with the following commands:

 $ cd shopping-cart
 $ npm run serve
 ```
* Pass the the two commands asked for
```bash
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT$ cd shopping-cart/
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT/shopping-cart$ npm run serve

> shopping-cart@0.1.0 serve
> vue-cli-service serve

 INFO  Starting development server...


 DONE  Compiled successfully in 3646ms                                                                                                                  15:48:46


  App running at:
  - Local:   http://localhost:8080/ 
  - Network: http://10.156.7.60:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.

No issues found.
```
* At *http://localhost:8080/* we have exactly the defaul screen