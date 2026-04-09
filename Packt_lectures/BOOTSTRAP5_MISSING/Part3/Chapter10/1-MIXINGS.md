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

- make_row is at [**The-Missing-Bootstrap-5-Guide/bootstrap/scss/mixins/_grid.scss** line 5 and up](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/bootstrap/scss/mixins/_grid.scss)

# 262 
* [The-Missing-Bootstrap-5-Guide/bootstrap/scss/mixins/_breakpoints.scss line 59 up](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/bootstrap/scss/mixins/_breakpoints.scss)
```scss
/ Media of at least the minimum breakpoint width. No query for the smallest breakpoint.
// Makes the @content apply to the given breakpoint and wider.
@mixin media-breakpoint-up($name, $breakpoints: $grid-breakpoints) {
  $min: breakpoint-min($name, $breakpoints);
  @if $min {
    @media (min-width: $min) {
      @content; // sass content inside media-breakpoint-up
    }
  } @else { //min is null or 0 typically for the lowest breakpoint
    @content; // sass content inside media-breakpoint-up
  }
}
```
* earlier in [The-Missing-Bootstrap-5-Guide/bootstrap/scss/_variables.scss line 430](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/bootstrap/scss/_variables.scss)
```scss
// scss-docs-start grid-breakpoints
$grid-breakpoints: (
  xs: 0, //min is 0 for the lowest breakpoint
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
) !default;
```
* use of it in [scss/style.scss](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/examples/mixins/responsive-grid-system/scss/style.scss):
```scss
article {
  @include make-col-ready();
  @include media-breakpoint-up(lg) { //Use of it with @include beacuase it is a mixin
    @include make-col(6); //the @Content (in the mixin definition)
  }
  background-color: greenyellow;
}
```
# 264
- To use [that example](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/examples/mixins/media-queries-for-breakpoints/index.html) I have to locally download the sass compiler
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/mixins/media-queries-for-breakpoints$ npm i sass --save-dev

added 12 packages in 1s

5 packages are looking for funding
  run `npm fund` for details
```
* good idea tho copy the breakpoint expression litteral inside the index.html
```html
<div class="up">@include media-breakpoint-up(lg): Visible on breakpoint sizes lg, xl and xxl</div>
<div class="down">@include media-breakpoint-down(md): Visible on breakpoint sizes xs and sm</div>
<div class="between">@include media-breakpoint-between(md, xl): Visible on breakpoint size md and lg</div>
<div class="only">@include media-breakpoint-only(sm): Visible on breakpoint size sm</div>
```
# 265
* How to truncate a text ?
  * Il it the alliance of *overflow* and nowrap !!!
```css
p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```
# 267
- [Changing light modes inside the example](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/website/index.html)
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/website$ npm i sass --save-dev

added 12 packages in 290ms

5 packages are looking for funding
  run `npm fund` for details
# Bootstrap is already there
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/website$ npm i bootstrap-icons --save

added 1 package in 643ms

9 packages are looking for funding
  run `npm fund` for details
```
## It happens [here The-Missing-Bootstrap-5-Guide/part-3/chapter-10/website/scss/_custom-styles.scss](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/website/scss/_custom-styles.scss)
## Problem (TO SOLVE)
* I don't know how to apply the color Scheme
- I try 
```scss
:root {
  /* light styles here */
  color-scheme: dark;
}
```
- In the scss/style.scss with no success
-  the author pretends the dark mode is already set which is not true
* **The-Missing-Bootstrap-5-Guide/part-3/chapter-10/website/css/darkmode.css** is there where the dark-mode is implemented (but also in the style.css)
  * In that file we have the traditional
```css
@media (prefers-color-scheme: dark) {
  body {
    background-color: var(--bs-dark);
    color: var(--bs-light);
  }
  .bg-light, .jumbotron {
    background-color: var(--bs-dark) !important;
  }
  .bg-dark {
    background-color: var(--bs-gray-700) !important;
  }
  .accordion-button,
  .accordion-item,
  .card,
  .list-group-item {
    background-color: var(--bs-dark);
  }
  .accordion-button,
  .breadcrumb-item.active,
  .figure-caption,
  .list-group-item,
  .navbar-light .navbar-brand,
  .navbar-light .navbar-nav .nav-link {
    color: var(--bs-light);
  }
}
```
## in the [MDN Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
* I made an exemple [an index2 simple file](./files/index2.html)
  * the dark mode works very well
## I Created an issue 
- Issue 1 on the [PacktPublishing GitHub Account of that book](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/issues/1)
# 271
## gradients [Gradient example on this book Github site](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-3/chapter-10/examples/mixins/gradients)
* defined in **mixins/_gradients.scss** in my case the mixin is called with no color which means black (000000) ?
```scss
@mixin gradient-bg($color: null) {
  background-color: $color;

  @if $enable-gradients {
    background-image: var(--#{$prefix}gradient);
  }
}
```

* In fact the null value for background-color is replaced with noththing the instruction does not appear in the generated css
* It is the .bg-dark class that makes the job (black bacground)
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/bootstrap/scss$ egrep -rin '\$gradient' .
./_root.scss:35:  --#{$prefix}gradient: #{$gradient};
./_variables.scss:364:$gradient: linear-gradient(180deg, rgba($white, .15), rgba($white, 0)) !default;
```
* the result in the css/style.css
```css
--bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
/** And later */
.gradient-bg {
  background-image: var(--bs-gradient);
}
```
* .bg-dark (seen previously in the book) défined from **mixins/_utilities.scss** 'line 67 as indicated by Firefox'
  * dand the utilities values in **_utilities.scss** especially
```scss
// scss-docs-start utils-bg-color
    "background-color": (
      property: background-color,
      class: bg,
      local-vars: (
        "bg-opacity": 1
      ),
      values: map-merge(
        $utilities-bg-colors,
        (
          "transparent": transparent
        )
      )
    ),
```
* all gradiant from **mixins/_gradients.scss**
* [The color stop](https://stackoverflow.com/questions/14989851/what-exactly-does-the-stop-color-mean-in-css-gradient) means full purple will be at 50% of the dicv width
```scss
@mixin gradient-x-three-colors($start-color: $blue, $mid-color: $purple, $color-stop: 50%, $end-color: $red) {
  background-image: linear-gradient(to right, $start-color, $mid-color $color-stop, $end-color);
}
```
* **gradient-striped** means that transparent it the .bg-dark, the values are from ... to ...

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
