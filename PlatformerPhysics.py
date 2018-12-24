import pygame
import time
pygame.init()
print("Created by Daimy0u - 2018")

def sleep(s):
    time.sleep(s)

screenWidth = 500
screenHeight = 500
gamewin = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Platformer Test")
x = 40
y = 460
width = 40
height = 40
xvel = 10
yvel = 10
jumpCount = 10
active = True
isJump = False


while active:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > 0:
        x -= xvel
        print("Pos: " + str(x) + " " + str(y))
    if keys[pygame.K_d] and x < screenWidth - width:
        x += xvel
        print("Pos: " + str(x) + " " + str(y))
    if not(isJump):
        if keys[pygame.K_w] and y > 0:
            isJump = True
        if keys[pygame.K_s] and y < screenHeight - height:
            y += yvel
            print("Pos: " + str(x) + " " + str(y))
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if x == 0:
        print("Obj: HIT LEFT BOUNDARY")
    if x == screenWidth - width:
        print("Obj: HIT RIGHT BOUNDARY")
    if y == 0:
        print("Obj: HIT TOP BOUNDARY")
    if y == screenHeight - height:
        print("Obj: HIT BOTTOM BOUNDARY")



    gamewin.fill((0,0,0))
    pygame.draw.rect(gamewin, (255, 255, 255), (x, y, width, height))
    pygame.display.update()


pygame.quit()
