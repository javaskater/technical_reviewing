 # creating a dev env
 # Créating the environment of a new project
* initializing the project
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide$ mkdir chapter5 && cd chapter5
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5$ npm init -y
Wrote to /home/jmena01/CONSULTANT/my_bootstrap5_guide/chapter5/package.json:

{
  "name": "chapter5",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```
* adding a sass compiler (dev) and the bootstrap sources (prod)
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5$ npm i --save-dev sass # the sass compiler

added 18 packages, and audited 19 packages in 2s

6 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5$ npm i --save bootstrap # the bootstrap source code (in the latest version)

added 2 packages, and audited 21 packages in 856ms

8 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
## the installed versions in the package-lock.json
```javascript
"packages": {
    "": {
      "name": "chapter4",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "bootstrap": "^5.3.3" //Bootstrap sources version
       },
      "devDependencies": {
        "sass": "^1.85.1" //sass compiler version
      }
    },
```
## Changing the package.json to access
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5$ cp -pv package.json package.json.bak$(date '+%d%m%Y')
'package.json' -> 'package.json.bak12032025'
# we add a run entry for the sass compiler that gives
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5$ diff -u package.json.bak$(date '+%d%m%Y') package.json
--- package.json.bak12032025	2025-03-12 15:06:52.801530034 +0100
+++ package.json	2025-03-12 15:08:48.165918399 +0100
@@ -4,7 +4,8 @@
   "description": "",
   "main": "index.js",
   "scripts": {
-    "test": "echo \"Error: no test specified\" && exit 1"
+    "test": "echo \"Error: no test specified\" && exit 1",
+    "sassc": "node_modules/.bin/sass" # compile command added to npm
   },
   "keywords": [],
   "author": "",
```
# Compilation test
* Just put in the *scss/style.scss* file
```scss
@import "../node_modules/bootstrap/scss/bootstrap.scss";
/**
* Personal part
*/
.jpm{
    background-color: $info;
}
```
* call the compilation
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5$ npm run sassc scss/style.scss css/styles.css 2>errorssassc.log

> chapter5@1.0.0 sassc
> node_modules/.bin/sass scss/style.scss css/styles.css
```
* and in the *index.html's* body
```html
  <div class="jpm">
    <h1>Bonjour tout le monde!!!</h1>
  </div>
```