# install SDKMan

- Eventhough I have a lot of Java versions already installed on my corporate computer

```bash
jmena01@m077-2281091:~$ curl -s https://get.sdkman.io | bash
###########################
All done!


You are subscribed to the STABLE channel.

Please open a new terminal, or run the following in the existing one:

    source "/home/jmena01/.sdkman/bin/sdkman-init.sh"

Then issue the following command:

    sdk help

Enjoy!!!
# test
jmena01@m077-2281091:~$ source "/home/jmena01/.sdkman/bin/sdkman-init.sh"
## All the openjdk versions I can install
jmena01@m077-2281091:~$ sdk list java | grep open
 Java.net      |     | 27.ea.25     | open    |            | 27.ea.25-open
               |     | 27.ea.24     | open    |            | 27.ea.24-open
               |     | 26.ea.35     | open    |            | 26.ea.35-open
               |     | 26.0.1       | open    |            | 26.0.1-open
               |     | 25.0.2       | open    |            | 25.0.2-open
               |     | 21.0.2       | open    |            | 21.0.2-open # The 21 is the lowest version any
```

# The corporate versions I already have

```bash
# from one toolbox
jmena01@m077-2281091:/home/soda/atelierjavaeclipse/jdk$ ll
total 64
drwxr-xr-x 16 jmena01 domain users 4096 juin  13  2025 ./
drwxr-xr-x 15 jmena01 domain users 4096 juin  18 10:11 ../
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-11.0.19+7/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-11.0.23+9/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-11.0.26+4/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-17.0.11+9/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-17.0.14+7/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-17.0.7+7/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-21.0.2+13/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-21.0.3+9/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-21.0.6+7/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-23.0.2+7/
drwxr-xr-x  8 jmena01 domain users 4096 juin  20  2025 jdk-7u60/
drwxr-xr-x  9 jmena01 domain users 4096 juin  20  2025 jdk-8u1xx/
drwxr-xr-x  8 jmena01 domain users 4096 juin  20  2025 jdk-8u412/
drwxr-xr-x  8 jmena01 domain users 4096 juin  20  2025 jdk-8u442/
# form another toolbox
jmena01@m077-2281091:~/AtelierCliR_v1.98/data/java-dgfip$ ll
total 20
drwxr-xr-x  5 jmena01 domain users 4096 févr. 26 11:07 ./
drwxr-xr-x  5 jmena01 domain users 4096 juil.  9  2025 ../
drwxr-xr-x  8 jmena01 domain users 4096 août   5  2022 jdk17/ # the only jsk
drwxr-xr-x  3 jmena01 domain users 4096 avril 23  2025 outils/
drwxr-xr-x 37 jmena01 domain users 4096 févr. 26 11:07 reposlocal/
```
