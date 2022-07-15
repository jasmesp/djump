import pygame

pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
background = pygame.image.load('./wheein.jpg')
# screen config
WIDTH = 480
HEIGHT = 640
fps = 60

# styling some things
player = pygame.image.load("evajump.bmp")
font = pygame.font.SysFont('arial', 16)
# physics?
timer = pygame.time.Clock()

# screen stuff again?
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('SEXY JUMP!')

# gamevars:
player_position_x = 240
player__position_y = 320
platforms = [[175, 480, 70, 10]]  # platform definition
running = True

while running == True:
    timer.tick(fps)
    screen.fill(white)
    screen.blit(background, (-240, 0))
    screen.blit(player, (player_position_x, player_position_x))
    blocks = []

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, black, platforms[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
