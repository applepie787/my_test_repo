import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLS = 10
BLOCK_SPACING = 10
BLOCK_START_Y = 50
BLOCK_COLOR = (0, 128, 255)
PADDLE_COLOR = (255, 0, 0)
BALL_COLOR = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Define fonts
font = pygame.font.Font(None, 36)

# Initialize ball and paddle
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = 5

paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT

# Create blocks
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block_x = col * (BLOCK_WIDTH + BLOCK_SPACING)
        block_y = BLOCK_START_Y + row * (BLOCK_HEIGHT + BLOCK_SPACING)
        blocks.append(pygame.Rect(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT))

# Game loop
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= 5
        if keys[pygame.K_RIGHT]:
            paddle_x += 5

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collisions with window boundaries
        if ball_x < 0 or ball_x > WIDTH:
            ball_dx *= -1
        if ball_y < 0:
            ball_dy *= -1

        # Ball collision with the paddle
        if ball_y + BALL_RADIUS >= paddle_y and ball_x >= paddle_x and ball_x <= paddle_x + PADDLE_WIDTH:
            ball_dy *= -1

        # Ball collision with blocks
        for block in blocks.copy():
            if block.colliderect((ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
                blocks.remove(block)
                ball_dy *= -1

        # Check for game over
        if ball_y > HEIGHT:
            game_over = True

        # Check for victory
        if not blocks:
            game_over = True

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the paddle
    pygame.draw.rect(window, PADDLE_COLOR, pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(window, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(window, BLOCK_COLOR, block)

    if game_over:
        if not blocks:
            text = font.render("You Win!", True, (255, 255, 255))
        else:
            text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text, text_rect)

    pygame.display.update()

# Quit the game
pygame.quit()
