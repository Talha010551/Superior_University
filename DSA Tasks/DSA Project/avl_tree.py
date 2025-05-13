from product import Product

class AVLNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, product):
        if not root:
            return AVLNode(product)
        if product.price < root.product.price:
            root.left = self.insert(root.left, product)
        else:
            root.right = self.insert(root.right, product)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and product.price < root.left.product.price:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and product.price > root.right.product.price:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and product.price > root.left.product.price:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and product.price < root.right.product.price:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def pre_order(self, root):
        if root:
            print(root.product)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
