# 128
## Ratios
**bootstrap/scss/helpers/_ratio.scss** _ means not directly called from the style.css
  * but from **bootstrap/scss/_helpers.scss**
```scss
@each $key, $ratio in $aspect-ratios {
  .ratio-#{$key} {
    --#{$prefix}aspect-ratio: #{$ratio};
  }
}
```
* That is why in scss/style.scss the new map is 
  * between *../../../../bootstrap/scss/functions* for the calc and array-merge functions
  * and *../../../../bootstrap/scss/helpers* for the _ratio.scss classes

* without
```css
.ratio-4x5 {
	--bs-aspect-ratio: 80%;
}
```
* the div has a null width (it is due to the ratio class on the same line)