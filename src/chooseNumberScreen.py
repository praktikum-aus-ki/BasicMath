import pygame
from const import gameState, COLOR_CODES, POSITIONS
from num import Number

class ChoosenNumberScreen():
    choosenNum = Number(0, 0, 9)
    gameMode = Number(1, 1, 8)

    def __init__(self, gameMode):
        self.gameMode = gameMode

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
        font = pygame.font.SysFont(None, 50)
        textcolor = COLOR_CODES[self.gameMode.getNum() - 1][1]
        pos = POSITIONS["boardPlay"]

        number = self.choosenNum.getNum()
        
        screen.blit(font.render(str(number), True, textcolor), pos[0])
        screen.blit(font.render("9", True, textcolor), pos[1])
        
        pygame.display.update()