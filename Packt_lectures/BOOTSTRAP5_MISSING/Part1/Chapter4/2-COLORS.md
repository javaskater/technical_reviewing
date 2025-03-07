# 77
* all colors variables have the default flag
* that means that their value will be maintained unless the same property has been set before importing *@import variables*
  * see [response 114 of this StackOverflow](https://stackoverflow.com/questions/10643107/what-does-default-in-a-css-property-value-mean)
* [using debug in SASS to check for values](https://sass-lang.com/documentation/at-rules/debug/) 
* I must put it to @warn for the message appears in the Visual Studio Watch console
  * *npm run sassc*  does not output it !!!
* [use of sass maps](https://sass-lang.com/documentation/modules/map/)
* I must declare sass:map before any others instructions
```scss
// Configuration
@use "sass:map"; //before any others instructions
@import "./node_modules/bootstrap/scss/functions";

//Default variable ovverrides
$enable-caret: false;
$enable-rounded: true;
$enable-shadows: false;
$enable-gradients: true;
$enable-reduced-motion: true;
$enable-smooth-scroll: true;
$enable-grid-classes: false;
$enable-cssgrid: false;
$enable-container-classes:true;
$enable-button-pointers: true;
$enable-rfs: true;
$enable-validation-icons: true;
$enable-negative-margins:true;
//$enable-important-utilities: false;
//$spacer: 3rem;


@import "./node_modules/bootstrap/scss/variables";
@import "./node_modules/bootstrap/scss/variables-dark";
@warn "grays of type 200 #{map.get($grays, "200")}"; //use of sass:map and @warn
```
* The use in *root* does not need sepcifically map
```scss
 @each $color, $value in $colors {
    --#{$prefix}#{$color}: #{$value};
  }
```
* I put it in my styles.scss file:
```scss
@each $color, $value in $grays {
    @warn "à la clé #{$color}: correspond la valeur #{$value}";
  }
```