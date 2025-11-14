import pygame
from const import gameState, COLOR_CODES, OPERATIONS
from num import Number
from random import randrange

class PlayingScreen():
    playing: int = 1
    choosenNum: int = None
    randomNum: int = None
    currentNumPos: int = 0
    points: int = 0
    gameMode: Number = None
    NumArr = None

    def __init__(self, gameMode, choosenNum):
        self.gameMode = gameMode
        self.choosenNum = choosenNum
        self.randomNum = self.genRandomNum()
        self.fillArr()

    def fillArr(self):
        self.NumArr = [Number(0, 0, 9) for i in range(6)]

    def genRandomNum(self):
        return randrange(10) if self.gameMode.getNum() < 4 else randrange(100)
    
    def logic(self, event):
        state = gameState.PLAYING

        match event.key:
            case pygame.K_LEFT:
                self.currentNumPos -= 1
            case pygame.K_RIGHT:
                self.currentNumPos += 1
            case pygame.K_DOWN:
                self.NumArr[self.currentNumPos].decrNum()
            case pygame.K_UP:
                self.NumArr[self.currentNumPos].incrNum()
            case pygame.K_RETURN:
                if self.playing <= 10:
                    result = int("".join(map(str, self.NumArr)))
                    operation = OPERATIONS[(self.gameMode.getNum() - 1) % 4]

                    if eval(str(self.choosenNum) + operation + str(self.randomNum)) == result:
                        points += 1
                    
                    self.randomNum = self.genRandomNum()
                    self.playing += 1
                    self.fillArr()
                else:
                    state = gameState.MENU if self.playing == 10 else gameState.PLAYING

        return state
    
    def draw(self, screen):
        for p, i in enumerate(self.NumArr):
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(i.getNum()), True, COLOR_CODES[self.gameMode.getNum()][1])
            screen.blit(text, (p * 25, 0))
            pygame.display.update()