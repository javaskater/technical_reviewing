# Créating the environment of a new project
* initializing the project
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide$ mkdir chapter4 && cd chapter4
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ npm init -y
Wrote to /home/jmena01/CONSULTANT/my_bootstrap5_guide/chapter4/package.json:

{
  "name": "chapter4",
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
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ npm i --save-dev sass # the sass compiler

added 18 packages, and audited 19 packages in 2s

6 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ npm i --save bootstrap # the bootstrap source code (in the latest version)

added 2 packages, and audited 21 packages in 1s

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
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ cp -pv package.json package.json.bak$(date '+%d%m%Y')
'package.json' -> 'package.json.bak03032025'
# we add a run entry for the sass compiler that gives
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ diff -u package.json.bak$(date '+%d%m%Y') package.json
--- package.json.bak03032025    2025-03-03 14:46:56.979846861 +0100
+++ package.json        2025-03-03 14:56:14.733832987 +0100
@@ -4,7 +4,8 @@
   "description": "",
   "main": "index.js",
   "scripts": {
-    "test": "echo \"Error: no test specified\" && exit 1"
+    "test": "echo \"Error: no test specified\" && exit 1",
+    "sassc": "node_modules/.bin/sass"
   },
   "keywords": [],
   "author": "",
```
## Compilation test
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ npm run sassc style.scss style.css 2>errorsassc.log

> chapter4@1.0.0 sassc
> node_modules/.bin/sass style.scss style.css
```