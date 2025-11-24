import pygame
from const import gameState, COLOR_CODES, POSITIONS, OPERATIONS
from num import Number

class ChoosenNumberScreen():
    choosenNum = Number(0, 0, 9)
    gameMode = Number(1, 1, 8)
    operation = None

    def __init__(self, gameMode):
        self.gameMode = gameMode
        self.operation = OPERATIONS[((gameMode.getNum() - 1) % 4)]

    def getChoosenNum(self) -> Number:
        return self.choosenNum.getNum()
    
    def logic(self, event) -> gameState:
        state = gameState.CHOOSE_NUMBER

        match event.key:
            case pygame.K_DOWN:
                self.choosenNum.decrNum()
                self.choosenNum.changeSet()
            case pygame.K_UP:
                self.choosenNum.incrNum()
                self.choosenNum.changeSet()
            case pygame.K_RETURN:
                state = gameState().PLAYING

        return state
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 50)
        textcolor = COLOR_CODES[self.gameMode.getNum() - 1][1]
        pos = POSITIONS["boardPlay"]

        number = self.choosenNum.getNum()

        if self.choosenNum.isSet:
            screen.blit(font.render(str(number), True, textcolor), pos[0])

        screen.blit(font.render("_", True, textcolor), (pos[0][0], 1 + pos[0][1]))

        screen.blit(font.render("9", True, textcolor), pos[1])
        screen.blit(font.render(str(self.operation[0]), True, textcolor), (0.75 * pos[1][0], pos[1][1]))
        screen.blit(font.render("_______", True, textcolor), (0.5 * pos[1][0], 1.25 * pos[1][1]))
        
        pygame.display.update()