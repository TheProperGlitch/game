# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1900, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


tavern = pygame.image.load("tavthree.png").convert_alpha()
sTable = pygame.image.load("selectedtable.png").convert_alpha()

tavern_rect = tavern.get_rect()
table_rect = sTable.get_rect()


pygame.mouse.set_pos(player_pos)

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False

    screen.fill("black")
    
    tavern_rect.center = player_pos
    table_rect.center = player_pos

    screen.blit(tavern, tavern_rect)
    screen.blit(sTable, table_rect)

    # Movement
    changex, changey = pygame.mouse.get_pos()
    player_pos.x = 1.75 * (1500 - changex)
    player_pos.y = 1.75 * (1080 - changey)
    
    if keys[pygame.K_w]:
        print(str(changex) + "|" + str(changey))
    if keys[pygame.K_s]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_a]:
        player_pos.x += 300 * dt
    if keys[pygame.K_d]:
        player_pos.x -= 300 * dt

    pygame.display.flip()
    dt = clock.tick(120) / 1000
