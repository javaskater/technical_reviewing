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