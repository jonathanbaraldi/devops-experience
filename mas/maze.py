from queue import Queue
import matplotlib.pyplot as plt
import numpy as np
import time

# Movimentos possíveis dos agentes
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Função para verificar se um movimento é válido
def is_valid(x, y, visited, maze):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if visited[x][y] or maze[x][y] == 0:
        return False
    return True

# Busca em largura
def bfs(start, end, maze):
    queue = Queue()
    queue.put(start)

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[start[0]][start[1]] = True

    while not queue.empty():
        x, y = queue.get()

        # Se o agente atingiu o fim do labirinto
        if x == end[0] and y == end[1]:
            return True

        # Explorando os movimentos possíveis
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if is_valid(newX, newY, visited, maze):
                print(f"Agent moving from ({x}, {y}) to ({newX}, {newY})")
                queue.put((newX, newY))
                visited[newX][newY] = True
                maze[newX][newY] = 2  # Represent the path found by agents
                
                # Plotting the maze
                plt.imshow(maze, cmap='hot')
                plt.show()
                time.sleep(0.5) # To slow down the visualization

    return False

# Representação do labirinto
maze = np.array([
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1]
])

start = (0, 0)
end = (4, 4)

print(bfs(start, end, maze))
