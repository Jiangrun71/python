import pygame
import sys

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('ship.png')  # Load ship image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1  # Adjust the position to the right
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1  # Adjust the position to the left

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        ship.update()

        screen.fill((0, 0, 0))  # Fill the background with black
        ship.blitme()  # Draw the ship on the screen

        pygame.display.flip()

if __name__ == '__main__':
    run_game()
