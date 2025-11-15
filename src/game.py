import pygame, sys
import random
from num import Number
from const import gameState, SCREEN_HEIGHT, SCREEN_WIDTH, COLOR_CODES
from menuScreen import MenuScreen
from playingScreen import PlayingScreen
from chooseNumberScreen import ChoosenNumberScreen


class Game():
    choosenNum: int = 0
    state = gameState().MENU
    gameMode = Number(1, 1, 8)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Basic Math")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def play(self):
        running = True
        gameScreen = MenuScreen()

        while running:
            colorCode = COLOR_CODES[self.gameMode.getNum() - 1]
            self.screen.fill(colorCode[0])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    self.state = gameScreen.logic(event)
                
                match self.state:
                    case gameState.MENU:
                        if(type(gameScreen) != MenuScreen):
                            gameScreen = MenuScreen()
                        
                        self.gameMode = gameScreen.getMode()
                    case gameState.CHOOSE_NUMBER:
                        if(type(gameScreen) != ChoosenNumberScreen):
                            gameScreen = ChoosenNumberScreen(self.gameMode)

                        self.choosenNum = gameScreen.getChoosenNum()
                    case gameState.PLAYING:
                        if(type(gameScreen) != PlayingScreen):
                            gameScreen = PlayingScreen(self.gameMode, self.choosenNum)
            
            gameScreen.draw(self.screen)
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()