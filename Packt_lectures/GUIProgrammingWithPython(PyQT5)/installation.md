# Installation of PyQT5

## Installation with pip
* could not install with pip3 (Already installed by the SOCLE Linuwx Developper)
* reason pip version too low like explained in that [StackOverflow Post](https://stackoverflow.com/questions/65447314/attributeerror-module-sipbuild-api-has-no-attribute-prepare-metadata-for-bui)
```bash
jmena01@M077-1840900:~$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8) #minimum version requires 21.1.1
```
## Installation directly through apt
* A [good Website that gives you all the opportunities to install PyQt](https://www.pythonguis.com/installation/install-pyqt-linux/)
```bash
jmena01@M077-1840900:~$ sudo apt install python3-pyqt5
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances       
Lecture des informations d'état... Fait
Les paquets supplémentaires suivants seront installés : 
  libqt5designer5 libqt5help5 libqt5sql5 libqt5sql5-sqlite libqt5test5 python3-sip
Paquets suggérés :
  python3-pyqt5-dbg
Les NOUVEAUX paquets suivants seront installés :
  libqt5designer5 libqt5help5 libqt5sql5 libqt5sql5-sqlite libqt5test5 python3-pyqt5 python3-sip
0 mis à jour, 7 nouvellement installés, 0 à enlever et 0 non mis à jour.
Il est nécessaire de prendre 5 617 ko dans les archives.
Après cette opération, 24,4 Mo d'espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n] O
```
## Testing the installation
* We are using the REPL like proposed in [installation under Linux](https://www.pythonguis.com/installation/install-pyqt-linux/)
```python
>>> import PyQT5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'PyQT5'
>>> import PyQt5
>>>
```
# Installing Qt Designer
* In the Packt Book [Mastering GUI Programming with Python](https://www.packtpub.com/product/mastering-gui-programming-with-python/9781789612905)
  * they propose to install (page 11 - 28/526) the debian/Ubuntu package **qttools5-dev-tools**
```bash
jmena01@M077-1840900:~$ sudo apt install qttools5-dev-tools
Lecture des listes de paquets... Fait
Construction de l arbre des dépendances       
Lecture des informations d'état... Fait
Les paquets supplémentaires suivants seront installés : 
  libclang1-10 libllvm10 libqt5designercomponents5 libqt5positioning5 libqt5qml5 libqt5quick5 libqt5quickwidgets5 libqt5sensors5 libqt5webchannel5 libqt5webkit5 qdoc-qt5 qhelpgenerator-qt5 qt5-assistant
  qtattributionsscanner-qt5 qtchooser
Paquets suggérés :
  qt5-qmltooling-plugins qt5-doc
Les NOUVEAUX paquets suivants seront installés :
  libclang1-10 libllvm10 libqt5designercomponents5 libqt5positioning5 libqt5qml5 libqt5quick5 libqt5quickwidgets5 libqt5sensors5 libqt5webchannel5 libqt5webkit5 qdoc-qt5 qhelpgenerator-qt5 qt5-assistant
  qtattributionsscanner-qt5 qtchooser qttools5-dev-tools
0 mis à jour, 16 nouvellement installés, 0 à enlever et 0 non mis à jour.
Il est nécessaire de prendre 40,9 Mo dans les archives.
Après cette opération, 182 Mo d'espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n] 
```
* I vae Three Icons with the __Qt5 Designer__ I take only the designer itself ...
* There is a [Qt Designer Manual](https://doc.qt.io/qt-5/qtdesigner-manual.html)
  * here in version 5 (the version 6 is the default version) 
## Intalling the doc package:
* The preceding installation proposes installing that packag
```bash
jmena01@M077-1840900:~$ sudo apt install qt5-doc
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances       
Lecture des informations d''état... Fait
Les paquets supplémentaires suivants seront installés : 
  qt3d5-doc qtbase5-doc qtcharts5-doc qtconnectivity5-doc qtdatavisualization5-doc qtdeclarative5-doc qtgraphicaleffects5-doc qtlocation5-doc qtmultimedia5-doc qtnetworkauth5-doc qtquickcontrols2-5-doc
  qtquickcontrols5-doc qtscript5-doc qtscxml5-doc qtsensors5-doc qtserialbus5-doc qtserialport5-doc qtsvg5-doc qttools5-doc qtvirtualkeyboard5-doc qtwayland5-doc qtwebchannel5-doc qtwebengine5-doc
  qtwebsockets5-doc qtwebview5-doc qtx11extras5-doc qtxmlpatterns5-doc
Paquets suggérés :
  qtbase5-dev
Les NOUVEAUX paquets suivants seront installés :
  qt3d5-doc qt5-doc qtbase5-doc qtcharts5-doc qtconnectivity5-doc qtdatavisualization5-doc qtdeclarative5-doc qtgraphicaleffects5-doc qtlocation5-doc qtmultimedia5-doc qtnetworkauth5-doc qtquickcontrols2-5-doc
  qtquickcontrols5-doc qtscript5-doc qtscxml5-doc qtsensors5-doc qtserialbus5-doc qtserialport5-doc qtsvg5-doc qttools5-doc qtvirtualkeyboard5-doc qtwayland5-doc qtwebchannel5-doc qtwebengine5-doc
  qtwebsockets5-doc qtwebview5-doc qtx11extras5-doc qtxmlpatterns5-doc
0 mis à jour, 28 nouvellement installés, 0 à enlever et 0 non mis à jour.
Il est nécessaire de prendre 130 Mo dans les archives.
Après cette opération, 159 Mo d'espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n] O
```
