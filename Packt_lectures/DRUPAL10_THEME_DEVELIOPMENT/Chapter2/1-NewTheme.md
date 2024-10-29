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

# 31 interesting git diff and git log commands
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
* [the presentation of WebPack](https://webpack.js.org/) is simple
* css-loader (see rules) makes the translation from Javascript to css.
* We didn't have to create css/main.css but css/tailwind.css (see [ERRATA Chapter 2](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/ERRATA.md#chapter-2))
```bash
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ mv css/main.css css/tailwind.css
```
* in the *webpack.config.js* I forgot the loader to
```javascript
module: {
        rules:[
            {
                test: /\.css/,
                use: [
                    MiniCssExtractPlugin.loader, //loader forgotten
                    "css-loader",
                    "postcss-loader"
                ]
            }
        ]
    },
```
* which gives:
```bash
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ node_modules/.bin/webpack --config webpack.config.js --mode development
asset styles.css 24.1 KiB [emitted] (name: main) 1 related asset
asset main.js 2.38 KiB [emitted] (name: main) 1 related asset
Entrypoint main 26.4 KiB (10.1 KiB) = styles.css 24.1 KiB main.js 2.38 KiB 2 auxiliary assets
orphan modules 35.5 KiB (javascript) 937 bytes (runtime) [orphan] 7 modules
runtime modules 274 bytes 1 module
cacheable modules 78 bytes (javascript) 23.7 KiB (css/mini-extract)
  ./js/main.js 28 bytes [built] [code generated]
  ./css/tailwind.css 50 bytes [built] [code generated]
  css ./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/dist/cjs.js!./css/tailwind.css 23.7 KiB [built] [code generated]
webpack 5.95.0 compiled successfully in 1725 ms
```
## 38 first line
* css-loader to allow main.js To load css files
* postcss-loder to run PostCSS and in turn *Tailwind* and *Autoprefixer*
* If I don't add *--mode development* there will be nothing in *build/main.js* which is used ao automize developement
## 38 config.json
* the -D switch of yarn is to call for a dev-dependency (we only have dev-dependencies here no node_modules directory to bring with in production deployment)
* With the new two commands/scripts
```bash
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ npm run  build

> alps_trips@1.0.0 build
> webpack --config webpack.config.js

asset styles.css 23.7 KiB [emitted] (name: main) 1 related asset
asset main.js 0 bytes [emitted] [minimized] (name: main)
Entrypoint main 23.7 KiB (8.57 KiB) = styles.css 23.7 KiB main.js 0 bytes 1 auxiliary asset
orphan modules 35.5 KiB (javascript) 937 bytes (runtime) [orphan] 8 modules
cacheable modules 28 bytes (javascript) 23.7 KiB (css/mini-extract)
  ./js/main.js 28 bytes [built] [code generated]
  css ./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/dist/cjs.js!./css/tailwind.css 23.7 KiB [built] [code generated]
webpack 5.95.0 compiled successfully in 1040 ms
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ npm run  build:dev

> alps_trips@1.0.0 build:dev
> webpack --config webpack.config.js --mode development

asset styles.css 24.1 KiB [emitted] (name: main) 1 related asset
asset main.js 2.38 KiB [emitted] (name: main) 1 related asset
Entrypoint main 26.4 KiB (10.1 KiB) = styles.css 24.1 KiB main.js 2.38 KiB 2 auxiliary assets
orphan modules 35.5 KiB (javascript) 937 bytes (runtime) [orphan] 7 modules
runtime modules 274 bytes 1 module
cacheable modules 78 bytes (javascript) 23.7 KiB (css/mini-extract)
  ./js/main.js 28 bytes [built] [code generated]
  ./css/tailwind.css 50 bytes [built] [code generated]
  css ./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/dist/cjs.js!./css/tailwind.css 23.7 KiB [built] [code generated]
webpack 5.95.0 compiled successfully in 949 ms
# or use yarn the same way
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ yarn run build
yarn run v1.22.22
$ webpack --config webpack.config.js
asset styles.css 23.7 KiB [emitted] (name: main) 1 related asset
asset main.js 0 bytes [emitted] [minimized] (name: main)
Entrypoint main 23.7 KiB (8.57 KiB) = styles.css 23.7 KiB main.js 0 bytes 1 auxiliary asset
orphan modules 35.5 KiB (javascript) 937 bytes (runtime) [orphan] 8 modules
cacheable modules 28 bytes (javascript) 23.7 KiB (css/mini-extract)
  ./js/main.js 28 bytes [built] [code generated]
  css ./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/dist/cjs.js!./css/tailwind.css 23.7 KiB [built] [code generated]
webpack 5.95.0 compiled successfully in 926 ms
Done in 1.44s.
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ yarn run build:dev
yarn run v1.22.22
$ webpack --config webpack.config.js --mode development
asset styles.css 24.1 KiB [emitted] (name: main) 1 related asset
asset main.js 2.38 KiB [emitted] (name: main) 1 related asset
Entrypoint main 26.4 KiB (10.1 KiB) = styles.css 24.1 KiB main.js 2.38 KiB 2 auxiliary assets
orphan modules 35.5 KiB (javascript) 937 bytes (runtime) [orphan] 7 modules
runtime modules 274 bytes 1 module
cacheable modules 78 bytes (javascript) 23.7 KiB (css/mini-extract)
  ./js/main.js 28 bytes [built] [code generated]
  ./css/tailwind.css 50 bytes [built] [code generated]
  css ./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/dist/cjs.js!./css/tailwind.css 23.7 KiB [built] [code generated]
webpack 5.95.0 compiled successfully in 865 ms
Done in 1.41s.
```
# 40 
* watch scripts
  * you can add *--config webpack.config.js* it is the default config file
```bash
jpmena@packt-web:/var/www/html/web/themes/custom/alps_trips$ yarn run watch:dev
yarn run v1.22.22
$ webpack --config webpack.config.js --watch --mode development
asset styles.css 24.1 KiB [compared for emit] (name: main) 1 related asset
asset main.js 2.38 KiB [compared for emit] (name: main) 1 related asset
Entrypoint main 26.4 KiB (10.1 KiB) = styles.css 24.1 KiB main.js 2.38 KiB 2 auxiliary assets
orphan modules 35.5 KiB (javascript) 937 bytes (runtime) [orphan] 7 modules
runtime modules 274 bytes 1 module
cacheable modules 78 bytes (javascript) 23.7 KiB (css/mini-extract)
  ./js/main.js 28 bytes [built] [code generated]
  ./css/tailwind.css 50 bytes [built] [code generated]
  css ./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/dist/cjs.js!./css/tailwind.css 23.7 KiB [built] [code generated]
webpack 5.95.0 compiled successfully in 881 ms
^C # Stop waiting for changes CTRL+C
```