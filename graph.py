class Graph:
  def __init__(self):
    self.nodes = {}

  def add_node(self, node: str):
    self.nodes[node] = []

  def add_edge(self, source, destination):
    self.nodes[source].append(destination)
    self.nodes[destination].append(source)

  def get_neighbours(self, node):
    if node in self.nodes:
      return self.nodes[node]

  def __str__(self):
    res = ''
    for node in self.nodes:
      res += f'{node}: {self.nodes[node]} \n'

    return res[:-1]
  
if __name__== '__main__':
  g = Graph()
  g.add_node('A')
  g.add_node('B')

  g.add_edge('A', 'B')
  print(g.get_neighbours('A'))
  print(g)