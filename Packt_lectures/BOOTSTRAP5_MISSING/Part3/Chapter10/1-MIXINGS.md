# MIXINS
- [The source Code of Chapter 10 is divided in two parts](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-3/chapter-10)
# 258
- the backdrop, is the background page behind the modal, when the modal is on
# 259
- The global options are at p 61 and on [the lines 337 to 352](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/bootstrap/scss/_variables.scss)
# 261
- reactivation od the sass compiler
  - using the [Dart Sass command line interface](https://sass-lang.com/documentation/cli/dart-sass/)
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/mixins/responsive-grid-system$ npm i sass --save-dev

added 12 packages in 1s

5 packages are looking for funding
  run `npm fund` for details
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/mixins/responsive-grid-system$ ./node_modules/.bin/sass scss/style.scss css/style.css
```
# Calculation of the gutter-width
- for the container *mixins/_container.scss*
```scss

```
- When 
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/bootstrap/scss$ grep -rin \$container-padding-x .
./_variables.scss:472:$container-padding-x: $grid-gutter-width !default; # $grid-gutter-width default 1.5
./_variables.scss:1368:$toast-spacing:                     $container-padding-x !default;
./mixins/_container.scss:3:@mixin make-container($gutter: $container-padding-x) { # if not specified 1.5
```