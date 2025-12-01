SCALINGFACTOR: int = 3
SCREEN_WIDTH: int = 160 * SCALINGFACTOR
SCREEN_HEIGHT: int = 210 * SCALINGFACTOR

X_OFFSET: int = 47 * SCALINGFACTOR
Y_OFFSET: int = 55 * SCALINGFACTOR

OPERATIONS = [
    ("+", "+"),
    ("-", "-"),
    ("x", "*"),
    ("÷", "/")
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

num0 = (X_OFFSET + 20 * SCALINGFACTOR, Y_OFFSET + 20 * SCALINGFACTOR)
num1 = (num0[0], num0[1] + 40 * SCALINGFACTOR)
num2 = (num1[0], num1[1] + 40 * SCALINGFACTOR)
bar0 = (num2[0], num2[1] + 29 * SCALINGFACTOR)
bar1 = (X_OFFSET, num1[1] + 20 * SCALINGFACTOR)
symbol = (X_OFFSET + 5 * SCALINGFACTOR, num1[1])

POSITIONS = {
    "num0": num0,
    "num1": num1,
    "num2": num2,
    "bar0": bar0,
    "bar1": bar1,
    "symbol": symbol
}

class gameState():
    MENU = 0
    CHOOSE_NUMBER = 1
    PLAYING = 2