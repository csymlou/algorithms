class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return 'Node({})'.format(self.val)


def print_list(root):
    p = root
    while p :
        if p.next:
            print(p.val, end='->')
        else:
            print(p.val)
        p = p.next