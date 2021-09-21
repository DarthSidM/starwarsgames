import pygame
import random
import math

#initialize the system
pygame.init()

#the game screen
screen=pygame.display.set_mode((800,600))
#background

background=pygame.image.load("backgroundImg.png")

#icon
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)


#title
pygame.display.set_caption("Space Invaders")
#other stats
level=0
lives=5
main_font = pygame.font.SysFont("comicsans",30) 

#score
score=0


#player
playerImg=pygame.image.load("battleship.png")
playerX=370
playerY=480
playerX_change=0
playerY_change=0


#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=5
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(200,600))
    enemyY.append(random.randint(-300,-100))
    enemyX_change.append(0)
    enemyY_change.append(random.random())





#bullet
#ready= you cant see the bullet
#fire= you can see the bullet
bulletImg=pygame.image.load("bullet.png")
bulletY=400
bulletY_change=10
bullet_state="ready"

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<=25:
        return True
    else:
        return False
    




running=True
while running:

    #game background color
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))

    score_label=main_font.render(f"Score:{score}",1,(255,255,255))
    screen.blit(score_label,(10,10))
    
    #keyboard movement controls
    for event in pygame.event.get():
        if  event.type==pygame.QUIT:
            running=False
    
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                    playerX_change -= 4
            if keys[pygame.K_d]:
                    playerX_change += 4

            if keys[pygame.K_w]:
                    playerY_change -= 4
            if keys[pygame.K_s]:
                    playerY_change += 4
            if keys[pygame.K_SPACE]:
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
                

    if event.type == pygame.KEYUP:
        if keys[pygame.K_a] or keys[pygame.K_d]:
            playerX_change = 0
        if keys[pygame.K_w] or keys[pygame.K_s]:
            playerY_change = 0
            
        
    #player movements
    playerX += playerX_change
    playerY += playerY_change
    #player X boundries
    if playerX <= 0:
        playerX=0
    elif playerX >=736:
        playerX=736
    
    #player y boundaries
    if playerY<=0:
        playerY=0
    elif playerY>=536:
        playerY=536
    
    
    #enemy boundary and dynamics
    '''enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change=1
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change=-1
        enemyY += enemyY_change'''
    for i in range(num_of_enemies):
        if enemyY[i]>536:
            
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                game_over_label=main_font.render(f"Game Over!",1,(255,255,255))
                screen.blit(game_over_label,(400,300))
            break



        enemyY[i] += enemyY_change[i]
        bulletX=playerX
        collision=isCollision(enemyX[i], enemyY[i], bulletX ,bulletY)
        if collision:
           bulletY=480
           bullet_state="ready"
           score +=5
           enemyX[i]=random.randint(200,600)
           enemyY[i]=random.randint(-50,5)
           enemyY_change[i]=random.random()
        enemy(enemyX[i],enemyY[i],i)

   
    #bullet dynamics
    if bulletY<=0:
        bulletY=playerY
        bullet_state="ready"





    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change 
    
         
    player(playerX,playerY)
        
    
            
    pygame.display.update()







