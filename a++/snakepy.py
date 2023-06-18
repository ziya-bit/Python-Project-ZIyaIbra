import pygame
import time

pygame.init()
pygame.mixer.init()
pysnake_list = []
lenght = 1

# Load the music file
music_file = "C:/Users/Leonovo/Downloads/spotifydown.com - Warm Colours.mp3"
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play(-1,0.0)

# Keep the program running while the music is playing
# while pygame.mixer.music.get_busy():
#     continue

display = pygame.display.set_mode((532, 622))
pygame.display.set_caption("PySnake!")
pygame.display.update()
gemeoverre = False
xp = 200
yp = 150
xs = 0
ys = 0

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, (255, 255, 255), [x[0], x[1], snake_block, snake_block])
        # display.blit(value, [0, 0])
clock = pygame.time.Clock()
while not gemeoverre:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            
            gemeoverre = True
        elif i.type == pygame.KEYDOWN:
            if i.key ==pygame.K_w:
                ys = -10
                xs = 0
            elif i.key ==pygame.K_s:
                ys = 10
                xs = 0
            elif i.key ==pygame.K_a:
                ys = 0
                xs = -10
            elif i.key ==pygame.K_d:
                ys = 0
                xs = 10
    # not in setup. creating sprite by turt in pyg.
    xp += xs
    yp += ys
    # for i in pysnake_list:
    #     pygame.draw.rect(display, (255, 255, 255), [xp, yp, 14, 14])
    head = []
    head.append(xp)
    head.append(yp)
    pysnake_list.append(head)
    if len(pysnake_list)>lenght:
        del pysnake_list[0]
    our_snake(14, pysnake_list)
    if (xp<0):
        xp = 0
    pygame.display.update()
    clock.tick(10)
pygame.quit()
# time.sleep(10)
