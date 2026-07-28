# Origin

- this project is the result of My lectures
- [Manning](https://www.manning.com)
- [Packt Publishing](https://www.packtpub.com/)
- [Informit (Pearson , Wiley)](https://www.informit.com/)

# I share my experience with the different lectures/trainings

- Is includes
  - remarks with links to the online documentation available in Markdown files
  - code samples in those same Markdown files or separately

# Problem when starting WSL/Visual Studio Code

- the [WSL Integration asks for update](https://github.com/microsoft/vscode-remote-release/issues/3839) (Downloading server)
- and you cannot do anything if you don't accept the Update

# To access th WSL/Ubuntu home directory

- from Windows it is _\\wsl.localhost\Ubuntu\home\jpmena_ to be passed in the explorer Adress Bar
- or when in WSL you can always call

```bash
jpmena@LAPTOP-E2MJK1UO:~$ explorer.exe .
```

- which opens on Windows the Windows Explorer at the _\\wsl.localhost\Ubuntu\home\jpmena_ address

## Access To GitLab

- as of july 2026 access using uer/password is no more allowed
- It is recommended that you are using Token!!!!
- My first token !!!

```
glpat-4RVW_4theDaDilZJywQWsWM6MQpvOjEKdToxNXZ2NA8.01.171dcvx0f
```

- [GitLab documentation](https://docs.gitlab.com/user/profile/personal_access_tokens/)

### Test on my corporate computer

```bash
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing$ git remote add token https://oauth2:glpat-4RVW_4theDaDilZJywQWsWM6MQpvOjEKdToxNXZ2NA8.01.171dcvx0f@gitla
b.com/jpmena/technical_reviewing.git/
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing$ git push token main
remote: Access denied: This operation requires a fine-grained personal access token with the following project permissions: [Code: Push].
fatal: impossible d''accéder à 'https://gitlab.com/jpmena/technical_reviewing.git/' : The requested URL returned error: 403
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing$
```

### I revoke the previous one and create a new one

- a fine grained token
- Add ressource permission
  - Repository / Code / (Gives All permissions)

```
glpat-RfPfzmjnkc3ve4gmKPQdn2M6MQpvOjEKdToxNXZ2NA8.01.170j5dtix
```

- I will automatically be revoked on the 27/08/2026 (that date could habe been changed durigin creation)
- my new remote

```bash
# I replace the remote site called token
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing$ git remote remove token
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing$ git remote add token https://oauth2:glpat-RfPfzmjnkc3ve4gmKPQdn2M6MQpvOjEKdToxNXZ2NA8.01.170j5dtix@gitla
b.com/jpmena/technical_reviewing.git/
# Push changes
## it does not ask for a password !!!!
jmena01@m077-2281091:~/CONSULTANT/technical_reviewing$ git push token main
Énumération des objets: 179, fait.
Décompte des objets: 100% (179/179), fait.
Compression par delta en utilisant jusqu'à 20 fils d'exécution
Compression des objets: 100% (153/153), fait.
Écriture des objets: 100% (170/170), 51.98 Kio | 3.71 Mio/s, fait.
Total 170 (delta 69), réutilisés 1 (delta 0), réutilisés du pack 0
remote: Resolving deltas: 100% (69/69), completed with 6 local objects.
To https://gitlab.com/jpmena/technical_reviewing.git/
   8da9392..e649f3e  main -> main
```

- I see the last commit [on my GitLab page for this documentation project](https://gitlab.com/jpmena/technical_reviewing)
