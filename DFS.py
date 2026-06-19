from time import sleep
from utils import build_graph, print_path, format_res

def find_target(graph, source, target, grant_print=False):
  res = []
  if grant_print:
    print_path([source])
  
  def DFS(path, target):
    nonlocal res
    if len(res) > 0 and len(path) >= len(res):
      return
    
    if path[-1] == target:
      if grant_print:
        print_path(path)
        sleep(1.5)
      if len(res) == 0:
        res = path[:]
        return
      elif len(path) < len(res):
        res = path[:]
      else: 
        return
       
    node = path[-1]
    for neighbour in graph.get_neighbours(node):
      if not neighbour in path:
        path.append(neighbour)
        if grant_print:
          print_path(path)
          sleep(2)
        DFS(path, target)
        path.pop()

  
  DFS([source], target)
  return res


if __name__ == "__main__":

  g = build_graph()

  res = find_target(g, 'A', 'H', True)
  formated_string_res = format_res(res)
  print(formated_string_res)
    