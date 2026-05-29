# My npmrc configuration directory

- this npm configuration is available only for this and the directores underneath it ovverides th $HOME/.npmrc
  - the $HOME/.npmrc accesses only the corporate npm registry

```bash
jmena01@m077-2281091:~$ cd CONSULTANT/
jmena01@m077-2281091:~/CONSULTANT$ touch .npmrc # this npm configuration is available only for this and the directores underneath it ovverides th $HOME/.npmrc
jmena01@m077-2281091:~/CONSULTANT$ vim .npmrc
jmena01@m077-2281091:~/CONSULTANT$ cat .npmrc
http-proxy = http://exampleHost:examplePort/ # to access internet
https-proxy=http://exampleHost:examplePort/
strict-ssl = false
registry = http://registry.npmjs.org/ # I want to access the internet not the corporate repo
jmena01@m077-2281091:~/CONSULTANT$ npm install --save-dev typescript # This module is not present in the corporate repo

added 1 package in 2s
jmena01@m077-2281091:~/CONSULTANT$ ll node_modules/
total 20
drwxr-xr-x  4 jmena01 domain users 4096 mai   21 17:44 ./
drwxr-xr-x 26 jmena01 domain users 4096 mai   21 17:44 ../
drwxr-xr-x  2 jmena01 domain users 4096 mai   21 17:44 .bin/
-rw-r--r--  1 jmena01 domain users  545 mai   21 17:44 .package-lock.json
drwxr-xr-x  4 jmena01 domain users 4096 mai   21 17:44 typescript/ # I he ir

```

## For tsc

- don't use npm use npx instead see [answer 256 of that StackOverflow Post](https://stackoverflow.com/questions/39404922/tsc-command-not-found-in-compiling-typescript)

```bash
jmena01@m077-2281091:~/CONSULTANT$ npx --version
10.9.2
jmena01@m077-2281091:~/CONSULTANT$ npx tsc
Version 6.0.3
tsc: The TypeScript Compiler - Version 6.0.3
                                                                                                                     TS
COMMON COMMANDS

  tsc
  Compiles the current project (tsconfig.json in the working directory.)

  tsc app.ts util.ts
  ###################### A lot of documentation follows
```

# creating a tsconfig file

```bash
jmena01@m077-2281091:~/CONSULTANT$ npx tsc --init

Created a new tsconfig.json
                                                                                                                     TS
You can learn more at https://aka.ms/tsconfig
```

## Todo

```bash
jmena01@m077-2281091:~/CONSULTANT$ mkdir clean_typscript
jmena01@m077-2281091:~/CONSULTANT$ cd clean_typscript/
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ npm init -y # ne pas oublier
Wrote to /home/jmena01/CONSULTANT/clean_typscript/package.json:

{
  "name": "clean_typscript",
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



jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ npm install typescript --save-dev
npm notice This endpoint is being retired. Use the bulk advisory endpoint instead. See the following docs for more info: https://api-docs.npmjs.com/#tag/Audit

added 1 package in 721ms
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ ll
total 20
drwxr-xr-x  3 jmena01 domain users 4096 mai   29 17:15 ./
drwxr-xr-x 27 jmena01 domain users 4096 mai   29 17:12 ../
drwxr-xr-x  4 jmena01 domain users 4096 mai   29 17:15 node_modules/
-rw-r--r--  1 jmena01 domain users  284 mai   29 17:15 package.json
-rw-r--r--  1 jmena01 domain users  761 mai   29 17:15 package-lock.json

jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ npx tsc --init

Created a new tsconfig.json
                                                                                                                     TS
You can learn more at https://aka.ms/tsconfig
```

# p 7 first commmand (Hello World)

```bash
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ cat index.ts
console.log("Hello, Typescript"); # a very simple command
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ npx tsc # from index.ts to index.js
jmena01@m077-2281091:~/CONSULTANT/clean_typscript$ node index.js
Hello, Typescript
```
