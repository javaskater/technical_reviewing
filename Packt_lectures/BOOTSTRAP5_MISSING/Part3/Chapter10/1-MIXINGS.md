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