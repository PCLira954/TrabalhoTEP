# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Posição inicial do player
player_pos = pygame.Vector2(screen.get_width() * 0.25, screen.get_height() - 200)
player_vel = 0  # Velocidade vertical do player
gravity = 1500  # Força da gravidade
jump_strength = 700  # Força do pulo
is_jumping = False  # Verifica se o player está pulando

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpa a tela
    screen.fill("black")

    # Desenha o player
    pygame.draw.circle(screen, "white", player_pos, 40)

    keys = pygame.key.get_pressed()

    # Se o player está no chão e a tecla de pulo é pressionada, inicia o pulo
    if keys[pygame.K_SPACE] and not is_jumping:
        player_vel = -jump_strength
        is_jumping = True

    # Aplica gravidade
    player_vel += gravity * dt
    player_pos.y += player_vel * dt

    # Limita o player ao "chão"
    if player_pos.y >= screen.get_height() - 200:
        player_pos.y = screen.get_height() - 200
        player_vel = 0
        is_jumping = False  # Permite novo pulo quando o player está no chão

    # Atualiza a tela
    pygame.display.flip()

    # Controla o FPS
    dt = clock.tick(60) / 1000

pygame.quit()
