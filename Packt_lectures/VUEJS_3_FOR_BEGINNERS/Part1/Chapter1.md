# Prerequisites
## VSCode and Node
* [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) is the Official Vue JS extension
* The [Node](https://nodejs.org/fr) version has to be greater than 16
  * in my case it is the node brought by my Entreprise [VS Codium](https://vscodium.com/), at the end of my *~/.bashrc* I have
```bash
# Nodejs 
 VERSION=v18.16.0 
 DISTRO=linux-x64 
 if [ ! `echo $PATH | grep $VERSION` ] 
 then 
 	 export PATH=/home/jmena01/Ateliers/AtelierCodium_v1.75/nodejs/node-$VERSION-$DISTRO/bin:$PATH 
 fi
```
* Which gives
```bash
jmena01@M077-1840900:~/Documents/CONSULTANT/technical_reviewing/Packt_lectures$ node --version
v18.16.0
```
## GIT
* I didn't know [Git Kraken](https://www.gitkraken.com/)
  * It can be a Visual Studio extension under the name of [Git Lens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
* Visual Sudio Code comes with a lot of Git Extensions
  * th one recommended during a Git training was [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) 
# The source code
* Each chapter/part of the book correspond to a branch
  * by default  [the project](https://github.com/PacktPublishing/Vue.js-3-for-Beginners) opens to the last branch (CH11) 
* Starts at Chapter 3 with
  * CH03 (beginning 3rd chapter) the skeleton
  * CH03-end the source code when the chapter is completed
## Testing the completed project:
### cloning
```bash
jmena01@M077-1840900:~/CONSULTANT$ git clone https://github.com/PacktPublishing/Vue.js-3-for-Beginners.git
Clonage dans 'Vue.js-3-for-Beginners'...
remote: Enumerating objects: 321, done.
remote: Counting objects: 100% (321/321), done.
remote: Compressing objects: 100% (179/179), done.
remote: Total 321 (delta 135), reused 298 (delta 116), pack-reused 0 (from 0)
Réception d''objets: 100% (321/321), 171.75 Kio | 3.73 Mio/s, fait.
Résolution des deltas: 100% (135/135), fait.
jmena01@M077-1840900:~/CONSULTANT$ cd Vue.js-3-for-Beginners/
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ git branch -a
* CH11
  remotes/origin/CH03
  remotes/origin/CH03-end
  remotes/origin/CH04
  remotes/origin/CH04-end
  remotes/origin/CH05
  remotes/origin/CH05-end
  remotes/origin/CH06
  remotes/origin/CH06-end
  remotes/origin/CH07
  remotes/origin/CH07-end
  remotes/origin/CH08
  remotes/origin/CH08-END
  remotes/origin/CH09
  remotes/origin/CH09-end
  remotes/origin/CH10
  remotes/origin/CH10-end
  remotes/origin/CH11
  remotes/origin/CH11-end
  remotes/origin/CH12
  remotes/origin/CH12-end
  remotes/origin/HEAD -> origin/CH11
  remotes/origin/dependabot/npm_and_yarn/follow-redirects-1.15.6
  remotes/origin/dependabot/npm_and_yarn/multi-cfd035cdb2
  remotes/origin/dependabot/npm_and_yarn/vite-4.5.3
  remotes/origin/master
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ git branch
* CH11 # I am by default on the last chapter
```
### Starting the project
```bash
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ npm i

added 444 packages, and audited 445 packages in 21s

105 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (5 moderate, 4 high)

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ npm run dev

> vue.js-for-beginners@0.0.0 dev
> vite


  VITE v4.4.9  ready in 588 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```
# Testing the finished project
```bash
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ git checkout remotes/origin/CH11-end
Note : basculement sur 'remotes/origin/CH11-end'.

Vous êtes dans l''état « HEAD détachée ». Vous pouvez visiter, faire des modifications
expérimentales et les valider. Il vous suffit de faire un autre basculement pour
abandonner les commits que vous faites dans cet état sans impacter les autres branches

Si vous voulez créer une nouvelle branche pour conserver les commits que vous créez,
il vous suffit d'utiliser l'option -c de la commande switch comme ceci :

  git switch -c <nom-de-la-nouvelle-branche>

Ou annuler cette opération avec :

  git switch -

Désactivez ce conseil en renseignant la variable de configuration advice.detachedHead à false

HEAD est maintenant sur 5f5d5f0 CH11-end
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ git switch -c remotes/origin/CH11-end
Basculement sur la nouvelle branche 'remotes/origin/CH11-end'
jmena01@M077-1840900:~/CONSULTANT/Vue.js-3-for-Beginners$ git branch
  CH11
* remotes/origin/CH11-end
```
* *npm run serve* does not work (script not found), *npm run dev* does the Job