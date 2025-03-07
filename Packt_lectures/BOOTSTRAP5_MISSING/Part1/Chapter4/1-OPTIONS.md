# 61 CARET 
* the variable in  *chapter4/node_modules/bootstrap/scss/_variables.scss* is at pôsition 370
  * the position 337 in the text corresponds to the *chapter4/node_modules/bootstrap/scss/_variables.scss* file without the comments
* the [index.html file to display the Caret is on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-1/chapter-4/options/caret/index.html)
* simplified the bootstrap.scss to include only the strict necessary (see my [Style.scss to test the carret](./files/style_caret.scss))
* for the bootstrap Javascript file, take if from the dist/js and not from the js/dist (you would not find it)
# 63
* the [index.html file to test the rounded corners is on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-1/chapter-4/options/rounded/index.html)
* I only need form, button, dropdown and alert
# 64 SHADOW
* see the [solution on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/shadows)
* the change brought by *$enable-shadows* is very subtle (shadows is plural).
# 65 GRADIENT
* see the [solution on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/gradients)
## Carousel
* You have to create the entire [carousel](https://getbootstrap.com/docs/5.3/components/carousel/)
  * I hope we will know more about it later
  * The slide class is only meant for Javascript animation
* enable-gradients (plural) to true enables the gradient in the prev and next button of the carousel
  * it does what the code says
```bash
jmena01@M077-1840900:~/CONSULTANT/my_bootstrap5_guide/chapter4$ grep -rin enable-gradients node_modules/bootstrap/scss/
node_modules/bootstrap/scss/_carousel.scss:117:  background-image: if($enable-gradients, linear-gradient(90deg, rgba($black, .25), rgba($black, .001)), null);
node_modules/bootstrap/scss/_carousel.scss:121:  background-image: if($enable-gradients, linear-gradient(270deg, rgba($black, .25), rgba($black, .001)), null);
```
# 68 reduced motion
* no difference noticeable [see code on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/reduced-motion)
# 68 [smooth scroll](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/smooth-scroll)
* to see the difference the html code is a goof idea
```html
  <a href="#anchor">Start scroll</a>
	<div style="height:20vw; background-color: aliceblue;"></div>
	<div id="anchor">Scroll target</div>
```
# 69 
## [grid classes on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/grid-classes)
* with this option to false the div are no more in [grid css](https://www.w3schools.com/css/css_grid.asp)
## [container classes on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/container-classes)
* the text is contained inside the main area
## [New Css grid](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/css-grid)
* both css grids are fully independents of eachothers
  * no same classes
  * the false of the actual one places all divs under eachothers eventhough *enable-grid-classes* is true
```scss
$enable-grid-classes:true;
$enable-cssgrid: false; //fully independent of the previous one
```
* Those grids are not responsive 'it is not bootstrap row/col classes'
# 70
## [Button pointers on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/button-pointers)
* if true changes the pointer to a hovered over it
# 71
## [Responsive font sizes](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/responsive-font-sizes)
```scss
$enable-rfs: false;
```
* **rfs** stands for *responsive font sizes*, if false the font size is the same independently of the actual screen size
## [Validation icons](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/validation-icons)
* the effect is only to make the icons in the input fields to disappear
* the other property that makes only the text appear (with the corresponding color) dependent on the input's valid class is not dependent on this property
# 72
## [Negative margins](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/negative-margins)
* The texts are mixed in each-others
## [Deprecation messages](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/deprecation-messages)
* No use, no deprecated code in this version of Bootstrap (in the sass compilation output console)
# 73
## [Important utilities](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/important-utilities)
* more on the [!important](https://www.w3schools.com/css/css_important.asp)
* we can place the important before the others and it still works
  * the following code makes the background red !!! enthough the others selector are declared after (and have higher priorities)  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon CSS5</title>
    <!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">-->
    <style>
        p {
            background-color: red !important;
        }
        #myid {
            background-color: blue;
        }

        .myclass {
            background-color: gray;
        }
    </style>
    <!--<link rel="stylesheet" href="css/bootstrap_solution.css">-->
  </head>
</head>
<body>
    <div>
        <p class="myclass" id="myid">bonjour tout le monde</p>
    </div>
</body>
</html>
```
* I add a background color to the paragraph to better see the paragraph alignment!
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid properties</title>
    <link rel="stylesheet" href="style.css">
</head>
<body class="p-3">
    <p class="text-center" style="text-align: right; background-color: yellow;">Center-aligned text.</p>
</body>
</html>
```
* if the option is false we get back to the normal priorities order
  * style has a higher priority than class!!!
# 74
[SPACER](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/spacer) 
[p-1 to p-5](https://bootstrapshuffle.com/fr/classes/spacing/p-1+%25_F+p-*-%23) are meant for padding!!!
```css
.p-2 {
	padding: 0.5rem !important;
}
```
* The role attribute is meant only for ARIA