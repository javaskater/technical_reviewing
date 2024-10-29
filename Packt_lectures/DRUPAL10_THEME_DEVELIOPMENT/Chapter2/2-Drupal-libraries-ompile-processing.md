# 38
## Adding a library from our 
* see this [ERRATUM of page 40](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/ERRATA.md)
  * *main.css* has to be replaced by *style.css* (the generated file in the build directory) 
# 39
* Drupal [differences between css/theme and css/component](https://www.drupal.org/docs/develop/standards/css/css-file-organization)
# 41
* The file *.ddev/commands/web/watch* tells us that ddev watch is padssing the command:
  * *yarn --cwd=web/themes/custom/alps_trips start:dev*
  * but in package.json I mistakenly defined *watch* and *watch:dev* instead of *start* and *start:dev*
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev watch
yarn install v1.22.22
[1/4] Resolving packages...
success Already up-to-date.
Done in 0.12s.
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
webpack 5.95.0 compiled successfully in 2386 ms
```
* on the other WSL Host's terminal
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev browsersync
Proxying browsersync on https://packt.ddev.site:3000
[Browsersync] Proxying: http://localhost
[Browsersync] Watching files...
[Browsersync] File event [change] : web/themes/custom/alps_trips/css/tailwind.css
[Browsersync] File event [change] : web/themes/custom/alps_trips/build/styles.css
```
* I don't have to either reload the page *https://packt.ddev.site:3000/*
  * in Firefox 
  * nor Chrome (which still ERR_CONN_RESET for https://packt.ddev.site)
* to get a red background
## To start to develop:
* on the WSL Host on two terminals
  * *jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev watch*
  * *jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev browsersync*
* and accessing  *https://packt.ddev.site:3000* preferably on Firefox (Chrome has problems with ERR_CON_RESET)
# BackStopJS
* in *.ddev/tests/backstop* you have the references screenshots
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev backstop init
Unable to find image 'backstopjs/backstopjs:6.2.1' locally
6.2.1: Pulling from backstopjs/backstopjs
3e440a704568: Downloading [======>                                            ]  6.957MB/55.05MB
68a71c865a2c: Download complete
670730c27c2e: Downloading [=========================>                         ]  5.642MB/10.88MB
5a7a2c95f0f8: Downloading [>                                                  ]   1.08MB/54.58MB
6d627e120214: Waiting
1dc4abe482bf: Waiting
d4712e486851: Waiting
469854e7775d: Waiting
b74f9b176667: Waiting
bc4dbc64c103: Waiting
e94e53a95342: Pulling fs layer
58d6083dae08: Pulling fs layer
369827dd0611: Waiting
```
* Takes time to moad the images I cancel that part for the moment
* **TODO**:  *ddev backstop init* and *ddev backstop test*