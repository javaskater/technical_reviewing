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
# in the [MDN Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
* I made an exemple [an index2 simple file](./files/index2.html)
  * the dark mode works very well
# I Created an issue 
- Issue 1 on the [PacktPublishing GitHub Account of that book](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/issues/1)