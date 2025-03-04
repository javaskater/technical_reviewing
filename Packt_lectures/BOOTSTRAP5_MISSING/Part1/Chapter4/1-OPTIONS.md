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
# 69 [grid classes on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-4/options/grid-classes)