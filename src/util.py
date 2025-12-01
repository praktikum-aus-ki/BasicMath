from random import randrange
from const import SCALINGFACTOR
import pygame
import os

class Util:
    def genRandomNum(gameMode, num) -> int:
        tmp = randrange(10) if gameMode.getNum() < 5 else randrange(100)
        while tmp > num or tmp < 1:
            tmp = randrange(10) if gameMode.getNum() < 5 else randrange(100)
        return tmp
    
    def load_digit_sprites(folder):
        sprites = {}
        symbols = {}
        underscores = {}
        
        for digit in range(10):
            path = os.path.join(folder, f"num{digit}.png")
            sprites[str(digit)] = pygame.image.load(path)

        for digit in range(4):
            path = os.path.join(folder, f"sym{digit}.png")
            symbols[str(digit)] = pygame.image.load(path)

        for digit in range(2):
            path = os.path.join(folder, f"underscore{digit}.png")
            underscores[str(digit)] = pygame.image.load(path)

        return sprites, symbols, underscores
    
    def scale_sprite(sprite_image):
        width = sprite_image.get_width() * SCALINGFACTOR
        height = sprite_image.get_height() * SCALINGFACTOR
        scaled_sprite = pygame.transform.scale(sprite_image, (int(width), int(height)))

        return scaled_sprite
    
    def draw_sprite(screen, drawn, color, position):
        drawn_surface = drawn.convert_alpha()
        drawn_surface.fill(color + (0,), special_flags=pygame.BLEND_RGBA_ADD)
        scaled = Util.scale_sprite(drawn_surface)
        screen.blit(scaled, position)