# 44 Stylint for CSS files
```javascript
    "devDependencies": { //Only for development
        "autoprefixer": "^10.4.20",
        "css-loader": "^7.1.2",
        "mini-css-extract-plugin": "^2.9.1",
        "postcss": "^8.4.47",
        "postcss-loader": "^8.1.1",
        "stylelint": "^16.10.0", // main
        "stylelint-config-standard": "^36.0.1", //other
        "stylelint-config-tailwindcss": "^0.0.7", //for tailwindcss
        "stylelint-order": "^6.0.4", // Other
        "tailwindcss": "3",
        "webpack": "^5.95.0",
        "webpack-cli": "^5.1.4"
    },
``` 
* There is well a file at *web/core/.stylelintrc.json* with already a lot of rules
* **.stylelintrc.json** is a new file to be created under *web/themes/custom/alps_trips*
## My question
```javascript
"extends":[
        "../../../core/.stylelintrc.json",
        "stylelint-config-tailwindcss" //Where is this file ?
    ],
```
### The answer:
* node_modules is in the path
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development/web/themes/custom/alps_trips$ find . -name stylelint-config-tailwindcss
./node_modules/stylelint-config-tailwindcss # There is well a file addinfg rules for tailwindcss
```
## Adding to yarn and ddev configuration
* There is 66 errors because it does not recognize css/components/*.css rules
* New ddev command lintcss created:
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ cat .ddev/commands/web/lintcss
yarn --cwd=web/themes/custom/alps_trips lint:cssj
```
* Calling it two ways
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev lintcss
# Or without defining the ddev command lintcss
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev yarn --cwd=web/themes/custom/alps_trips lint:css
```
# 45 ESLint for Javascript Files
```javascript
"devDependencies": {
        "autoprefixer": "^10.4.20",
        "css-loader": "^7.1.2",
        "eslint": "^9.13.0",//
        "eslint-config-airbnb-base": "^15.0.0",//
        "eslint-config-prettier": "^9.1.0",//
        "eslint-plugin-import": "^2.31.0",//
        "eslint-plugin-prettier": "^5.2.1",//
        "eslint-plugin-yml": "^1.14.0",//
        "mini-css-extract-plugin": "^2.9.1",
        "postcss": "^8.4.47",
        "postcss-loader": "^8.1.1",
        "prettier": "^3.3.3",//
        "stylelint": "^16.10.0",
        "stylelint-config-standard": "^36.0.1",
        "stylelint-config-tailwindcss": "^0.0.7",
        "stylelint-order": "^6.0.4",
        "tailwindcss": "3",
        "webpack": "^5.95.0",
        "webpack-cli": "^5.1.4"
    },
```
## copy/modify the Drupal Core File
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development/web/themes/custom/alps_trips$ cp -pv ../../../core/.eslintrc.json .
'../../../core/.eslintrc.json' -> './.eslintrc.json'
# After adding the last line
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development/web/themes/custom/alps_trips$ diff -u ../../../core/.eslintrc.json
 .eslintrc.json 
--- ../../../core/.eslintrc.json        2023-07-06 10:25:16.000000000 +0200
+++ .eslintrc.json      2024-10-29 16:51:19.938763401 +0100
@@ -47,5 +47,6 @@
     "no-unused-vars": ["warn"],
     "operator-linebreak": ["error", "after", { "overrides": { "?": "ignore", ":": "ignore" } }],
     "yml/indent": ["error", 2]
-  }
+  },
+  "ignorePatterns":["postcss.config.js", "build/*.js"]
 }
```
## .prettierrc.json
* Visual StudioCode proposes directly the keys and the values
## Problem runnin ESLint
* I completed the [Issure 52 ont the website](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/52https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/52)
  * because this version of ESLint wants another configuration file with other plugins
# 46 PHPCS (PHP Coding Standards)
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev composer require --dev drupal/coder
./composer.json has been updated
Running composer update drupal/coder
Gathering patches for root package.
Loading composer repositories with package information
Updating dependencies
Lock file operations: 0 installs, 1 update, 0 removals
  - Upgrading drupal/coder (8.3.20 => 8.3.23)
