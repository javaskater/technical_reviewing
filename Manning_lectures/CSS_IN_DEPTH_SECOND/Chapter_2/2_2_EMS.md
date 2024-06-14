## inheriting sizes through ems
* the actual padding size is based on the _actual font size_ which is itself calculated on the _inherited font size_
```css
body {
    font-size: 16px;
}
.slogan {
    font-size: 1.2em;
    padding: 1.2em;
    background-color: #ccc;
}
```
* which gives for the padding:
  * The padding and the actual font size are calculated differentlys though the have the same value
```python
>>> 16 * 1.2 * 1.2
23.04
```
* p 46: interesting size ineritance effect in nested list
  * can be avoided using a class for the _top ul_
  * other solution proposed by the book
    * define a style for a simple ul
    * define a style for the ul sons of a ul (selector _ul ul_)
* p 48: em, px or rems ? TIP: _use rems for font sizes, pixels for borders, and ems or rems for most other measures, especially paddings, margins, and border radius._
  * defining a font size as em or rem is useful for accessibility!