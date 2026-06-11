# preparing the exercice

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/website$ npm i sass --save-dev
npm notice This endpoint is being retired. Use the bulk advisory endpoint instead. See the following docs for more info: https://api-docs.npmjs.com/#tag/Audit

changed 1 package in 727ms

9 packages are looking for funding
  run `npm fund` for details
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/website$ npm i bootstrap-icons --save
npm notice This endpoint is being retired. Use the bulk advisory endpoint instead. See the following docs for more info: https://api-docs.npmjs.com/#tag/Audit

up to date in 584ms

9 packages are looking for funding
  run `npm fund` for details
```

- the package.json now contains

```javascript
{
  "devDependencies": {
    "sass": "^1.99.0"
  },
  "dependencies": {
    "bootstrap": "^5.3.8",
    "bootstrap-icons": "^1.13.1"
  }
}
```

- now the path to the icons is:

```html
<link
  rel="stylesheet"
  href="node_modules/bootstrap-icons/font/bootstrap-icons.css"
/>
```

- h1 for the jumbotron-heading has the same effect as a div I can avoid it

# 291

## preferring mixins

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/custom-component$ npm i sass --save-dev

added 12 packages in 275ms

5 packages are looking for funding
  run `npm fund` for details
```

## The [Timeline component](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/examples/custom-component/index.html)

- we rewrite the rules, using the variables and functions/mixins
  - to understand, [use the debug utility](https://sass-lang.com/documentation/at-rules/debug/)
- in scss/style.scss I added the debug command

```scss
@each $state, $value in $theme-colors {
  @debug "[theme-colors] doing for state state #{$state} with color value #{$value}"; //line added
  .timeline-item-#{$state} {
    border-color: $value;

    &::before {
      border-color: $value;
    }

    .timeline-time {
      color: $value;
    }
  }
}
```

- when putting the command

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/custom-component$ node_modules/.bin/sass scss/style.scss css/style.css
#######################################################
scss/style.scss:43 Debug: [theme-colors] doing for state state primary with color value #0d6efd
scss/style.scss:43 Debug: [theme-colors] doing for state state secondary with color value #6c757d
scss/style.scss:43 Debug: [theme-colors] doing for state state success with color value #198754
scss/style.scss:43 Debug: [theme-colors] doing for state state info with color value #0dcaf0
scss/style.scss:43 Debug: [theme-colors] doing for state state warning with color value #ffc107
scss/style.scss:43 Debug: [theme-colors] doing for state state danger with color value #dc3545
scss/style.scss:43 Debug: [theme-colors] doing for state state light with color value #f8f9fa
scss/style.scss:43 Debug: [theme-colors] doing for state state dark with color value #212529
Warning: 292 repetitive deprecation warnings omitted.
Run in verbose mode to see all warnings.
```

- with the colors that gives

```html
<h2>Colors</h2>
<ul class="timeline">
  <li class="timeline-item timeline-item-primary">
    <!-- we neeed the base and the color version-->
    <div class="timeline-time">2022</div>
    <p class="timeline-text">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis convallis
      velit quis sapien sollicitudin ultrices.
    </p>
  </li>
</ul>
```

- Firefox / F12 is a great Help ...

## for the breakpoints

```scss
@each $breakpoint in map-keys($grid-breakpoints) {
@include media-breakpoint-up($breakpoint) {
  $infix: breakpoint-infix($breakpoint, $grid-breakpoints);
  @debug "[timeline-breakpoints] breakpoint #{$breakpoint} with infix #{$infix}"; //adding some debug
  .timeline-horizontal#{$infix} {
    display: flex;
    padding-top: 0.6rem;
    overflow-y: scroll;

    .timeline-item {
      border-left: none;
      border-top: $border-width solid $border-color;

      &::before {
        top: -0.6rem;
      }
    }
  }
}
```

- the debug instruction gives

```bash
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint xs with infix
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint sm with infix -sm
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint md with infix -md
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint lg with infix -lg
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint xl with infix -xl
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint xxl with infix -xxl
```

- the correponding html is

```html
<p>Breakpoint xxl and up</p>
<ul class="timeline timeline-horizontal-xxl">
  <li class="timeline-item">
    <div class="timeline-time">2022</div>
    <p class="timeline-text">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis convallis
      velit quis sapien sollicitudin ultrices.
    </p>
  </li>
</ul>
```

# 291

- list-unstyled (bootstrap/scss/mixins/\_lists.scss) is so much used that it is a mixin

# 291-292

- the [position:relative -- see demo](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position) of timeline-item allow the **::before** which is a son timeline-item element to position absolute to the timeline-element
- same with timeline-time the top with the poisition relative allows to offset the top but to keep the element as a block element in the flow
  - position absolute would put the element out of the flow

# 292

- state in $theme-colors are the keys of:

```scss
// scss-docs-start theme-colors-map
$theme-colors: (
  "primary": $primary,
  "secondary": $secondary,
  "success": $success,
  "info": $info,
  "warning": $warning,
  "danger": $danger,
  "light": $light,
  "dark": $dark,
) !default;
```

- li elements have the original and the colored classes

```html
<h2>Colors</h2>
<ul class="timeline">
  <!--the two classes-->
  <li class="timeline-item timeline-item-primary">
    <div class="timeline-time">2022</div>
  </li>
</ul>
```

# page 295

- I time ago already printed on the console what append

```scss
@each $breakpoint in map-keys($grid-breakpoints) {
  @include media-breakpoint-up($breakpoint) {
    $infix: breakpoint-infix($breakpoint, $grid-breakpoints);
    @debug "[timeline-breakpoints] breakpoint |#{$breakpoint}| with infix |#{$infix}|";
    .timeline-horizontal#{$infix} {
      display: flex;
      padding-top: 0.6rem;
      overflow-y: scroll;

      .timeline-item {
        border-left: none;
        border-top: $border-width solid $border-color;

        &::before {
          top: -0.6rem;
        }
      }
    }
  }
}
```

- the result is

```bash
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint |xs| with infix ||
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint |sm| with infix |-sm|
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint |md| with infix |-md|
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint |lg| with infix |-lg|
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint |xl| with infix |-xl|
scss/style.scss:60 Debug: [timeline-breakpoints] breakpoint |xxl| with infix |-xxl|
```

- the **display: flex;** property makes all the li-items place themself horizontally
- for the fonts inspect is a sass function which makes a SASS array into a string !!!
