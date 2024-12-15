# I cannot access *http://packt.ddev.site:6006/*
* Answer 404 page not found
  * The port is accessible 
* I created the [Issue 63](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/63)
  * with the following explanations
* enventhough
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev start
Starting packt...
Port 80 is busy, using 33000 instead, see https://ddev.com/s/port-conflict
time="2024-11-29T16:21:41+01:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.next.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
time="2024-11-29T16:21:41+01:00" level=warning msg="/home/jpmena/D10Theming/Modernizing-Drupal-10-Theme-Development/.ddev/docker-compose.selenium-chrome.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
Building project images...
.Project images built in 2s.
 Network ddev-packt_default  Created
 Container ddev-packt-storybook  Created
 Container ddev-packt-db  Created
 Container ddev-packt-next  Created
 Container ddev-packt-selenium-chrome  Created
 Container ddev-packt-web  Created
 Container ddev-packt-next  Started
 Container ddev-packt-db  Started
 Container ddev-packt-storybook  Started # no problem the storybook container is said to be started
 Container ddev-packt-selenium-chrome  Started
 Container ddev-packt-web  Started
Waiting for containers to become ready: [web db]
Starting ddev-router if necessary...
 Container ddev-router  Created
 Container ddev-router  Started
Waiting 120s for additional project containers [ddev-packt-selenium-chrome ddev-packt-next ddev-packt-storybook] to become ready...
Successfully started packt
Your project can be reached at https://packt.ddev.site
See 'ddev describe' for alternate URLs.
```
* When I access that container and run the ddev commands
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development/patches$ docker exec -it ddev-packt-storybook sh
/storybook # ls -l
total 992
drwxr-xr-x  754 root     root         24576 Oct 25 12:54 node_modules
-rw-r--r--    1 node     node          1862 Oct 25 10:23 package.json
-rw-r--r--    1 node     node           196 Oct 25 10:23 postcss.config.js
drwxr-xr-x    3 node     node          4096 Oct 25 13:05 public
drwxr-xr-x    2 node     node          4096 Oct 25 10:23 src
drwxr-xr-x    9 node     node          4096 Oct 25 10:23 stories
-rw-r--r--    1 node     node          1090 Oct 25 10:23 tailwind.config.js
-rw-r--r--    1 node     node        538979 Oct 25 10:23 yarn-error.log
-rw-r--r--    1 node     node        422310 Oct 25 10:23 yarn.lock
/storybook # yarn install
yarn install v1.22.19
[1/4] Resolving packages...
success Already up-to-date. # nothing to do all already installe
Done in 0.79s.
/storybook # npm run storybook # I run the second command which the container has to run when created

> storybook@1.0.0 storybook
> storybook dev -p 6006

@storybook/cli v7.0.18

✔ Port 6006 is not available. Would you like to run Storybook on port 6007 instead? … yes # I answer yes
## A lot of errors messages
[Error: EACCES: permission denied, mkdir '/storybook/node_modules/.cache'] { # cause of the crash ?
  errno: -13,
  code: 'EACCES',
  syscall: 'mkdir',
  path: '/storybook/node_modules/.cache'
}
/storybook # exit
```
## I access the same container using ddev commands
```bash
jpmena@LAPTOP-E2MJK1UO:~/D10Theming/Modernizing-Drupal-10-Theme-Development$ ddev ssh --service storybook
```
* *storybook* is the name of a service, not of a container see [ddev compose for storybook](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/blob/main/.ddev/docker-compose.storybook.yaml)
* I try the commands
```yaml
command:
      - /bin/sh
      - -c
      - |
        yarn install && npm run storybook
    container_name: "ddev-${DDEV_SITENAME}-storybook"
```
* And I get the same error
## I created the [Issue 63 on Github](https://github.com/PacktPublishing/Modernizing-Drupal-10-Theme-Development/issues/63) 
# 95
* the author proposes other design tools
## [Emulsify](https://www.emulsify.info/)
## [WingSuite](https://wingsuit-designsystem.github.io/)
* Works with Storybook
## [Europa Component Library](https://ec.europa.eu/component-library/playground/eu/?path=/story/components-accordion--default&globals=viewport:responsive)