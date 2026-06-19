# 42

## the demo project in IntelliJ

- the given Maven Wrapper from IntelliJ does not access the Internet
- Settings / Maven Configuration
  - back to the

```bash
jmena01@m077-2281091:/home/soda/atelierjavaeclipse/outils/construction/maven$ ll conf
total 20
drwxr-xr-x  2 jmena01 domain users  4096 juin  20  2025 ./
drwxr-xr-x 11 jmena01 domain users  4096 juin  13  2025 ../
-rw-r--r--  1 jmena01 domain users 12100 juin  20  2025 settings.xml
jmena01@m077-2281091:/home/soda/atelierjavaeclipse/outils/construction/maven$ ll apache-maven-3.9.4-DGFiP
total 56
drwxr-xr-x  6 jmena01 domain users  4096 juin  20  2025 ./
drwxr-xr-x 11 jmena01 domain users  4096 juin  13  2025 ../
drwxr-xr-x  2 jmena01 domain users  4096 juin  20  2025 bin/
drwxr-xr-x  2 jmena01 domain users  4096 juin  20  2025 boot/
drwxr-xr-x  3 jmena01 domain users  4096 juin  20  2025 conf/
drwxr-xr-x  4 jmena01 domain users  4096 juin  20  2025 lib/
-rw-r--r--  1 jmena01 domain users 18945 juin  20  2025 LICENSE
-rw-r--r--  1 jmena01 domain users  5034 juin  20  2025 NOTICE
-rw-r--r--  1 jmena01 domain users  2533 juin  20  2025 README.txt
```

# Running the demo application in IntelliJ

- I didn't configure a PostgreSQL Database

```
Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.

Reason: Failed to determine a suitable driver class


Action:

Consider the following:
	If you want an embedded database (H2, HSQL or Derby), please put it on the classpath.
	If you have database settings to be loaded from a particular profile you may need to activate it (no profiles are currently active).


Process finished with exit code 1
```

# 43

## Starting a SpringBoot project directly from IntelliJ

- File / new / Project ...
- in the left pane of the window select _Spring Boot_
- There is no more difference between the Community and the Entreprise Edition, so the menu is available by default
  - don't need the [plugin link](https://plugins.jetbrains.com/plugin/10229-spring-assistant)

### New project new Maven configuration

- same as above, use locally intalled Maven not the default Maven Wrapper
-
