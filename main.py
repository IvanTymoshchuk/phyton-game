import pygame
from pygame .constants import QUIT
import random

pygame.init()

screen = width, height = 800, 600

WHITE = 255, 255, 255
BLAK = 0, 0 , 0
RED = 255, 0, 0
YELLOW = 255, 255, 0
VIOLET = 136, 0, 255
GREEN = 0, 255, 0

colors = (WHITE, RED, YELLOW, VIOLET, GREEN )

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill((WHITE))
ball_rect = ball.get_rect()
ball_spead = [1, 1]

is_working = True
while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_spead)

    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball_spead[1] = -ball_spead[1]
        ball.fill(random.choice(colors))

    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_spead[0] = -ball_spead[0]
        ball.fill(random.choice(colors))



    main_surface.fill((BLAK))
    main_surface.blit(ball, ball_rect)

    pygame.display.flip()
