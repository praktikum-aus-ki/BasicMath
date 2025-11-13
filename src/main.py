import pygame, sys
import random

SCREEN_WIDTH: int = 900
SCREEN_HEIGHT: int = 600

class gameState():
    MENU = 0
    CHOOSE_NUMBER = 1
    PLAYING = 2

COLOR_CODES = [
    [(89, 90, 10), (140, 151, 62)],
    [(143, 80, 21), (37, 89, 127)],
    [(37, 89, 127), (142, 107, 39)],
    [(147, 146, 32), (26, 46, 129)],
    [(18, 46, 137), (113, 115, 25)],
    [(143, 114, 41), (63, 1, 106)],
    [(110, 110, 15), (145, 120, 43)],
    [(161, 104, 35), (161, 104, 35)]
]

class Num():
    value = None
    min = None
    max = None

    def __init__(self, value, min, max):
        self.value = value
        self.min = min
        self.max = max

    def setNum(self, newVal):
        if newVal >= self.min and newVal <= self.max:
            self.value = newVal
        elif newVal < self.min:
            self.value = self.max
        elif newVal > self.max:
            self.value = self.min

    def incrNum(self):
        self.setNum(self.getNum() + 1)
    
    def decrNum(self):
        self.setNum(self.getNum() - 1)

    def getNum(self):
        return self.value

class Game():
    playing: int = 1
    NumArr = [None, None, None]
    choosenNumsPos = 0
    state = gameState().MENU

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Basic Math")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.NumArr[0] = Num(1, 1, 8)
        self.NumArr[1] = Num(0, 0, 9)
        self.fillArr()

    def play(self):
        running = True

        pygame.key.set_repeat(300, 200)
        while running:
            colorCode = COLOR_CODES[self.NumArr[0].getNum() - 1]
            self.screen.fill(colorCode[0])
            numTmp = self.NumArr[self.state] if type(self.NumArr[self.state]) == Num else self.NumArr[self.state][self.choosenNumsPos]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.state == gameState.MENU:
                        if event.key == pygame.K_LEFT:
                            numTmp.decrNum()
                        elif event.key == pygame.K_RIGHT:
                            numTmp.incrNum()
                        elif event.key == pygame.K_RETURN:
                            self.state = gameState().CHOOSE_NUMBER

                    elif self.state == gameState.CHOOSE_NUMBER:
                        if event.key == pygame.K_DOWN:
                            numTmp.decrNum()
                        elif event.key == pygame.K_UP:
                            numTmp.incrNum()
                        elif event.key == pygame.K_RETURN:
                            self.state = gameState().PLAYING

                    elif self.state == gameState.PLAYING:
                        if event.key == pygame.K_LEFT:
                            self.choosenNumsPos -= 1
                        elif event.key == pygame.K_RIGHT:
                            self.choosenNumsPos += 1
                        elif event.key == pygame.K_DOWN:
                            numTmp.decrNum()
                        elif event.key == pygame.K_UP:
                            numTmp.incrNum()
                        elif event.key == pygame.K_RETURN:
                            if self.playing <= 10:
                                self.fillArr()
                                self.playing += 1
                            else:
                                self.state = gameState().MENU
            
            num = numTmp.getNum()
            text = self.font.render(str(num), True, colorCode[1])
            self.screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

    def fillArr(self):
        tmp = []
        for i in range(6):
            tmp.append(Num(0, 0, 9))
        self.NumArr[2] = tmp

if __name__ == "__main__":
    p = Game()
    p.play()