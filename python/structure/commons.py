class Node():
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt
    
    def __str__(self):
        return "Node({})".format(self.val)
    
    def __repr__(self):
        return self.__str__()


def gen_linked_list():
    n1 = Node(1, None)
    n2 = Node(2, n1)
    n3 = Node(3, n2)
    return n3


def gen_linked_seq(n, start=1) -> Node:
    if n == 0:
        return None
    lst = []
    for i in range(n):
        lst.append(Node(i+start, None))
    for i in range(0, n - 1):
        lst[i].nxt = lst[i + 1]
    return lst[0]


def gen_linked_by_list(s):
    lst = []
    for c in s:
        lst.append(Node(c, None))
    for i in range(len(lst) - 1):
        lst[i].nxt = lst[i + 1]
    return lst[0]




class TreeNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return "{}-{}-{}".format(self.left.val if self.left else '' , self.val, self.right.val if self.right else '')
    
    def __repr__(self):
        return "{}".format(self.val)