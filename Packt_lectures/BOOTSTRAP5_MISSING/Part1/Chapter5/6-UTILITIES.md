# 129 Borders
* the variable redefines a variable from *bootstrap/scss/_variables.scss*
* and is used in *bootstrap/scss/_utilities.scss*
* We could have defined the variable before *bootstrap/scss/_variables.scss* because in _variables.scss *$border-widths* is marked as !default see [answer 23 to this StackOverflow Post](https://stackoverflow.com/questions/19611240/what-is-the-default-keyword-in-bootstrap-and-foundation-scss-frameworks-used-fo)
* They are defined with *border border-i*
## Remember 
* p stands for padding
* mb stands for margin bottom
# 133 spacing
* by default in _variables.scss we have
```scss
// scss-docs-start spacer-variables-maps
$spacer: 1rem !default;
$spacers: (
  0: 0,
  1: $spacer * .25,
  2: $spacer * .5,
  3: $spacer,
  4: $spacer * 1.5,
  5: $spacer * 3,
) !default;
```
* We change it for:
```scss
// Specify spacer sizes
$spacers: (
  0: 0,
  q: $spacer / 4,
  h: $spacer / 2,
  1: $spacer,
  2: $spacer * 2,
  3: $spacer * 3,
  4: $spacer * 4,
  5: $spacer * 5
);
```
* compilation
```bash
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5$ npm run sassCompile utilities/spacing/scss/style.scss utilities/spacing/css/mystyle.css
```
* it is unsed in the _utilities.scss_ (line 442)
```scss
    "padding-top": (
      responsive: true,
      property: padding-top,
      class: pt,
      values: $spacers
    ),
    "padding-end": (
      responsive: true,
      property: padding-right,
      class: pe,
      values: $spacers
    ),
    "padding-bottom": (
      responsive: true,
      property: padding-bottom,
      class: pb,
      values: $spacers
    ),
    "padding-start": (
      responsive: true,
      property: padding-left,
      class: ps,
      values: $spacers
    ),
```