# 103 [Breakpoints](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/layout/breakpoints)
* We see in the F12 console the col-xx-yy acutally active
# 103 [Containers](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/layout/containers)
* We see in the F12 console the container size changing when reducing the Firefox's width
```css
@media (min-width: 576px) {
  .container-sm, .container {
    max-width: 300px;
  }
}
```
* for widths smaller than 576px (typically xs or smartphone in portrait mode)
  * the container takes the full width
```css
.container, .container-fluid, .container-xxl, .container-xl, .container-lg, .container-md, .container-sm {
  --bs-gutter-x: 1.5rem;
  --bs-gutter-y: 0;
  width: 100%;
```
# 105
## [GRID](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-5/layout/grids)
* Still working with F12