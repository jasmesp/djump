import pygame



pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
hottie_pink = (	255, 20, 147)
gray = (128, 128, 128)
background = pygame.image.load('./wheein.jpg')
# screen config
game_window_width = 480
game_window_height = 640
fps = 60

# styling some things
scale_factor = (50,50)
player = pygame.transform.scale(pygame.image.load("evajump.bmp"), (scale_factor))
font = pygame.font.SysFont('arial', 16)
# physics?
timer = pygame.time.Clock()

# screen stuff again?
screen = pygame.display.set_mode([game_window_width, game_window_height])
pygame.display.set_caption('SEXY JUMP!')

# gamevars:
player_position_x = 220
player_position_y = 525
platforms = [[190, 600, 100, 15]]  # x axis y axis width and height of platform.
running = True

while running == True:
    timer.tick(fps)
    screen.fill(white)
    screen.blit(background, (-240, 0))
    screen.blit(player, (player_position_x, player_position_y))
    blocks = []

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, hottie_pink, platforms[i])
        blocks.append(block)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
