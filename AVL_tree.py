class TreeNode:
    def __init__(self, val=0, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height

class AVLTree:
    def insert(self, root, key):
        # 1. Perform the normal BST insertion
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Get the balance factor
        balance = self.getBalance(root)

        # 4. If the node becomes unbalanced, then we handle the 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, key):
        # 1. Perform the normal BST deletion
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the in-order successor (smallest in the right subtree)
            temp = self.getMinValueNode(root.right)

            # Copy the in-order successor's content to this node
            root.val = temp.val

            # Delete the in-order successor
            root.right = self.delete(root.right, temp.val)

        # If the tree had only one node, then return
        if root is None:
            return root

        # 2. Update the height of the current node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Get the balance factor
        balance = self.getBalance(root)

        # 4. If the node becomes unbalanced, then we handle the 4 cases

        # Left Left Case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Left Right Case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Right Left Case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search(self, root, key):
        # Standard BST search
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

# Example usage:
avl = AVLTree()
root = None

# Insertion
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)

# Pre-order Traversal
print("Pre-order traversal of the constructed AVL tree is:")
avl.preOrder(root)
print("\n")

# Searching for a value
search_key = 25
result = avl.search(root, search_key)
if result:
    print(f"Value {search_key} found in the AVL tree.")
else:
    print(f"Value {search_key} not found in the AVL tree.")

# Deletion
root = avl.delete(root, 30)

# Pre-order Traversal after Deletion
print("Pre-order traversal after deletion of 30:")
avl.preOrder(root)
print()
