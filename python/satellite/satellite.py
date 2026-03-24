from itertools import takewhile, dropwhile

def tree_from_traversals(preorder, inorder):
  # End case
  if not preorder and not inorder:
    return {}

  # Validate inputs
  if len(preorder) != len(inorder):
    raise ValueError("traversals must have the same length")
  if set(preorder) != set(inorder):
    raise ValueError("traversals must have the same elements")
  if len(preorder) != len(set(inorder)):
    raise ValueError("traversals must contain unique items")

  # Empty tree
  if not preorder:
    return {}

  # Root is first item in preorder
  root = preorder[0]

  # Get left and right subtrees inorder
  left_in = list(takewhile(lambda x: x != root, inorder))
  right_in = list(dropwhile(lambda x: x != root, inorder))[1:]


  # Get left and right subtrees preorder
  preorder = preorder[1:]
  left_pre = preorder[:len(left_in)]
  right_pre = preorder[len(left_in):]

  return {
    "v": root,
    "l": tree_from_traversals(left_pre, left_in),
    "r": tree_from_traversals(right_pre, right_in)
  }
