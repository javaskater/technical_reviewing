# 220
* The new ratio is applied to the Google Map IFrame in the Contact page 
* utilities.scss is placed at the very end of [style.scss](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-2/chapter-8/website/scss/style.scss)
* the bootstrap's utilities is where it is played with the class names
# 222
* in the bootstrap utilities.scss we have, the class is border and is not responsive
```scss
"border-width": (
      property: border-width,
      class: border,
      values: $border-widths
    ),
```
## responsive: true
* We add the reponsive to true to add the breakpoint suffixes to the classes
```scss
"border-end": (
      property: border-right,
      class: border-end, //on ly this property to that class
      values: (
        null: var(--#{$prefix}border-width) var(--#{$prefix}border-style) var(--#{$prefix}border-color),
        0: 0,
      )
    ),
```
* and the corresponding styles are placed underneath the corresponding breakpoint instruction 
```css
@media (min-width: 1440px) {
  .float-xxl-start {
    float: left !important;
  }
  .float-xxl-end {
    float: right !important;
  }
  .float-xxl-none {
    float: none !important;
```
# 224 
* [currentcolor is a css keyword, not specific to Bootstrap](https://www.w3schools.com/colors/colors_currentcolor.asp)
* offcanvas is applied to a button which appears only when we are less than lg
```html
 <div class="d-flex justify-content-end mb-3">
        <button type="button" class="btn btn-secondary me-auto d-lg-none" data-bs-toggle="offcanvas" data-bs-target="#offcanvasFilters" aria-controls="offcanvasFilters">Filter</button>
```
