import pygame
import keyboard
import sys
import time

pygame.init()
win = pygame.display.set_mode((640,450))
pygame.display.set_caption(("Dota for bad pc's, and windows emulators(only sf)"))

pz_h = 0
pz_w = 0

throne_x = 965
throne_y = -565

throne = pygame.image.load("throne.png")
throne = pygame.transform.scale(throne,(100,100))

score = 0

enemy = pygame.image.load("pudj.png")
enemy = pygame.transform.scale(enemy,(150,100))

enemy_x = 1010
enemy_y = -655

spawn_x_en = 1010
spawn_y_en = -655

x_pl = 45
y_pl = 285

t_x = 445
t_y = -265

map_x = 0
map_y = -730

spawn_x = 45
spawn_y = 285

tower_h = 200
tower_w = 200

is_move = True

damage = False

damage_tower = False

razor_skill_one_up = False

razor_skill_one_down = False

map_dota = pygame.image.load("map.jpg")

pl = pygame.image.load("razor.png")
pl = pygame.transform.scale(pl,(100,100))


run = True

while run:
    pygame.time.delay(30)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    plazmafield_rect = pygame.Rect(x_pl,y_pl,pz_h,pz_w)
    pl_rect = pygame.Rect(x_pl,y_pl,50,50)
    tower_rect = pygame.Rect(t_x,t_y,tower_h,tower_w)
    throne_rect = pygame.Rect(throne_x,throne_y,100,100)
    enemy_rect = pygame.Rect(enemy_x,enemy_y,150,100)

    win.blit(map_dota,(map_x,map_y))

    plazmafield = pygame.image.load("plazmafield.png")
    plazmafield = pygame.transform.scale(plazmafield,(pz_h,pz_w))

    tower = pygame.image.load("tower.png")
    tower = pygame.transform.scale(tower,(tower_h,tower_w))
    
    win.blit(pl,(x_pl,y_pl))
    win.blit(enemy,(enemy_x,enemy_y))
    win.blit(plazmafield,(x_pl,y_pl))
    win.blit(tower,(t_x,t_y))
    win.blit(throne,(throne_x,throne_y))

    if is_move == True:
        if keyboard.is_pressed("a"):
            x_pl -= 5
        if keyboard.is_pressed("d"):
            x_pl += 5
        if keyboard.is_pressed("w"):
            y_pl -= 5
        if keyboard.is_pressed("s"):
            y_pl += 5  
        if keyboard.is_pressed("right"):
            map_x -= 5
            x_pl -= 5
            t_x -= 5
            spawn_x -= 5
            throne_x -= 5
            enemy_x -= 5
        if keyboard.is_pressed("left"):
            map_x += 5
            x_pl += 5
            t_x += 5
            spawn_x += 5
            throne_x += 5
            enemy_x += 5
        if keyboard.is_pressed("up"):
            map_y += 5
            y_pl += 5
            t_y += 5
            spawn_y += 5
            throne_y += 5
            enemy_y += 5
        if keyboard.is_pressed("down"):
            map_y -= 5
            y_pl -= 5
            t_y -= 5 
            spawn_y -= 5
            throne_y -= 5
            enemy_y -= 5
        if keyboard.is_pressed("q"):
            razor_skill_one_up = True
        if razor_skill_one_up == True:
            pz_h += 12
            pz_w += 12
        if pz_w == 300 and pz_h == 300:
            razor_skill_one_down = True
            razor_skill_one_up = False
        if razor_skill_one_down == True:
            pz_w -= 15
            pz_h -= 15
            if pz_w <= 0 and pz_h <= 0:
                razor_skill_one_down = False
                
    if enemy_rect.colliderect(tower_rect) == False:
        enemy_x -= 5
        enemy_y += 5

    if plazmafield_rect.colliderect(enemy_rect) == True:
        enemy_x = spawn_x_en
        enemy_y = spawn_y_en

    if pl_rect.colliderect(tower_rect) == True:
        x_pl = spawn_x
        y_pl = spawn_y
    if pl_rect.colliderect(enemy_rect) == True:
        print("game over!!")
        time.sleep(1)
        pygame.quit()
    if plazmafield_rect.colliderect(throne_rect) == True and score == 1:
        print("you win!!!")
        time.sleep(1)
        pygame.quit()
    if plazmafield_rect.colliderect(tower_rect) == True:
        damage_tower = True
    if damage_tower == True:
        tower_h -= 200
        tower_w -= 200
        if tower_w == 0 and tower_h == 0:
            damage_tower = False
            score = 1

    if keyboard.is_pressed("space"):
        print(enemy_x,enemy_y)