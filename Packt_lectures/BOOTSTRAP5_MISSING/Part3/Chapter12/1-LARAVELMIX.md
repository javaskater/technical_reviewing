# 339

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ npm init -y
Wrote to /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website/package.json:

{
  "name": "website",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}



jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ npm install bootstrap --save-dev
npm notice This endpoint is being retired. Use the bulk advisory endpoint instead. See the following docs for more info: https://api-docs.npmjs.com/#tag/Audit

added 2 packages in 615ms

2 packages are looking for funding
  run `npm fund` for details
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ grep -i bootstrap package.json
    "bootstrap": "^5.3.8" # it is no more version 5.2.0
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ npm install @popperjs/core --save-dev
npm notice This endpoint is being retired. Use the bulk advisory endpoint instead. See the following docs for more info: https://api-docs.npmjs.com/#tag/Audit

up to date in 501ms

2 packages are looking for funding
  run `npm fund` for details
# laravel-mix is not in our Corporate repositories
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ npm install laravel-mix --save-dev
npm error code E404
npm error 404 Not Found - GET https://nexus3.appli.dgfip/repository/npmjs_group/laravel-mix - Not found
npm error 404
npm error 404  'laravel-mix@*' is not in this registry.
npm error 404
npm error 404 Note that you can also install from a
npm error 404 tarball, folder, http url, or git url.
npm error A complete log of this run can be found in: /home/jmena01/.npm/_logs/2026-06-12T07_39_42_266Z-debug-0.log
```

- I have to use that .npmrc

```bash
jmena01@m077-2281091:~$ cat ./CONSULTANT/.npmrc
http-proxy = http://proxy.infra.dgfip:3128/
https-proxy=http://proxy.infra.dgfip:3128/
strict-ssl = false
registry = http://registry.npmjs.org/
```

- I put it on our project

```bash
jmena01@m077-2281091:~$ cp -pv CONSULTANT/.npmrc ~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website
'CONSULTANT/.npmrc' -> '/home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website/.npmrc'
```

- And I call laravel-mix again

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ npm install laravel-mix --save-dev
npm notice Beginning October 4, 2021, all connections to the npm registry - including for package installation - must use TLS 1.2 or higher. You are currently using plaintext http to connect. Please visit the GitHub blog for more information: https://github.blog/2021-08-23-npm-registry-deprecating-tls-1-0-tls-1-1/
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm warn deprecated glob@7.2.3: Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me
npm warn deprecated uuid@8.3.2: uuid@10 and below is no longer supported.  For ESM codebases, update to uuid@latest.  For CommonJS codebases, use uuid@11 (but be aware this version will likely be deprecated in 2028).
npm warn deprecated stable@0.1.8: Modern JS already guarantees Array#sort() is a stable sort, so this library is deprecated. See the compatibility table on MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility
npm warn deprecated @babel/plugin-proposal-object-rest-spread@7.20.7: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-object-rest-spread instead.
npm notice Beginning October 4, 2021, all connections to the npm registry - including for package installation - must use TLS 1.2 or higher. You are currently using plaintext http to connect. Please visit the GitHub blog for more information: https://github.blog/2021-08-23-npm-registry-deprecating-tls-1-0-tls-1-1/

added 746 packages in 28s

105 packages are looking for funding
  run `npm fund` for details
```

