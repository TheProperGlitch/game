import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1500, 900))
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

    pygame.display.flip()
    dt = clock.tick(120) / 1000

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if table_rect.collidepoint(mouse_pos):
                print("Table clicked!")
