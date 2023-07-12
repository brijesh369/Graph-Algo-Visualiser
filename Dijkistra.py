import heapq
import sys
import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Dijkstra's Algorithm Visualizer")

# Font for displaying distance on nodes
font = pygame.font.SysFont(None, 20)

# Class to represent a node
class Node:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.neighbors = []
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))

    def reset(self):
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

# Function to draw the graph on the screen
def draw_graph(nodes):
    screen.fill(BLACK)
    for node in nodes:
        pygame.draw.circle(screen, WHITE, (node.x, node.y), 20)
        text = font.render(str(node.distance), True, BLACK)
        text_rect = text.get_rect(center=(node.x, node.y))
        screen.blit(text, text_rect)

        for neighbor, weight in node.neighbors:
            pygame.draw.line(screen, BLUE, (node.x, node.y), (nodes[neighbor].x, nodes[neighbor].y), 2)

    pygame.display.flip()

# Function to run Dijkstra's algorithm
def dijkstra(nodes, source, target):
    nodes[source].distance = 0
    pq = [(0, source)]

    while pq:
        distance, u = heapq.heappop(pq)

        if nodes[u].visited:
            continue

        nodes[u].visited = True

        for v, weight in nodes[u].neighbors:
            if not nodes[v].visited and nodes[u].distance + weight < nodes[v].distance:
                nodes[v].distance = nodes[u].distance + weight
                nodes[v].previous = u
                heapq.heappush(pq, (nodes[v].distance, v))

        draw_graph(nodes)
        pygame.time.wait(500)

    # Calculate the shortest path
    shortest_path = []
    node = target
    while node is not None:
        shortest_path.insert(0, node)
        node = nodes[node].previous

    # Display the shortest path
    print("Shortest path from node", source, "to node", target, ":")
    print(" -> ".join(map(str, shortest_path)))

    # Display the final result
    print("Shortest distances from node", source, ":")
    for node in nodes:
        print("Node", node.index, ":", node.distance)

    draw_graph(nodes)
    pygame.time.wait(2000)

# Create nodes
nodes = [
    Node(0, 100, 100),
    Node(1, 200, 300),
    Node(2, 400, 200),
    Node(3, 600, 300),
    Node(4, 700, 100)
]

# Define edges
nodes[0].add_neighbor(1, 3)
nodes[0].add_neighbor(2, 4)
nodes[1].add_neighbor(2, 2)
nodes[1].add_neighbor(3, 1)
nodes[2].add_neighbor(3, 6)
nodes[3].add_neighbor(4, 2)

running = True
source = 0
target = 4

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                for node in nodes:
                    node.reset()
                dijkstra(nodes, source, target)

    draw_graph(nodes)

pygame.quit()
