# 38
* SassMeister has been replaced by [SASS Playgrounf online](https://sass-lang.com/playground/) 
# 40 
* I started the project in *sass_compilation/index.html* and *sass_compilation/style.scss*
# 42
* contrary to the book I decide to install sass locally
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation$ npm init -y #answers yes to all the questions
Wrote to /home/jmena01/CONSULTANT/my_bootstrap5_guide/sass_compilation/package.json:

{
  "name": "sass_compilation",
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


jjmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation$ npm i --save-dev sass # --save-dev must be before the package

added 18 packages, and audited 19 packages in 956ms

6 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
* Testing sass local command
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation$ node_modules/.bin/sass --version
1.83.4 compiled with dart2js 3.6.1
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation$ node_modules/.bin/sass style.scss style.css # Compiling
```
* the last command creates style.css and style.css.map
## By defining a command in package.json
* Defining the command in *sass_compilation/package.json*
```javascript
{
  "name": "sass_compilation",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "sassCompile": "node_modules/.bin/sass" //The shortcut command
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "sass": "^1.83.4" //It is in dev dependencies
  }
}
```
# 43
* passing the command
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation$ npm run sassCompile style.scss style.css

> sass_compilation@1.0.0 sassCompile
> node_modules/.bin/sass style.scss style.css
```
* accessing with Firefow inspecting the title in index.html we see the css but also the correponding line in the sass file.
  * this is due to the production of style.css.map together with style.css
## Just a small problem
* *npm run sassCompile --version* givees the version of npm not of the sass compiler
# 44 VSCode Extension
* [Live Sass Compiler by Glenn Marks](https://marketplace.visualstudio.com/items?itemName=glenn2223.live-sass)