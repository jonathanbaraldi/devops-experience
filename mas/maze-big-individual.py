from queue import Queue
import matplotlib.pyplot as plt
import numpy as np
import time

# Movements for agents
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Function to validate if a move is allowed
def is_valid(x, y, visited, maze):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if visited[x][y] or maze[x][y] == 0:
        return False
    return True

# Breadth-First Search (BFS) function
def bfs(start, end, maze, agent_id):
    queue = Queue()
    queue.put(start)

    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[start[0]][start[1]] = True

    while not queue.empty():
        x, y = queue.get()

        # If the agent has reached the end
        if x == end[0] and y == end[1]:
            print(f"Agent {agent_id} reached the goal")
            return True

        # Exploring the neighborhood
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if is_valid(newX, newY, visited, maze):
                print(f"Agent {agent_id} moving from ({x}, {y}) to ({newX}, {newY})")
                queue.put((newX, newY))
                visited[newX][newY] = True
                maze[newX][newY] = 2  # Represent the path found by agents

                # Plotting the maze
                plt.imshow(maze, cmap='hot')
                plt.title(f"Agent {agent_id} moving")
                plt.show()
                time.sleep(0.5)  # To slow down the visualization

    print(f"Agent {agent_id} could not reach the goal")
    return False

# Maze representation
maze = np.array([
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Agent's starting positions
starts = [(0, 0), (9, 9)]
end = (9, 0)

for i, start in enumerate(starts):
    print(bfs(start, end, maze.copy(), i+1))  # We use maze.copy() to give each agent a fresh copy of the maze
