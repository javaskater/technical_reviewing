# 80
* *alps_weather_details* in the *HOOK_theme* points to  *web/modules/custom/alps_weather/templates/alps-weather-details.html.twig* because there is no template key see [answer 1 to Drupal Stack Exchange](https://drupal.stackexchange.com/questions/286881/hook-theme-path-to-template-in-a-folder)
# 81
* *https://packt.ddev.site/admin/config/regional/translate*
# 82
* When I click on the *More info* link
  * *class="use-ajax"* tells call the route name: *alps_weather.details* using [Jquery's $_POST](https://api.jquery.com/jQuery.post/)
    * recieves back the html (not the json nor the xml)
  * *data-dialog-type="dialog"* the html back is put inside the body of the [JQuery dialog Box](https://api.jqueryui.com/dialog/) 
```html
<a href="{{ path('alps_weather.details', {city:forecast.city.name, date:item.dt_txt}) }}" class="use-ajax"
         data-dialog-type="dialog"
         data-dialog-options='{"width":700,"title":"{{ 'Details'|t }}"}'>More info</a>
```
# 83
* when using *use-ajax* the block placement is skipped (we are not rendering a Drupal page) we only retrieve only the *controller's render array*
* using the Firefox Dev Tool we see (when clickin for Rome the 23/11/2024 at 21h00m00s)
  * that the url called *https://packt.ddev.site/weather/Rome/2024-11-23%2021%3A00%3A00?_wrapper_format=drupal_dialog*
  * it is a post request passing in the form all ajax libraries
# 84
```html
<a href="{{ path('alps_weather.details', {city:forecast.city.name, date:item.dt_txt}) }}" class="use-ajax"
    data-dialog-type="dialog" data-dialog-rendered="off_canvas"
    data-dialog-options='{"width":700,"title":"{{ 'Details'|t }}", "buttons":[{"text":"OK", "click":"logue"}]}'>More info</a>
```
* The the click on the OK button gives an error
* **TODO** [more on the ajax dialog](https://www.drupal.org/docs/develop/drupal-apis/ajax-api/ajax-dialog-boxes)  