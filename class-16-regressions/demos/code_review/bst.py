class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        pass

    def __repr__(self):
        pass


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None

        if iterable is None:
            iterable = []

        for ele in iterable:
            self.insert(ele)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, value):
        """
        """
        #  Check if Root is None: Add new Node if so / Return
        #  Set root to current
        #  While current has a value
            # if val == current val: raise a value error or some other exception
            #  if val is less than current: Go left
                #  if left child has value: current = left
                #  else add new Node to left

            #  if val is greater than current: Go right
                #  if right child has value: current = right
                #  else add new Node to right

        node = Node(value)
        if self.root is None:
            self.root = node
            return node

        current = self.root
        while current:
            if value == current.value:
                raise ValueError('Value already exists')

            if value < current.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left

            if value > current.value:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

        return node

    def in_order(self, callable=lambda node: print(node)):
        """Go left, visit, then go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left:
                _walk(node.left)

            # Visit
            callable(node)

            # Go right
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left, then right
        """
        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go left
            if node.left:
                _walk(node.left)

            # Go right
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Go left, then right, Visit
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left:
                _walk(node.left)

            # Go right
            if node.right:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)
