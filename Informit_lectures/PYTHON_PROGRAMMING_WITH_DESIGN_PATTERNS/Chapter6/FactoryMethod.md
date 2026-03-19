# [The Main Resource on giThub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/6.%20FactoryMethod/SwimClasses.py)
## calcLaneOrder
* If we have 7 lines it will get [4,5,3,6,2,7,1] 
  * il is a bit complicated algorithm
# Some error in StraightSeeding
```python
class StraightSeeding(Seeding):
    def __init__(self, sw, nlanes):
        self.swimmers = sw
        self.numLanes = nlanes
        self.count = len(sw)
        self.lanes = self.calcLaneOrder()
        self.seed()
# --------------------------------
    def seed(self):
    #loads the swmrs array and sorts it
        asw = self.sortUpwards()  # number in last heat
        self.lastHeat = self.count % self.numLanes
        if (self.lastHeat < 3):
            self.lastHeat = 3 # last heat must have 3 or more

        lastLanes =self.count - self.lastHeat
        self.numHeats = self.count / self.numLanes

        if (lastLanes > 0): # it should be self.count % self.numLanes
            self.numHeats += 1 # compute total number of heats
        heats = self.numHeats
```
* At the end we should have
```python
        swimmers = [] # shouldn't it be self.swimmers
        for i in range(0, self.count):
            swimmers.append(asw[i]); # shouldn't it be self.swimmers
```
- The Circle Seeding forgets to regoanize the other swimmers .... (who already are in the non top heats!!)