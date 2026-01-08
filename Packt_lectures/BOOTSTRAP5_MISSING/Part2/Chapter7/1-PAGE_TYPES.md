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
## ofcanvas
* the modal (contains the filters when screensize has is greater or equal than lg) has a ofcanvas class that set its position as absolute and its coordinate on the upperleft
## The filters (lg and up)
```html
<div class="col-lg-4 col-xxl-3 d-none d-lg-block"> <!--d-lg-blck with lg appear otherwise d-none disappear-->
          <aside class="sticky-top pt-lg-3 pb-lg-5">
```
* When lower than lg it is not seen/displayed 
  * *d-none d-lg-block*
## sticky 
* makes the sidebar stays at the top/left  see *bootstrap/scss/helpers/_position.scss*
```css
.sticky-top {
	position: -webkit-sticky;
	position: sticky;
	top: 0;
	z-index: 1020;
}
```
## input (form-check) checked
* it is just changing the position of the check which is replaced by a white circle in SVG
# 185
## Review Part of Product
* [the symbol before the review Text is floated](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
```css
.float-start {
	float: left !important;
}
```
## About page
* the figure tag assoicated with the figure-caption is pure hmtl 5. Th corresponding classes do the job !!!
# 186
* Our brands responsive images !!!!
  * the gutter width is given one level up on the row
```html
<div class="col-6 col-sm-4 col-lg-2"><!--Very interesting responsive col widths-->
  <img src="img/400x300.png" class="img-fluid"> <!--adpats to the container-->
</div> 
```
# 189
## Team
* We create a section div just to put a margin bottom of 5
* one row
```html
<div class="row gy-3"> <!--the cols gutter is defined at the row level-->
  <div class="col-6 col-md-4 col-lg-3 col-xl-2 text-center">
    <img src="img/200x200.png" class="img-fluid rounded-circle mb-2" alt="Employee image">
    <ul class="list-inline mb-2">
      <li class="list-inline-item"><a href="#"><i class="bi-twitter"></i><span class="visually-hidden">Twitter</span></a></li>
      <li class="list-inline-item"><a href="#"><i class="bi-linkedin"></i><span class="visually-hidden">LinkedIn</span></a></li>
    </ul>
    <div class="h5">Firstname Lastname</div>
    <div>Job Title</div>
  </div>
```
## Location:
* playing with ratio and 
```css
.ratio::before { /** prepare the needed space in hight for the iFrame */
  display: block;
  padding-top: var(--bs-aspect-ratio);
  content: "";
}
.ratio > * {
  position: absolute; /** The IFrame has an absolute position in a empty space */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```
## Contact Form
* It is also a section (with a margin bottom)
* The for elements themselves are in col of a row which is itself in a col of a row
* note the two Bootstrap classes
  * form-label
  * and the more important form-control
* The two button are freely placed under the main row (no need of a div to encapsulate them)
# 192
## Whishlist
### SideBar
* the sticky class of the aside tag allows the side to remain always present at the top of the current windows
  * especially useful when the page is scrolled down
* the nav only gives an aria-label: used by screen readers for impaired peoples
* underneath there is a [Card using list groups](https://getbootstrap.com/docs/5.0/components/card/#list-groups)
### Main area
* The 6 product images are in one row (with gutter 4)
  * the row itself is in a column that represents the page's main area
* Each product is also a card with a image as a header
  * the header is a simple div (no card-header) with a position of relative 
    * to allow the absolute placement of the Tag

* Same thing the card-body has a position:relative class
  * this to allo the absolute placement of the In Stock text with icon
  * We put it inside a div to make it appear outside the normal flow
    * the position is 0,0 but with the two margins we place it inside the container
```html
<div class="small position-absolute bottom-0 end-0 mb-2 me-3 text-success">
  <i class="bi-check-circle"></i>
  In stock
</div>
```
#### CardFooter
* we vreate an extra div to allow the items be placed using d-flex
* for the prices note the used classes
  * the sapn redefines:
    * the font size
    * the font style (strike through)
    * the font color (text-muted)
* the 2 buttons are themseleves inside a d-flex div
## Modal
* The author placed a main div around the modal dialog div
  * placed just after the footer div.
  * with inline style *display: block* or *display:none*
* The form is made of a div of input-group class
# 193
## Cart
The Tab panes are just an ul and a div
### Shopping Cart
* Same thing tha Product Review just above
* a d-flex arangment of a flex column
# 197
## CART / Shippping Details 
* Note the use of Fieldset for the définition of an entire form section
  * the first element is legend
  * the rest are rows 
    * and inside rows form-label, form-control or form-select classes
### The [ButtonGroup](https://getbootstrap.com/docs/5.0/components/button-group/#checkbox-and-radio-button-groups) Shipping Method
* By default the first is checked, that has nothing to do with the checed attribute
* The d-flex class makes the button group occupy the entire width of the enclosing fieldset
* The alert is very intersting
### Buttons next and close
* are just placed without any div (their parent is the form itself)
## Summary
* common to the *Payment Option* and to the *Shipping Details* Tabs
* IThe parent div has a d-flex (horizontal)
  * The first sibling has a d-flex (horisontal + vertical) associated to align-items-center
* for the pricing there is a lot of use of *justify-content-between* to maximize the spéce between title and price
```html
<div class="d-flex justify-content-between">
  <span>Shipping (Standard Delivery)</span>
  <span>$5</span>
</div>
```
## Cart / Payment Options
* The right part is the same than *Shipping Details*
* For each Payment Option we use a Card (that garantees the 4 borders)
  * for-check, form-check-input adn form-check-label are the 3 used classes
  * not inside the label the span with the class visually hidden very useful for text-readers

# 198 FAQ
* Accordeons, each accordeon is in its own section (just for the margin bottom)
* The three sections are in a container div
## [Accordion](https://getbootstrap.com/docs/5.3/components/accordion/)
* The most complicated is a accordion item body
  * headingCategory1One refers to the title's id
  * accordionCategory1 refers to the main accordeon id
```html
<div id="collapseCategory1One" class="accordion-collapse collapse" aria-labelledby="headingCategory1One" data-bs-parent="#accordionCategory1" style="">
  <div class="accordion-body"><!--The text we want to put--></div>
</div>
```
# 202
## Example of terms of Service
### A card on the left
* with a cardheader
* and a [listgroup](https://getbootstrap.com/docs/4.0/components/list-group/#links-and-buttons) (we have full autonomy for what we put in a card)
* it is made sticky by the class of a containing div
### An article On the right
* An article is made of many sections, each section has a id linked the left Page Navigation.
#### main p
* interesting class lead
#### Section 1
* remember image's class fluid
  * it takes the entire conteneur width, but no more
#### Section 4
* we have the example of a [bootstrap striped table](https://getbootstrap.com/docs/5.3/content/tables/#striped-rows)
