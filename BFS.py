from time import sleep
from utils import build_graph, print_path, format_res
from collections import deque

def BFS(graph, source, destination, grant_print=False):
  queue = deque([(source, [source])])
  visited = set()

  while len(queue) > 0:
    node, path = queue.popleft()
    if grant_print:
      print_path(path)
      sleep(1.5)
    
    if node in visited:
      continue

    visited.add(node)

    if node == destination:
      return path

    for neighbour in graph.get_neighbours(node):
      if not neighbour in visited:
        new_path = path + [neighbour]
        queue.append((neighbour, new_path))

  return None


if __name__ == "__main__":
  g = build_graph()

  res = BFS(g, 'A', 'H', True)
