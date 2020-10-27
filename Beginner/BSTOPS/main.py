class Bst:
    def __init__(self, data, pos):
        self.left = None
        self.right = None
        self.pos = pos
        self.data = data


def insert(root, data, pos):
    if root is None:
        print(pos)
        return Bst(data, pos)
    else:
        if data < root.data:
            root.left = insert(root.left, data, 2*pos)
        else:
            root.right = insert(root.right, data, 2*pos+1)
    return root


def findMin(root):
    while root.left:
        root = root.left
    return root


def delete(root, data):
    if root is None:
        return root
    elif data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        print(root.pos)
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            temp = findMin(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root


t = int(input())
root = None
while t:
    w, ns = input().split(' ')
    n = int(ns)
    if w == 'i':
        root = insert(root, n, 1)
    else:
        root = delete(root, n)
    t -= 1
