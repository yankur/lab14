class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def rebalance(self):
    items = list(self.inorder())
    items.sort()

    def recurse(root, items):
        if len(items) > 1:
            mid = (len(items)) // 2
            root = BSTNode(items[mid])
            root.left = recurse(items[:mid])
            root.right = recurse(items[mid + 1:])
        else:


    if self.isEmpty():
        self._root = BSTNode(item)
    # Otherwise, search for the item's spot
    else:
        recurse(self._root)
    self._size += 1

def sortedArrayToBST(arr):
    if not arr:
        return None

    # find middle
    mid = (len(arr)) / 2

    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root

def find(self, item):
    """If item matches an item in self, returns the
    matched item, or None otherwise."""

    def recurse(node):
        if node is None:
            return None
        elif item == node.data:
            return node.data
        elif item < node.data:
            return recurse(node.left)
        else:
            return recurse(node.right)

    return recurse(self._root)
