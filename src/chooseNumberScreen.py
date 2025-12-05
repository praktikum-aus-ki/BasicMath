import pygame
from const import gameState, COLOR_CODES, POSITIONS, OPERATIONS
from num import Number
from util import Util

class ChoosenNumberScreen():
    gameMode: int = 1
    choosenNum = Number(0, 9)
    operation = None
    sprites, symbols, underscores = Util.load_digit_sprites("/home/fuge/Downloads/JAXAtari_BasicMath/scripts/BasicMath_screenshots")

    def __init__(self, gameMode):
        self.gameMode = gameMode
        self.operation = OPERATIONS[((gameMode- 1) % 4)]

    def getChoosenNum(self) -> Number:
        return self.choosenNum.getNum()
    
    def logic(self, event) -> gameState:
        state = gameState.CHOOSE_NUMBER

        match event.key:
            case pygame.K_DOWN:
                self.choosenNum.decrNum()
            case pygame.K_UP:
                self.choosenNum.incrNum()
            case pygame.K_RETURN:
                state = gameState().PLAYING

        return state
    
    def draw(self, screen):
        textcolor = COLOR_CODES[self.gameMode - 1][1]
        num = self.choosenNum.getNum()
        drawn = [self.sprites[str(num)], self.sprites["9"]] if not num == None else [self.underscores["0"], self.sprites["9"]]

        for i in range(2):
            Util.draw_sprite(screen, drawn[i], textcolor, POSITIONS["num" + str(i)])

        Util.draw_sprite(screen, self.underscores["1"], textcolor, POSITIONS["bar1"])
        Util.draw_sprite(screen, self.symbols[str((self.gameMode - 1) % 4)], textcolor, POSITIONS["symbol"])


        pygame.display.update()