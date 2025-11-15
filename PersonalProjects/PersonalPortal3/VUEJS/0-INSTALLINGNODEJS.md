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