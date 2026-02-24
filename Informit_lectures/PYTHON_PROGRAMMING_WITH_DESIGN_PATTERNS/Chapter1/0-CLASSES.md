# 13
```python
baididea = 2.77 # global variable don't use them

class ShowData():
    
    localidea = 3.56

    def __init__(self):
        self._instvar = 5.55
    
    @property # it say the pseudo attribute has a name of that getter method
    def dummyName(self):
        print(f"passing through the getter function {self._instvar}")
        return self._instvar
    
    @dummyName.setter # it is the peudo attribute setter
    def dummyName(self, x): 
        self._instvar = x
        print(f"passing through the setter method with that new value {self._instvar}")


def main():
    print(f"before instanciating, class variable: {ShowData.localidea}")
    s = ShowData()
    print("after initialasing")
    s.dummyName # using the getter
    s.dummyName = 300.33 # using the setter

if __name__== "__main__":
    main()
```
# 14
```python
class Summer():
    
    def addNums(self, x:float, y:float):
        print(f"passing by the method with the two float parameters")
        return x+y
    
    def addNums(self, x:float, s:str):
        print(f"passing by the method with one parameter as float and one parmeter as string")
        y = float(s)
        return x+y
    
def main():
   sumr = Summer()
   print(sumr.addNums(12.0, 2.3))
   print(sumr.addNums(22.3, "13.5"))

if __name__== "__main__":
    main()
```
* problem: it always uses the second defined method (the most recently defined)