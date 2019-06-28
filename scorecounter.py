import pygame, random

class ScoreCounter(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((1, 10000))

        #comment out this line to show collision detection:
        self.image.set_alpha(0)

        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-10, 0)

    def update(self):
        #screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
