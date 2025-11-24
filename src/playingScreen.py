import pygame
from const import gameState, COLOR_CODES, OPERATIONS, POSITIONS
from num import Number
from random import randrange
from util import Util

class PlayingScreen():
    NumArr = None
    playing: int = 1
    choosenNum: int = 0
    points: int = 0
    gameMode = Number(1, 1, 8)
    currentNumPos = Number(0, 0, 5)
    operation = None

    def __init__(self, gameMode, choosenNum):
        self.gameMode = gameMode
        self.operation = OPERATIONS[((gameMode.getNum() - 1) % 4)]
        self.choosenNum = randrange(100) if gameMode.getNum() > 4 else choosenNum
        self.randomNum = Util.genRandomNum(gameMode, self.choosenNum)
        self.fillArr()

    def fillArr(self):
        self.NumArr = [Number(0, 0, 9) for i in range(6)]
    
    def logic(self, event) -> gameState:
        state = gameState.PLAYING

        match event.key:
            case pygame.K_LEFT:
                self.currentNumPos.decrNum()
            case pygame.K_RIGHT:
                self.currentNumPos.incrNum()
            case pygame.K_DOWN:
                self.NumArr[self.currentNumPos.getNum()].decrNum()
                self.NumArr[self.currentNumPos.getNum()].changeSet()
            case pygame.K_UP:
                self.NumArr[self.currentNumPos.getNum()].incrNum()
                self.NumArr[self.currentNumPos.getNum()].changeSet()
            case pygame.K_RETURN:
                if self.playing <= 10:
                    int_list = [self.NumArr[i].getNum() for i in range(4)]
                    remainder_list = [self.NumArr[i].getNum() for i in range(4, 6)]

                    result = int("".join(map(str, int_list)))
                    remainder = int("".join(map(str, remainder_list))) if self.operation else 0

                    starterBool = int(eval(str(self.choosenNum) + self.operation[1] + str(self.randomNum))) == result
                    endBool = int(eval(str(self.choosenNum) + "%" + str(self.randomNum))) == remainder
                    isRight = starterBool and endBool if self.operation[1] == "/" else endBool

                    if isRight:
                        print(self.operation[1])
                        self.points += 1
                        print("RIGHT!")

                    self.choosenNum = randrange(100) if self.gameMode.getNum() > 4 else self.choosenNum
                    self.randomNum = Util.genRandomNum(self.gameMode, self.choosenNum)

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
        screen.blit(font.render(str(self.operation[0]), True, textcolor), (0.75 * pos[1][0], pos[1][1]))
        screen.blit(font.render("_______", True, textcolor), (0.5 * pos[1][0], 1.25 * pos[1][1]))

        for i, p in enumerate(self.NumArr):
            if p.isSet:
                number = p.getNum()

                screen.blit(font.render(str(number), True, textcolor), (25 * i + pos[1][0] / 2, 1.5 * pos[1][1]))

        screen.blit(font.render("_", True, textcolor), (25 * self.currentNumPos.getNum() + pos[1][0] / 2, 1.55 * pos[1][1]))
        pygame.display.update()