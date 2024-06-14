# Installing the compiler
* On my Work Computer
```bash
# Where is node installed on my computer
jmena01@M077-1840900:~$ tail -7 .bashrc
 # Nodejs 
 VERSION=v18.16.0 
 DISTRO=linux-x64 
 if [ ! `echo $PATH | grep $VERSION` ] 
 then 
 	 export PATH=/home/jmena01/Ateliers/AtelierCodium_v1.75/nodejs/node-$VERSION-$DISTRO/bin:$PATH 
 fi
jmena01@M077-1840900:~$ node --version # We find the version like in the .bashrc file
v18.16.0
jmena01@M077-1840900:~$ npm --version # The version is higher than in the book
9.5.1
# The typescript compiler will install itself accordingly
jmena01@M077-1840900:~$ npm install -g typescript

added 1 package in 912ms
jmena01@M077-1840900:~$ whereis tsc
tsc: /home/jmena01/Ateliers/AtelierCodium_v1.75/nodejs/node-v18.16.0-linux-x64/bin/tsc
jmena01@M077-1840900:~$ tsc --version # on amjor version hoghrer than in the book
Version 5.4.5
```
## Simple compiler test
```bash
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ touch hello_typescript.ts
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ tsc hello_typescript.ts 
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ node hello_typescript.js 
hello typescript
```
## Using templates in Typescript
* The typescript code
```typescript
var version = `es6`
console.log(`hello ${version} typescript`);
```
* is compiled into:
```javascript
var version = "es6";
console.log("hello ".concat(version, " typescript"));
```
* We test all programs using node (not a navigator)
# p 11
* Si je fais le code suivant:
```typescript
var mysString: string = `this is a String`;
console.log(`My string is : ${mysString}`);
mysString = 1;
console.log(`My string is : ${mysString}`);
```
* VSCode met la ligne 3 en rouge, et à la compilation j'obtiens:
```bash
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ tsc type.ts 
type.ts:3:1 - error TS2322: Type 'number' is not assignable to type 'string'.

3 mysString = 1;
  ~~~~~~~~~


Found 1 error in type.ts:3
```
* However (Although there has been an error) it generates javascript files (which does not have these constraints):
```javascript
var mysString = "this is a String";
console.log("My string is : ".concat(mysString));
mysString = 1;
console.log("My string is : ".concat(mysString));
```
# p 12
* Je teste ce [petit typage](./code/ch1/type1.ts)
* On est obligé de le compiler
  * appelé directement par no provoque une erreur
```bash
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ tsc type1.ts # compilation OK
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ node type1.ts # Typescript ne peut être lu drectement par node
/home/jmena01/CONSULTANT/mastering_typescript_packt/code/ch1/type1.ts:1
var myBoolean: boolean = true;
             ^

SyntaxError: Unexpected token ':'
    at internalCompileFunction (node:internal/vm:73:18)
    at wrapSafe (node:internal/modules/cjs/loader:1176:20)
    at Module._compile (node:internal/modules/cjs/loader:1218:27)
    at Module._extensions..js (node:internal/modules/cjs/loader:1308:10)
    at Module.load (node:internal/modules/cjs/loader:1117:32)
    at Module._load (node:internal/modules/cjs/loader:958:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:23:47

Node.js v18.16.0
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ node type1.js # on exécute le fichier généré par le compilateur tsc
myBoolean = false
myStringArray = 1234,5678
myNumber = 2
```
* type [inference example](./code/ch1/type2.ts) When I hover the mouse on a variable, VSCode gives me the *inferred type*

# p 14
* [Duck typing example](./code/ch1/type3.ts)
  * the [generated Javascript code](./code/ch1/type3.js) is interesting to read!
```bash
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ tsc type3.ts 
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ node type3.js
2 - another Name
```
* When Duck Typing does not work: [(last line of type3.ts)](./code/ch1/type3.js):
```bash
jmena01@M077-1840900:~/CONSULTANT/mastering_typescript_packt/code/ch1$ tsc type3.ts 
type3.ts:4:1 - error TS2741: Property 'print' is missing in type '{ id: number; name: string; }' but required in type '{ name: string; id: number; print(): void; }'.

4 nameIdObject = {id: 3, name: "Third Name"};
  ~~~~~~~~~~~~

  type3.ts:1:46
    1 var nameIdObject = { name: "my Name", id: 1, print(){}};
                                                   ~~~~~
    'print' is declared here.


Found 1 error in type3.ts:4
```
# p 15
* test of [obj1 and obj2](./code/ch1/type4.ts)
  * the type is defined when writing var obj1
* so obj1 can accept obj2 because obj2 contains at least the fields of obj1
  * obj1 is enriched of the select function from obj2 (javascript side effect)
  * but the definition of obj1 remains the same
* That is why Typescript cannot affect obj1 to obj2 (obj1 is still considered with one field and one function, the declaration has priority over the affectation)

# p 16