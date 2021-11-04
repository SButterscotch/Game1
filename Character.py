import pygame
from Windows import windows

class character():
    x_change = 0
    v = 10
    default_jump = 10
    jump_count = default_jump
    char_size = (windows.winWidth/6, windows.winWidth/6)

    def __init__(self, x=windows.winWidth/2, y=windows.winHeight - char_size[0], w=char_size[0], h = char_size[1]):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def jump(self):
        is_jump = True
        if is_jump:
            if self.jump_count >= -self.default_jump:
                self.y -= (self.jump_count * abs(self.jump_count)) * 0.8
                self.jump_count -= 2
            
            else:
                self.jump_count = self.default_jump
                is_jump = False
                return True
                
        
    
    def punch(self, val):
        if val == 0:
            img = pygame.image.load('Hero/Images/HeroLeftPunch.png')
            img = pygame.transform.scale(img, self.char_size)
            windows.win.blit(img, (self.x, self.y))
            return True
        
        if val == 1:
            img = pygame.image.load('Hero/Images/HeroRightPunch.png')
            img = pygame.transform.scale(img, self.char_size)
            windows.win.blit(img, (self.x, self.y))
            return True

    def left_walk(self, walk_count):
        if walk_count == 0:
            img = pygame.image.load('Hero/Images/HeroLeftWalk.png')
            img = pygame.transform.scale(img, self.char_size)
            windows.win.blit(img, (self.x, self.y))
        
        elif walk_count == 1:
            img = pygame.image.load('Hero/Images/HeroLeftWalk1.png')
            img = pygame.transform.scale(img, self.char_size)
            windows.win.blit(img, (self.x, self.y))

    def right_walk(self, walk_count):
        if walk_count == 0:
            img = pygame.image.load('Hero/Images/HeroRightWalk.png')
            img = pygame.transform.scale(img, self.char_size)
            windows.win.blit(img, (self.x, self.y))
        
        elif walk_count == 1:
            img = pygame.image.load('Hero/Images/HeroRightWalk1.png')
            img = pygame.transform.scale(img, self.char_size)
            windows.win.blit(img, (self.x, self.y))