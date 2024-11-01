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