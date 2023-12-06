from pygame import *
from time import time as timer

Clock = time.Clock()
FPS = 60
Clock.tick(FPS)

ball_x = 0
ball_y = 0

speed_x = 4
speed_y = 4

font.init()

font1 = font.Font(None, 35)
winp1 = font1.render("!Player1 WON!", True, (180, 0, 0))
winp2 = font1.render("!Player2 WON!", True, (180, 0, 0))

class Gamesprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (width, height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.y = p_y
        self.rect.x = p_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class player(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if key_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y += 10

class player2(Gamesprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if key_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += 10

ball = Gamesprite("tenis_ball.png", ball_x, ball_y, 4, 50, 50)

win_width = 700
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
window.fill((255, 255, 255))
p1 = player("racket.png", 5, win_height - 100, 80, 40, 150)

p2 = player2("racket.png", 650, win_height - 100, 80, 40,150)

finish = False

game = True
while game:

    Clock.tick(FPS)

    if finish == False:
        window.fill((255, 255, 255))  
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        p2.reset()
        p2.update()

        p1.reset()
        p1.update()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(winp1, (200, 200))


        if ball.rect.x > win_width:
            finish = True
            window.blit(winp2, (200, 200))

    
    ball.reset()
    
    display.update()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
