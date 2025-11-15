import pygame
from const import gameState, COLOR_CODES, OPERATIONS, POSITIONS
from num import Number
from random import randrange
from util import Util

class PlayingScreen():
    playing: int = 1
    choosenNum: int = 0
    currentNumPos: int = 0
    points: int = 0
    gameMode = Number(1, 1, 8)
    NumArr = None

    def __init__(self, gameMode, choosenNum):
        self.gameMode = gameMode
        self.choosenNum = choosenNum
        self.randomNum = Util.genRandomNum(gameMode)
        self.choosenNum = randrange(100) if self.gameMode.getNum() >= 4 else choosenNum
        self.fillArr()

    def fillArr(self):
        self.NumArr = [Number(0, 0, 9) for i in range(6)]
    
    def logic(self, event) -> gameState:
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
                    print(self.NumArr)
                    int_list = [i.getNum() for i in self.NumArr]
                    result = int("".join(map(str, int_list)))
                    print(result)
                    operation = OPERATIONS[(self.gameMode.getNum() - 1) % 4]

                    if eval(str(self.choosenNum) + operation + str(self.randomNum)) == result:
                        points += 1
                    
                    self.randomNum = Util.genRandomNum(self.gameMode)
                    self.playing += 1
                    self.fillArr()
                else:
                    state = gameState.MENU if self.playing == 10 else gameState.PLAYING

        return state
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 50)
        pos = POSITIONS["boardPlay"]
        posResult = POSITIONS["result"]
        textcolor = COLOR_CODES[self.gameMode.getNum() - 1][1]

        screen.blit(font.render(str(self.choosenNum), True, textcolor), pos[0])
        screen.blit(font.render(str(self.randomNum), True, textcolor), pos[1])
        
        for i, p in enumerate(self.NumArr):
            number = p.getNum()

            screen.blit(font.render(str(number), True, textcolor), (i * posResult[0] * (1/6), posResult[1]))

        pygame.display.update()