import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    pygame.init()
    pygame.display.set_caption("Pygame에서 한국어 표시하기")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("malgungothic", 80)
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        txt1 = font.render("한국어 표시 " + str(tmr), True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt1, [100, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()