from random import randrange

class Util:
    def genRandomNum(gameMode) -> int:
        return randrange(10) if gameMode.getNum() < 4 else randrange(100)