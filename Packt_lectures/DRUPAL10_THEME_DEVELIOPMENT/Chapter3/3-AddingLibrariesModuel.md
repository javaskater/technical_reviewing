# 73
in *web/modules/custom/alps_weather/src/Controller/ForecastController.php* render Array we attach a library
```php
'#attached' => [
        'library' => [
          'alps_weather/base', //name of the library {machine name}/{library name}
        ],
        'drupalSettings' => [
          'alps_weather' => [
            'message' => 'Hello from the render array!',
          ],
        ],
      ],
```
* Why do we add component this is due to [SMACCSS css file categorization](https://www.drupal.org/node/1887922)
# 75
* link (in Firefox) **https://packt.ddev.site/forecast/paris** The content Layout is made
  * by comparing *web/modules/custom/alps_weather/css/alps_weather.css*
  * with *web/modules/custom/alps_weather/templates/alps-weather-forecast.html.twig*
* Note a very interesting way 
  * to create a dialogBox a [dialogBox](https://api.jqueryui.com/dialog/) of width 700 and title *Details*
  * whose body contains the result of a Ajax call to the route named *alps_weather.details*
    * which expects a city and a date (which format ? I don't know) 
```html
<a href="{{ path('alps_weather.details', {city:forecast.city.name, date:item.dt_txt}) }}" class="use-ajax"
         data-dialog-type="dialog"
         data-dialog-options='{"width":700,"title":"{{ 'Details'|t }}"}'>More info</a>
```
* It is the role a the custom Javascript to create the dialog box
# 77
* We don't need to call the JQuery ready function. Drupal does it for us by 
* (after the DOM is loaded) calling every callbacks attached to the *Drupal.behaviours* object
* [good example of using once in Drupal](https://mark.ie/blog/how-to-use-once-in-drupal/)
  * here we attach the on change event only one
  * the first parameter of once is an arbitrary name we give to the data-one attribute of the element selected
  * the second parameter is the JQuery selector
  * the third parameter is the context (that will be changed contrary to the document which is not changed)
* [The new Javascript once (Drupal Library) comes frm the previous Jquery.once](https://drupalbook.org/blog/replace-jqueryonce-javascript-once-drupal-10)
  * here we bind the click event only one
* In our case it has only one specific message...
  * in the [second example](https://drupalbook.org/blog/replace-jqueryonce-javascript-once-drupal-10) we add the class only one
* this [Drupal Issue](https://www.drupal.org/project/drupal/issues/444344) explains how to do with and without (when the function risks to be run many times)
# 78
* on the php Side (Controller) under *drupalSettings* I put the key *alps_weather* (Should be the module name because all drupalSettings are merged)
* on the javascript side *Drupal.behaviors.alps_weather = {* I put the key *alps_weather* (Should be the module name because all *Drupal.behaviours* are merged)
  * they are put in the settings parameters (after the context parameter)
* I change the message on the controller render array (the php side) and I go to *https://packt.ddev.site/forecast/rome*
* When I click the *WebProfilerToolbar* On the right *Collectors*
  * I don't see Assets / Settings (perhaps it does not exists anymore)