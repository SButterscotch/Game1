from os import truncate, walk
import pygame
from Character import character
pygame.init()
from Windows import windows


def main():
    left = False
    right = False
    is_jump = False
    is_punch = False
    walk_count = 0
    clock = pygame.time.Clock()
    run = True
    char1 = character()

    #PunchDelay
    punchTime = pygame.USEREVENT + 0
    pygame.time.set_timer(punchTime, 300)
    

    while run:
        
        clock.tick(20)
        windows.win.fill((255,255,255))


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and char1.x >= 0:
            left = True
            right = False
            char1.x -= char1.v
            walk_count += 1
            if walk_count >= 2:
                walk_count = 0
            
            
        
        if keys[pygame.K_RIGHT] and char1.x <= windows.winWidth - (char1.w +char1.v):
            left = False
            right = True
            char1.x += char1.v
            walk_count += 1
            if walk_count >= 2:
                walk_count = 0
        
        
        
        if is_jump:
            if char1.jump():
                is_jump = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jump = True
                
                if event.key == pygame.K_f:
                    is_punch = True

            
            if event.type == punchTime:
                is_punch = False
            
            
                
        if left:
            if is_punch:
                char1.punch(0)
                

                
                
            else:
                char1.left_walk(walk_count)
            

        if right:
            if is_punch:
                char1.punch(1)
                
                    
                
            else:
                char1.right_walk(walk_count)
        
        
        
        
            
            
            
        
        pygame.display.update()


main()