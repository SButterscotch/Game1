import pygame, random
from Windows import windows

class character():
    x_change = 0
    v = 20
    default_jump = 10
    jump_count = default_jump
    char_size = (windows.winWidth/6, windows.winHeight/3)

    def __init__(self, x=windows.winWidth/2, y=windows.winHeight - windows.winHeight/3, w=char_size[0], h = char_size[1]):
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
    
    
    


class enemy():
    x_axis = (random.randint(100, windows.winWidth))
    enemy_size = 50, 100
    v = 10
    def_y = 0
    valid = True
    

    def __init__(self, x=x_axis, y=def_y, w=enemy_size[0], h=enemy_size[1]):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def downfall(self):
        
        if self.valid:
            self.y += self.v
            if self.y >= windows.winHeight - self.h:
                self.valid = False
            

    # def collision(self):

    
    def draw_enemy(self):
        windows.win.fill((0, 0, 0), (self.x, self.y, self.w, self.h))
