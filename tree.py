class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def depth(self):
        right_depth = self.right.depth() if self.right else 0
        left_depth = self.left.depth() if self.left else 0
        return max(right_depth, left_depth) + 1

    def insert(self, item):
        if self.item:
            if item < self.item:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.item)
        if self.right:
            self.right.printtree()

    def traverse(self, root):
        res = []
        if root:
            res = self.traverse(root.left)
            res.append(root.item)
            res = res + self.traverse(root.right)
        return res


b = Node(100)
print(b.depth())
a = Node(1, Node(2), Node(3))
print(a.depth())

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
# root.printtree()
print(root.traverse(root))