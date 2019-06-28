import pygame, random

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.image = pygame.transform.smoothscale(self.image, (20 , 40))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-10, 0)

    def update(self):
        #screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
