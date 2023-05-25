from queue import Queue
import matplotlib.pyplot as plt
import numpy as np
import imageio

# Movements of the agents
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(x, y, visited, maze):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if visited[x][y] or maze[x][y] == 0:
        return False
    return True

def bfs(start, end, maze):
    queue = Queue()
    queue.put(start)
    
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[start[0]][start[1]] = True
    
    frames = []  # To store frames for the GIF
    dpi = 80  # Explicitly set the DPI
    
    while not queue.empty():
        x, y = queue.get()
        
        if x == end[0] and y == end[1]:
            return frames  # Return the frames when the end is reached

        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if is_valid(newX, newY, visited, maze):
                print(f"Agent moving from ({x}, {y}) to ({newX}, {newY})")
                queue.put((newX, newY))
                visited[newX][newY] = True
                maze[newX][newY] = 2  # Represent the path found by agents

                # Save the current state of the maze as a frame
                fig, ax = plt.subplots(dpi=dpi)
                ax.imshow(maze, cmap='hot')
                fig.canvas.draw()  # draw the canvas, cache the renderer
                width, height = fig.canvas.get_width_height()
                image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
                image = image.reshape(height, width, 3)
                frames.append(image)
                plt.close(fig)

    return frames

maze = np.array([
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1]
])

start = (0, 0)
end = (4, 4)

frames = bfs(start, end, maze)

# Save frames as a GIF using imageio
imageio.mimsave('maze.gif', frames, 'GIF', duration=0.5)
