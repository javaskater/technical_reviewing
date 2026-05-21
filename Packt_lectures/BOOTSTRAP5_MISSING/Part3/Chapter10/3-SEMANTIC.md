# p 280

- [The Semantic Book example on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/examples/semantic-extend/default/index.html)

- on compile ?
  - ici pas de feuille de style scss ...
  - C'est du Boostrap nu...

# p 282

- on supprime toutes les classes bootstrap...
  - on n'utilise que le HTML 5 ce qui donne [index.html on Packt's GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-10/examples/semantic-extend/extended-classes/index.html)

## we change the default layout step by step

- [Good explaination of exted in SASS](https://sass-lang.com/documentation/at-rules/extend/)

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/semantic-extend/extended-classes$ npm i sass --save-dev

added 12 packages in 279ms

5 packages are looking for funding
  run `npm fund` for details
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-10/examples/semantic-extend/extended-classes$ node_modules/.bin/sass scss/mystyle.scss css/style.css # I introduce the different styles step by stop in mystyle.scss
Deprecation Warning [import]: Sass @import rules are deprecated and will be removed in Dart Sass 3.0.0.
##################################
```

# p 284

## container

```scss
@import "../../../../../../bootstrap/scss/bootstrap.scss";

body {
  @extend .container;
}
```

- change the body width
- but the style and size of the characters is given by the bootstrap.scss import

## header

```css
.lead,
header p {
  font-size: 1.25rem;
  font-weight: 300;
}

.display-1,
header h1,
header .h1 {
  font-size: calc(1.625rem + 4.5vw);
}
/*
and further down
*/
.text-center,
header h1,
header .h1 {
  text-align: center !important;
}
```

# 285

- I work on the footer before anything else
- At the end, everywhere in the genrated style.css we have things like

```css
.input-group .btn,
.input-group main > aside > div > div > a {
  position: relative;
  z-index: 2;
}
```
