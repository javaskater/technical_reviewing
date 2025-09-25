# Back to the book
## Compiling Sass [Compiling Sass in Chapter 2](../Chapter2/3-SASS_Compiling.md)
* Installing the compiler
```bash
# creating a node project
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/forms/range$ npm init # answer all the question
# installing the compiler
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/forms/range$ npm i --save-dev sass

added 17 packages, and audited 18 packages in 913ms

5 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
## Testing directly
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/forms/range$ ./node_modules/.bin/sass scss/style.scss css/mystyle.css
Deprecation Warning [import]: Sass @import rules are deprecated and will be removed in Dart Sass 3.0.0.
## A lot of deprecation warning
## but it compiles
```
* Adding a command to the *package.json*
```bash
# saving the actual package.json
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/forms/range$ cp -pv package.json package.back_$(date '+%d%m%Y').json
'package.json' -> 'package.back_25092025.json'
# editing it so that
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/forms/range$ diff -u package.back_$(date '+%d%m%Y').json package.json 
--- package.back_25092025.json  2025-09-25 12:27:39.801438945 +0200
+++ package.json        2025-09-25 12:39:16.962344278 +0200
@@ -3,7 +3,8 @@
   "version": "1.0.0",
   "main": "index.js",
   "scripts": {
-    "test": "echo \"Error: no test specified\" && exit 1"
+    "test": "echo \"Error: no test specified\" && exit 1",
+    "sassCompile": "node_modules/.bin/sass"
   },
   "author": "",
   "license": "ISC",
# on teste
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/forms/range$ npm run sassCompile scss/style.scss css/mystyle.css
```

# 119 [RANGE](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/forms/range)
* The variables for the FORM elements 
  * start at 798 (with the buttons) to 1124 (Form validation states)
  * 1423 - 1428 (Form tooltips)  
```scss
$form-range-track-height: 1.5rem;
```
* does no appear in the F12 css (neither in the line-height nor the font-height)