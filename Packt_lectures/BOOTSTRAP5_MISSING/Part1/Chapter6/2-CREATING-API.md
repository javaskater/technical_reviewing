# 154 simple utility
* example of different cursor style 
```bash
# compiler instalation
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/examples/add-simple-utility$ npm i sass --save-dev

added 17 packages in 2s

5 packages are looking for funding
  run `npm fund` for details
# compiling
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1/chapter-6/examples/add-simple-utility$ node_modules/.bin/sass scss/style.scss css/style.css
# A lot of deprecation Warnings
```
* in the generated css/style.css file
```css
.cursor-auto {
  cursor: auto !important;
}
```
* The Html uses all the generated cursor classes
```html
<p class="cursor-auto">.cursor-auto</p>
<p class="cursor-context-menu">.cursor-context-menu</p>
```
# 155 complex utility
* in the *css/style.css* 
```css
.o-25 {
  opacity: 0.25 !important;
}

.o-25-hover:hover {
  opacity: 0.25 !important;
}
```
* the opacity 0.25 applies to the p element with the *o-25-hover* class only when it is hovered
  * otherwise th classes of the body class does apply
# 158 Overwrting a utility
* in the *bootstrap/scss/_utilities.scss* file line 164, we have
```scss
"width": (
      property: width,
      class: w,
      values: (
        25: 25%,
        50: 50%,
        75: 75%,
        100: 100%,
        auto: auto
      )
    ),
 ```
 * When we merge with *part-1/chapter-6/examples/overwrite-utility/scss/style.scss*
 ```scss
 // Overwrite sizing utility for width
$utilities: map-merge(
  $utilities,
  (
    "width": (
      property: width,
      class: w,
      values: (
        10: 10%,
        20: 20%,
        30: 30%,
        40: 40%,
        50: 50%,
        60: 60%,
        70: 70%,
        80: 80%,
        90: 90%,
        100: 100%,
        auto: auto
      )
    )
  )
);
 ```
 * merge overwrite the values (it replaces the first ones with the second ones)
   * we now have in css/style.css
```css
.w-10 {
  width: 10% !important;
}

.w-20 {
  width: 20% !important;
}

.w-30 {
  width: 30% !important;
}

.w-40 {
  width: 40% !important;
}

.w-50 {
  width: 50% !important;
}

.w-60 {
  width: 60% !important;
}

.w-70 {
  width: 70% !important;
}

.w-80 {
  width: 80% !important;
}

.w-90 {
  width: 90% !important;
}

.w-100 {
  width: 100% !important;
}

.w-auto {
  width: auto !important;
}
```
* in the index.html we have
```html
<div class="w-10 bg-secondary text-white p-3 mb-2">.w-10</div>
<div class="w-20 bg-secondary text-white p-3 mb-2">.w-20</div>
```
* for the mb class see [Answer 435 of this StackOverflow](https://stackoverflow.com/questions/41574776/what-is-class-mb-0-in-bootstrap-4)

# 160 modifying a utility
* the scss we want to adapt is in *bootstrap/scss/_utilities.scss*
```scss
  "margin-start": (
    responsive: true,
    property: margin-left,
    class: ms,
    values: map-merge($spacers, (auto: auto))
  ),
```
* do I still have ms or only ml in the compiled *css/style.css* ?
* I only have **.ml** (no *.ms* anymore)
```css
.ml-0 {
  margin-left: 0 !important;
}

.ml-1 {
  margin-left: 0.25rem !important;
}

.ml-2 {
  margin-left: 0.5rem !important;
}
```
* The reponsive flag to true makes that we also have
```css
.ml-sm-0 {
  margin-left: 0 !important;
}
.ml-sm-1 {
  margin-left: 0.25rem !important;
}
.ml-sm-2 {
  margin-left: 0.5rem !important;
}
```
# 162 removing an utility
* without removing we have in the css/style.css
```css
.pe-none {
  pointer-events: none !important;
}

.pe-auto {
  pointer-events: auto !important;
}
```
* they don't appear affter activating
```scss
$utilities: map-merge(
  $utilities, (
    "margin-start": map-merge(
      map-get($utilities, "margin-start"),
      ( class: ml ),
    )
  )
);
```