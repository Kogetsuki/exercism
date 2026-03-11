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
  records.sort(key=lambda r: r.record_id)

  # Validate IDs
  for i, record in enumerate(records):
    if record.record_id != i:
      raise ValueError("Record id is invalid or out of order.")

    if record.record_id == 0:
      if record.parent_id != 0:
        raise ValueError("Node parent_id should be smaller than its record_id.")

    else:
      if record.record_id == record.parent_id:
        raise ValueError("Only root should have equal record and parent id.")

      if record.parent_id >= record.record_id:
        raise ValueError("Node parent_id should be smaller than its record_id.")

  # Create nodes
  nodes = [
    Node(r.record_id)
    for r in records
  ]

  # Link parent and children
  for record in records[1:]:    # skip root
    parent_node = nodes[record.parent_id]
    parent_node.children.append(nodes[record.record_id])

  return nodes[0]   # root
