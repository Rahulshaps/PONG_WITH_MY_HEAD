#importing the modules
import pygame
from random import randint
#color definition
BLACK = (0,0,0)
WHITE = (0,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
#init pygmae
pygame.init()
#creating image for you head NOTE: make sure that you use png and the size within 60x60
img = pygame.image.load("C:\\Users\\admin\\Desktop\\codes\\certificate\\SHA22.png")
#Initializing the display window
size = (800,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong with my head")
#Starting coordinates of the paddle
rect_x = randint(0,700)
rect_y = 580
#initial speed of the paddle
rect_change_x = 0
rect_change_y = 0
#initial position of the ball
ball_x = 50
ball_y = 50
#speed of the ball
ball_change_x = 5
ball_change_y = 5
#score variable init
score = 0
#draws the paddle
def drawrect(screen,x,y):

    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,RED,[x,y,100,20])

#game's main loop (control the movement of paddle and ball logic and writes head image)
#creating a clock setting for the game
clock=pygame.time.Clock()
#done is loop exit variable
done = False
while not done:
    #checkes for windows close 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True
    #checkes the keydown of left and right keys
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                rect_change_x = -6

            elif event.key == pygame.K_RIGHT:

                rect_change_x = 6

    #check for the keyup of left and right to stop the paddle
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                rect_change_x = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:

                rect_change_y = 0            

    screen.fill(BLACK)
    rect_x += rect_change_x
    rect_y += rect_change_y
    ball_x += ball_change_x
    ball_y += ball_change_y
    #for the movement of the ball and score control
    if ball_x<0:
        ball_x=0
        ball_change_x = ball_change_x * -1

    elif ball_x>785:

        ball_x=785
        ball_change_x = ball_change_x * -1
    elif ball_y<0:

        ball_y=0

        ball_change_y = ball_change_y * -1

    elif ball_x>=rect_x and ball_x<=rect_x+100 and ball_y==565:

        ball_change_y = ball_change_y * -1

        score = score + 1

    elif ball_y>600:

        ball_change_y = ball_change_y * -1

        score = 0

    #other elements
    pygame.draw.circle(screen,WHITE,[ball_x,ball_y],10,10)
    screen.blit(img,(ball_x - 15,ball_y - 15))
    drawrect(screen,rect_x,rect_y)
    pygame.draw.rect(screen,RED,[0,675,800,200],1)
    pygame.draw.rect(screen,RED,[500,675,800,200],1)
    font= pygame.font.SysFont('impact', 30, False, False)
    font1= pygame.font.SysFont('impact', 20, False, False)
    text = font.render("SCORE  =  " + str(score), True, WHITE)
    text1 = font1.render("PONG WITH MY HEAD",True,WHITE)
    text2= font1.render("- RAHUL SHA",True,WHITE)
    screen.blit(text2,[650,750])
    screen.blit(text1,[550,700])
    screen.blit(text,[50,700])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()   