from pygame import *
from time import time as timer

Clock = time.Clock()
FPS = 60
Clock.tick(FPS)

racket1 = transform.scale(
        image.load('racket.png'),
        (30, 180))

class Gamesprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed, width, height):
        super().__init__()
        self.image = racket1
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.y = p_y
        self.rect.x = p_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class player(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]:
            self.rect.y -= 10
        if key_pressed[K_s]:
            self.rect.y += 10

class player2(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]:
            self.rect.y -= 10
        if key_pressed[K_DOWN]:
            self.rect.y += 10

win_width = 700
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
window.fill((255, 255, 255))
p1 = player(racket1, 5, win_height - 100, 80, 2, 10)

p2 = player2(racket1, 660, win_height - 100, 80, 2, 10)

game = True
while game:
    window.fill((255, 255, 255))    

    Clock.tick(FPS)
    
    p1.reset()
    p1.update()

    p2.reset()
    p2.update()
    
    display.update()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
