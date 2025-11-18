# Reference
* The Work at [working on Packt Book VueJS For Beginners](../../../Packt_lectures/VUEJS_3_FOR_BEGINNERS/Part1/Chapter1.md)
* And the [official Vuejs Quick Start](https://vuejs.org/guide/quick-start)
# creating a VueJS project
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT$ npm create vue@latest
Need to install the following packages:
create-vue@3.18.2
Ok to proceed? (y)


> npx
> "create-vue"

┌  Vue.js - The Progressive JavaScript Framework
│
◇  Project name (target directory):
│  jpm_pages_client
│
◇  Select features to include in your project: (↑/↓ to navigate, space to select, a to toggle all, enter to confirm)
│  TypeScript, Router (SPA development), Pinia (state management), Vitest (unit testing), End-to-End Testing, ESLint (error prevention), Prettier (code
formatting)
│
◇  Select an End-to-End testing framework: (↑/↓ to navigate, enter to confirm)
│  Cypress
│
◇  Select experimental features to include in your project: (↑/↓ to navigate, space to select, a to toggle all, enter to confirm)
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
* To continue (I have a slow Internet) npm i takes too much time (it is already full) to call again
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client$ npm i
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client$ ll node_modules/ | wc -l
433 # already 433 libraries downloaded
```