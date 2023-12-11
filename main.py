from map import Map
from snake import Snake
from apple import Apple
from time import sleep
import pygame
import sys

if __name__ == "__main__":
        width = 10
        height = 10
        screan_width, screan_height = width * 50, height * 50
        color_apple = (255, 0, 0)
        color_snake = (0, 255, 0)
        color_empty = (0, 0, 0)
        color_head = (150, 150, 0)
        cell_size = 50
        FPS = 10
        pygame.init()
        screen = pygame.display.set_mode((screan_width, screan_height))
        pygame.display.set_caption("Snake")
        clock = pygame.time.Clock()
        snake = Snake()
        apple = Apple(width, height)
        map = Map(width, height, snake=snake.body, head=snake.head, apple=apple.location)

        while snake.live:
            screen.fill((0, 255, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.change_direction('u')
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction('d')
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction('l')
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction('r')
            snake.move(width, height)
            if snake.eat(apple.location):
                  apple.recreate(snake.body, snake.body)
            map = Map(width, height, snake=snake.body, head=snake.head, apple=apple.location)
            
            for i in range(len(map.map)):
                for j in range(len(map.map[i])):
                    if map.map[i][j] == '*':
                        pygame.draw.rect(screen, color_apple, (j * cell_size, i * cell_size, cell_size, cell_size))
                    elif map.map[i][j] == 's':
                        pygame.draw.rect(screen, color_snake, (j * cell_size, i * cell_size, cell_size, cell_size))
                    elif map.map[i][j] == 'O':
                        pygame.draw.rect(screen, color_head, (j * cell_size, i * cell_size, cell_size, cell_size))
                    elif map.map[i][j] == 'X':
                        pygame.draw.rect(screen, color_empty, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.display.flip()
            #map.print_map()
            snake.check_live()
            clock.tick(FPS)