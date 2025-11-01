# IntelliPHESENSE and Docker container
* It doesn't help on the container side
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/symfony-docker$ docker compose exec -it php bash
root@c7fe34350fb4:/app# ll src/Entity/
bash: ll: command not found
root@c7fe34350fb4:/app# ls -l src/Entity/
total 4
-rw-rw-rw- 1 root root 1959 Nov  1 15:38 JpmDiplom.php # That was created by symfony console called from the host
root@c7fe34350fb4:/app# ls -l src/DataFixtures/
total 8
-rw-r--r-- 1 root root 331 Nov  1 15:46 AppFixtures.php # That wa created alos by symfony console from the hos
-rw-r--r-- 1 root root 491 Nov  1 15:57 DiplomsFixtures.php
root@c7fe34350fb4:/app# chmod 666 src/DataFixtures/*.php # To make them writable from the Host
```
* On the Host Side it works but does not see the vendor classes
* Do I have to create another link (todo)
  * vendor -> vendor