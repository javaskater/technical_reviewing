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
- Toast the embedding TostContiner is there only to make the embedded Toasts be already at the right position when displayed
# 236
* closest bubble uo until reaching  DOM element with the **card** class
 * it then remove the parent diw which is the container Bootstrap column
```javascript
removeFromWishlistButtons[i].closest('.card').parentElement.remove();
```
# 239
* novalidate is there to replace the defult navigator validationn, by our javascript's validation
## The modal is at the very end of the Page Markup
- just before **</body>**
```html
<div class="modal fade" id="newsletterModal" tabindex="-1" aria-labelledby="newsletterModalTitle" aria-hidden="true">
      <div class="modal-dialog modal-lg modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="newsletterModalTitle">Terms and conditions</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas feugiat, urna ut pharetra ultricies, augue tellus euismod turpis, vitae semper i
              ## A Lot of text
              velit consequat, facilisis leo vitae, volutpat nisi. Nunc hendrerit libero mi. Integer scelerisque mattis neque placerat condimentum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla eu odio mi. Duis interdum vulputate turpis pretium congue.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  ```
  * valid-feedback and invalid-feedback have both the attribute **dispaly:none**
  # 240
  - the ~ is used for sibling here an input with the peudo state of valid and a parapgraph with the valid class
  - [check validity](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checkValidity) class the check validaty of each element
    - for example for the email input we have:
  ```html
   <input type="email" class="form-control" placeholder="mail@example.com" id="email" required>
   ```
   * it checks of a presence of a value and if that value has the form of a valid email
# 243

* it is always interesting to encapsulate th Bootstrap element (here an Alert) in a div
```css
.collapse:not(.show) {
  display: none;
}
```
- when I click on the sumit after a while the class id collapse show.
  - The display None falls
# 244
* it seems that the code
```javascript
const newsletterConfirmationElement = document.querySelector('#newsletterConfirmation');
new bootstrap.Collapse(newsletterConfirmationElement).show();
```
* just adds the show class to the element queried !!! (Taht has already the collapse class)
# 246
```javascript
// Shipping Details form
const shippingForm = document.querySelector('#shippingForm');
shippingForm.addEventListener('submit', function (event) {
  if (!shippingForm.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
  } else {
    event.preventDefault();
    // Go to cart tab 3
    scrollToTop();
    setTimeout(function() {
      const cartTabs3Element = document.querySelector('#cartTabs-3');
      new bootstrap.Tab(cartTabs3Element).show();
      cartProgressBar.classList.remove("w-33");
      cartProgressBar.classList.add("w-67");
      cartProgressBar.ariaValueNow = 67;
    }, 600)
  }
  shippingForm.classList.add('was-validated');
}, false)
```
* [The function passed to setTiemout is exectued after the timeout expires](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)
* [The scroll function is also a pure javascript one](https://developer.mozilla.org/en-US/docs/Web/API/Window/scroll)
  * in our case it is used only in the cartPage
```javascript
 // Only execute the following code on cartPage
  if (cartPage) {

    // Scroll effect for forms
    function scrollToTop() {
      scroll({
        top: 0,
        behavior: "smooth"
      });
    }
```
* to show a specfific Tab
```javascript
const cartTabs2Element = document.querySelector('#cartTabs-2'); //It is the button in the li Tab Header element
new bootstrap.Tab(cartTabs2Element).show(); // makes the button active and the other one inactive  and display the associatd data-bs-target (hides the other ones)
```
* new bootstrap.Tab(cartTabs2Element).show() is a very handy function makes a lot behind the scene ...
# 249
-  in the [chapter-9/website/scss/_utilities.scss](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-2/chapter-9/website/scss/_utilities.scss)
- we define thoses styles w-33 and w-67 very simply
```scss
$utilities: map-merge(
  $utilities,
  (
    "width": (
      property: width,
      responsive: true,
      class: w,
      values: (
        25: 25%,
        33: 33%, //We are using it in the cart.html
        50: 50%,
        67: 67%, //We are using it in the cart.html
        75: 75%,
        100: 100%,
        auto: auto
      )
    )
  )
);
```
- but I don't find any information about the **responsive** css property
# 252
- When we
```javascript
productGalleryImage.src = productGalleryThumbnails[i].dataset.src; // We take the values from data-src HTML attribute
```
- Then we address
```html
<a href="#" class="js-productGalleryThumbnail" data-bs-toggle="modal" data-bs-target="#productGallery" data-src="img/1600x900.png"> <!--We adress the data-src attribute-->
    <img src="img/185x104.png" class="img-thumbnail" alt="Product image">
</a>
```