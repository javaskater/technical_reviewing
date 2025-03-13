# [FONTS/TYPOGRAPHY](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/content/typography)
* The display-i class takes control over the title itself !!!! it does not matter what the tag is h1, h2, p ?
* The customization needs sometimes the variables contained in _variables.scss
* the body-styles makes things softer ...
* The link-style is very interesting especially for link...
* I have to fill the style.scss one line at a time in order to understand what the consequence of every varibale is on the index.html page 
## There are three parts
* one for titles
* one for Display headings
* one for lead paragraphs
## To save works
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter5/scss$ cp -pv style.scss style.scss.bak_$(date '+%d%m%Y')
'style.scss' -> 'style.scss.bak_13032025'
```
# 115 [Images](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/content/images)
* The image path in the html must be relative
* the sass code generates css variables
* $prefix (see F12 on Firefox) is **bs-** (bs for Bootstrap)
```scss
// scss-docs-start thumbnail-variables
$thumbnail-padding:                 .25rem !default;
$thumbnail-bg:                      var(--#{$prefix}body-bg) !default;
$thumbnail-border-width:            var(--#{$prefix}border-width) !default;
$thumbnail-border-color:            var(--#{$prefix}border-color) !default;
$thumbnail-border-radius:           var(--#{$prefix}border-radius) !default;
$thumbnail-box-shadow:              var(--#{$prefix}box-shadow-sm) !default;
```
* The [css variable are defined in the _root.scss](https://getbootstrap.com/docs/5.3/customize/css-variables/)
  * it allows to have the same varibales be it in the light or dark mode...
* There are used in the variables.scss but they will be applied in classes later (after root)
# 117 [Figures](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/content/figures)
* figcaption tag inside figure tag puts the caption text underneath the image and not at its right side
