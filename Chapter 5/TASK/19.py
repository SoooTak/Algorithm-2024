class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 후위 순회 함수
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')
        
a = TreeNode('A', None, None)
b = TreeNode('B', None, None)
c = TreeNode('C', None, None)
d = TreeNode('D', None, None)
e = TreeNode('E', None, None)

s = TreeNode('/', a, b)
s1 = TreeNode('*', s, c)
s2 = TreeNode('*', s1, d)
root = TreeNode('+', s2, e)

print("후위 ", postorder(root))