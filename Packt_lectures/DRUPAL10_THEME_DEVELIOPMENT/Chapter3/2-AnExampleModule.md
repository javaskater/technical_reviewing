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
