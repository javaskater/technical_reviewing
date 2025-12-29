* [Answer 58 to this StackOverflow Post](https://stackoverflow.com/questions/65547199/using-bootstrap-5-with-vue-3)
* [Using Bootstrap in a project and compiling](https://getbootstrap.com/docs/5.3/customize/sass/#compiling)
  * You need to [load bootstrap source using npm](https://www.npmjs.com/package/bootstrap)
## saving the actual files
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs/src$ cp -pv ./main.js main.js_ori$(date '+%d%m%Y')
'./main.js' -> 'main.js_ori29122025'
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs/src$ cp -pv ./App.vue App.vue_ori$(date '+%d%m%Y')
'./App.vue' -> 'App.vue_ori29122025'
```
## Loading the necessay libraries
```bash
# The Bootstrap source
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ npm i bootstrap --save-dev

added 575 packages, and audited 576 packages in 23s

147 packages are looking for funding
  run `npm fund` for details

2 high severity vulnerabilities

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
# The compiler
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ npm i sass --save-dev

added 8 packages, and audited 584 packages in 9s

151 packages are looking for funding
  run `npm fund` for details

2 high severity vulnerabilities

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
```
# First Bootstrap without customization
* creating a *src/assets/boot.scss* file only containing: 
```scss
@import '../../node_modules/bootstrap/scss/bootstrap';
```
## compiling that file see [Sass Compiling in the Packt Boostrap Guide](../../../Packt_lectures/BOOTSTRAP5_MISSING/Part1/Chapter2/3-SASS_Compiling.md)
* one time compiling
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ ./node_modules/.bin/sass ./src/assets/boot.scss ./src/assets/boot.css
Deprecation Warning [import]: Sass @import rules are deprecated and will be removed in Dart Sass 3.0.0.
# lots of deprecations warnings
```
* I now have a very long *src/assets/boot.css*
* I replace the css path with that path inside *src/main.js*
```javascript
//import './assets/main.css' // The file given with the Vue Example
import './assets/boot.css' //Our bootstrap compiled file
```
* It workdbut I don't see the mapping
* following [this Boostrap/sass guide](https://getbootstrap.com/docs/4.3/getting-started/theming/)
* I relocate the scss and the css files, the sompile command becomes
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/jpm_pages_client_vuejs$ ./node_modules/.bin/sass ./scss/boot.scss ./css/boot.css
```
* still des not follow the source map
### perhaps [answer 0 of thei StackOverflow](https://stackoverflow.com/questions/79823513/how-do-i-enable-stylesheet-source-maps-in-dev-mode-for-vuejsvite-3-0)
* it works!!!
* Now **vite.config.js** contains:
```javascript
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  css: {
    devSourcemap: true, // What we added
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
```