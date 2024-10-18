import pygame
import sys
import random
import heapq

WIDTH, HEIGHT = 600, 800
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pathfinding A* example")

# Creare una griglia con degli ostacoli casuali
def create_grid(start, end):
    grid = []
    for row in range(ROWS):
        grid.append([])
        for col in range(COLS):
            #20% di probabilità di incontrare un ostacolo
            if random.random() < 0.2:
                grid[row].append(1)
            else:
                grid[row].append(0)
        grid
        return grid

grid = create_grid()

start = (0, 0)
end = (9, 9)
grid = create_grid(start, end)

def draw_grid(win, grid):
    for row in range(ROWS):
        for col in range(COLS):
            color = "white"
            if grid[row][col] == 1:
                color = "black"
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = { row: {col: float('inf') for col in range(COLS)} for row in range(ROWS)}
    g_score[start[0]][start[1]] = 0
    f_score = { row: {col: float('inf') for col in range(COLS)} for row in range(ROWS)}
    f_score[start[0]][start[1]] = heuristic(start, end)

    while open_set:
        current = heapq.heappop(open_set)[1]

        # Se siamo arrivati alla fine, ricostruiamo il percorso
        if current == end:
            path = []
            while current in came_from:



def draw_path(win, path)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    draw_grid(win, grid)
    draw_path(win, grid)
    pygame.display.update()