from pygame import *

wid, hei = 600, 700

FPS = 60

clock = time.Clock()

window = display.set_mode((wid, hei))
backgroundcolor = (200, 255, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_size_x, player_size_y, speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def control_wasd(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < hei - 80:
            self.rect.y += self.speed
        
    def control_keys(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect. y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < hei - 80:
            self.rect.y += self.speed

player1 = Player('racket.png', 5, 350, 30, 130, 10)
player2 = Player('racket.png', 570, 350, 30, 130, 10)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(backgroundcolor)

    player1.control_wasd()
    player2.control_keys()

    player1.reset()
    player2.reset()



    display.update()
    clock.tick(FPS)
