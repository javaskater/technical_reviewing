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
# 149 State (todo)