from collections import deque, defaultdict

class RelativeDistance:
  def __init__(self, family_tree):
    # Undirected graph
    self.graph = defaultdict(set)
    self.all_people = set()

    for parent, children in family_tree.items():
      self.all_people.add(parent)

      for child in children:
        self.all_people.add(child)
        # Link both ways --> parent-child
        self.graph[parent].add(child)
        self.graph[child].add(parent)

        # Sibling
        for sibling in children:
          if sibling != child:
            self.graph[child].add(sibling)
            self.graph[sibling].add(child)



  def degree_of_separation(self, person_a, person_b):
    # Check existence
    if person_a not in self.all_people:
      raise ValueError("Person A not in family tree.")
    if person_b not in self.all_people:
      raise ValueError("Person B not in family tree.")

    if person_a == person_b:
      return 0

    # BFS for shortest path
    queue = deque([(person_a, 0)])
    visited = {person_a}

    while queue:
      current_person, distance = queue.popleft()

      for neighbor in self.graph[current_person]:
        if neighbor == person_b:
          return distance + 1

        if neighbor not in visited:
          visited.add(neighbor)
          queue.append((neighbor, distance + 1))

    raise ValueError("No connection between person A and person B.")
