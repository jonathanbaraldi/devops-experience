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

def bfs(agent_queue, maze, visited, agent_colors):
    while not agent_queue.empty():
        agent_id, x, y, end = agent_queue.get()

        # If the agent has reached the end
        if x == end[0] and y == end[1]:
            print(f"Agent {agent_id} reached the goal")
            return  # Stop the simulation when an agent reaches the goal

        # Exploring the neighborhood
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if is_valid(newX, newY, visited, maze):
                print(f"Agent {agent_id} moving from ({x}, {y}) to ({newX}, {newY})")
                agent_queue.put((agent_id, newX, newY, end))
                visited[newX][newY] = True
                maze[newX][newY] = agent_colors[agent_id]  # Represent the path found by agents

        # Plotting the maze
        plt.imshow(maze, cmap='hot')
        plt.title(f"Agent {agent_id} moving")
        plt.pause(0.5)  # To slow down the visualization

    print("All agents have reached their goals or are stuck")
    plt.show()


# Maze representation
maze = np.array([
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Agent's starting positions and end positions
agents = [(1, 0, 0, (0, 9)), (2, 9, 9, (0, 9))]

# Colors for agents
agent_colors = {1: 2, 2: 3}

# Shared visited array
visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

# Creating a queue for all agents
agent_queue = Queue()
for agent in agents:
    agent_queue.put(agent)

bfs(agent_queue, maze.copy(), visited, agent_colors)
