# 63
## Resources
- [The classes on the Book Github](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/5.%20SimpleFactory/NamerConsole.py)
## My Code
- My Code
```python
class Builder():
    def compute(self):
        namestr = ""
        while namestr != "quit":
            namestr = input("Entrez un nom valide: ")
            print(f"The entered name is |{namestr}|")
            #namerf = FirstFirst(namestring=namestr)
            #namerl = LastFirst(namestring=namestr)
            #print(f"[FirstFirst] The Worked out name is first: {namerf.first} - last: {namerf.last}")
            #print(f"[LastFirst] The Worked out name is first: {namerl.first} - last: {namerl.last}")
            namer = NamerFactory(namestring=namestr).getNamer()
            print(f"[NamerFactory] The Worked out name is first: {namer.first} - last: {namer.last}")```
```
- The ouput
```bash
jmena01@m077-2281091:~/CONSULTANT/PYTHON/tests$ /bin/python3 /home/jmena01/CONSULTANT/PYTHON/tests/FACTORY/NamerConsoel.py
Entrez un nom valide: Jean-Pierre MENA
The entered name is |Jean-Pierre MENA|
[NamerFactory] The Worked out name is first: Jean-Pierre - last: MENA
Entrez un nom valide: MENA,JEan-Pierre
The entered name is |MENA,JEan-Pierre|
[NamerFactory] The Worked out name is first: JEan-Pierre - last: MENA
```