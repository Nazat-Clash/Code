import pygame
import random
import time

# Initialize Pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Set up game window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodger")

ICON = pygame.image.load("python/Project/Space Dodger App/Images/game_icon.png")  # Replace with your icon path
pygame.display.set_icon(ICON)

# Load images
BG = pygame.transform.scale(pygame.image.load("python/Project/Space Dodger App/Images/bg.png"), (WIDTH, HEIGHT))


# Player properties
PLAYER_IMG = pygame.transform.scale(pygame.image.load("python/Project/Space Dodger App/Images/player.png"), (64, 64))
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
PLAYER_SPEED = 5

# Asteroid properties
STAR_IMGS = [
    pygame.transform.scale(pygame.image.load("python/Project/Space Dodger App/Images/asteroid1.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("python/Project/Space Dodger App/Images/asteroid2.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("python/Project/Space Dodger App/Images/asteroid3.png"), (30, 30))
]
STAR_WIDTH = 30
STAR_HEIGHT = 30
STAR_SPEED = 3

# Bullet properties
BULLET_IMG = pygame.transform.scale(pygame.image.load("python/Project/Space Dodger App/Images/bullet.png"), (50, 30))
BULLET_SPEED = 7
BULLET_RELOAD_TIME = -0.2

# Load sounds
loop_music = pygame.mixer.Sound('python/Project/Space Dodger App/Sounds/backround_music.wav')
bullet_sound = pygame.mixer.Sound('python/Project/Space Dodger App/Sounds/bullet.wav')
asteroid_destroy_sound = pygame.mixer.Sound('python/Project/Space Dodger App/Sounds/explosion-nearby.mp3')
spaceship_destroy_sound = pygame.mixer.Sound('python/Project/Space Dodger App/Sounds/explosion-nearby.mp3')
game_over_sound = pygame.mixer.Sound('python/Project/Space Dodger App/Sounds/game_over.wav')

# Set volume for each sound (0.0 to 1.0)
loop_music.set_volume(0.7)
bullet_sound.set_volume(0.68)
asteroid_destroy_sound.set_volume(0.65)
spaceship_destroy_sound.set_volume(0.7)
game_over_sound.set_volume(0.7)

# Play background music in a loop
loop_music.play(loops=-1)


# Font properties
FONT = pygame.font.SysFont("Lato", 30)

# Function to draw on the screen
def draw(player, elapsed_time, stars, bullets):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Score: {int(elapsed_time)}", 1, "white")
    WIN.blit(time_text, (10, 10))
    WIN.blit(PLAYER_IMG, (player.x, player.y))
    
    for star in stars:
        WIN.blit(star['image'], (star['rect'].x, star['rect'].y))
    for bullet in bullets:
        WIN.blit(BULLET_IMG, (bullet.x, bullet.y))

    pygame.display.update()

# Function to draw game over screen
def draw_game_over(elapsed_time):
    WIN.fill((0, 0, 0))
    game_over_text = FONT.render(f"Game Over! Score: {int(elapsed_time)}", 1, "white")
    WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    play_again_text = FONT.render("Play Again", 1, "white")
    play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    WIN.blit(play_again_text, play_again_rect.topleft)
    pygame.display.update()
    return play_again_rect

# Main game loop
def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    starting_time = time.time()
    elapsed_time = 0
    star_add_increment = 1000
    star_count = 0
    stars = []
    bullets = []
    last_shot_time = 0
    game_over = False

    while run:
        if game_over:
            play_again_rect = draw_game_over(elapsed_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_again_rect.collidepoint(event.pos):
                    game_over = False
                    loop_music.play(loops=-1)  # Restart the loop music
                    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
                    starting_time = time.time()
                    elapsed_time = 0
                    stars = []
                    bullets = []
                    last_shot_time = 0
                    star_add_increment = 1000
                    star_count = 0
            continue

        star_count += clock.tick(60)
        elapsed_time = time.time() - starting_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star_img = random.choice(STAR_IMGS)
                star_rect = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append({'rect': star_rect, 'image': star_img})
            star_add_increment = max(200, star_add_increment - 10)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and time.time() - last_shot_time > BULLET_RELOAD_TIME:
                    bullet_rect = pygame.Rect(player.x + PLAYER_WIDTH // 2 - 25, player.y, 50, 30)
                    bullets.append(bullet_rect)
                    bullet_sound.play()
                    last_shot_time = time.time()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += PLAYER_SPEED

        for star in stars[:]:
            star['rect'].y += STAR_SPEED
            if star['rect'].y > HEIGHT:
                stars.remove(star)
            elif star['rect'].colliderect(player):
                spaceship_destroy_sound.play()
                loop_music.stop()  # Stop the loop music
                game_over_sound.play()  # Play the game over sound
                game_over = True

        for bullet in bullets[:]:
            bullet.y -= BULLET_SPEED
            if bullet.y < 0:
                bullets.remove(bullet)
            else:
                for star in stars[:]:
                    if bullet.colliderect(star['rect']):
                        asteroid_destroy_sound.play()
                        stars.remove(star)
                        bullets.remove(bullet)
                        break

        if player.x < 0: 
            player.x = 0
        elif player.x > WIDTH - PLAYER_WIDTH:
            player.x = WIDTH - PLAYER_WIDTH
        if player.y < 0:
            player.y = 0
        elif player.y > HEIGHT - PLAYER_HEIGHT:
            player.y = HEIGHT - PLAYER_HEIGHT

        draw(player, elapsed_time, stars, bullets)

    pygame.quit()

if __name__ == "__main__":
    main()
