# 7 method 1 [editing bootstrap.css](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-1/customization-methods/editing-css)
##  to test the differents css Bootstrap
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon CSS5</title>
    <!--<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">-->
    <link rel="stylesheet" href="css/bootstrap.css">
    <!--<link rel="stylesheet" href="css/bootstrap_solution.css">-->
  </head>
</head>
<body>
    <nav aria-label="Breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item"><a href="#">Sports</a></li>
            <li class="breadcrumb-item"><a href="#">Ball Games</a></li>
            <li class="breadcrumb-item active"><a href="#">Baseball</a></li>
        </ol>
    </nav>
</body>
</html>
```
* [bootstrap.css from the official examples](https://getbootstrap.com/docs/5.3/examples/)
* CDN Bootstrap
* [bootstrap_solution.css from the solution on Github (editing the Bootstrap.css)](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-1/chapter-1/customization-methods/editing-css/css/bootstrap.css)
* VSCode helps you modify the css Files
  * var is a new css term for importing a variable
# 8
* Changing the index.html for
```html
<nav aria-label="Breadcrumb" style="--bs-breadcrumb-divider: '$'">
```
* gives a value to the variable and change the separation/element in the breadcrumb to $
* [interesting post about pseudo elements](https://www.smashingmagazine.com/2011/07/learning-to-use-the-before-and-after-pseudo-elements-in-css/)
  * they are inserted inside the container that calls them before or after all the elements inside the container.
  * at the same level than the <a> elements
# 9 method 2 [overwriting bootstrap.css](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-1/customization-methods/overwriting-css)
* only modified properties in css/style.css
# 10 method 3 [SASS](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-1/chapter-1/customization-methods/using-sass)
* No code here, just watch the files
* The $spacer variable is defined in SASS [Bootstrap _variables section line 374](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/bootstrap/scss/_variables.scss)
* from there in the [bootstrap.scss line 10](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-1/chapter-1/customization-methods/using-sass/scss/bootstrap.scss) whe redefine from the [Bootstrap _variables section line 1530](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/bootstrap/scss/_variables.scss)
```scss
$breadcrumb-border-radius:          null !default;
```
