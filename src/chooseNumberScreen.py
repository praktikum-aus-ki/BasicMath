import pygame
from const import gameState, COLOR_CODES
from num import Number

class ChoosenNumberScreen():
    choosenNum = Number(0, 0, 9)
    gameMode: Number = None

    def __init__(self, gameMode):
        self.gameMode = gameMode

    def getChoosenNum(self):
        return self.choosenNum
    
    def logic(self, event):
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
        font = pygame.font.SysFont(None, 50)
        text = font.render(str(self.choosenNum.getNum()), True, COLOR_CODES[self.gameMode.getNum()][1])
        screen.blit(text, (0, 0))
        pygame.display.update()