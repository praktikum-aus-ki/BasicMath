class Number():
    value: int = None
    min: int = 0
    max: int = 0
    isSet: bool = False

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def setNum(self, newVal):
        if newVal >= self.min and newVal <= self.max:
            self.value = newVal
        else:
            self.value = None

    def incrNum(self):
        if self.value == None:
            self.setNum(self.min)
        else:
            self.setNum(self.getNum() + 1)
    
    def decrNum(self):
        if self.value == None:
            self.setNum(self.max)
        else:
            self.setNum(self.getNum() - 1)

    def getNum(self) -> int:
        return self.value