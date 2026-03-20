# The bootstrap.bundle.min/js
* is imported with the bootstrap library
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-9/website$ ll node_modules/bootstrap/dist/js/
total 2480
drwxr-xr-x 2 jpmena jpmena   4096 Jan 31 16:46 ./
drwxr-xr-x 4 jpmena jpmena   4096 Jan 31 16:46 ../
-rw-r--r-- 1 jpmena jpmena 207836 Jan 31 16:46 bootstrap.bundle.js
-rw-r--r-- 1 jpmena jpmena 431870 Jan 31 16:46 bootstrap.bundle.js.map
-rw-r--r-- 1 jpmena jpmena  80496 Jan 31 16:46 bootstrap.bundle.min.js # it is imported by the bootstrap libray
-rw-r--r-- 1 jpmena jpmena 332111 Jan 31 16:46 bootstrap.bundle.min.js.map
-rw-r--r-- 1 jpmena jpmena 135902 Jan 31 16:46 bootstrap.esm.js
-rw-r--r-- 1 jpmena jpmena 297005 Jan 31 16:46 bootstrap.esm.js.map
-rw-r--r-- 1 jpmena jpmena  73811 Jan 31 16:46 bootstrap.esm.min.js
-rw-r--r-- 1 jpmena jpmena 222322 Jan 31 16:46 bootstrap.esm.min.js.map
-rw-r--r-- 1 jpmena jpmena 145474 Jan 31 16:46 bootstrap.js
-rw-r--r-- 1 jpmena jpmena 298167 Jan 31 16:46 bootstrap.js.map
-rw-r--r-- 1 jpmena jpmena  60539 Jan 31 16:46 bootstrap.min.js # the bootstrap library without the Tooltip
-rw-r--r-- 1 jpmena jpmena 220618 Jan 31 16:46 bootstrap.min.js.map
```

# 228
```html
    <div class="toast-container position-fixed end-0 mt-3 me-3">
      <div class="toast js-cartToast" role="status" aria-live="polite" aria-atomic="true"> <!--The part We Show-->
        <div class="toast-header fw-bold">Added to cart</div>
        <div class="toast-body">Product Name was added to the cart.</div>
      </div>
      <div class="toast js-wishlistToast" role="status" aria-live="polite" aria-atomic="true">
        <div class="toast-header fw-bold">Added to wishlist</div>
        <div class="toast-body">Product Name was added to the wishlist.</div>
      </div>
    </div>
```
* The toast calss belong to bootstrap either with *display none* or *opacity 0* 
* the _custom.scss only adds:
```scss
// Add z-index to get the right position along the z-axis
.toast-container {
  z-index: $zindex-fixed;
}
```
* WISHLIST: The removal of the div one level up to the cart containing the remove button does not work !!!!
# 229
* we work in the third Tab of the Cart.html (The icons must be present)
# 230
* [Tooltip takes the text from the title attribute](https://getbootstrap.com/docs/4.0/components/tooltips/)
# 234
- TODO Toast