- now we have

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/website$ cat package.json
{
  "name": "website",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "@popperjs/core": "^2.11.8",
    "bootstrap": "^5.3.8",
    "laravel-mix": "^6.0.49"
  }
}
```

## In an empty folder

- I pass the same commands

```bash
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ cat package.json
{
  "name": "testlaravelmix",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "@popperjs/core": "^2.11.8", # dev dependency beacause it will be aggregatesd and minified to a production file
    "bootstrap": "^5.3.8", # dev dependency beacause it will be aggregatesd and minified to a production file
    "laravel-mix": "^6.0.49"
  }
}
```

# 340

```bash
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ touch webpack.min.js
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ mkdir -p src/js
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ touch src/js/script.js
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ mkdir -p src/scss
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ touch src/scss/style.scss
```

## I did everything

```bash
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ cat webpack.min.js
let mix = require("laravel-mix");
mix.js("src/js/script.js", "js/").sass("src/scss/styles.scss", "css/");
```

## I get the error

```bash
jmena01@m077-2281091:~/CONSULTANT/testLaravelMix$ npx mix
[webpack-cli] Error: Cannot find module 'webpack/lib/SizeFormatHelpers'
Require stack:
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/laravel-mix/src/webpackPlugins/BuildOutputPlugin.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/laravel-mix/src/builder/webpack-plugins.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/laravel-mix/src/builder/WebpackConfig.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/laravel-mix/src/Mix.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/laravel-mix/setup/webpack.config.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/webpack-cli/lib/webpack-cli.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/webpack-cli/lib/bootstrap.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/webpack-cli/bin/cli.js
- /home/jmena01/CONSULTANT/testLaravelMix/node_modules/webpack/bin/webpack.js
    at Function._resolveFilename (node:internal/modules/cjs/loader:1225:15)
    at Function._load (node:internal/modules/cjs/loader:1055:27)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:220:24)
    at Module.require (node:internal/modules/cjs/loader:1311:12)
    at require (node:internal/modules/helpers:136:16)
    at Object.<anonymous> (/home/jmena01/CONSULTANT/testLaravelMix/node_modules/laravel-mix/src/webpackPlugins/BuildOutputPlugin.js:6:24)
    at Module._compile (node:internal/modules/cjs/loader:1554:14)
    at Object..js (node:internal/modules/cjs/loader:1706:10)
    at Module.load (node:internal/modules/cjs/loader:1289:32) {
  code: 'MODULE_NOT_FOUND',
```

- in the package.json we have

```json
"devDependencies": {
    "@popperjs/core": "^2.11.8",
    "bootstrap": "^5.3.8",
    "laravel-mix": "^6.0.49"
  },
  "dependencies": {
    "webpack": "^5.107.2"
  }
```

## using the template

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ cp ~/CONSULTANT/.npmrc . # we bring the proxy npm configuration
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npm i
########################### lots of notice

added 763 packages in 25s

112 packages are looking for funding
  run `npm fund` for details
```

## in the package.json we have

```json
"devDependencies": {
    "@popperjs/core": "^2.11.5",
    "bootstrap": "^5.2.0",
    "bootstrap-icons": "^1.9.1",
    "laravel-mix": "^6.0.43",
    "resolve-url-loader": "^5.0.0",
    "sass": "^1.52.1",
    "sass-loader": "^12.6.0"
  }
```

- I still have the problem

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npx mix
[webpack-cli] Error: Cannot find module 'webpack/lib/SizeFormatHelpers'
Require stack:
- /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/node_modules/laravel-mix/src/webpackPlugins/BuildOutputPlugin.js
- /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/node_modules/laravel-mix/src/builder/webpack-plugins.js
- /home/jmena01/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template/node_modules/laravel-mix/src/builder/WebpackConfig.js
```

### Solution that work

- [Following davidvandertuijn 3 weeks ago on that Laracast post](https://laracasts.com/discuss/channels/elixir/laravel-mix-is-breaking)
  - I had to add **"webpack": "5.93.0"** to the package .json
- then remove:

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ rm package-lock.json
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ rm -rf node_modules
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npm i
##############################################"""
added 761 packages in 14s

112 packages are looking for funding
  run `npm fund` for details
```

- the new package.json is (I could have added the resolution part)

```json
{
  "name": "examples",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@popperjs/core": "^2.11.5",
    "bootstrap": "^5.2.0",
    "bootstrap-icons": "^1.9.1",
    "laravel-mix": "^6.0.49",
    "webpack": "5.93.0", // The line I added to force for an old webpack version
    "resolve-url-loader": "^5.0.0",
    "sass": "^1.52.1",
    "sass-loader": "^12.6.0"
  }
}
```

- the the command runs succesfully

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npx mix

● Mix █████████████████████████ building (37%) 1/2 entries 3/3 dependencies 1/3 modules 2 active
 css-loader › postcss-loader › resolve-url-loader › sass-loader › src/scss/style.scss|0





✔ Mix
  Compiled successfully in 409.94ms
















   Laravel Mix v6.0.49


✔ Compiled Successfully in 407ms
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬──────────┐
│                                                                                                                                                               File │ Size     │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────────┤
│                                                                                                                                                      /js/script.js │ 6.34 KiB │
│                                                                                                                                                      css/style.css │ 1 bytes  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴──────────┘
webpack compiled successfully
```

- now I have two new folders:

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ ll css/ # new folder
total 12
drwxr-xr-x 2 jmena01 domain users 4096 juin  15 09:04 ./
drwxr-xr-x 6 jmena01 domain users 4096 juin  15 09:04 ../
-rw-r--r-- 1 jmena01 domain users    1 juin  15 09:04 style.css
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ ll js # new folder
total 16
drwxr-xr-x 2 jmena01 domain users 4096 juin  15 09:04 ./
drwxr-xr-x 6 jmena01 domain users 4096 juin  15 09:04 ../
-rw-r--r-- 1 jmena01 domain users 6488 juin  15 09:04 script.js
```
