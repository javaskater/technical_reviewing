* copying the Ressources
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-1$ cp -pvr chapter-6 ~/CONSULTANT/monBootstrap5/
```
* Adding the sass compiler (see PArt 1 / chapter 2 of the Book)
```bash
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-6$ npm init #lot of questions to answer
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-6$ npm i sass --save-dev

added 17 packages, and audited 18 packages in 1s

5 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
* adding a task sassCompile in the package.json file
```bash
jmena01@m077-2281091:~/CONSULTANT/monBootstrap5/chapter-6$ cat package.json 
{
  "name": "chapter-6",
  "version": "1.0.0",
  "main": "index.js",
  "directories": {
    "example": "examples"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "sassCompile": "node_modules/.bin/sass" # command added
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "sass": "^1.93.2"
  }
}
```