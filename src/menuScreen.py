import pygame
from num import Number
from const import gameState, COLOR_CODES, POSITIONS, OPERATIONS
from util import Util

class MenuScreen():
    choosenNum: int = 0
    currentNumPos: int = 0
    gameMode = Number(1, 1, 8)
    operation = OPERATIONS[((gameMode.getNum() - 1) % 4)]
    sprites, symbols, underscores = Util.load_digit_sprites("/home/fuge/Downloads/JAXAtari_BasicMath/scripts/BasicMath_screenshots")

    def __init__(self):
        pass

    def getMode(self) -> Number:
        return self.gameMode
    
    def logic(self, event) -> gameState:
        state = gameState.MENU

        match event.key:
            case pygame.K_LEFT:
                self.gameMode.decrNum()
                self.operation = OPERATIONS[((self.gameMode.getNum() - 1) % 4)]
            case pygame.K_RIGHT:
                self.gameMode.incrNum()
                self.operation = OPERATIONS[((self.gameMode.getNum() - 1) % 4)]
            case pygame.K_RETURN:
                state = gameState().CHOOSE_NUMBER if self.gameMode.getNum() < 5 else gameState.PLAYING

        return state
    
    def draw(self, screen):
        textcolor = COLOR_CODES[self.gameMode.getNum() - 1][1]
        number = self.gameMode.getNum()
        nums = (1, 9) if self.gameMode.getNum() < 5 else (1, 1)
        drawn = [self.sprites[str(number)], self.sprites[str(nums[0])], self.sprites[str(nums[1])]]

        Util.draw_sprite(screen, drawn[0], textcolor, (POSITIONS["symbol"][0], POSITIONS["num0"][1]))

        for i in range(1, 3):
            Util.draw_sprite(screen, drawn[i], textcolor, POSITIONS["num" + str(i)])

        Util.draw_sprite(screen, self.symbols[str((self.gameMode.getNum() - 1) % 4)], textcolor, (POSITIONS["symbol"][0], POSITIONS["symbol"][1]))

        pygame.display.update()