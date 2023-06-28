import pygame
import random

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))

# Create a player sprite
player = pygame.sprite.Sprite()
player.image = pygame.image.load("player.png")
player.rect = player.image.get_rect()

# Create some enemies
enemies = []
for i in range(10):
    enemy = pygame.sprite.Sprite()
    enemy.image = pygame.image.load("enemy.png")
    enemy.rect = enemy.image.get_rect()
    enemy.rect.x = random.randint(0, 640)
    enemy.rect.y = random.randint(0, 480)

# Create a game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit if the user quits
        if event.type == pygame.QUIT:
            running = False

        # Move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 10
            elif event.key == pygame.K_UP:
                player.rect.y -= 10
            elif event.key == pygame.K_DOWN:
                player.rect.y += 10

    # Update the enemies
    for enemy in enemies:
        enemy.rect.x += 10

        # Check if the player has collided with an enemy
        if player.rect.colliderect(enemy.rect):
            # Game over!
            running = False

    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)

    pygame.display.update()

# Quit pygame
pygame.quit()
