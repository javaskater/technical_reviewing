# Reference
* The Work at [working on Packt Book VueJS For Beginners](../../../Packt_lectures/VUEJS_3_FOR_BEGINNERS/Part1/Chapter1.md)
* And the [official Vuejs Quick Start](https://vuejs.org/guide/quick-start)
# creating a VueJS project
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ npm create vue@latest

> npx
> "create-vue"

┌  Vue.js - The Progressive JavaScript Framework
│
◇  Project name (target directory):
│  jpm_pages_client
│
◇  Select features to include in your project: (↑/↓ to navigate, space to select, a to toggle all, enter to confirm)
│  Router (SPA development), Pinia (state management), Vitest (unit testing), End-to-End Testing, ESLint (error
prevention), Prettier (code formatting)
│
◇  Select an End-to-End testing framework: (↑/↓ to navigate, enter to confirm)
│  Cypress
│
◇  Select experimental features to include in your project: (↑/↓ to navigate, space to select, a to toggle all, enter to
confirm)
│  none
│
◇  Skip all example code and start with a blank Vue project?
│  No

Scaffolding project in /home/jpmena/CONSULTANT/jpm_pages_client...
│
└  Done. Now run:

   cd jpm_pages_client
   npm install
   npm run format
   npm run dev

| Optional: Initialize Git in your project directory with:

   git init && git add -A && git commit -m "initial commit"
```
# The preceding command tells you what to do next
* I called the following command from my home with fiber connection
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client$ npm i

> jpm_pages_client@0.0.0 prepare
> cypress install


Cypress 15.6.0 is installed in /home/jpmena/.cache/Cypress/15.6.0

Skipping installation:

  Pass the --force option if you''d like to reinstall anyway.

added 572 packages, and audited 573 packages in 21s

145 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client$ ll node_modules | wc -l
418
```
## Testing and saving the new project
* The intructions are at the output of the first command
## running locally
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client$ npm run dev

> jpm_pages_client@0.0.0 dev
> vite


  VITE v7.2.2  ready in 460 ms

  ➜  Local:   http://localhost:5173/ # the demo page
  ➜  Network: use --host to expose
  ➜  Vue DevTools: Open http://localhost:5173/__devtools__/ as a separate window # very interesting link
  ➜  Vue DevTools: Press Alt(⌥)+Shift(⇧)+D in App to toggle the Vue DevTools
  ➜  press h + enter to show help
```
* http://localhost:5173/ on the Windows side opens the demo page (Vite+Vue3)
  * note http://localhost:5173/__devtools__/ to have a kind of Vue Console
## Saving the project
* command given above
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git init && git add -A && git commit -m "initial commit of client"
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/jpmena/CONSULTANT/jpm_pages_client_vuejs/.git/
[master (root-commit) be6ecf0] initial commit of client
 38 files changed, 9327 insertions(+)
 create mode 100644 .editorconfig
 create mode 100644 .gitattributes
 create mode 100644 .gitignore
 create mode 100644 .prettierrc.json
 create mode 100644 .vscode/extensions.json
 create mode 100644 README.md
 create mode 100644 cypress.config.js
 create mode 100644 cypress/e2e/example.cy.js
 create mode 100644 cypress/fixtures/example.json
 create mode 100644 cypress/jsconfig.json
 create mode 100644 cypress/support/commands.js
 create mode 100644 cypress/support/e2e.js
 create mode 100644 eslint.config.js
 create mode 100644 index.html
 create mode 100644 jsconfig.json
 create mode 100644 package-lock.json
 create mode 100644 package.json
 create mode 100644 public/favicon.ico
 create mode 100644 src/App.vue
 create mode 100644 src/assets/base.css
 create mode 100644 src/assets/logo.svg
 create mode 100644 src/assets/main.css
 create mode 100644 src/components/HelloWorld.vue
 create mode 100644 src/components/TheWelcome.vue
 create mode 100644 src/components/WelcomeItem.vue
 create mode 100644 src/components/__tests__/HelloWorld.spec.js
 create mode 100644 src/components/icons/IconCommunity.vue
 create mode 100644 src/components/icons/IconDocumentation.vue
 create mode 100644 src/components/icons/IconEcosystem.vue
 create mode 100644 src/components/icons/IconSupport.vue
 create mode 100644 src/components/icons/IconTooling.vue
 create mode 100644 src/main.js
 create mode 100644 src/router/index.js
 create mode 100644 src/stores/counter.js
 create mode 100644 src/views/AboutView.vue
 create mode 100644 src/views/HomeView.vue
 create mode 100644 vite.config.js
 create mode 100644 vitest.config.js
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git config --global init.defaultBranch main # for future gi init
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git branch
* master
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git branch -m master main # after this git init
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git branch
* main
```
* Going to my GitHubAccout and creating an empty [**jpm_pages_client_vuejs** project](https://github.com/javaskater/jpm_pages_client_vuejs) and then
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git remote add origin git@github.com:javaskater/jpm_pages_client_vuejs.git
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ git push -u origin main
Enumerating objects: 54, done.
Counting objects: 100% (54/54), done.
Delta compression using up to 8 threads
Compressing objects: 100% (46/46), done.
Writing objects: 100% (54/54), 83.36 KiB | 10.42 MiB/s, done.
Total 54 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:javaskater/jpm_pages_client_vuejs.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```
# Note to go to production 
*  see also [official Vuejs Quick Start](https://vuejs.org/guide/quick-start)
* **npm run build**