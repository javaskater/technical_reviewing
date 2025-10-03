# The [Book](https://www.packtpub.com/en-us/product/vuejs-3-for-beginners-9781805126775)
* It is a Pckt Book [ Vue.js 3 for Beginners: Learn the essentials of Vue.js 3 and its ecosystem to build modern web applications](https://www.packtpub.com/en-us/product/vuejs-3-for-beginners-9781805126775)

# [source Code][https://github.com/PacktPublishing/Vue.js-3-for-Beginners]
* The example code is updated at the [Packt Github space](https://github.com/PacktPublishing/Vue.js-3-for-Beginners)
* I only see one project. It is the unique companion project of this book.
* Each chapter/part of the book correspond to a branch
  * by default  [the project](https://github.com/PacktPublishing/Vue.js-3-for-Beginners) opens to the last branch (CH11) 

# Working another time on the book
* on the 29/09/2025 end of [Chapter 3](./Part2/Chapter3.md) Starting [Chapter 4](./Part2/Chapter4.md)
* my code is at *jmena01@m077-2281091:~/CONSULTANT/Vue.js-3-for-Beginners*
```bash
jmena01@m077-2281091:~/CONSULTANT/Vue.js-3-for-Beginners$ git remote -v
origin  https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git (fetch) # connected to the book's repo
origin  https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git (push)
jmena01@m077-2281091:~/CONSULTANT/Vue.js-3-for-Beginners$ git branch
* CH03 # working on the beginning of branch 03
  CH11
```
* To start a new chapter
```bash
jmena01@m077-2281091:~/CONSULTANT/Vue.js-3-for-Beginners$ cd .. # I cannot change branch when file aren't saved
jmena01@m077-2281091:~/CONSULTANT$ rm -rf Vue.js-3-for-Beginners
jmena01@m077-2281091:~/CONSULTANT$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git
Clonage dans 'Vue.js-3-for-Beginners'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 321 (delta 19), reused 13 (delta 13), pack-reused 299 (from 1)
Réception d''objets: 100% (321/321), 223.30 Kio | 7.20 Mio/s, fait.
Résolution des deltas: 100% (132/132), fait.
jmena01@m077-2281091:~/CONSULTANT/Vue.js-3-for-Beginners$ npm i
jmena01@m077-2281091:~/CONSULTANT/Vue.js-3-for-Beginners$ npm run dev
```