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