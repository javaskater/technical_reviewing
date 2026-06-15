# 341-342

## copying from the [Chapter 12/website](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-3/chapter-12/website)

```bash
# for javascript file
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ cp -pv js/script.js ~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/js/
'js/script.js' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/js/script.js'
# for scss templates
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ cp -pv scss/*.scss /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/scss/
'scss/_custom-styles.scss' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/scss/_custom-styles.scss'
'scss/_default-variable-overrides.scss' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/scss/_default-variable-overrides.scss'
'scss/style.scss' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/scss/style.scss'
'scss/_utilities.scss' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/scss/_utilities.scss'
'scss/_variable-value-using-variable.scss' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/src/scss/_variable-value-using-variable.scss'
# The HTML files
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ cp -pv *.html /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template
'about.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/about.html'
'cart.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/cart.html'
'contact.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/contact.html'
'faq.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/faq.html'
'index.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/index.html'
'privacy-policy.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/privacy-policy.html'
'product.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/product.html'
'returns.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/returns.html'
'shipping.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/shipping.html'
'shop.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/shop.html'
'terms-of-service.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/terms-of-service.html'
'wishlist.html' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/wishlist.html'
# we need the images added in the page
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ cp -pvr img /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/
'img' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img'
'img/1000x600.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/1000x600.png'
'img/100x100.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/100x100.png'
'img/1600x900.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/1600x900.png'
'img/160x90.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/160x90.png'
'img/185x104.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/185x104.png'
'img/200x200.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/200x200.png'
'img/30x22.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/30x22.png'
'img/400x300.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/400x300.png'
'img/592x333.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/592x333.png'
'img/800x600.png' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/img/800x600.png'
```

-

## Running the compilation to porduction

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npx mix

● Mix █████████████████████████ building (37%) 1/2 entries 2/3 dependencies 1/2 modules 1 active
 css-loader › postcss-loader › resolve-url-loader › sass-loader › src/scss/style.scss
```

## adding the icons

- the default link to the icons does not work

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npm i bootstrap-icons --save
```

- replacing in the head

```html
<link
  rel="stylesheet"
  href="../../../bootstrap-icons/font/bootstrap-icons.css"
/>
```

- by

```html
<link
  rel="stylesheet"
  href="node_modules/bootstrap-icons/font/bootstrap-icons.css"
/>
```

# 343

```json
{
  "name": "examples",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@popperjs/core": "^2.11.5",
    "bootstrap": "^5.2.0", //it is a dev dependency because it will be compiled in a production ready version
    "bootstrap-icons": "^1.13.1",
    "laravel-mix": "^6.0.49",
    "resolve-url-loader": "^5.0.0",
    "sass": "^1.52.1",
    "sass-loader": "^12.6.0",
    "webpack": "5.93.0"
  }
```

- now that we have bootstrap in the node_modules we change the **part-3/chapter-12/laravel-mix/template/src/scss/style.scss** file accordingly:

```scss
@import "~bootstrap/scss/helpers/ratio"; //after ~ means in the node_modules path (no ~/bootstrap but ~bootstrap)
@import "~bootstrap/scss/helpers/position"; //after
// @import "../../../../bootstrap/scss/helpers/stacks";
@import "../../../../bootstrap/scss/helpers/visually-hidden"; //before
@import "../../../../bootstrap/scss/helpers/stretched-link"; //before
```

- for the Javascript file to work we need to import bootstrap javascript file in the to be compiled file (part-3/chapter-12/laravel-mix/template/src/js/script.js) :

```javascript
import * as bootstrap from "bootstrap"; //The line I added !!! VSCode can go into the imported file CTRL+click on the file

document.addEventListener("DOMContentLoaded", function () {
```

- the generated file (part-3/chapter-12/laravel-mix/template/js/script.js) is now a lot bigger and
- in the index.html file the carousel now runs by itself !!!
