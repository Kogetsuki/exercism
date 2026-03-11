class Record:
  def __init__(self, record_id, parent_id):
    self.record_id = record_id
    self.parent_id = parent_id


class Node:
  def __init__(self, node_id):
    self.node_id = node_id
    self.children = []


def BuildTree(records):
  if not records:
    return None

  # Sort records by record_id
  records.sort(
    key=lambda r: r.record_id
  )

  nodes = []

  for i, r in enumerate(records):
    # Validation
    if r.record_id != i:
      raise ValueError("Record id is invalid or out of order.")

    if r.record_id == 0 and r.parent_id != 0:
      raise ValueError("Node parent_id should be smaller than its record_id.")

    if r.record_id != 0:
      if r.record_id == r.parent_id:
        raise ValueError("Only root should have equal record and parent id.")

      if r.parent_id >= r.record_id:
        raise ValueError("Node parent_id should be smaller than its record_id.")

    # Create node and link to parent
    nodes.append(Node(r.record_id))
    if r.record_id > 0:
      nodes[r.parent_id].children.append(nodes[i])

  return nodes[0]   # root
