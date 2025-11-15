SCREEN_WIDTH: int = 900
SCREEN_HEIGHT: int = 600

OPERATIONS = [
    "+",
    "-",
    "*",
    "/"
]

COLOR_CODES = [
    [(89, 90, 10), (140, 151, 62)],
    [(143, 80, 21), (37, 89, 127)],
    [(37, 89, 127), (142, 107, 39)],
    [(147, 146, 32), (26, 46, 129)],
    [(18, 46, 137), (113, 115, 25)],
    [(143, 114, 41), (63, 1, 106)],
    [(110, 110, 15), (145, 120, 43)],
    [(161, 104, 35), (65, 144, 58)]
]

POSITIONS = {
    "gameMode": (SCREEN_WIDTH /  10, SCREEN_HEIGHT/ 10),
    "boardMenu": [(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 5), (SCREEN_WIDTH / 5 , SCREEN_HEIGHT / 4)],
    "boardPlay": [(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 5), (SCREEN_WIDTH / 5 , SCREEN_HEIGHT / 4)],
    "result": (SCREEN_WIDTH / 5 , SCREEN_HEIGHT / 2)
}

class gameState():
    MENU = 0
    CHOOSE_NUMBER = 1
    PLAYING = 2