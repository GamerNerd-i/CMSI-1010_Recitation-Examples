from shutil import move
import pip
import pygame
import pygame.rect as rect
import pygame.display as Display
import pygame.draw as Draw
import random

GRAVITY = 0.2
GAME_SPEED = 2

MAX_PIPES = 4
PIPE_Y_BUFFER = 10

pygame.init()
screen = Display.set_mode((720, 1280))
clock = pygame.time.Clock()

HEIGHT = screen.get_height()
WIDTH = screen.get_width()

BIRD_SIZE = WIDTH // 10
BIRD_RADIUS = BIRD_SIZE // 2


class Pipe:
    def __init__(self):
        gap_top = random.randint(int(HEIGHT * 0.25), int(HEIGHT * 0.75))
        gap_bottom = gap_top + random.randint(BIRD_SIZE * 2, BIRD_SIZE * 4)
        self.starting_x = WIDTH * 1.25

        self.gap = {
            "top": gap_top,
            "bottom": gap_bottom,
        }
        self.width = int(BIRD_SIZE * 1.25)

        self.top_rect = rect.Rect(
            (self.starting_x, -PIPE_Y_BUFFER),
            (self.width, self.gap["top"] + PIPE_Y_BUFFER),
        )
        self.bottom_rect = rect.Rect(
            (self.starting_x, self.gap["bottom"]),
            (self.width, HEIGHT + PIPE_Y_BUFFER),
        )

        self.hit = False
        self.color = "green"

    def draw(self):
        Draw.rect(screen, self.color, self.top_rect)
        Draw.rect(screen, self.color, self.bottom_rect)

    def move(self, amount=-GAME_SPEED):
        self.top_rect.move_ip(amount, 0)
        self.bottom_rect.move_ip(amount, 0)

        if self.top_rect.x + self.top_rect.width < 0:
            self.top_rect.x = self.starting_x
            self.bottom_rect.x = self.starting_x


bird_y = screen.get_height() / 2
bird_x = screen.get_width() / 3

pipes = []
pipe_gap = 2.5

for pipe_num in range(MAX_PIPES):
    new_pipe = Pipe()
    new_pipe.move(new_pipe.width * pipe_gap * pipe_num)
    pipes.append(new_pipe)


def move_all():
    for pipe in pipes:
        pipe.move()


def draw_all():
    Draw.circle(screen, "blue", (bird_x, bird_y), BIRD_RADIUS)

    for pipe in pipes:
        pipe.draw()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("skyblue")

    move_all()
    draw_all()

    Display.flip()
    clock.tick(60)


pygame.quit()
