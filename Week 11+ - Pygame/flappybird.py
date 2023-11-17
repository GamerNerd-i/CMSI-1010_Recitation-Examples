import pygame
import pygame.rect as Rect
import pygame.display as Display
import pygame.draw as Draw
import random

GRAVITY = 0.2
GAME_SPEED = 2

MAX_PIPES = 4
PIPE_WIDTH_SCALAR = 10
PIPE_Y_BUFFER = 10

BIRD_SIZE = 30

pygame.init()
screen = Display.set_mode((720, 1280))
HEIGHT = screen.get_height()
WIDTH = screen.get_width()


class Pipe:
    def __init__(self):
        gap_top = random.randint(HEIGHT * 0.25, HEIGHT * 0.75)
        gap_height = gap_top + random.randint(BIRD_SIZE * 1.25, BIRD_SIZE * 2)
        starting_x = WIDTH * 1.25

        self.gap = {
            "top": gap_top,
            "bottom": gap_height + gap_top,
        }

        self.top_rect = Rect(
            (starting_x, -PIPE_Y_BUFFER),
            (WIDTH / PIPE_WIDTH_SCALAR, self.gap["top"] + PIPE_Y_BUFFER),
        )
        self.bottom_rect = Rect(
            (starting_x, self.gap["bottom"]),
            (WIDTH / PIPE_WIDTH_SCALAR, HEIGHT + PIPE_Y_BUFFER),
        )

        self.hit = False
        self.offscreen = False
        self.color = "green"

    def draw(self):
        Draw.rect(screen, self.color, self.top_rect)
        Draw.rect(screen, self.color, self.bottom_rect)

    def move(self, amount=GAME_SPEED):
        self.top_rect.move_ip(amount)
        self.bottom_rect.move_ip(amount)

        self.offscreen = self.top_rect.x + self.top_rect.width < 0


bird_y = screen.get_height() / 2
bird_x = screen.get_width() / 3

pipes = []

for pipe_num in range(MAX_PIPES):
    newPipe = Pipe()
    newPipe.move((WIDTH / MAX_PIPES) * pipe_num)
    pipes.append(newPipe)


def move_all():
    for pipe in pipes:
        pipe.move()

    index = 0
    while len(pipes) > MAX_PIPES:
        if pipes[index].offscreen:
            pipes.remove(index)
        else:
            index += 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("skyblue")


pygame.quit()
