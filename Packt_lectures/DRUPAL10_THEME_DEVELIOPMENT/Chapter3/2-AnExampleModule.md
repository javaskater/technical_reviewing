# 57 Opening the Alps Module
* All the Alps Modules can be instreresting for a Course on Drupal Programing
* *web/modules/custom/alps_weather/alps_weather.info.yml* the package key defines the category (here *Alps*) under which we will find the module
* Human readable Name (to be found in Admin/Extensions but also under the name key here *Weather*)
* Machine name (the folder name to be found under the other configurations files and if you publish your module in the Drupal project url) here *alps_weather*
* Note that a service can render a template, it is not always the Controller's duty
# 58
* *WebProfiler / Services display* has a CPU Like icon
## An example of service
* *web/modules/custom/alps_weather/src/WeatherClient.php* is a ggod service example...
### just a question 
```php
/**
   * {@inheritdoc} 
   */
  public function getForecastDetail(string $city, string $date): array {
    $forecast = $this->getForecastData($city);

    $detail = array_filter($forecast['list'], function ($item) use ($date) {
      return $item['dt_txt'] == $date;
    });

    return array_shift($detail);
  }
```  
* inheritdoc comes from an interface that the client expects
* array_shift takes the first value of the array and returns it
 * since array_filter returns an array with one element, it is that element
* array_filter see [this link for the item part](https://www.scaler.com/topics/php-array-filter/)
  * *use keyword* grant access to variables outside the scope of the function see [answer 122 to this StackOverflow Post](https://stackoverflow.com/questions/6320521/use-keyword-in-functions-php)
## An example of configuration from
* *web/modules/custom/alps_weather/src/Form/SettingsForm.php* it is extending FormBase which has access tho settings 
* The first part of *web/modules/custom/alps_weather/alps_weather.routing.yml* is where the Form Routing is defined
```yaml
alps_weather.settings:
  path: '/admin/config/system/alps-weather' # Admin / Configuration/ System part of the page /  
  defaults:
    _title: 'Weather Settings'
    _form: 'Drupal\alps_weather\Form\SettingsForm'
  requirements:
    _permission: 'administer site configuration'
```
* The corresponding Menu in *web/modules/custom/alps_weather/alps_weather.links.menu.yml*
  * it is the only menu link defined by this module
```yaml
alps_weather.settings:
  title: Weather Settings
  description: 'Configure weather settings.'
  parent: system.admin_config_system # The parent menu Admin / Configuration / System
  route_name: alps_weather.settings
  weight: 10
```
## Nice definition of Hooks
* Pervasive in the Drupal 7 and earlier version
# 59
* The Help page defines a lot of routes (one per module) whose route name is *help.page.{machine name of the module}*
# 60
* The outer key name in the hook_thme is the template name (replacing underscores by dashes) see p 61
  * it is the thme hook name (it must be unique in all Drupal so it is good use to prefix it with the module name) 
# 61
* To connect the service obtained data to Drupal Theme Hook (and with it to the corresponding template) use a render Array (in a controller ?)
* The code snippet in the middle of the page is versy clear
  * It is the very minimal render array and is OK for training purposes...
  * It has been a bit extended in *web/modules/custom/alps_weather/src/Controller/ForecastController.php*
# 62 using the render array in the Twig template
# 64 with the dump function 
* we see that forecast has a list element which is an array of 5 elements 
# 65 TODO signal a mistake
* The code at the loawer part of the page has a mistake
* should be **#forecast** intead of **weather** ([The accomagnying code](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/web/modules/custom/alps_weather/src/Controller/ForecastController.php) is right be it for page or for detail)
# 66 the Cache part
* [The think process in the link](https://www.drupal.org/docs/drupal-apis/render-api/cacheability-of-render-arrays#s-the-thought-process) gives a precious representation of what may be cached
  * The rendering process described does it from Top to bottom (The larger element down to the more elementary/atom) 
# 67 Controllers and Blocks 
* Are the main producers of render arrays (interesting for training purpose)
* the [Controller](https://symfonycasts.com/screencast/drupal8-under-the-hood/modules-routes-controllers) returns content for the mainContent Area
* The block calculate their content and add it when they are defined visible for that page ...
* the hook for that array is page (outer key) which for Olivero calls *web/core/themes/olivero/templates/layout/page.html.twig*
# 68
* The content region is always present (it is normal because it is the region where the controllers put their contents)
* The 8 points here are very important
* The template presented is from *web/core/themes/olivero/templates/layout/page.html.twig*
# 69
* Drupal is rendering render arrays althoug twig's {{}} are meant for scalar values (Drupal extension)
## Route and Contoller
* Route in *web/modules/custom/alps_weather/alps_weather.routing.yml*
```yaml
alps_weather.forecast:
  path: '/forecast/{city}' #The name city correspond to the $city paramter of ForecastController::page
  defaults:
    _title: 'Forecast'
    _controller: '\Drupal\alps_weather\Controller\ForecastController::page'
  requirements:
    _permission: 'access content'
```
* Controller *web/modules/custom/alps_weather/src/Controller/ForecastController.php*
```php
/**
   * Return a render array with full forecast data for the next 5 days.
   *
   * @param string $city
   *
   * @return array
   */
  public function page(string $city): array { //the parameter name city must be the same as the url parameter une thn routing.yaml
    $forecast = $this->weatherClient->getForecastData($city); //weatherClient is the service of id: alps_weather.weather_client

    $build['content'] = [
      '#theme' => 'alps_weather_forecast',
      '#forecast' => $forecast,
      '#units' => $this->config('alps_weather.settings')->get('units'),
      '#cache' => [
        'max-age' => 10800,
        'tags' => [
          'forecast:' . $city,
        ],
        'contexts' => [
          'url.path',
        ],
      ],
      '#attached' => [
        'library' => [
          'alps_weather/base',
        ],
        'drupalSettings' => [
          'alps_weather' => [
            'message' => 'Hello from the render array!',
          ],
        ],
      ],
    ];

    return $build;
  }
```
* *$this->weatherClient* is the service of id: *alps_weather.weather_client*
  * see *web/modules/custom/alps_weather/src/WeatherClient.php*
  * **This service is well written**
  * no static create method (see Controller) instead a public constructor
    * with the paramters in the order, the arguments' order
```yaml
  alps_weather.weather_client:
    class: 'Drupal\alps_weather\WeatherClient'
    arguments:
      - '@http_client'
      - '@logger.channel.alps_weather'
      - '@config.factory'
```
# 70 The render array of the controller
## The theme is defined in the module file
* *web/modules/custom/alps_weather/alps_weather.module*
* [the hook theme](https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Render%21theme.api.php/function/hook_theme/11.x)
  * Here we don't have a template key so the template name is the same as the theme_hook here *alps_weather_forecast* 
```php
function alps_weather_theme(): array {
  return [
    'alps_weather_forecast' => [ //The theme we pass no theme key
      'variables' => [
        'forecast' => [],
        'units' => 'metric',
      ],
    ],
    'alps_weather_details' => [ 
      'variables' => [
        'forecast' => [],
        'units' => 'metric',
      ],
    ],
```
* see *web/modules/custom/alps_weather/templates/alps-weather-forecast.html.twig*
## Cache
* [cache tag](https://www.drupal.org/docs/drupal-apis/cache-api/cache-tags)
* [cache context](https://www.drupal.org/docs/drupal-apis/cache-api/cache-contexts)
## Block
* not depending on a route
* depending of a visibility variable see unordered lis at the end of the page 70