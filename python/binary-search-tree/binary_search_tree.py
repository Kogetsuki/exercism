class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right


  def __str__(self):
    return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
  def __init__(self, tree_data):
    self.tree = None
    
    for data in tree_data:
      self.tree = self.insert_value(self.tree, data)
      
      
  def insert_value(self, node, value):
    if node is None:
      return TreeNode(value)

    if value <= node.data:
      node.left = self.insert_value(node.left, value)
    else:
      node.right = self.insert_value(node.right, value)

    return node
  

  def data(self):
    return self.tree


  def sorted_data(self):
    result = []

    def in_order(node):
      if node is None:
        return
      
      in_order(node.left)
      result.append(node.data)
      in_order(node.right)

    in_order(self.tree)

    return result
      
print(BinarySearchTree(["4"]).data())