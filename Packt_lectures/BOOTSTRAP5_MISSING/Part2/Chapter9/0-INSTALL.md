# The souce code
* [Chapter 9 website in the accompagnying GitHub Code](https://github.com/PacktPublishing/The-Missing-Bootstrap-5-Guide/tree/main/part-2/chapter-9/website)
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-9/website$ npm i bootstrap bootstrap-icons --save

added 3 packages in 2s

3 packages are looking for funding
  run `npm fund` for details
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-9/website$ npm i sass --save-dev

added 12 packages, and audited 16 packages in 2s

8 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
* now the *~/CONSULTANT/The-Missing-Bootstrap-5-Guide/part-2/chapter-9/website/package.json* contains:
```javascript
{
  "dependencies": {
    "bootstrap": "^5.3.8", //^is the up arrrow, it means at least the given version
    "bootstrap-icons": "^1.13.1"
  },
  "devDependencies": {
    "sass": "^1.97.3"
  }
}
```
## Script.js
```html
    <script src="../../../bootstrap/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/script.js"></script> <!--Our custom script-->
  </body>
</html>
```