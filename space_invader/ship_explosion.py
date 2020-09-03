import pygame

class ShipExplosion(pygame.sprite.Sprite):
    def __init__(self, ship, *groups):
        super(ShipExplosion, self).__init__(*groups)
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(ship.rect.x, ship.rect.y))
        self.timer = pygame.time.get_ticks()

    def update(self, current_time, window):
        passed = current_time - self.timer
        if 300 < passed <= 600:
            window.blit(self.image, self.rect)
        elif 900 < passed:
            self.kill()