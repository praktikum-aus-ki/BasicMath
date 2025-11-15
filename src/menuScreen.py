import pygame
from const import gameState, COLOR_CODES, POSITIONS
from num import Number

class MenuScreen():
    choosenNum: int = 0
    currentNumPos: int = 0
    gameMode = Number(1, 1, 8)

    def __init__(self):
        pass

    def getMode(self) -> Number:
        return self.gameMode
    
    def logic(self, event) -> gameState:
        state = gameState.MENU

        match event.key:
            case pygame.K_LEFT:
                self.gameMode.decrNum()
            case pygame.K_RIGHT:
                self.gameMode.incrNum()
            case pygame.K_RETURN:
                state = gameState().CHOOSE_NUMBER if self.gameMode.getNum() < 4 else gameState.PLAYING

        return state
    
    def draw(self, screen):
        font = pygame.font.SysFont(None, 50)
        textcolor = COLOR_CODES[self.gameMode.getNum() - 1][1]
        number = self.gameMode.getNum()
        text = font.render(str(number), True, textcolor)
        screen.blit(text, POSITIONS["gameMode"])

        nums = (1, 9) if self.gameMode.getNum() < 4 else (1, 1)

        for i, p in enumerate(POSITIONS["boardMenu"]):
            screen.blit(font.render(str(nums[i]), True, textcolor), p)

        pygame.display.update()