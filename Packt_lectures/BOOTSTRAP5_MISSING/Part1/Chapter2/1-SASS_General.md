# 22
* no example code in the [GitHub code](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide)
# 24
* Two classes for an element see [645 and 1008 in this stackOverflow Post](https://stackoverflow.com/questions/3772290/css-selector-that-applies-to-elements-with-two-classes)
# 28
* a partial file starts with an underscore that prevents il to be transformed into a css file (only the calling file for example bootstrap.scss is transformed/transpiled into a css file)
# p 29 down
* /bootstrap-5.3.3/scss/bootstrap.scss still use @import and not @use
# 31 @mixin
* *@mixin* the @include places the css code of the mixin at the place of the include
  * id does not create a new selector like in the case of **&**
# 32
* @extends takes a selector as parameter
  * The extending selector is added to the extended selector
  * the rest of the extending selector is in the extending selector alone (no more extends part anymore that the difference with the @include)
# 33
* The operations are done using the unit *5px + 10px* or _(30 / 2) * 1px_
* You also can concatenate strings *content: "Hello "+ "world"*
* / is used in CSS [see answer 19 of this StackOverflow](https://stackoverflow.com/questions/13416856/forward-slash-in-css-style-declarations)
  * it is deprecated in SASS
  * we prefer *math.div(30,2)*
  # 34
  * using map: OK
  # 35
  * built in modules [explanation of the scale function from the color module](https://sass-lang.com/documentation/modules/color/#scale)
    * many named parameters have their default value to null
    * if I want to change only $lightness I call *$lightness: 25%*