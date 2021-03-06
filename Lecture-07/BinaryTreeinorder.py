class Node:

    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if  self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inoderTraveresal(self, root):
        res = []
        if root:
            res = self.inoderTraveresal(root.left)
            res.append(root.data)
            res = res + self.inoderTraveresal(root.right)
        return res


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = Node(27)
root.insert(34)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inoderTraveresal(root))
