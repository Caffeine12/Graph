class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def createNode(self,data):
        return Node(data)

    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left = self.insertNode(node.left,data)
        else:
            node.right = self.insertNode(node.right,data)
        return node
    
    def traverse_Inorder(self,node):
        if node.left:
            node.left = self.traverse_Inorder(node.left)
        print(node.data)
        if node.right:
            node.right = self.traverse_Inorder(node.right)
        return node
    
    def find_replacement(self,node):
        while node.left:
            node = node.left
        return node.data

    def delete_node(self,root,delete_data):
        if root is None:
            return root
        if delete_data<root.data:
            root.left = self.delete_node(root.left, delete_data)
        elif delete_data>root.data:
            root.right = self.delete_node(root.right, delete_data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.find_replacement(root.right)
            root.right = self.delete_node(root.right,root.data)
        return root
    


tree = Tree()
root = tree.createNode(5)
#print(root.data)

tree.insertNode(root,2)
tree.insertNode(root,10)
tree.insertNode(root,7)
tree.insertNode(root,15)
tree.insertNode(root,12)
tree.insertNode(root,20)
tree.insertNode(root,30)
tree.insertNode(root,6)
tree.insertNode(root,8)


tree.delete_node(root,15)
tree.traverse_Inorder(root)