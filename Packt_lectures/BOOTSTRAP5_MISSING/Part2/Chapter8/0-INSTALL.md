# the final code is at [Chapter 8 / website on GitHub](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-2/chapter-8/website)
* we put our variables before bootstrap5 variables
  * because Bootstrap5 variable are defined as [default](https://thoughtbot.com/blog/sass-default)
    * that means there are set only if a variable with the same name has not been set before.
## The utility api
* is the object of chapter 6
* an example is givent p 141 and p 142 for multiple property
# compiling th scss in css
* because the delivered [css/style.css](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-2/chapter-8/website/css/style.css) in the is in compressed mode we need to recompile the [scss/style.scss](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/blob/main/part-2/chapter-8/website/scss/style.scss)
## charging the sass compiler
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-8/website$ npm i sass --save-dev

added 17 packages in 2s

5 packages are looking for funding
  run `npm fund` for details
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.7.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
npm notice To update run: npm install -g npm@11.7.0
npm notice
```
* don't forget that for the icons (which have been forgotten from the source code) I need to import bootstrap
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-8/website$ npm i bootstrap --save

added 3 packages, and audited 21 packages in 2s

8 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
* it created a package.json with only the depedencies:
```javascript
{
  "devDependencies": {
    "sass": "^1.97.2"
  },
  "dependencies": {
    "bootstrap": "^5.3.8"
  }
}
```
* I now want to recompile
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-8/website$ ./node_modules/.bin/sass scss/style.scss css/style.css
## lots of deprecation warnings
```
## Missing Bootstrap-icons
```bash
jmena01@m077-2281091:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-8/website$ npm i bootstrap-icons --save

added 1 package, and audited 22 packages in 743ms

9 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
* it enriched the package.json with that dependency
```javascript
{
  "devDependencies": {
    "sass": "^1.97.2"
  },
  "dependencies": {
    "bootstrap": "^5.3.8",
    "bootstrap-icons": "^1.13.1" // the new package
  }
}
```