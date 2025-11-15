from random import randrange

class Util:
    def genRandomNum(gameMode, num) -> int:
        tmp = randrange(10) if gameMode.getNum() < 5 else randrange(100)
        while tmp > num or tmp < 1:
            tmp = randrange(10) if gameMode.getNum() < 5 else randrange(100)
        return tmp