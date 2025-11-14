import pygame
from const import gameState, COLOR_CODES
from num import Number

class MenuScreen():
    choosenNum: int = None
    currentNumPos: int = 0
    gameMode = Number(1, 1, 8)

    def __init__(self):
        pass

    def getMode(self):
        return self.gameMode
    
    def logic(self, event):
        state = gameState.MENU

        match event.key:
            case pygame.K_LEFT:
                self.gameMode.decrNum()
            case pygame.K_RIGHT:
                self.gameMode.incrNum()
            case pygame.K_RETURN:
                state = gameState().CHOOSE_NUMBER

        return state
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 50)
        text = font.render(str(self.gameMode.getNum()), True, COLOR_CODES[self.gameMode.getNum() - 1][1])
        screen.blit(text, (0, 0))
        pygame.display.update()