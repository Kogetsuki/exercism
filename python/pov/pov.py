from json import dumps
from collections import deque


class Tree:
  def __init__(self, label, children=None):
    self.label = label
    self.children = children if children is not None else []


  def __dict__(self):
    return {self.label: [c.__dict__() for c in sorted(self.children)]}


  def __str__(self, indent=None):
    return dumps(self.__dict__(), indent=indent)


  def __lt__(self, other):
    return self.label < other.label


  def __eq__(self, other):
    return self.__dict__() == other.__dict__()


  def from_pov(self, from_node):
    pass


  def path_to(self, from_node, to_node):
    pass


class Tree:
  def __init__(self, label, children=None):
    self.label = label
    self.children = children if children is not None else []


  def __dict__(self):
    return {self.label: [c.__dict__() for c in sorted(self.children)]}


  def __str__(self, indent=None):
    return dumps(self.__dict__(), indent=indent)


  def __lt__(self, other):
    return self.label < other.label


  def __eq__(self, other):
    return self.__dict__() == other.__dict__()


  # Build graph
  def _to_graph(self):
    graph = {}

    def dfs(node, parent=None):
      if node.label not in graph:
        graph[node.label] = []

      if parent:
        graph[node.label].append(parent.label)
        graph[parent.label].append(node.label)

      for child in node.children:
        dfs(child, node)

    dfs(self)

    return graph


  def from_pov(self, from_node):
    graph = self._to_graph()

    if from_node not in graph:
      raise ValueError("Tree could not be reoriented")

    def build(node, parent):
      children = [
        build(neigh, node)
        for neigh in graph[node]
        if neigh != parent
      ]

      return Tree(node, children)

    return build(from_node, None)


  def path_to(self, from_node, to_node):
    graph = self._to_graph()

    if from_node not in graph:
      raise ValueError("Tree could not be reoriented")

    if to_node not in graph:
      raise ValueError("No path found")

    # BFS to find shortest path
    queue = deque([(from_node, [from_node])])
    visited = set()

    while queue:
      node, path = queue.popleft()

      if node == to_node:
        return path

      visited.add(node)

      for neigh in graph[node]:
        if neigh not in visited:
          queue.append((neigh, path + [neigh]))

    raise ValueError("No path found")
