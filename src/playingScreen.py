import pygame
from const import gameState, COLOR_CODES, OPERATIONS, POSITIONS, SCALINGFACTOR
from num import Number
from random import randrange
from util import Util

class PlayingScreen():
    NumArr = None
    playing: int = 1
    choosenNum: int = 0
    points: int = 0
    gameMode: int = 1
    currentNumPos: int = 2
    operation = None
    sprites, symbols, underscores = Util.load_digit_sprites("/home/fuge/Downloads/JAXAtari_BasicMath/scripts/BasicMath_screenshots")

    def __init__(self, gameMode, choosenNum):
        self.gameMode = gameMode
        self.operation = OPERATIONS[((gameMode - 1) % 4)]
        self.choosenNum = randrange(100) if gameMode > 4 else choosenNum
        self.randomNum = Util.genRandomNum(gameMode, self.choosenNum)
        self.fillArr()

    def fillArr(self):
        self.NumArr = [Number(0, 9) for i in range(6)]
    
    def logic(self, event) -> gameState:
        state = gameState.PLAYING

        match event.key:
            case pygame.K_LEFT:
                print(self.currentNumPos)
                self.currentNumPos = 5 if self.currentNumPos == 0 else self.currentNumPos - 1
            case pygame.K_RIGHT:
                print(self.currentNumPos)
                self.currentNumPos = 0 if self.currentNumPos == 5 else self.currentNumPos + 1
            case pygame.K_DOWN:
                self.NumArr[self.currentNumPos].decrNum()
            case pygame.K_UP:
                self.NumArr[self.currentNumPos].incrNum()
            case pygame.K_RETURN:
                if self.playing <= 10:
                    int_list = [self.NumArr[i].getNum() for i in range(3) if self.NumArr[i].getNum() is not None]
                    remainder_list = [self.NumArr[i].getNum() for i in range(3, 6) if self.NumArr[i].getNum() is not None]

                    result = int("".join(map(str, int_list)))
                    remainder = int("".join(map(str, remainder_list))) if self.operation == ("÷", "/") else 0

                    starterBool = int(eval(str(self.choosenNum) + self.operation[1] + str(self.randomNum))) == result
                    endBool = int(eval(str(self.choosenNum) + "%" + str(self.randomNum))) == remainder
                    isRight = starterBool and endBool if self.operation[1] == "/" else endBool

                    if isRight:
                        self.points += 1

                    self.choosenNum = randrange(100) if self.gameMode > 4 else self.choosenNum
                    self.randomNum = Util.genRandomNum(self.gameMode, self.choosenNum)

                    self.playing += 1
                    self.fillArr()
                else:
                    state = gameState.MENU if self.playing == 10 else gameState.PLAYING

        return state
    
    def draw(self, screen):
        textcolor = COLOR_CODES[self.gameMode - 1][1]
        drawn = [self.sprites[str(self.choosenNum)], self.sprites[str(self.randomNum)]]

        for i in range(6):
            if not self.NumArr[i].getNum() == None:
                Util.draw_sprite(screen, self.sprites[str(self.NumArr[i].getNum())], textcolor, (35 * SCALINGFACTOR + i * 15 * SCALINGFACTOR, POSITIONS["num2"][1]))

        for i in range(2):
            Util.draw_sprite(screen, drawn[i], textcolor, POSITIONS["num" + str(i)])

        Util.draw_sprite(screen, self.underscores["0"], textcolor, (35 * SCALINGFACTOR + self.currentNumPos * 15 * SCALINGFACTOR, POSITIONS["bar0"][1]))
        Util.draw_sprite(screen, self.underscores["1"], textcolor, POSITIONS["bar1"])

        Util.draw_sprite(screen, self.symbols[str((self.gameMode - 1) % 4)], textcolor, POSITIONS["symbol"])

        pygame.display.update()