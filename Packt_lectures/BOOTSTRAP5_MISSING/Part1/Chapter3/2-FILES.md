# separate files
* You have to put _/* comment */_ to find it again in the generated file
```scss
@use "sass:color";
@import "./node_modules/bootstrap/scss/bootstrap";
/*
* fin de bootstrap début de customisation
*/
$color-primary:blue;
h1 {
    color: $color-primary;
    background-color: color.scale($color-primary, $lightness: 75%);
}
```
# 55 variables
* all variables use the **!default** flag
  * this is meant do define the variables before calling the modules that use them
* [use of the !default](https://thoughtbot.com/blog/sass-default) *Optimization* chapter
  * the *base-variable* with all its defaults comes only after the overrides
  * if there is no overides, the default *base-variables* applys 
  * if there is a  client-1-overrides its value applys although it is also defined in *base-variables* aftermath
  * but the !default says: *it is not for you I am already defined default value does not apply*
* In the case of the scss underneath the H1 color is blue
```scss
@use "sass:color";
@import "./node_modules/bootstrap/scss/bootstrap";
/*
* fin de bootstrap début de customisation
*/
$color-primary: blue;
$color-primary:red !default; //It will be red only if there is no previous definition

h1 {
    color: $color-primary;
    background-color: color.scale($color-primary, $lightness: 75%);
}
```
# default null value
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation/node_modules/bootstrap/scss$ grep -Rin "headings-font-style" .
./_reboot.scss:87:  font-style: $headings-font-style;
./_variables.scss:655:$headings-font-style:         null !default;
```
* eventhough the font-style is null by default SASS compiles (différent from the book)
## Way to compile
* in the package.json I have
```javascript
{
  "name": "sass_compilation",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "sassCompile": "node_modules/.bin/sass" //making a npm command from the sass compiler
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "sass": "^1.83.4" //The sass compiler
  },
  "dependencies": {
    "bootstrap": "^5.3.3" // My bootstrap source 
  }
}
```
* That makes in the bash
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/sass_compilation$ npm run sassCompile style.scss 2>&1 | tee compile.log
```