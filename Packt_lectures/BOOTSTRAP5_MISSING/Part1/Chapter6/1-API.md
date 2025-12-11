# 140
* The mixin is the most complicated one of all mixins
# 142
* styles.css contains the only translated utility and no more one...
* the key of $spacers suffixes the name of the map ("Spacing": name translated in lowercase)
* The value of each $spacers element is given to the 2 properties
# 144
* You can do it with a variable
```scss
$font-weights : ( //( and not { for a sass map
  light: 300,
  normal: 400,
  bold: 700
);

$utilities: (
  "Font weight": (
    property: font-weight,
    values: $font-weights
  )
);
```
# 145 class
* without the class key-value pair it translate to
  * The class name comes from the property name suffixed by the value (if a list) or by the key (if a map)
```css
.font-weight-300 {
  font-weight: 300 !important;
}
```
# 147
```css
p[class^="font-weight"] {
	font-weight: var(--bs-fw);
}
.font-weight-700 {
  --bs-fw: 700;
}
```
* the class font-weight-700 only defines a varibale, it does not apply any style
* It is in the style part of index.html that we apply a font-weight property
> sets the font weight using the --bs-fw variable stored together with the various class names.
* A class can define a variable used with the redefinition of the same class afterward
* in that case each class name defines a variable
# 148
* local variables same sa variables but the class name not only defines a variable but also sets a property
```scss
$utilities: (
  "Font weight": (
    property: font-weight, //Defines a css property
    values: 300 400 700,  // values of the css property
    local-vars: (
      font-weight-opacity: 0.5  // Defines a variable to be used in the style part with the same class name
    )
  )
);
```
* Which gives (Firefox inspecttor)
```css
p[class^="font-weight"] {
  opacity: var(--bs-font-weight-opacity); /*uses the corresponding variable*/
}
.font-weight-400 {
  --bs-font-weight-opacity: .5; /*defines a variable*/
  font-weight: 400 !important; /*sets a property*/
}
```
## back to the sass compilation system
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/local-css-variables$ npm i --save-dev sass # --save-dev must be before the package

added 17 packages in 1s

5 packages are looking for funding
  run `npm fund` for details
```
* Testing sass local command
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/local-css-variables$ node_modules/.bin/sass --version
1.94.2 compiled with dart2js 3.10.1
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/local-css-variables$ node_modules/.bin/sass scss/style.scss css/style.css 
Deprecation Warning [import]: Sass @import rules are deprecated and will be removed in Dart Sass 3.0.0.
## A lot of Deprecation Warnings
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/local-css-variables$ ll css/
total 16
drwxr-xr-x 2 jpmena jpmena 4096 Nov 23 17:06 ./
drwxr-xr-x 6 jpmena jpmena 4096 Nov 23 17:04 ../
-rw-r--r-- 1 jpmena jpmena  296 Nov 23 17:06 style.css
-rw-r--r-- 1 jpmena jpmena  189 Nov 23 17:06 style.css.map
```
# 151 Responsive State
```bash
# loading the compiler
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/responsive$ npm i --save-dev sass

added 17 packages in 2s

5 packages are looking for funding
  run `npm fund` for details
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.7.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
npm notice To update run: npm install -g npm@11.7.0
npm notice

# Compiling
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/responsive$ node_modules/.bin/sass scss/style.scss css/style.css
## A lot of deprecation warnings
@return red($value), green($value), blue($value);
   │                                       ^^^^^^^^^^^^
   ╵
    ../../../../bootstrap/scss/_functions.scss 37:39  to-rgb()
    ../../../../bootstrap/scss/_functions.scss 61:36  map-loop()
    ../../../../bootstrap/scss/_maps.scss 6:20        @import
    scss/style.scss 4:9                               root stylesheet

Warning: 139 repetitive deprecation warnings omitted.
Run in verbose mode to see all warnings.
```
* When I start in Phone Screen, only the first chapters change font weight
* When I extend the Firefox windows size, the other chpaters begin to chnage font-weigth because the correspondin class applies (by default the body style applies)
```html
<h3>Breakpoint xxl</h3>
		<p class="font-weight-xxl-300">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rerum blanditiis quod culpa dolorum fugit? Iure eum molestiae repudiandae esse. Consequuntur soluta alias possimus voluptas repudiandae assumenda, voluptate quibusdam laudantium accusantium!</p>
```
* corresponding to that style definition in the css/style.css
  * which exists only when screen width is greater than 1400px
```css
@media (min-width: 1400px) {
  .font-weight-xxl-300 {
    font-weight: 300 !important;
  }
  .font-weight-xxl-400 {
    font-weight: 400 !important;
  }
  .font-weight-xxl-700 {
    font-weight: 700 !important;
  }
}
```
# 152
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/print$ npm i --save-dev sass

added 17 packages in 1s

5 packages are looking for funding
  run `npm fund` for details
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/api-syntax/print$ node_modules/.bin/sass scss/style.scss css/style.css
# A lot of deprecation Warnings
```
* The bold styles only apply when previewing the print version, otherwise all chapters have the same font weight (By default body style)....
