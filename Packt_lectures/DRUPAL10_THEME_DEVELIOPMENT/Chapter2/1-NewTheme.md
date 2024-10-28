# 30
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev ssh
jpmena@packt-web:/var/www/html$ cd web/
jpmena@packt-web:/var/www/html/web$ rm -Rf themes/custom/alps_trips
jpmena@packt-web:/var/www/html/web$ php core/scripts/drupal generate-theme alps_trips --path themes/custom/
Theme generated successfully to themes/custom/alps_trips
```
* The folder *web/core/lib/Drupal/Core/Command* contains interesting command objects 
  * **GenerateTheme.php** is one of them
# 35
* Yarn add -D added 109 packages and added a dependecies paragraph to the package.json
```javascript
{
    "name": "alps_trips",
    "version": "1.0.0",
    "description": "alps_trips dependencies",
    "author": "Luca Lusso",
    "license": "GPL-3.0",
    "devDependencies": {
        "tailwindcss": "3"
    }
}
```
## tailwind.config.js
* We look for classes used in the storyBook/stories outside of the Drupal WebSite (not in the container but in the host)
  * It is the design system
* We only have the [content part](https://tailwindcss.com/docs/content-configuration) Where we tell tailwind the classname we use
# 36
## PostCSS autoprefixer
* Added 10 new dependencies
* It just add navigator prefixes to compiled tailwindcss classes
  * tailwindcss comiles itself its calsses
## WebPack
* has added 101 new dependencies
# 37 more on WebPack 
