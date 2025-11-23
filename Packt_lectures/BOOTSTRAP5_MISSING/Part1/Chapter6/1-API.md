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
# 149 State (todo)