# 274 Sass functions
* To know where the css style comes from
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/functions$ npm i sass --save-dev

added 12 packages in 286ms

5 packages are looking for funding
  run `npm fund` for details
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/functions$ ./node_modules/.bin/sass scss/style.scss css/style.css 
Deprecation Warning [import]: Sass @import rules are deprecated and will be removed in Dart Sass 3.0.0.
# lots of warnings
```
# 278 color-contrast
* [color-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color) is a pure CSS function
  * not a sass function
* it is very used in our bootstrap sources
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/bootstrap/scss$ grep -rin color-contrast .
# lots of results
```