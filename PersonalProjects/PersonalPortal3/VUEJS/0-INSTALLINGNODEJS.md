# installing through [nvm](https://github.com/nvm-sh/nvm)
* I need it mainly to manage npm packages
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16631  100 16631    0     0   119k      0 --:--:-- --:--:-- --:--:--  121k
=> Downloading nvm from git to '/home/jpmena/.nvm'
=> Cloning into '/home/jpmena/.nvm'...
remote: Enumerating objects: 383, done.
remote: Counting objects: 100% (383/383), done.
remote: Compressing objects: 100% (326/326), done.
remote: Total 383 (delta 43), reused 180 (delta 29), pack-reused 0 (from 0)
Receiving objects: 100% (383/383), 391.80 KiB | 6.03 MiB/s, done.
Resolving deltas: 100% (43/43), done.
* (HEAD detached at FETCH_HEAD)
  master
=> Compressing and cleaning up git repository

=> Appending nvm source string to /home/jpmena/.bashrc
=> Appending bash_completion source string to /home/jpmena/.bashrc
=> You currently have modules installed globally with `npm`. These will no
=> longer be linked to the active version of Node when you install a new node
=> with `nvm`; and they may (depending on how you construct your `$PATH`)
=> override the binaries of modules installed with `nvm`:

C:\Users\jeanp\AppData\Roaming\npm
+-- @vue/cli-service-global@4.5.15
`-- @vue/cli@4.5.15
=> If you wish to uninstall them at a later point (or re-install them under your
=> `nvm` node installs), you can remove them from the system Node as follows:

     $ nvm use system
     $ npm uninstall -g a_module

=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```
* [useful nvm commands](https://gist.github.com/chranderson/b0a02781c232f170db634b40c97ff455)
  * see *nvm ls* and *nvm ls-remote*
```bash
jpmena@LAPTOP-E2MJK1UO:~$ nvm ls
            N/A
iojs -> N/A (default)
node -> stable (-> N/A) (default)
unstable -> N/A (default)
lts/* -> lts/krypton (-> N/A)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.17.1 (-> N/A)
lts/carbon -> v8.17.0 (-> N/A)
lts/dubnium -> v10.24.1 (-> N/A)
lts/erbium -> v12.22.12 (-> N/A)
lts/fermium -> v14.21.3 (-> N/A)
lts/gallium -> v16.20.2 (-> N/A)
lts/hydrogen -> v18.20.8 (-> N/A)
lts/iron -> v20.19.5 (-> N/A)
lts/jod -> v22.21.1 (-> N/A)
lts/krypton -> v24.11.1 (-> N/A)
jpmena@LAPTOP-E2MJK1UO:~$ nvm use lts/krypton
N/A: version "lts/krypton -> v24.11.1" is not yet installed. # I have to install it before using it

You need to run `nvm install lts/krypton` to install and use it.
```
* On my phone it takes time to download the 56 MB of the node.Linux.tar.gz
  * it compiles everything with g++ and also I have 8 Core it takes time
  * it is stuck at compiling nodeJs 24
* i got rid of nvm
```bash
jpmena@LAPTOP-E2MJK1UO:~$ vim .bashrc # I get rid of the last lines for nvm
jpmena@LAPTOP-E2MJK1UO:~$ rm -rf .nvm/ # everything seems to be there
```
# Using Volta
* Still on the [official Node download page](https://nodejs.org/en/download)
  * let the last LTS Version
  * select Linux
  * select Volta
  * let the npm selection
* following the instructions
```bash
jpmena@LAPTOP-E2MJK1UO:~$ curl https://get.volta.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10460  100 10460    0     0   5166      0  0:00:02  0:00:02 --:--:--  5167
  Installing latest version of Volta (2.0.2)
    Checking for existing Volta installation
    Fetching archive for Linux, version 2.0.2
######################################################################## 100.0%
    Creating directory layout
  Extracting Volta binaries and launchers
    Finished installation. Updating user profile settings.
Updating your Volta directory. This may take a few moments...
success: Setup complete. Open a new terminal to start using Volta!
```
* install node using Volta
```bash
jpmena@LAPTOP-E2MJK1UO:~$ tail -4 .bashrc
  fi
fi
export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"
jpmena@LAPTOP-E2MJK1UO:~$ source .bashrc # putting Volta in the PATH
jpmena@LAPTOP-E2MJK1UO:~$ volta install node@24
success: installed and set node@24.11.1 (with npm@11.6.2) as default # it does not try to compile
jpmena@LAPTOP-E2MJK1UO:~$ node --version
v24.11.1 # The latest LTS version at the date of 2025-11-18
jpmena@LAPTOP-E2MJK1UO:~$ npm --version
11.6.2
```