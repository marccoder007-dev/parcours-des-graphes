from graph import Graph

def build_graph():
  g = Graph()

  for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    g.add_node(letter)

  g.add_edge('A', 'B')
  g.add_edge('B', 'C')
  g.add_edge('C', 'D')
  g.add_edge('C', 'G')
  g.add_edge('D', 'H')
  g.add_edge('D', 'E')
  g.add_edge('D', 'G')
  g.add_edge('E', 'F')
  g.add_edge('G', 'H')

  return g


def format_res(res):
  return "->".join(res)


def print_path(path):
  print(format_res(path))