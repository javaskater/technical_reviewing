# p 7
* in the example there are using a ref
* remeber me what is ref for ? 
  * [answer 1 to this Stack Overflow Question](https://stackoverflow.com/questions/75931136/someone-can-explain-me-what-ref-function-do)
# p 8 creating a VueJS3 application using Vite
* The environment on my desktop PC
```bash
jmena01@m077-2281091:~/CONSULTANT$ node --version
v20.18.1
jmena01@m077-2281091:~/CONSULTANT$ npm --version
10.8.2
jmena01@m077-2281091:~/CONSULTANT$ /usr/bin/node --version
v18.19.1 # it is not that one used
jmena01@m077-2281091:~/CONSULTANT$ /home/jmena01/.volta/bin/node --version
v20.18.1 # but it is ths one
jmena01@m077-2281091:~/CONSULTANT$ tail -10 ~/.bashrc
export https_proxy="http://{proxy_url}:{proxy_port}/"
export ftp_proxy="http://{proxy_url}:{proxy_port}/"
export no_proxy="localhost,127.0.0.1"
export HTTP_PROXY="http://{proxy_url}:{proxy_port}/"
export HTTPS_PROXY="http://{proxy_url}:{proxy_port}/"
export FTP_PROXY="http://{proxy_url}:{proxy_port}/"
export NO_PROXY="localhost,127.0.0.1"
# Node JS
export VOLTA_HOME="$HOME/.volta" # theis version of node has priority
export PATH="$VOLTA_HOME/bin:$PATH"
```
## Creating the app
* The real command is:
```bash
jmena01@m077-2281091:~/CONSULTANT$ npm create vite@latest
Need to install the following packages:
create-vite@8.0.1
Ok to proceed? (y) 

npm warn EBADENGINE Unsupported engine {
npm warn EBADENGINE   package: 'create-vite@8.0.1',
npm warn EBADENGINE   required: { node: '^20.19.0 || >=22.12.0' },
npm warn EBADENGINE   current: { node: 'v20.18.1', npm: '10.8.2' }
npm warn EBADENGINE }

> npx
> create-vite

│
◇  Project name:
│  pinterest-app-clone
│
◇  Select a framework:
│  Vue
│
◇  Select a variant:
│  JavaScript
│
◇  Use rolldown-vite (Experimental)?:
│  No
│
◇  Install with npm and start now?
│  Yes
│
◇  Scaffolding project in /home/jmena01/CONSULTANT/pinterest-app-clone...
│
◇  Installing dependencies with npm...
npm warn EBADENGINE Unsupported engine {
npm warn EBADENGINE   package: '@vitejs/plugin-vue@6.0.1',
npm warn EBADENGINE   required: { node: '^20.19.0 || >=22.12.0' },
npm warn EBADENGINE   current: { node: 'v20.18.1', npm: '10.8.2' }
npm warn EBADENGINE }
npm warn EBADENGINE Unsupported engine {
npm warn EBADENGINE   package: 'vite@7.1.7',
npm warn EBADENGINE   required: { node: '^20.19.0 || >=22.12.0' },
npm warn EBADENGINE   current: { node: 'v20.18.1', npm: '10.8.2' }
npm warn EBADENGINE }

added 34 packages, and audited 35 packages in 4s

6 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
│
◇  Starting dev server...

> pinterest-app-clone@0.0.0 dev
> vite

You are using Node.js 20.18.1. Vite requires Node.js version 20.19+ or 22.12+. Please upgrade your Node.js version.

  VITE v7.1.7  ready in 188 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```
* I point firefox to http://localhost:5173/
### And If I want to restart it ?
CTRL + C to stop the app
* restart it
```bash
jmena01@m077-2281091:~/CONSULTANT$ cd pinterest-app-clone/
jmena01@m077-2281091:~/CONSULTANT/pinterest-app-clone$ npm run dev

> pinterest-app-clone@0.0.0 dev
> vite

You are using Node.js 20.18.1. Vite requires Node.js version 20.19+ or 22.12+. Please upgrade your Node.js version.

  VITE v7.1.7  ready in 175 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

```

## Creating a strapi project
```bash
jmena01@m077-2281091:~/CONSULTANT$ npx create-strapi-app strapi-api --quickstart
Need to install the following packages:
create-strapi-app@5.24.1
Ok to proceed? (y) y


 Strapi   v5.24.1 🚀 Let's create your new project

[ERROR] An error occurred while trying to interact with Strapi servers. Use strapi deploy command once the project is generated.
? Participate in anonymous A/B testing (to improve Strapi)? No

 Strapi   Creating a new application at /home/jmena01/CONSULTANT/strapi-api

   deps   Installing dependencies with npm
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm warn deprecated mailcomposer@3.12.0: This project is unmaintained
npm warn deprecated buildmail@3.10.0: This project is unmaintained
npm warn deprecated boolean@3.2.0: Package no longer supported. Contact Support at https://www.npmjs.com/support for more info.

added 1267 packages, and audited 1268 packages in 36s

192 packages are looking for funding
  run `npm fund` for details

15 vulnerabilities (13 low, 2 moderate)

To address issues that do not require attention, run:
  npm audit fix

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.

       ✓  Dependencies installed

    git   Initializing git repository.

       ✓  Initialized a git repository.

 Strapi   Your application was created!
          Available commands in your project:
          
          Start Strapi in watch mode. (Changes in Strapi project files will trigger a server restart)
          npm run develop
          
          Start Strapi without watch mode.
          npm run start
          
          Build Strapi admin panel.
          npm run build
          
          Deploy Strapi project.
          npm run deploy
          
          Display all available commands.
          npm run strapi

          To get started run
          
          cd /home/jmena01/CONSULTANT/strapi-api
          npm run develop

    Run   Running your Strapi application

> strapi-api@0.1.0 develop
> strapi develop

⠹ Loading Strapi[2025-09-26 16:12:53.183] info: The Users & Permissions plugin automatically generated a jwt secret and stored it in .env under the name JWT_SECRET.
[2025-09-26 16:12:53.184] warn: admin.auth.options.expiresIn is deprecated and will be removed in Strapi 6. Please configure admin.auth.sessions.maxRefreshTokenLifespan and admin.auth.sessions.maxSessionLifespan.
⠋ Building build context
⠸ Loading Strapi[INFO] Including the following ENV variables as part of the JS bundle:
    - ADMIN_PATH
    - STRAPI_ADMIN_BACKEND_URL
    - STRAPI_TELEMETRY_DISABLED
    - STRAPI_ANALYTICS_URL
✔ Building build context (49ms)
✔ Creating admin (222ms)
✔ Loading Strapi (5700ms)
✔ Generating types (167ms)
✔ Cleaning dist dir (7ms)
✔ Compiling TS (961ms)

 Project information                                                          

┌────────────────────┬──────────────────────────────────────────────────┐
│ Time               │ Fri Sep 26 2025 16:12:57 GMT+0200 (heure d’été … │
│ Launched in        │ 6833 ms                                          │
│ Environment        │ development                                      │
│ Process PID        │ 104660                                           │
│ Version            │ 5.24.1 (node v20.18.1)                           │
│ Edition            │ Community                                        │
│ Database           │ sqlite                                           │
│ Database name      │ .tmp/data.db                                     │
└────────────────────┴──────────────────────────────────────────────────┘

 Actions available                                                            

One more thing...
Create your first administrator 💻 by going to the administration panel at:

┌─────────────────────────────┐
│ http://localhost:1337/admin │
└─────────────────────────────┘

[2025-09-26 16:12:57.852] info: Strapi started successfully
[2025-09-26 16:12:57.999] http: GET /admin (37 ms) 200
[2025-09-26 16:12:59.304] http: GET /admin/project-type (2 ms) 200
[2025-09-26 16:12:59.305] http: GET /favicon.ico (0 ms) 200
[2025-09-26 16:12:59.374] http: GET /admin/init (2 ms) 200
```
* It automatically opens a new Firefox tab to http://localhost:1337/admin/auth/register-admin 
* The email pythonrubylang@gmail.com and the password is research2Strapi
* It brings me to http://localhost:1337/admin
* CTRL +C to shut it down
### I want to restart it
* calling **npm run dev** inside the project is enough
```bash
jmena01@m077-2281091:~/CONSULTANT$ cd strapi-api/ # going inside the project
jmena01@m077-2281091:~/CONSULTANT/strapi-api$ npm run dev # just call that

> strapi-api@0.1.0 dev
> strapi develop

✔ Cleaning dist dir (6ms)
⠹ Loading Strapi[2025-09-26 16:18:12.181] warn: admin.auth.options.expiresIn is deprecated and will be removed in Strapi 6. Please configure admin.auth.sessions.maxRefreshTokenLifespan and admin.auth.sessions.maxSessionLifespan.
⠋ Building build context
⠸ Loading Strapi[INFO] Including the following ENV variables as part of the JS bundle:
    - ADMIN_PATH
    - STRAPI_ADMIN_BACKEND_URL
    - STRAPI_TELEMETRY_DISABLED
    - STRAPI_ANALYTICS_URL
✔ Building build context (44ms)
✔ Creating admin (206ms)
✔ Loading Strapi (675ms)
✔ Generating types (141ms)
✔ Cleaning dist dir (3ms)
✔ Compiling TS (950ms)

 Project information                                                          

┌────────────────────┬──────────────────────────────────────────────────┐
│ Time               │ Fri Sep 26 2025 16:18:13 GMT+0200 (heure d’été … │
│ Launched in        │ 1772 ms                                          │
│ Environment        │ development                                      │
│ Process PID        │ 105953                                           │
│ Version            │ 5.24.1 (node v20.18.1)                           │
│ Edition            │ Community                                        │
│ Database           │ sqlite                                           │
│ Database name      │ .tmp/data.db                                     │
└────────────────────┴──────────────────────────────────────────────────┘

 Actions available                                                            

Welcome back!
To access the server ⚡️, go to:
http://localhost:1337

[2025-09-26 16:18:13.582] info: Strapi started successfully
[2025-09-26 16:18:13.762] http: GET /admin (40 ms) 200
[2025-09-26 16:18:14.257] http: GET /admin/project-type (2 ms) 200
[2025-09-26 16:18:14.324] http: GET /admin/init (2 ms) 200
[2025-09-26 16:18:14.338] http: GET /admin/users/me (10 ms) 200
[2025-09-26 16:18:14.351] http: GET /admin/users/me/permissions (13 ms) 200
[2025-09-26 16:18:14.366] http: GET /admin/information (13 ms) 200
[2025-09-26 16:18:14.366] http: GET /admin/telemetry-properties (13 ms) 200
[2025-09-26 16:18:14.408] http: GET /admin/guided-tour-meta (7 ms) 200
[2025-09-26 16:18:14.414] http: GET /admin/license-limit-information (5 ms) 200
[2025-09-26 16:18:14.509] http: GET /content-manager/homepage/recent-documents?action=update (13 ms) 200
[2025-09-26 16:18:14.516] http: GET /content-manager/homepage/recent-documents?action=publish (7 ms) 200
[2025-09-26 16:18:14.524] http: GET /content-manager/homepage/count-documents (8 ms) 200
[2025-09-26 16:18:14.531] http: GET /admin/homepage/key-statistics (6 ms) 200
```