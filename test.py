import pygame
import time
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
is_blue = True
x = 0
y = 180
a = 5
t = 0
def jump():
    global a
    global t
    if(t<5):
        t+=1
        return -0.5*a*(t**2)
    else:
        t+=1
        if(t == 10):
            t = 0
        return 0.5*a*((t-5)**2)


def checkDims(x,y,x1,y1):
    if x>x1:
       x = x1
    elif x<0:
        x = 0
    if y>y1:
        y = y1
    elif y<0:
        y=0
    else:
        pass
    return [x,y]

while not done:
    screen.fill(0)
    color = (255, 100, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
                x+=10
                y+=10
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
                x-=10
                y+=10
    elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
                x+=10
                y-=10
    elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
                x-=10
                y-=10
    if  pressed[pygame.K_LEFT]:
            x-=10
    if pressed[pygame.K_RIGHT]:
            x+=10
    if pressed[pygame.K_SPACE]:
        y += int(jump())
    elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
        a = 5
        t = 0

    #elif pressed[pygame.K_UP]:
    #        y-=10
    #elif pressed[pygame.K_DOWN]:
    #        y+=10
    x,y = checkDims(x,y,400,200)
    background = pygame.Surface(screen.get_size())
    background.fill((0, 128, 255))
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 30))
    pygame.draw.rect(screen, (165,140,100), pygame.Rect(0, 200, 400, 100))
    pygame.display.flip()
    time.sleep(0.05)
