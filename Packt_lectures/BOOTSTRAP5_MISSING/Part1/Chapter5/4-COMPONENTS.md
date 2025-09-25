# After installing the sass compiler
```bash
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-5/components$ npm run sassCompile breadcrumbs/scss/style.scss breadcrumbs/css/mystyle.css
```
# 122 breadcrumb
* The active class does not seem to have an effect on the display
* It is normal because in eventhough in *bootstrap/scss/_variables.scss* the li color is gray-500
  * but the a color keeps being blue (and it has priority - more specific!!!
# 123 Cards
* The grid layout was very quickly touched in the [Content Pages](./2-CONTENT.md)
  * There where changed to default 16 columns on the page layout grid !!!
```scss
:$grid-columns:                12 !default; //Line 466 of ./scss/_variables.scss
```
## The Layout
* g for gutter
* mb for margin bottom
* *row row-colsxl-3* acts at the *col* level underneath
```css
@media (min-width: 1200px) {
  .row-cols-xl-3 > * {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }
}
```
  * very interesting for my personal WebSite

