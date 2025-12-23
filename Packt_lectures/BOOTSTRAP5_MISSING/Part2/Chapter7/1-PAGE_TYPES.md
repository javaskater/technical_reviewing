# HERO
* The two element are stacked when below lg
  * we then have a below margin of 1rem (mb-3)
```html
<div class="col-lg-6 mb-3 mb-lg-0">
    <img src="img/800x600.png" class="img-fluid">
</div>
```
# BENEFITS

```html
    <div class="row row-cols-1 row-cols-lg-2 gy-3 gy-md-4 g-lg-5"> <!--Outer grid: First way to define the col width-->
        <div class="col">
            <div class="row align-items-center"> <!-- Inner grid: second and direct col width definition -->
                <div class="col-sm-4 mb-3 mb-sm-0"> 
                    <img src="img/592x333.png" class="img-fluid">
                </div>
                <div class="col-sm-8">
                    <h3>Benefit #1</h3>
                    <p class="mb-0">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis convallis velit quis sapien sollicitudin ultrices.</p>
                </div>
            </div>
        </div>
        <!-- The same pattern repeats for other outer cols -->
    </div>
```
## For outer grid
* The main row defines column grids
  * *row-cols-1* by defaul the col takes all the screen width
  * *row-cols-lg-2* except for large screen where one col takes half of the screen: two cols for a row
* *gy-3* g stays for gutter ...
## The inner grid
* *col-sm-4* the image takes on-third of the outer column width from the small medium up
  * otherwise it takes the entire outer column width
  * then (sm) on small medium and upper there id no margin bottom *mb-sm-0*
    * les than small medium (where the image and the text) stack on eache other there is a mrgin bottom for the image only *mb-3*
# Popular products
* each col takes the whole width until the md breakpoint then takes half of the width until the lg breakpoint then takes one third of the width
* card class helps define a lot of css variables (only for my div and underneath)
```html
<div class="col-md-6 col-xxl-4"> 
    <div class="card h-100">
```
## more on the [Bootstrap Tag](https://getbootstrap.com/docs/5.0/components/card/)
## Tag on the image
```html
<div class="position-relative">
    <img src="img/1600x900.png" alt="Product image" class="card-img-top">
    <div class="badge bg-info position-absolute top-0 end-0 mt-2 me-2">Tag</div>
</div>
```
* the tag is placed on the image, by using a div with abolute position inside a DIV with relative position
* we have two interesting class related to cart
  * cart-body
  * card-footer
# COLLECTIONS
* still on page 178
* It is a tritional Carousel still developped by Bootstrap5 (started long time ago)
  * needs a bit Javascript
## General questions
### backface visibility
* see the [MDN Official documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#values)
  * [The code sample is very interesting](https://developer.mozilla.org/en-US/play?uuid=02ebf697a70c1bda614cf0a65b5803e5f8162701&state=7VRNc9owEP0rO%2B5kBjI4QAikITSX9tpTe0g7XGRrbasRkkdSQmgm%2F70r2YD55pBjyUDW8tvdp9XTe4sKN5PROJo4lkh8mCqAiSuQ8RD6B1NH4cXDJNUcHxKWPmUsxfhFWJEIKdxiDCGWeD%2FpBsykS%2FAzUwvBOao9mRRW%2Ff3aktXEJZov9hLkq5ieuHiBVDJrv0yjVCvHhEIzjRqQbdBzgmALPY%2BTbAu3hfQ7gMxQUcL1J116dxLud07o6%2FPQRuSFLz44Dy4x8%2Bib89BOlwQenslbO6dnhB%2Ft4rdXdp7LDfgPoaggkxJ8ZQvMIJTMOEFLC3CGKUuPqFwH6LjDxGpk67oDNx0YtpvlfHqtOsIb%2FZwXIS8czDKx34FBB0btqybLNS0SFv9YAZGY8b%2BAPk5AP4twurhfD0EElX9cHTjXponUzkFR7XdRJ0qtJQfsXsJXz5qKu4I5mAuSqTcD0CacqZdWKLhDRmdBdtX5TyO47E7VVe0j4Mfx5vOOmuZUvU8VZdXiOZFV%2B2WdRMy%2FYUbaDCxWQvU1qnsUZBmemOLAIEd6LdLAviK7TgpN54K7Ygz9Ya98vfcLBXo1NVdmzORCjeF2WL5Cj%2F58EN4k2nA0Y1BarfcVKGzU7vUuNksvF0o0tsTUiRccw3DVsLEcaxK3b050LsJPQAT%2FyLSZxdYtJCWXBi0awg%2F4ikjYcyDChS0lo2kmUqdPVQ9thROaKrPEavns8H6T8vY4VitbmwaQNM14F5fRoOOMzYSkxpb4xsRQZOt3Vvwl5qMlPtVSU9l5IWouDl9dzKTIiWRKTolmVwbI0gJqy7DIQSvarPGzoyicd%2BWQK4Hl5J2Kj8HkSasXTrMLg95Fe3Os4yqUzOHvlj%2BX9mqq4TLslJNihs1dJJLVg27UNNpRwV%2Bt%2Fucex7x9uEcwtP2c%2B3ejmvXtHtbLDncnGngLPDwT3%2BN4%2FfhUA3LNw%2FyrPRzr8HhyB5XTHpvRqV08ntwFyew7e6q8JpgoGQq5kqNAiZQcxAvMFZ2pKunr%2BDabuBbDJwyfDTNZ3XXGuVA53YMzrk3zRvgjrIiSr%2F%2Fxtk7%2FiekMKZReQNH7Pw%3D%3D&srcPrefix=%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackface-visibility%2F)
### what does border box
```css
*, ::after, ::before {
	box-sizing: border-box;
}
```
* see [MDN Official Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing#values)
  * all the elements dim apply to the Content + Padding + border width (not the margin)
# Popular Products
* still page 178
* The grid is just 3 lg-4 columns in the Bootstrap Grid (nothing to do with de CSS3 Grid)
# NewsLetter
* the 3 inputs are three Bootstrap Cols from the md (medium size) up
  * otherwise the _.row > *_ selector makes them occupy 100% of the available width
```html
<div class="row">
    <div class="col-md-4">
        <div class="mb-3">
        <label for="firstName" class="visually-hidden">First name:</label>
        <input type="text" class="form-control" placeholder="Firstname" id="firstName" required="">
        </div>
    </div>
    <div class="col-md-4">
        <div class="mb-3">
        <label for="lastName" class="visually-hidden">Last name:</label>
        <input type="text" class="form-control" placeholder="Lastname" id="lastName" required="">
        </div>
    </div>
    <div class="col-md-4">
        <div class="mb-3">
        <label for="email" class="visually-hidden">Your email:</label>
        <input type="email" class="form-control" placeholder="mail@example.com" id="email" required="">
        </div>
    </div>
</div>
```
## note opening the modal
```html
<label class="form-check-label" for="terms">Lorem ipsum dolor sit amet, consectetur <a href="#" data-bs-toggle="modal" data-bs-target="#newsletterModal">adipiscing elit</a>.</label>
```
# Modal
* end of Page 178
* the modal itself is a div with id *newsletterModal* it does not work well in Phone mode it has element's style to display:none
  * the Javascript makes it to *display:block*
# Shop
* p 179