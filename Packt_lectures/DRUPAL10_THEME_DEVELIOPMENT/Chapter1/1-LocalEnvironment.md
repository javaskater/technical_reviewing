# 7
* Although We were asked to install [ddev](https://ddev.com/get-started/) We are using here [Docker Desktop 4Windows](https://docs.docker.com/desktop/install/windows-install/) 
* more about DDEV integration on a [separate md page](../DDEV.md)
# 8
* All the Extensions I should For Visual Studio Code
  * No Drupal specific extensions
* *PHP Intelephense* already installed from a previous tutorial
* **PHP Debug** to install. I don't know if it will work well with WSL-Integration
* **Tailwind CSS IntelliSense** to install
* **Twig Language 2** to install
* *Prettier* already installed from a previous tutorial  
# 9 Installing the demo WebSite
* By default the [main branch](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/tree/main) is the CMS just installed
* There is a [final branch](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/tree/final)
* and four intermediates branches like [dependabot/npm_and_yarn/next/next-14.1.1](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/tree/dependabot/npm_and_yarn/next/next-14.1.1)
* I clone the main branch on the *$HOME/D10Theming* folder
```bash
jpmena@LAPTOP-E2MJK1UO:~$ mkdir D10Theming
jpmena@LAPTOP-E2MJK1UO:~$ cd D10Theming/
jpmena@LAPTOP-E2MJK1UO:~/D10Theming$ git clone https://github.com/PacktPublishing/Modernizing-Drupal-10-
Theme-Development
Cloning into 'Modernizing-Drupal-10-'...
remote: Invalid username or password. # The command given int the Book is not the right one
fatal: Authentication failed for 'https://github.com/PacktPublishing/Modernizing-Drupal-10-/' 
Theme-Development: command not found
# The real command as taken from the GitHub page
jpmena@LAPTOP-E2MJK1UO:~/D10Theming$ git clone https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development.git
Cloning into 'Modernizing-Drupal-10-Theme-Development'...
remote: Enumerating objects: 1466, done.
remote: Counting objects: 100% (315/315), done.
remote: Compressing objects: 100% (203/203), done.
remote: Total 1466 (delta 170), reused 113 (delta 112), pack-reused 1151 (from 1)
Receiving objects: 100% (1466/1466), 55.01 MiB | 443.00 KiB/s, done.
Resolving deltas: 100% (347/347), done.
```
* Start ddev
  * Works only if I chack back [WSL Dcoker Integration on Docker Desktop 4 Windows like show in GitHu Issue](https://github.com/ddev/ddev/issues/6647)
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev start
Network ddev_default created

 TIP OF THE DAY
 You can have as many databases as you want!
 https://ddev.readthedocs.io/en/stable/users/usage/faq/#can-i-use-additional-databases-with-ddev

It looks like you have a new DDEV release.
May we send anonymous DDEV usage statistics and errors?
To know what we will see please take a look at
https://ddev.readthedocs.io/en/stable/users/usage/diagnostics/#opt-in-usage-information
Permission to beam up? [Y/n] (yes): Y
Starting packt...
Port 80 is busy, using 33000 instead, see https://ddev.com/s/port-conflict
v1.23.5: Pulling from ddev/ddev-webserver
d82880e18c4b: Pull complete
Digest: sha256:1e71e7ed38cbceaa1a7af0a6fb2328331cd1788d158be730080ea9441bebe341
Status: Downloaded newer image for ddev/ddev-webserver:v1.23.5
docker.io/ddev/ddev-webserver:v1.23.5
stable: Pulling from library/busybox
2fce1e0cdfc5: Pull complete
Digest: sha256:c230832bd3b0be59a6c47ed64294f9ce71e91b327957920b6929a0caa8353140
Status: Downloaded newer image for busybox:stable
docker.io/library/busybox:stable
Using default tag: latest
latest: Pulling from ddev/ddev-utilities
43c4264eed91: Pull complete
134d3819e0e6: Pull complete
Digest: sha256:97822ff9a06416ea8ba09853427565b351556fb08a3b1ef944101fcf829b2710
Status: Downloaded newer image for ddev/ddev-utilities:latest
docker.io/ddev/ddev-utilities:latest
v1.23.5: Pulling from ddev/ddev-ssh-agent
fa0650a893c2: Pull complete
64258e6c9b2f: Pull complete
ff69a4ad4055: Pull complete
4f4fb700ef54: Pull complete
30b6407d2d1a: Pull complete
9d09b6626d3b: Pull complete
Digest: sha256:57ea8badb44f5958cf35fe486e11e3bca1d1f67c8f0906480ba3838d27eee13f
Status: Downloaded newer image for ddev/ddev-ssh-agent:v1.23.5
docker.io/ddev/ddev-ssh-agent:v1.23.5
v1.23.5: Pulling from ddev/ddev-traefik-router
ec99f8b99825: Pull complete
8168e2be9d20: Pull complete
4c4266770910: Pull complete
67e108beaf7a: Pull complete
1d1c4e8c6d7e: Pull complete
1fce12dcf09c: Pull complete
31ad6a19afe3: Pull complete
17346b8ba07d: Pull complete
Digest: sha256:9931eda2d7152952a03c376c155de0509517e2d0b60fc0f7a5624851d64e6d6d
Status: Downloaded newer image for ddev/ddev-traefik-router:v1.23.5
docker.io/ddev/ddev-traefik-router:v1.23.5
 Volume "ddev-ssh-agent_dot_ssh"  Created
 Volume "ddev-ssh-agent_socket_dir"  Created
 Container ddev-ssh-agent  Created
 Container ddev-ssh-agent  Started
ssh-agent container is running: If you want to add authentication to the ssh-agent container, run 'ddev auth ssh' to enable your keys.
time="2024-10-25T13:18:28+02:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.next.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
time="2024-10-25T13:18:28+02:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.selenium-chrome.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
v1.23.5: Pulling from ddev/ddev-dbserver-mariadb-10.4
9ea8908f4765: Pull complete
1b268493d4d2: Pull complete
23c574624b10: Pull complete
21f121a86c05: Pull complete
78e65804d0db: Pull complete                                                                                             4e4647f3a286: Pull complete                                                                                             6de3379de9f7: Pull complete
7907dba24a2b: Pull complete
2c8bf7b113e6: Pull complete
4f4fb700ef54: Pull complete                                                                                             f3c073d18e32: Pull complete                                                                                             db8b0e330caf: Pull complete                                                                                             c3c635177687: Pull complete
6defea7f2412: Pull complete
5cec622140c1: Pull complete
365c2ff88545: Pull complete
41b1ab44ca44: Pull complete
92facb55b35c: Pull complete
28160628dbda: Pull complete
128fad6ccc8a: Pull complete
62a4535c6844: Pull complete
7b7940577cf4: Pull complete
a2c5f9715003: Pull complete
8cf1c832fa48: Pull complete
1e120468bc37: Pull complete
Digest: sha256:5aa379aeef7b12a111862b090b921fe9cab3df8af0f4250be5ff2ea152ef06f3
Status: Downloaded newer image for ddev/ddev-dbserver-mariadb-10.4:v1.23.5
docker.io/ddev/ddev-dbserver-mariadb-10.4:v1.23.5
18-buster-slim: Pulling from library/node
b338562f40a7: Pull complete
874bf4d93720: Pull complete
b16337721583: Pull complete
7d955db85b85: Pull complete
2c706596bd17: Pull complete
Digest: sha256:8ddce69c50b5e3c2e7abc611f30d76747b1baa1f8b1e442cfb5f7a4ac8ee798b
Status: Downloaded newer image for node:18-buster-slim
docker.io/library/node:18-buster-slim
4.1.4-20220429: Pulling from seleniarm/standalone-chromium
6aefca2dc61d: Pulling fs layer
32605ffb5353: Pulling fs layer
32605ffb5353: Downloading [======>                                            ]  14.44MB/105.3MB
4c1b389d2ff5: Download complete                                                                                         a188dd90c028: Download complete
0c359b9faa48: Download complete
2f7efa2c32e3: Download complete
589c1bcaa24f: Downloading [=======================================>           ]  17.37MB/21.8MB
fa07f28814a4: Waiting
79e50f8fd7e1: Waiting
4712f76ff662: Waiting
948d4aba37ea: Waiting                                                                                                   6fbd37426cec: Waiting
154ef0ae7e06: Waiting                                                                                                   4f4fb700ef54: Waiting
01e877eeb0f8: Waiting                                                                                                   f64a228d3e8f: Waiting
563698b9335f: Waiting                                                                                                   b3b1df4ab2c9: Waiting
fdbb62a3913e: Waiting
7f4b135d7319: Waiting
7d7a34350a3b: Waiting
7a5773ac7406: Waiting
0bc6ed931670: Waiting
1441143845dd: Waiting
9453581cacde: Waiting
eb991cdffb32: Waiting
4c05f3d6fa7d: Waiting
d26b39ba28ea: Waiting
259e5dd00dc7: Waiting
1076650a1ca1: Waiting
.......................
Digest: sha256:ecf74556cdeee48382e555a377ddb12d36161bd33349dc79290f733f763df711
Status: Downloaded newer image for node:16-alpine3.15
docker.io/library/node:16-alpine3.15
Building project images...
.....................................Project images built in 40s.
 Network ddev-packt_default  Created
 Container ddev-packt-storybook  Created
 Container ddev-packt-db  Created
 Container ddev-packt-next  Created
 Container ddev-packt-selenium-chrome  Created
 Container ddev-packt-web  Created
 Container ddev-packt-storybook  Started
 Container ddev-packt-next  Started
 Container ddev-packt-db  Started
 Container ddev-packt-selenium-chrome  Started
 Container ddev-packt-web  Started
Waiting for containers to become ready: [web db]Digest: sha256:ecf74556cdeee48382e555a377ddb12d36161bd33349dc79290f733f763df711
Status: Downloaded newer image for node:16-alpine3.15
docker.io/library/node:16-alpine3.15
Building project images...
.....................................Project images built in 40s.
 Network ddev-packt_default  Created
 Container ddev-packt-storybook  Created
 Container ddev-packt-db  Created
 Container ddev-packt-next  Created
 Container ddev-packt-selenium-chrome  Created
 Container ddev-packt-web  Created
 Container ddev-packt-storybook  Started
 Container ddev-packt-next  Started
 Container ddev-packt-db  Started
 Container ddev-packt-selenium-chrome  Started
 Container ddev-packt-web  Started
Waiting for containers to become ready: [web db]
Waiting for containers to become ready: [web db]
Warning: command 'n install 16' run as 'jpmena' failed with exit code 124:
Command 'n install 16' timed out after 30 seconds
Starting ddev-router if necessary...
 Container ddev-router  Created
 Container ddev-router  Started
Waiting 120s for additional project containers [ddev-packt-next ddev-packt-selenium-chrome ddev-packt-storybook] to become ready...
Some components of the project packt were not installed properly.
The project is running anyway, but see the warnings above for details.
If offline, run 'ddev restart' once you are back online.
If online, check your connection and run 'ddev restart' later.
If this seems to be a config issue, update it accordingly.
Successfully started packt
Your project can be reached at https://packt.ddev.site
See 'ddev describe' for alternate URLs.
```
* I restart the containers and I have the same problem
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev start
Starting packt...
Port 80 is busy, using 33001 instead, see https://ddev.com/s/port-conflict
time="2024-10-25T14:47:03+02:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.next.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
time="2024-10-25T14:47:03+02:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.selenium-chrome.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
Building project images...
.Project images built in 2s.
 Container ddev-packt-selenium-chrome  Running
 Container ddev-packt-next  Running
 Container ddev-packt-storybook  Running
 Container ddev-packt-db  Recreate
 Container ddev-packt-web  Recreate
 Container ddev-packt-db  Recreated
 Container ddev-packt-web  Recreated
 Container ddev-packt-db  Started
 Container ddev-packt-web  Started
Waiting for containers to become ready: [web db]
Warning: command 'n install 16' run as 'jpmena' failed with exit code 124: # problem here !!!
Command 'n install 16' timed out after 30 seconds
Starting ddev-router if necessary...
 Container ddev-router  Recreate
 Container ddev-router  Recreated
 Container ddev-router  Started
Waiting 120s for additional project containers [ddev-packt-next ddev-packt-selenium-chrome ddev-packt-storybook] to become ready...
Some components of the project packt were not installed properly.
The project is running anyway, but see the warnings above for details.
If offline, run 'ddev restart' once you are back online.
If online, check your connection and run 'ddev restart' later.
If this seems to be a config issue, update it accordingly.
Successfully started packt
Your project can be reached at https://packt.ddev.site
See 'ddev describe' for alternate URLs.
```
* I get the warning/error see console above I I get the **403 forbidden** when trying to access [https://packt.ddev.site](https://packt.ddev.site) 
* I issued the [issue 60 on the Github Website of the Book](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/60)
## I seems to be normal no webstite has still be installed 
* Do not I to install the composer integration of ddev ?
# 10 ddev build
* installs all the 183 composer dependencies
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev build
Installing dependencies from lock file (including require-dev)
Verifying lock file contents can be installed on current platform.
Package operations: 185 installs, 0 updates, 0 removals
  - Downloading composer/installers (v2.2.0)
  - Downloading drupal/core-composer-scaffold (10.1.1)
  - Downloading drupal/core-project-message (10.1.1)
  - Downloading cweagans/composer-patches (1.7.3)
  - Downloading phpstan/phpstan (1.10.25)
  - Downloading phpstan/extension-installer (1.3.1)
  - Downloading squizlabs/php_codesniffer (3.7.2)
  - Downloading dealerdirect/phpcodesniffer-composer-installer (v1.0.0)
  - Downloading composer/ca-bundle (1.3.6)
  - Downloading symfony/finder (v6.3.0)
  - Downloading composer/pcre (3.1.0)
  - Downloading composer/class-map-generator (1.1.0)
  - Downloading composer/metadata-minifier (1.0.0)
  - Downloading composer/spdx-licenses (1.5.7)
  - Downloading psr/log (3.0.0)
  - Downloading composer/xdebug-handler (3.0.3)
  - Downloading symfony/polyfill-mbstring (v1.27.0)
  - Downloading symfony/polyfill-intl-normalizer (v1.27.0)
  - Downloading symfony/polyfill-intl-grapheme (v1.27.0)
  - Downloading symfony/polyfill-ctype (v1.27.0)
  - Downloading symfony/string (v6.3.0)
  - Downloading psr/container (2.0.2)
  - Downloading symfony/service-contracts (v3.3.0)
  - Downloading symfony/deprecation-contracts (v3.3.0)
  - Downloading symfony/console (v6.3.0)
  - Downloading consolidation/log (3.0.0)
  - Downloading dflydev/dot-access-data (v3.0.2)
  - Downloading consolidation/output-formatters (4.3.2)
  - Downloading symfony/filesystem (v6.3.1)
  - Downloading composer/semver (3.3.2)
  - Downloading consolidation/self-update (2.2.0)
  - Downloading paragonie/random_compat (v9.99.100)
  - Downloading defuse/php-encryption (v2.4.0)
  - Downloading twig/twig (v3.6.1)
  - Downloading symfony/yaml (v6.3.0)
  - Downloading symfony/translation-contracts (v3.3.0)
  - Downloading symfony/polyfill-php80 (v1.27.0)
  - Downloading symfony/polyfill-php83 (v1.27.0)
  - Downloading symfony/validator (v6.3.1)
  - Downloading symfony/serializer (v6.3.1)
  - Downloading symfony/routing (v6.3.1)
  - Downloading symfony/http-foundation (v6.3.1)
  - Downloading psr/http-message (1.1)
  - Downloading symfony/psr-http-message-bridge (v2.2.0)
  - Downloading symfony/process (v6.3.0)
  - Downloading symfony/polyfill-iconv (v1.27.0)
  - Downloading symfony/polyfill-php72 (v1.27.0)
  - Downloading symfony/polyfill-intl-idn (v1.27.0)
  - Downloading symfony/mime (v6.3.0)
  - Downloading psr/event-dispatcher (1.0.0)
  - Downloading symfony/event-dispatcher-contracts (v3.3.0)
  - Downloading symfony/event-dispatcher (v6.3.0)
  - Downloading symfony/var-dumper (v6.3.1)
  - Downloading symfony/error-handler (v6.3.0)
  - Downloading symfony/http-kernel (v6.3.1)
  - Downloading symfony/var-exporter (v6.3.0)
  - Downloading symfony/dependency-injection (v6.3.1)
  - Downloading sebastian/diff (4.0.5)
  - Downloading pear/pear_exception (v1.0.2)
  - Downloading pear/console_getopt (v1.4.3)
  - Downloading pear/pear-core-minimal (v1.10.13)
  - Downloading pear/archive_tar (1.4.14)
  - Downloading mck89/peast (v1.15.2)
  - Downloading masterminds/html5 (2.8.0)
  - Downloading ralouphie/getallheaders (3.0.3)
  - Downloading psr/http-factory (1.0.2)
  - Downloading guzzlehttp/psr7 (2.5.0)
  - Downloading psr/http-client (1.0.2)
  - Downloading guzzlehttp/promises (2.0.0)
  - Downloading guzzlehttp/guzzle (7.7.0)
  - Downloading doctrine/deprecations (v1.1.1)
  - Downloading doctrine/lexer (2.1.0)
  - Downloading egulias/email-validator (4.0.1)
  - Downloading psr/cache (3.0.0)
  - Downloading doctrine/annotations (1.14.3)
  - Downloading asm89/stack-cors (v2.1.1)
  - Downloading drupal/core (10.1.1)
  - Downloading drupal/ckeditor5_dev (1.0.3)
  - Downloading chi-teck/drupal-code-generator (2.6.2)
  - Downloading drupal/cl_generator (2.0.0-beta1)
  - Downloading drupal/components (3.0.0-beta3)
  - Downloading symfony/phpunit-bridge (v6.3.1)
  - Downloading symfony/lock (v6.3.1)
  - Downloading symfony/dom-crawler (v6.3.1)
  - Downloading symfony/css-selector (v6.3.0)
  - Downloading symfony/browser-kit (v6.3.0)
  - Downloading sebastian/version (3.0.2)
  - Downloading sebastian/type (3.2.1)
  - Downloading sebastian/resource-operations (3.0.3)
  - Downloading sebastian/recursion-context (4.0.5)
  - Downloading sebastian/object-reflector (2.0.4)
  - Downloading sebastian/object-enumerator (4.0.4)
  - Downloading sebastian/global-state (5.0.5)
  - Downloading sebastian/exporter (4.0.5)
  - Downloading sebastian/environment (5.1.5)
  - Downloading sebastian/comparator (4.0.8)
  - Downloading sebastian/code-unit (1.0.8)
  - Downloading sebastian/cli-parser (1.0.1)
  - Downloading phpunit/php-timer (5.0.3)
  - Downloading phpunit/php-text-template (2.0.4)
  - Downloading phpunit/php-invoker (3.1.1)
  - Downloading phpunit/php-file-iterator (3.0.6)
  - Downloading theseer/tokenizer (1.2.1)
  - Downloading nikic/php-parser (v4.16.0)
  - Downloading sebastian/lines-of-code (1.0.3)
  - Downloading sebastian/complexity (2.0.2)
  - Downloading sebastian/code-unit-reverse-lookup (2.0.3)
  - Downloading phpunit/php-code-coverage (9.2.26)
  - Downloading phar-io/version (3.2.1)
  - Downloading phar-io/manifest (2.0.3)
  - Downloading myclabs/deep-copy (1.11.1)
  - Downloading doctrine/instantiator (2.0.0)
  - Downloading phpunit/phpunit (9.6.10)
  - Downloading phpstan/phpstan-phpunit (1.3.13)
  - Downloading webmozart/assert (1.11.0)
  - Downloading phpstan/phpdoc-parser (1.22.1)
  - Downloading phpdocumentor/reflection-common (2.2.0)
  - Downloading phpdocumentor/type-resolver (1.7.2)
  - Downloading phpdocumentor/reflection-docblock (5.3.0)
  - Downloading phpspec/prophecy (v1.17.0)
  - Downloading phpspec/prophecy-phpunit (v2.0.2)
  - Downloading mikey179/vfsstream (v1.6.11)
  - Downloading webflo/drupal-finder (1.2.2)
  - Downloading mglaman/phpstan-drupal (1.1.36)
  - Downloading justinrainbow/json-schema (5.2.12)
  - Downloading instaclick/php-webdriver (1.4.16)
  - Downloading slevomat/coding-standard (8.13.1)
  - Downloading sirbrillig/phpcs-variable-analysis (v2.11.16)
  - Downloading drupal/coder (8.3.20)
  - Downloading symfony/polyfill-php81 (v1.27.0)
  - Downloading symfony/polyfill-php73 (v1.27.0)
  - Downloading seld/signal-handler (2.0.1)
  - Downloading seld/phar-utils (1.2.1)
  - Downloading seld/jsonlint (1.10.0)
  - Downloading react/promise (v2.10.0)
  - Downloading composer/composer (2.5.8)
  - Downloading colinodell/psr-testlogger (v1.2.0)
  - Downloading behat/mink (v1.10.0)
  - Downloading behat/mink-selenium2-driver (v1.6.0)
  - Downloading behat/mink-browserkit-driver (v2.1.0)
  - Downloading drupal/critical_css (1.19.0)
  - Downloading drupal/default_content (2.0.0-alpha2)
  - Downloading drupal/easy_breadcrumb (2.0.5)
  - Downloading drupal/formdazzle (3.0.0)
  - Downloading monolog/monolog (3.4.0)
  - Downloading drupal/monolog (3.0.0)
  - Downloading galbar/jsonpath (1.3.1)
  - Downloading drupal/subrequests (3.0.7)
  - Downloading league/uri-interfaces (2.3.0)
  - Downloading league/uri (6.8.0)
  - Downloading league/event (2.2.0)
  - Downloading psr/clock (1.0.0)
  - Downloading lcobucci/clock (3.0.0)
  - Downloading lcobucci/jwt (4.3.0)
  - Downloading league/oauth2-server (8.5.3)
  - Downloading steverhoades/oauth2-openid-connect-server (v2.5.0)
  - Downloading drupal/consumers (1.17.0)
  - Downloading drupal/simple_oauth (5.2.3)
  - Downloading drupal/token (1.12.0)
  - Downloading drupal/ctools (4.0.4)
  - Downloading drupal/pathauto (1.11.0)
  - Downloading drupal/decoupled_router (2.0.4)
  - Downloading drupal/next (1.6.3)
  - Downloading drupal/entity_reference_revisions (1.10.0)
  - Downloading drupal/paragraphs (1.15.0)
  - Downloading drupal/restui (1.21.0)
  - Downloading drupal/search_api (1.29.0)
  - Downloading drupal/twig_tweak (3.2.1)
  - Downloading psy/psysh (v0.11.18)
  - Downloading league/container (4.2.0)
  - Downloading enlightn/security-checker (v1.10.0)
  - Downloading grasmash/expander (3.0.0)
  - Downloading consolidation/config (2.1.2)
  - Downloading consolidation/site-alias (4.0.1)
  - Downloading consolidation/site-process (5.2.0)
  - Downloading phootwork/lang (v3.2.2)
  - Downloading phootwork/collection (v3.2.2)
  - Downloading phpowermove/docblock (v4.0)
  - Downloading consolidation/annotated-command (4.9.1)
  - Downloading consolidation/robo (4.0.6)
  - Downloading consolidation/filter-via-dot-access-data (2.0.2)
  - Downloading drush/drush (11.6.0)
  - Downloading symfony/stopwatch (v6.3.0)
  76/183 [===========>----------------]  41%
   [notice] Performed install task: install_finished
 [success] Installation complete.
>  [notice] Successfully indexed 14 items on Contents.
>  [notice] Message: Successfully indexed 14 items.
>
 [success] Cache rebuild complete.
yarn install v1.22.22
[1/4] Resolving packages...
[2/4] Fetching packages...
[3/4] Linking dependencies...
[4/4] Building fresh packages...
success Saved lockfile.
Done in 0.11s.
yarn run v1.22.22
$ ls
alps_trips.info.yml  node_modules  package.json  yarn.lock
Done in 0.05s.

> storybook@1.0.0 generate-css
> postcss src/tailwind.css -o public/main.css

Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
  ```
  * **https://packt.ddev.site/** starts a website with no CSS
* Stopping the containers
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev stop
 Container ddev-packt-db  Stopped
 Container ddev-packt-storybook  Stopped
 Container ddev-packt-next  Stopped
 Container ddev-packt-web  Stopped
 Container ddev-packt-selenium-chrome  Stopped
 Container ddev-packt-storybook  Stopped
 Container ddev-packt-next  Stopped
 Container ddev-packt-db  Stopped
 Container ddev-packt-web  Stopped
 Container ddev-packt-db  Removed
 Container ddev-packt-web  Removed
 Container ddev-packt-selenium-chrome  Stopped
 Container ddev-packt-selenium-chrome  Removed
 Container ddev-packt-next  Removed
 Container ddev-packt-storybook  Removed
 Network ddev-packt_default  Removed
Project packt has been stopped.
```
* Now I have vendor and web under **~/D10Theming/Modernizing-Drupal-10-Theme-Development**
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ll web
total 96
drwxr-xr-x  8 jpmena jpmena 4096 Oct 25 15:05 ./
drwxr-xr-x 15 jpmena jpmena 4096 Oct 25 15:05 ../
-rw-r--r--  1 jpmena jpmena 1025 Oct 25 15:05 .csslintrc
-rw-r--r--  1 jpmena jpmena  151 Oct 25 15:05 .eslintignore
-rw-r--r--  1 jpmena jpmena   41 Oct 25 15:05 .eslintrc.json
-rw-r--r--  1 jpmena jpmena   14 Oct 25 12:23 .gitignore
-rw-r--r--  1 jpmena jpmena 2467 Oct 25 15:05 .ht.router.php
-rw-r--r--  1 jpmena jpmena 8024 Oct 25 15:05 .htaccess
-rw-r--r--  1 jpmena jpmena   94 Oct 25 15:05 INSTALL.txt
-rw-r--r--  1 jpmena jpmena 3205 Oct 25 15:05 README.md
-rw-r--r--  1 jpmena jpmena  315 Oct 25 15:05 autoload.php
drwxr-xr-x 14 jpmena jpmena 4096 Oct 25 15:05 core/
-rw-r--r--  1 jpmena jpmena 1495 Oct 25 15:05 example.gitignore
-rw-r--r--  1 jpmena jpmena  549 Oct 25 15:05 index.php
drwxr-xr-x  2 jpmena jpmena 4096 Oct 25 12:23 js_client/
drwxr-xr-x  4 jpmena jpmena 4096 Oct 25 15:05 modules/
-rwxr-xr-x  1 jpmena jpmena  249 Oct 25 12:23 phpcs.xml.dist*
drwxr-xr-x  3 jpmena jpmena 4096 Oct 25 12:23 profiles/
-rw-r--r--  1 jpmena jpmena 1706 Oct 25 15:05 robots.txt
drwxr-xr-x  3 jpmena jpmena 4096 Oct 25 12:23 sites/
drwxr-xr-x  3 jpmena jpmena 4096 Oct 25 12:23 themes/
-rw-r--r--  1 jpmena jpmena  804 Oct 25 15:05 update.php
-rw-r--r--  1 jpmena jpmena 4039 Oct 25 15:05 web.config
```
* *.ddev/commands/db/README.txt* is actually empty I think we will add our scripts following the book code
## The interesting commands:
* ddev start/stop (problem it downloads/destroy the image)
* ddev describe
* ddev drush
* ddev ssh
# 12 (blocked the 26/10/2024)
## [Issue 61](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/61)
* I can't go further on as long as [My 61 Issue on the Book's Github account](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/61) is not solved
* When I start/restart the project (thi 26/10/2024 4 p.m.) ddev downloads once again all the images
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev restart
Restarting project packt...
Port 80 is busy, using 33000 instead, see https://ddev.com/s/port-conflict
v1.23.5: Pulling from ddev/ddev-webserver
d82880e18c4b: Downloading [=======================>                           ]  244.5MB/517.3MB
```
* should I use *ddev poweroff* instead of *ddev stop* ?
* I also ask the question on the [DDEV project on GitHub](https://github.com/ddev/ddev/issues/6653)
  * it is the [issue 6653](https://github.com/ddev/ddev/issues/6653) 
## Reading the page 12
* [*web/modules/contrib/default_content*](https://www.drupal.org/project/default_content) when called creates a the Demo Module *web/modules/custom/alps_demo/alps_demo.info.yml* with contents! Whe use it as is
# p 14 the website at the main branch
* It should be like indicated in the [ERRATA.md](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/ERRATA.md) which means [this]().
  * The version in the book corresponds to the [final branch](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/tree/final)
