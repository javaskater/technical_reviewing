# 345

- each time I import an Element, I check ist name in the Code
  - sometimes it is not in the code but directly called from the page through attibutes !!!

## only to be directly used in the Javascript Code

```javascript
import Collapse from "bootstrap/js/dist/collapse";
import Tab from "bootstrap/js/dist/tab";
import Toast from "bootstrap/js/dist/toast";
import Tooltip from "bootstrap/js/dist/tooltip";
```

- the import path mus be all lowercase!!!
- VSCode proposes a more actual way to import partials

```javascript
import { Tooltip, Toast } from "bootstrap";
```

## commenting the Carousel

- When you comment the Carousel import in _part-3/chapter-12/laravel-mix/template/src/js/script.js_ like

```javascript
//import Carousel from "bootstrap/js/dist/carousel";
```

- the Carousel does not react to mouse event
  - eventhough the **part-3/chapter-12/laravel-mix/template/src/js/script.js** does not explicitely calls for the Carousel bootstrap object

# 346

## Minyfying for production

- just add the --production flag

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ npx mix --production

● Mix █████████████████████████ sealing (92%) asset processing
 RealContentHashPlugin
```

### In development mode

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ ll -h js/script.js
-rw-r--r-- 1 jmena01 domain users 323K juin  15 14:40 js/script.js
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ ll -h css/style.css
-rw-r--r-- 1 jmena01 domain users 237K juin  15 14:40 css/style.css
```

### in production mode (minifyed)

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ ll -h js/script.js
-rw-r--r-- 1 jmena01 domain users 83K juin  15 14:42 js/script.js ## Divided by 4
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ ll -h css/style.css
-rw-r--r-- 1 jmena01 domain users 194K juin  15 14:42 css/style.css # a Bit less
```

- There is a license file in production mode:

```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ head -10 js/script.js.LICENSE.txt
/*!
  * Bootstrap alert.js v5.3.8 (https://getbootstrap.com/)
  * Copyright 2011-2025 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
  */

/*!
  * Bootstrap backdrop.js v5.3.8 (https://getbootstrap.com/)
  * Copyright 2011-2025 The Bootstrap Authors (https://github.com/twbs/bootstrap/graphs/contributors)
  * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
```

- in fact it took the las version of bootstrap : 5.3.8 (still a minor evolution)

```bash
# Expected
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ grep bootstrap package.json
    "bootstrap": "^5.2.0",
    "bootstrap-icons": "^1.13.1"
# in fact
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-3/chapter-12/laravel-mix/template$ grep bootstrap package-lock.json
        "bootstrap": "^5.2.0",
        "bootstrap-icons": "^1.13.1",
    "node_modules/bootstrap": {
      "resolved": "https://registry.npmjs.org/bootstrap/-/bootstrap-5.3.8.tgz",
          "url": "https://opencollective.com/bootstrap"
    "node_modules/bootstrap-icons": {
      "resolved": "https://registry.npmjs.org/bootstrap-icons/-/bootstrap-icons-1.13.1.tgz",
          "url": "https://opencollective.com/bootstrap"
```
