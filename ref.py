class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)

    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insertNode(node.left,data)
        else:
            node.right = self.insertNode(node.right,data)
        return node
    def traverse_Inorder(self,root):
        if root.left:
            self.traverse_Inorder(root.left)
        print(root.data)
        if root.right:
            self.traverse_Inorder(root.right)

    def traverse_Preorder(self, root):
        print(root.data)
        if root.left:
            self.traverse_Preorder(root.left)
        if root.right:
            self.traverse_Preorder(root.right)
    

    def find_replace(self,node):
        while node.left:
            node = node.left       
        return node.data

    def delete_node(self,root,delete_node):  
        if root is None:
            return root
        if delete_node<root.data:
            root.left = self.delete_node(root.left,delete_node)
        elif delete_node>root.data:
            root.right = self.delete_node(root.right,delete_node)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.find_replace(root.right)
            root.right = self.delete_node(root.right, root.data)
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


#tree.traverse_Inorder(root)
tree.delete_node(root,20)
tree.traverse_Inorder(root)