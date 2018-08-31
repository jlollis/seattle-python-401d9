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

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, value):
        pass

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
