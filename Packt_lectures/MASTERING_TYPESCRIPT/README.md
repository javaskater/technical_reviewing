# Preface
## xiv
* There is a [GitHub Website for the book](https://github.com/PacktPublishing/Mastering-TypeScript-Fourth-Edition)
```bash
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT$ git clone https://github.com/PacktPublishing/Mastering-TypeScript-Fourth-Edition.git
Clonage dans 'Mastering-TypeScript-Fourth-Edition'...
remote: Enumerating objects: 465, done.
remote: Counting objects: 100% (465/465), done.
remote: Compressing objects: 100% (320/320), done.
remote: Total 465 (delta 127), reused 435 (delta 110), pack-reused 0 (from 0)
Réception d''objets: 100% (465/465), 6.16 Mio | 22.44 Mio/s, fait.
Résolution des deltas: 100% (127/127), fait.
```
# 4
## installting Typescript gobally
```bash
jmena01@M077-1840900:~/CONSULTANT$ npm i -g typescript

changed 1 package in 874ms #very fast
jmena01@M077-1840900:~/CONSULTANT$ tsc --version
Version 5.6.3
```
## Testing
```bash
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT/ch01$ cat hello_typescript.ts 
console.log(`Hello Typesript`);
mena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT/ch01$ tsc hello_typescript.ts # Compilation from Typescript to Javascript
jmena01@M077-1840900:~/CONSULTANT/MY_MASTERING_TYPESCRIPT/ch01$ node hello_typescript.js 
Hello Typesript
```