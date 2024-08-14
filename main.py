import pygame
pygame.init()
#global variables
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white=(255,255,255)
yellow = (255,255,0)
black=(0,0,0)

screen.fill(white)

class myRect():
    def __init__(self,color, pos, hit=0, wid=0):
        self.color = color
        self.pos = pos
        self.hit = hit
        self.wid = wid
        self.scrn = screen
        
    def draw(self):
        pygame.draw.rect(self.scrn, self.color, self.pos, self.hit, self.wid )

    def grow(self,x):
        self.hit += x
        pygame.draw.rect(self.scrn, self.color, self.pos, self.hit, self.wid )
        

#how to draw a circle
position = (300,300)
hit = 5
wid = 2
pygame.draw.rect(screen, red, position, hit, wid )
pygame.display.update()



#creating instances
blueRectangle = myRect(blue, position, hit+60)
redRectangle = myRect(red, position, hit+40)
yellowRectangle = myRect(yellow, position, hit, 5)
greenRectangle = myRect(green, position, 20)


while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueRectangle.draw()
            redRectangle.draw()
            yellowRectangle.draw()
            greenRectangle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueRectangle.grow(2)
            redRectangle.grow(2)
            yellowRectangle.grow(2)
            greenRectangle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackRectangle = myRect(black, pos, 5)
            blackRectangle.draw()
            pygame.display.update()