import pygame


class windows():
    winWidth = 1200
    winHeight = 600
    win = pygame.display.set_mode((winWidth, winHeight))
    caption = pygame.display.set_caption("Dracule")
    ground = winHeight - winHeight/3