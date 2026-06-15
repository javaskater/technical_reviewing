# [Code for chapter 12](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-3/chapter-12)

- [Laravel Mix has its own site](https://laravel-mix.com/docs/6.0/what-is-mix)

## The main mix file

[part-3/chapter-12/laravel-mix/template/webpack.mix.js](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-3/chapter-12/laravel-mix/template/webpack.mix.js):

```javascript
let mix = require("laravel-mix");
mix.js("src/js/script.js", "js/").sass("src/scss/style.scss", "css/");
```
