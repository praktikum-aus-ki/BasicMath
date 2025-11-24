class Number():
    value: int = 0
    min: int = 0
    max: int = 0
    isSet: bool = False

    def __init__(self, value, min, max):
        self.value = value
        self.min = min
        self.max = max

    def setNum(self, newVal):
        if newVal >= self.min and newVal <= self.max:
            self.value = newVal
        elif newVal < self.min:
            self.value = self.max
        elif newVal > self.max:
            self.value = self.min

    def incrNum(self):
        self.setNum(self.getNum() + 1)
    
    def decrNum(self):
        self.setNum(self.getNum() - 1)

    def getNum(self) -> int:
        return self.value
    
    def changeSet(self):
        self.isSet = True