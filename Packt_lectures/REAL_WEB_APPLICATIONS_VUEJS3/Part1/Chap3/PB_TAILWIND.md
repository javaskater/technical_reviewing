# vue-local-weather/src/style.css
## in *Chapter3/vue-local-weather/src/style.css* 
* I change the background color, il changes in the output. Vite reloads the server
* It seems not seeing @ I change base to base222 nothing happens it does nothing it reloads but no error messages
# [Official documentation](https://tailwindcss.com/docs/guides/vite)
* It is a react project, but we don't care
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js$ npm create vite@latest my-project -- --template react
Need to install the following packages:
  create-vite@5.5.2
Ok to proceed? (y) y

Scaffolding project in /home/jmena01/CONSULTANT/my_vue_js/my-project...

Done. Now run:

  cd my-project
  npm install
  npm run dev
```
* Tailwind toolkit installation
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js$ cd my-project/
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/my-project$ npm install -D tailwindcss postcss autoprefixer
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/js@9.11.1',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'eslint@9.11.1',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/config-array@0.18.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/core@0.6.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/eslintrc@3.1.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/plugin-kit@0.2.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@humanwhocodes/retry@0.3.0',
npm WARN EBADENGINE   required: { node: '>=18.18' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'eslint-scope@8.0.2',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'eslint-visitor-keys@4.0.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'espree@10.1.0',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: '@eslint/object-schema@2.1.4',
npm WARN EBADENGINE   required: { node: '^18.18.0 || ^20.9.0 || >=21.1.0' },
npm WARN EBADENGINE   current: { node: 'v18.16.0', npm: '9.5.1' }
npm WARN EBADENGINE }

added 352 packages, and audited 353 packages in 21s

125 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
* Perhaps my node is too old ? *18.16.0* instead of *18.18.0 || ^20.9.0 || >=21.1.0*
* initilisation of configuration:
```bash
jmena01@M077-1840900:~/CONSULTANT/my_vue_js/my-project$ npx tailwindcss init -p

Created Tailwind CSS config file: tailwind.config.js
Created PostCSS config file: postcss.config.js
```
* When I change the content of the jsx I get
  * the styles are taken into account
```bash
13:13:45 [vite] hmr update /src/App.jsx, /src/index.css
```
* If I inspect with Firefox the H1 element the classes are well be created
```css
.underline {
  text-decoration-line: underline;
}
.font-bold {
  font-weight: 700;
}
.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}
```
* The applies styles come from *@tailwind utilities;* (If I change it for utilities222 we get a classical H1)
* I mispelled utilities (utilititis) in the Book's weather app *Chapter3/vue-local-weather/src/style.css*
  * Vite does not tells you that it cannot find the library   
* Now it works !!!!
## Remarks noted in the resolution process
* we can rotate a inline-bloc
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <p><span class="inline" style="transform: rotate(20deg); display:inline-block">&darr;</span></p>
    </div>
</body>
</html>
```