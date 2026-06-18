# 19 -21 

## [The download link has changed](https://www.jetbrains.com/idea/download/?section=linux)

> IntelliJ IDEA is now a single, unified product.
>
> > Core Java and Kotlin features remain free, with even more functionality available at no cost. When you need advanced tools, simply unlock them with an Ultimate >> subscription – no switching editions, no extra setup.

- no more free community version on one side
  - and full paid version on the other side
- the .tar.gz is 1.5Go big

```bash
jmena01@m077-2281091:~/Ateliers$ ls -lhtr
total 1,5G
-rw-r--r-- 1 jmena01 domain users 136K sept.  4  2025 sshpilot_3.5.4-1_all.deb
-rw-r--r-- 1 jmena01 domain users 178K sept. 11  2025 gnome-connection-manager_1.2.1_all.deb
-rw-r--r-- 1 jmena01 domain users 281K sept. 24  2025 sshpilot_4.0.8-1_all.deb
-rw-r--r-- 1 jmena01 domain users 1,5G juin  17 09:33 idea-2026.1.3.tar.gz # The IntelliJ i 1.5Go big
-rw-r--r-- 1 jmena01 domain users   87 juin  17 09:40 idea-2026.1.3.tar.gz.sha256 # I also downloaded the checksum to verify the archive
# Verification of the downloaded archive
jmena01@m077-2281091:~/Ateliers$ sha256sum -c idea-2026.1.3.tar.gz.sha256
idea-2026.1.3.tar.gz: Réussi # The checksum matches with the archive
```

# Extensions

- _Lombok_ is already installed
- _Maven_ is already installed but not _Maven Helper_ to be installed OK
- _JUnit Mockito Code Generator_ to be installed OK
- _Adapter for Eclipse Code Formatter_ to be installed OK
- _TabNine_ (It is the Legacy version and not the Enterprise one) installed OK
- _Add to gitignore_ Installed OK (small extension)
