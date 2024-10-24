## The [DDEV Docker running solution](https://ddev.com/get-started/)
* This book uses [DDEV](https://ddev.com/get-started/) [its documentation](https://ddev.com/get-started/) for Windows 
  * lets you install WSL2
  * I install DEDEV with the given Powershell script on a [administrative blue Windows Powershell terminal](https://www.ninjaone.com/blog/open-an-elevated-powershell-prompt/)
    * CTRL+SHIFT+RETURN
  * It takes time to update the Ubuntu/Jammy packages And the install th ddev conainers
  * It has installed docker inside WSL2 (it is not Docker4Windows)
```powershell
After this operation, 472 MB of additional disk space will be used.                                                                                           Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 pigz amd64 2.6-1 [63.6 kB]                                                                        Get:3 https://download.docker.com/linux/ubuntu jammy/stable amd64 containerd.io amd64 1.7.22-1 [29.5 MB]                                                      Get:4 http://archive.ubuntu.com/ubuntu jammy/main amd64 bc amd64 1.07.1-3build1 [87.6 kB]                                                                     Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnspr4 amd64 2:4.35-0ubuntu0.22.04.1 [119 kB]                                               Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnss3 amd64 2:3.98-0ubuntu0.22.04.2 [1347 kB]                                               Get:2 https://pkg.ddev.com/apt */* amd64 ddev amd64 1.23.5 [14.0 MB]                                                                                          Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libnss3-tools amd64 2:3.98-0ubuntu0.22.04.2 [570 kB]Get:8 http://archive.ubuntu.com/ubuntu jammy/main amd64 desktop-file-utils amd64 0.26-1ubuntu3 [55.9 kB]                                                                                            Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpulse0 amd64 1:15.99.1+dfsg1-1ubuntu2.2 [298 kB]                                           Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libpulsedsp amd64 1:15.99.1+dfsg1-1ubuntu2.2 [23.3 kB]                                       Get:11 http://archive.ubuntu.com/ubuntu jammy/main amd64 libslirp0 amd64 4.6.1-1build1 [61.5 kB]                                                              Get:12 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 pulseaudio-utils amd64 1:15.99.1+dfsg1-1ubuntu2.2 [76.1 kB]                                  Get:13 http://archive.ubuntu.com/ubuntu jammy/universe amd64 slirp4netns amd64 1.0.1-2 [28.2 kB]                                                              Get:14 http://archive.ubuntu.com/ubuntu jammy/universe amd64 wslu amd64 3.2.3-0ubuntu3 [89.7 kB]                                                              Get:15 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-buildx-plugin amd64 0.17.1-1~ubuntu.22.04~jammy [30.3 MB]                           Get:16 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce-cli amd64 5:27.3.1-1~ubuntu.22.04~jammy [15.0 MB]                                Get:17 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce amd64 5:27.3.1-1~ubuntu.22.04~jammy [25.6 MB]                                    
Get:18 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce-rootless-extras amd64 5:27.3.1-1~ubuntu.22.04~jammy [9589 kB]                    Get:19 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-compose-plugin amd64 2.29.7-1~ubuntu.22.04~jammy [12.7 MB] 
``` 
* During the installed blocked:
  * I have to CTRL+C and give my WSL2/Ubuntu's password
* I finishes with
```powershell
Download complete.
 ITEM             VALUE
 DDEV version     v1.23.5
 architecture     amd64
 cgo_enabled      0
 db               ddev/ddev-dbserver-mariadb-10.11:v1.23.5
 ddev-ssh-agent   ddev/ddev-ssh-agent:v1.23.5
 docker           27.3.1
 docker-api       1.47
 docker-compose   v2.29.7
 docker-platform  wsl2-docker-ce
 global-ddev-dir  /home/jpmena/.ddev
 mutagen          0.17.2
 os               linux
 router           ddev/ddev-traefik-router:v1.23.5
 web              ddev/ddev-webserver:v1.23.5
```
* Without starting docker4Windows I get In WSL/Ubuntu
```bash
jpmena@LAPTOP-E2MJK1UO:~$ docker --version
Docker version 27.3.1, build ce12230
jpmena@LAPTOP-E2MJK1UO:~$ ll  /usr/bin/docker-compose #in red means not installed
lrwxrwxrwx 1 root root 56 Oct  2 13:57 /usr/bin/docker-compose -> /mnt/wsl/docker-desktop/cli-tools/usr/bin/docker-compose 
# If I start docker4Windows
jpmena@LAPTOP-E2MJK1UO:~$ ll  /usr/bin/docker-compose # the link is in green
jpmena@LAPTOP-E2MJK1UO:~$ /usr/bin/docker-compose --version
Docker Compose version v2.20.2-desktop.1 # It is not the version installed by ddev which is the v2.29.7
lrwxrwxrwx 1 root root 56 Oct 24 17:32 /usr/bin/docker-compose -> /mnt/wsl/docker-desktop/cli-tools/usr/bin/docker-compose*
jpmena@LAPTOP-E2MJK1UO:~$ ddev -v
ddev version v1.23.5 #Like proposed on the WebSite
```
* I have to file an issue to the project