Writing lock file
Installing dependencies from lock file (including require-dev)
Package operations: 0 installs, 1 update, 0 removals
  - Downloading drupal/coder (8.3.23)
Gathering patches for root package.
Gathering patches for dependencies. This might take a minute.
  - Upgrading drupal/coder (8.3.20 => 8.3.23): Extracting archive
Generating autoload files
94 packages you are using are looking for funding.
Use the `composer fund` command to find out more!
phpstan/extension-installer: Extensions installed
Found 9 security vulnerability advisories affecting 4 packages.
Run composer audit for a full list of advisories.
Using version ^8.3 for drupal/coder # It is the version 8.3
```
* The [project page](https://www.drupal.org/project/coder) recommends the **8.3.25** version 
 * Here it updated from *8.3.20* to the *8.3.23* version
 * the 8.3.25 date back one month ago (22/09/2024)
## already a web/phpcs.xml.dist
* with already the required information
* it is not due to the installation of coder but already [created by the author in the main branch](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/web/phpcs.xml.dist)
## Testing
```bash
jpmena@packt-web:/var/www/html/web$ ../vendor/bin/phpcs themes/custom/alps_trips/

FILE: /var/www/html/web/themes/custom/alps_trips/src/StarterKit.php
----------------------------------------------------------------------
FOUND 1 ERROR AFFECTING 1 LINE
----------------------------------------------------------------------
 8 | ERROR | [x] Missing class doc comment
----------------------------------------------------------------------
PHPCBF CAN FIX THE 1 MARKED SNIFF VIOLATIONS AUTOMATICALLY
----------------------------------------------------------------------


FILE: /var/www/html/web/themes/custom/alps_trips/alps_trips.info.yml
-----------------------------------------------------------------------------------------------------------
FOUND 0 ERRORS AND 2 WARNINGS AFFECTING 1 LINE
-----------------------------------------------------------------------------------------------------------
 1 | WARNING | Remove "version" from the info file, it will be added by drupal.org packaging automatically
 1 | WARNING | "Description" property is missing in the info.yml file
-----------------------------------------------------------------------------------------------------------

Time: 193ms; Memory: 6MB
```
## Creating a composer.json script
* That you can call from the host using *ddev composer*
```command already entered
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev composer | tail -2
 lint
  lint:php             Runs the lint:php script as defined in composer.json
```
* At the end of the **composer.json** I already have
  * It had been [added by the author in the main branch](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/composer.json) at the very end of the **composer.json**
```javascript
    "scripts": {
        "lint:php" : [
            "vendor/bin/phpcs --standard=web/phpcs.xml.dist web/themes/custom/alps_trips/"
        ]
    }
}
```
## Run the composer script
* we now have a composer command we don't need to call for run-script
* The composer command returns an error because phpcs returned an error (and 2 warnings)
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev composer lint:php # we don't need to call run-script because in composer it is a command
> vendor/bin/phpcs --standard=web/phpcs.xml.dist web/themes/custom/alps_trips/

FILE: /var/www/html/web/themes/custom/alps_trips/src/StarterKit.php
----------------------------------------------------------------------
FOUND 1 ERROR AFFECTING 1 LINE
----------------------------------------------------------------------
 8 | ERROR | [x] Missing class doc comment
----------------------------------------------------------------------
PHPCBF CAN FIX THE 1 MARKED SNIFF VIOLATIONS AUTOMATICALLY # Beacause of that error the composer command returned an error code 2
----------------------------------------------------------------------


FILE: /var/www/html/web/themes/custom/alps_trips/alps_trips.info.yml
-----------------------------------------------------------------------------------------------------------
FOUND 0 ERRORS AND 2 WARNINGS AFFECTING 1 LINE
-----------------------------------------------------------------------------------------------------------
 1 | WARNING | Remove "version" from the info file, it will be added by drupal.org packaging automatically
 1 | WARNING | "Description" property is missing in the info.yml file
-----------------------------------------------------------------------------------------------------------

Time: 126ms; Memory: 6MB

Script vendor/bin/phpcs --standard=web/phpcs.xml.dist web/themes/custom/alps_trips/ handling the lint:php event returned with error code 2
Composer [lint:php] failed, composer command failed: exit status 2. stderr=
```