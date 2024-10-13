from pygame import * 
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
                self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <420:
            self.rect.y += self.speed
back =(200,255,255)
window = display.set_mode((600,500))
display.set_caption('ping-pong game')
game = True 
finish = False
clock = time.Clock()
FPS = 60 

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None,35)
lose1 = font.render('player1 Lose!:(',True,(180,0,0))
lose2 = font.render('player2 Lose!:(',True,(180,0,0))

racket1 = Player('racket.png',30,200,50,150,4)
racket2 = Player('racket.png',520,200,50,150,4) 
ball = GameSprite('tenis_ball.png',200,200,50,50,4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            exit()

    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1 
            speed_y *= 1 

        if ball.rect.y > 420 or ball.rect.y <0:
            speed_y *= -1 

        if ball.rect.x <0 : 
            finish = True 
            window.blit(lose1,(200,200))
            game = False

        if ball.rect.x > 520 : 
            finish = True 
            window.blit(lose2,(200,200))
            game = False

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(60)

        

