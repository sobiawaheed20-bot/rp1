import pygame
pygame.init()

WIDTH=500
HEIGHT=500

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("grey")
imi1=pygame.image.load("rocketgamep1/images/1314202.jpg")

imi2=pygame.image.load("rocketgamep1/images/OIP-removebg-preview.png")
imis2=pygame.transform.scale(imi2,(110,110))
imi3=pygame.image.load("rocketgamep1/images/R-removebg-preview.png")

x=200
y=250
while True:
    y=y+0.03
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.QUIT()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>-20:
              x=x-15
              pygame.display.update()
            if event.key==pygame.K_RIGHT and x<400:
              x=x+15
              pygame.display.update()
            if event.key==pygame.K_UP and y>0:
              y=y-15
              pygame.display.update()
            if event.key==pygame.K_DOWN and y<510:
              y=y+15
              pygame.display.update()

    

    screen.blit(imi1,(0,0))
    screen.blit(imis2,(x,y))
    if y>530:
      screen.blit(imi3,(-80,0)) 
      pygame.display.update()
      pygame.time.wait(4000)
      break
      





    pygame.display.update()
