from os import walk
from typing import ValuesView
import pygame
from pygame import key
from pygame.constants import K_SPACE
import threading
import time

pygame.init()
clock = pygame.time.Clock()

winWidth = 1200
winHeight = 600

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Sam's")



class fps():

    def __init__(self, fps):
        self.fps = fps

    def set_fps(self):
        clock = pygame.time.Clock()
        return clock.tick(self.fps)

fps30 = fps(30)
fps60 = fps(60)



class shapes():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw_rect(self):
        win.fill((0, 0, 0), rect=(self.x, self.y, self.w, self.h))

    
class character():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    def walk_left(self):
        img1 = pygame.image.load('Hero/Images/HeroLeftWalk.png')
        img1 = pygame.transform.scale(img1, (self.w, self.h))

        img2 = pygame.image.load('Hero/Images/HeroLeftWalk1.png')
        img2 = pygame.transform.scale(img2, (self.w, self.h))

        imgs = [img1,
                    img2]    
        
        return imgs
    
    def walk_right(self):
        img1 = pygame.image.load('Hero/Images/HeroRightWalk.png')
        img1 = pygame.transform.scale(img1, (self.w, self.h))

        img2 = pygame.image.load('Hero/Images/HeroRightWalk1.png')
        img2 = pygame.transform.scale(img2, (self.w, self.h))

        imgs = [img1,
                    img2]    
        
        return imgs

    def punch(self):
        left_punch = pygame.image.load('Hero/Images/HeroLeftPunch.png')
        left_punch = pygame.transform.scale(left_punch, (self.w, self.h))
        right_punch = pygame.image.load('Hero/Images/HeroRightPunch.png')
        right_punch = pygame.transform.scale(right_punch, (self.w, self.h))

        imgs = [left_punch, right_punch]
        return imgs


def char_values():
    walk_count = 0
    left = False
    right = False

    return walk_count, left, right




def values():
    x_change = 0
    y_change = 0
    default_jump = 10
    jump_count = default_jump
    w = winWidth/6
    h = winWidth/6
    x = winWidth  - w
    y = winHeight - h
    v = 10
    is_jump = False
    is_punch = False
    return (x_change, y_change, default_jump, jump_count, w, h, x, y, v, is_jump, is_punch)


    
  

def main():
    
    x_change, y_change, jump, jump_count, w, h, x, y, v, is_jump, is_punch = values()

    char1 = character(x, y, w, h)
    walk_left = char1.walk_left()
    walk_right = char1.walk_right()
    punch = char1.punch()
    right_punch = punch[1]
    left_punch = punch[0]
    walk_count, left, right = char_values()

    run = True
    while run:

        
        
    
        fps30.set_fps()
        win.fill((255,255,255))
        rect = shapes(x, y, w, h)
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x >= v:
            
            x_change -= v
            left = True
            right = False
            walk_count += 1
            if walk_count >= 2:
                walk_count = 0
            if x_change <= -v:
                x_change = -v
            

        elif keys[pygame.K_RIGHT] and x <= winWidth - w:
            x_change += v
            left = False
            right = True
            walk_count += 1
            if walk_count >= 2:
                walk_count = 0
            if x_change >= v:
                x_change = v
            
        
        else:
            x_change = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jump = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    is_punch = True
            
                
            

            
        
        

        
        
            
                
                    
            
        
        

        if is_jump:
            
            if jump_count >= -jump:
                y -= (jump_count * abs(jump_count))
                jump_count -= 2

                
            else:
                jump_count = jump
                is_jump = False
        
        

        if left:
            
            
            if is_punch:
                win.blit(left_punch, (x, y))  
                
                is_punch = False
                
                    

            else:  
                    
                
                
                if walk_count == 0:
                    win.blit(walk_left[0], (x, y))
                    
                
                if walk_count == 1:
                    win.blit(walk_left[1], (x, y))

        
        
                

        if right:
            if is_punch:
                win.blit(right_punch, (x, y))
                is_punch = False
                
            
            else:
                if walk_count == 0:
                    win.blit(walk_right[0], (x, y))
                    
                
                if walk_count == 1:
                    win.blit(walk_right[1], (x, y))
                
                        
        x += x_change
        
        pygame.display.update()

    

main()