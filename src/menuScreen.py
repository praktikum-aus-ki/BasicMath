import pygame
from num import Number
from const import gameState, COLOR_CODES, POSITIONS, OPERATIONS

class MenuScreen():
    choosenNum: int = 0
    currentNumPos: int = 0
    gameMode = Number(1, 1, 8)
    operation = OPERATIONS[((gameMode.getNum() - 1) % 4)]

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
        font = pygame.font.SysFont(None, 50)
        textcolor = COLOR_CODES[self.gameMode.getNum() - 1][1]
        number = self.gameMode.getNum()
        text = font.render(str(number), True, textcolor)
        screen.blit(text, POSITIONS["gameMode"])

        nums = (1, 9) if self.gameMode.getNum() < 5 else (1, 1)
        pos = POSITIONS["boardMenu"]

        for i, p in enumerate(pos):
            screen.blit(font.render(str(nums[i]), True, textcolor), p)

        screen.blit(font.render(str(self.operation[0]), True, textcolor), (0.75 * pos[1][0], pos[1][1]))

        pygame.display.update()