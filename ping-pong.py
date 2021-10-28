from pygame import *

fps = 60
game = True
clock= time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Ding Dong')
background = transform.scale(image.load('phone.png'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): 
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 5:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed

rocket_1 = Player("gui.png", 10, 10, 50, 100, 10)
rocket_2 = Player("gui.png", 630, 10, 50, 100, 10)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    rocket_1.update_l()
    rocket_1.reset()
    rocket_2.update_r()
    rocket_2.reset()
    display.update()
    clock.tick(fps)
