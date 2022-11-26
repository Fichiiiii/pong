import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

# colors
background_colour = (0, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

(width, height) = (1440, 810)

# ingame stuff
game_started = False
start = False
gamemode = 0
gamemode_buffer = False
pos_pad1, pos_pad2 = 330, 330
pad1_up, pad1_down = False, False
speed = 10
standard_speed = 10
multiplier = 0
destination = 395
xpos_ball, ypos_ball = 710, 395
ball_speedx, ball_speedy = 15, 0
count_pad1, count_pad2 = 0, 0
goal = 5
game_end = False
move = False

screen = pygame.display.set_mode((width, height))

icon = pygame.image.load('pong_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Pong')

score_font = pygame.font.Font("Sqair-Solid.otf", 100)
text_font = pygame.font.Font("Sqair-Solid.otf", 50)
options_font = pygame.font.Font("Sqair-Solid.otf", 35)

screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    clock.tick(60)
    
    mousex, mousey = pygame.mouse.get_pos()
    mouse = pygame.Rect(mousex, mousey, 1, 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and game_started == False and game_end == False and gamemode != 0:
                pygame.draw.rect(screen, black, (0, 0, 1440, 810))
                start = True
                game_started = True
                move = True
                
        if event.type == pygame.MOUSEBUTTONDOWN and game_end == True:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and mouse.colliderect(retry):
                    gamemode_buffer = True
                    pygame.draw.rect(screen, black, (0, 0, 1440, 810))
                    count_pad1, count_pad2 = 0,0
                    pos_pad1, pos_pad2 = 330, 330
                    gamemode = 0
                    move = True
                    speed = standard_speed
                    ball_speedx, ball_Speedy = 15, 0
                    game_started == False
                    game_end = False
                if mouse_presses[0] and mouse.colliderect(end):
                    running = False
        if event.type == pygame.MOUSEBUTTONUP:
                gamemode_buffer = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_end == False and gamemode == 0 and gamemode_buffer == False:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and mouse.colliderect(singleplayer):
                    gamemode = 1
                if mouse_presses[0] and mouse.colliderect(multiplayer):
                    gamemode = 2
                
                
    # paddle 1
    pressed=pygame.key.get_pressed()
    if gamemode == 1 and move == True:
        if pressed[pygame.K_UP] and game_started == True or pressed[pygame.K_w]:
            pygame.draw.rect(screen, black, (20, pos_pad1, 20, 150))
            pos_pad1 -= speed
        if pressed[pygame.K_DOWN] and game_started == True or pressed[pygame.K_s]:
            pygame.draw.rect(screen, black, (20, pos_pad1, 20, 150))
            pos_pad1 += speed
        
    if gamemode == 2 and move == True:
        if game_started == True and pressed[pygame.K_w]:
            pygame.draw.rect(screen, black, (20, pos_pad1, 20, 150))
            pos_pad1 -= speed
        if game_started == True and pressed[pygame.K_s]:
            pygame.draw.rect(screen, black, (20, pos_pad1, 20, 150))
            pos_pad1 += speed
        
    if pos_pad1 < 0:
        pos_pad1 = 0
    if pos_pad1 > 660:
        pos_pad1 = 660
    
    pad1_collision0 = pygame.Rect(20, pos_pad1 + 60, 30, 20)
    pad1_collision1a, pad1_collision1b = pygame.Rect(20, pos_pad1 + 40, 20, 20), pygame.Rect(20, pos_pad1 + 80, 20, 20)
    pad1_collision2a, pad1_collision2b = pygame.Rect(20, pos_pad1 + 10, 20, 30), pygame.Rect(20, pos_pad1 + 100, 20, 30)
    pad1_collision3a, pad1_collision3b = pygame.Rect(20, pos_pad1, 20, 10), pygame.Rect(20, pos_pad1 + 130, 20, 10)
    
    pygame.draw.rect(screen, white, (20, pos_pad1, 20, 150))
    
    # paddle 2
    if gamemode == 1:
        if xpos_ball < 720:
            multiplier = random.randint(-90, 90)
        if xpos_ball > 720:
            destination = ypos_ball + multiplier
        if destination < 80:
            destination = 80
        if destination > 730:
            destination = 730
    
        if xpos_ball >= 720 and game_started == True and ball_speedx > 0:
            if pos_pad2 > destination - 70:
                pygame.draw.rect(screen, black, (1400, pos_pad2, 20, 150))
                pos_pad2 -= speed
                
            if pos_pad2 < destination - 70:
                pygame.draw.rect(screen, black, (1400, pos_pad2, 20, 150))
                pos_pad2 += speed
                
        if xpos_ball < 1100 and game_started == True and ball_speedx < 0:
            if pos_pad2 > 330:
                pygame.draw.rect(screen, black, (1400, pos_pad2, 20, 150))
                pos_pad2 -= speed
            if pos_pad2 < 330:
                pygame.draw.rect(screen, black, (1400, pos_pad2, 20, 150))
                pos_pad2 += speed
    
    if gamemode == 2 and move == True:
        if game_started == True and pressed[pygame.K_UP]:
            pygame.draw.rect(screen, black, (1400, pos_pad2, 20, 150))
            pos_pad2 -= speed
        if game_started == True and pressed[pygame.K_DOWN]:
            pygame.draw.rect(screen, black, (1400, pos_pad2, 20, 150))
            pos_pad2 += speed
        
        if pos_pad2 < 0:
            pos_pad2 = 0
        if pos_pad2 > 660:
            pos_pad2 = 660
    
    pad2_collision0 = pygame.Rect(1400, pos_pad2 + 60, 40, 20)
    pad2_collision1a, pad2_collision1b = pygame.Rect(1400, pos_pad2 + 40, 20, 20), pygame.Rect(1400, pos_pad2 + 80, 20, 20)
    pad2_collision2a, pad2_collision2b = pygame.Rect(1400, pos_pad2 + 10, 20, 30), pygame.Rect(1400, pos_pad2 + 100, 20, 30)
    pad2_collision3a, pad2_collision3b = pygame.Rect(1400, pos_pad2, 20, 10), pygame.Rect(1400, pos_pad2 + 130, 20, 10)
    
    pygame.draw.rect(screen, white, (1400, pos_pad2, 20, 150))
    
    # count
    pygame.draw.rect(screen, black, (300, 57, 110, 88))
    score1 = score_font.render(str(count_pad1), 1, white)
    score1_pos = score1.get_rect(center=(357, 100))
    screen.blit(score1, score1_pos)
    
    pygame.draw.rect(screen, black, (1030, 57, 110, 88))
    score2 = score_font.render(str(count_pad2), 1, white)
    score2_pos = score2.get_rect(center=(1087, 100))
    screen.blit(score2, score2_pos)
    
    # ball
    if start == True:
        start_pad = random.randint(0, 1)
        
        if start_pad == 0:
            xpos_ball = 50
            ball_speedx = ball_speedx * 1
        if start_pad == 1:
            xpos_ball = 1370
            ball_speedx = ball_speedx * -1
            
        start = False
        
    pygame.draw.rect(screen, black, (xpos_ball, ypos_ball, 20, 20))
    pygame.draw.rect(screen, white, (width/2-10, 0, 20, height))
        
    xpos_ball = xpos_ball + ball_speedx
    ypos_ball = ypos_ball + ball_speedy
            
    if game_started == True:
        ball_collision = pygame.Rect(xpos_ball, ypos_ball, 20, 20)
        pygame.draw.rect(screen, white, (xpos_ball, ypos_ball, 20, 20))
            
        if xpos_ball <= 10:
            pygame.draw.rect(screen, black, (xpos_ball, ypos_ball, 20, 20))
            ball_speedx, ball_speedy = -15, 0
            xpos_ball, ypos_ball = 1370, 395
            count_pad2 += 1
        if xpos_ball >= 1430:
            pygame.draw.rect(screen, black, (xpos_ball, ypos_ball, 20, 20))
            ball_speedx, ball_speedy = 15, 0
            xpos_ball, ypos_ball = 50, 395
            count_pad1 += 1
            
        if ypos_ball <= 0:
            ball_speedy = ball_speedy * -1
        if ypos_ball >= 810:
            ball_speedy = ball_speedy * -1
            
        if ball_collision.colliderect(pad1_collision0):
            ball_speedx, ball_speedy = 15, 0
        if ball_collision.colliderect(pad1_collision1a) or ball_collision.colliderect(pad1_collision1b):
            if ball_speedy <= 0:
                ball_speedx, ball_speedy = 15, -5
            else:
                ball_speedx, ball_speedy = 15, 5
        if ball_collision.colliderect(pad1_collision2a) or ball_collision.colliderect(pad1_collision2b):
            if ball_speedy <= 0:
                ball_speedx, ball_speedy = 10, -10
            else:
                ball_speedx, ball_speedy = 10, 10
        if ball_collision.colliderect(pad1_collision3a) or ball_collision.colliderect(pad1_collision3b):
            if ball_speedy <= 0:
                ball_speedx, ball_speedy = 5, -15
            else:
                ball_speedx, ball_speedy = 5, 15
            
        if ball_collision.colliderect(pad2_collision0):
            ball_speedx, ball_speedy = -15, 0
        if ball_collision.colliderect(pad2_collision1a) or ball_collision.colliderect(pad2_collision1b):
            if ball_speedy <= 0:
                ball_speedx, ball_speedy = -15, -5
            else:
                ball_speedx, ball_speedy = -15, 5
        if ball_collision.colliderect(pad2_collision2a) or ball_collision.colliderect(pad2_collision2b):
            if ball_speedy <= 0:
                ball_speedx, ball_speedy = -10, -10
            else:
                ball_speedx, ball_speedy = -10, 10
        if ball_collision.colliderect(pad2_collision3a) or ball_collision.colliderect(pad2_collision3b):
            if ball_speedy <= 0:
                ball_speedx, ball_speedy = -5, -15
            else:
                ball_speedx, ball_speedy = -5, 15

    # gamemode
    if game_started == False and game_end == False and gamemode == 0:
        pygame.draw.rect(screen, white, (420, 305, 600, 200))
        pygame.draw.rect(screen, black, (430, 315, 580, 180))
        
        gamemode_text = text_font.render(("CHOOSE  GAMEMODE"), 1, white)
        gamemode_text_pos = gamemode_text.get_rect(center=(width/2, height/2 - 25))
        screen.blit(gamemode_text, gamemode_text_pos)
        
        sp_text = options_font.render(("1  PLAYER"), 1, white)
        sp_text_pos = sp_text.get_rect(center=(600, 449))
        screen.blit(sp_text, sp_text_pos)
        
        mp_text = options_font.render(("2  PLAYER"), 1, white)
        mp_text_pos = mp_text.get_rect(center=(846, 449))
        screen.blit(mp_text, mp_text_pos)
        
        singleplayer = pygame.Rect(509, 433, 182, 33)
        multiplayer = pygame.Rect(749, 433, 194, 33)
        
        if mouse.colliderect(singleplayer):
            pygame.draw.rect(screen, white, (510, 466, 182, 3))
            pygame.draw.rect(screen, (107, 107, 107), (510, 469, 182, 1))
        if mouse.colliderect(multiplayer):
            pygame.draw.rect(screen, white, (750, 466, 194, 3))
            pygame.draw.rect(screen, (107, 107, 107), (750, 469, 194, 1))

    # before game
    if game_started == False and game_end == False and gamemode != 0:
        pygame.draw.rect(screen, white, (420, 305, 600, 200))
        pygame.draw.rect(screen, black, (430, 315, 580, 180))
        
        start_text = text_font.render(("PRESS  SPACE"), 1, white)
        start_text_pos = start_text.get_rect(center=(width/2, height/2))
        screen.blit(start_text, start_text_pos)

    # game end
    if count_pad1 >= goal or count_pad2 >= goal:
        game_end = True
        game_started = False
        start = False
        xpos_ball, ypos_ball = 710, 395
        speed = 0
        move = False
        ball_speedx, ball_speedy = 0, 0
        
        if count_pad1 >= goal:
            winner = "PLAYER  1"
        if count_pad2 >= goal:
            winner = "PLAYER  2"
        
        pygame.draw.rect(screen, white, (420, 305, 600, 200))
        pygame.draw.rect(screen, black, (430, 315, 580, 180))
        
        end_text = text_font.render((f"{winner}   WINS"), 1, white)
        end_text_pos = end_text.get_rect(center=(width/2, height/2 - 25))
        screen.blit(end_text, end_text_pos)
        
        retry_text = options_font.render(("RETRY"), 1, white)
        retry_text_pos = retry_text.get_rect(center=(600, 449))
        screen.blit(retry_text, retry_text_pos)
        
        quit_text = options_font.render(("QUIT"), 1, white)
        quit_text_pos = quit_text.get_rect(center=(841, 449))
        screen.blit(quit_text, quit_text_pos)
        
        retry = pygame.Rect(536, 433, 128, 33)
        end = pygame.Rect(776, 433, 128, 33)
        
        if mouse.colliderect(retry):
            pygame.draw.rect(screen, white, (537, 466, 126, 3))
            pygame.draw.rect(screen, (107, 107, 107), (537, 469, 126, 1))
        if mouse.colliderect(end):
            pygame.draw.rect(screen, white, (796, 466, 88, 3))
            pygame.draw.rect(screen, (107, 107, 107), (796, 469, 88, 1))
            

    pygame.display.flip()
    
sys.exit()