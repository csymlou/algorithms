from commons import Node
from commons import gen_linked_list
from commons import gen_linked_seq

def print_list(root:Node):
    if root is None:
        print('Empty')
        return
    p = root
    while p.nxt:
        print(p.val, end='->')
        p = p.nxt
    print(p.val)


def print_reverse(root:Node):
    '''
    反向打印链表，使用递归
    '''
    if root is None:
        return
    print_reverse(root.nxt)
    print(root.val, end='->')


# 将单链表反转
def reverse(root:Node) -> Node:
    if root is None or root.nxt is None:
        return root
    q, p = root, root.nxt
    while p :
        t = p.nxt
        p.nxt = q
        q, p = p, t
    root.nxt = None
    return q


# 求单链表中结点的个数
def count(root:Node):
    cnt = 0
    p = root
    while p:
        cnt += 1
        p = p.nxt
    return cnt


# 查找单链表中的倒数第K个结点（k > 0）
# 快慢指针
def last_k(root:Node, k:int):
    if k <= 0:
        return None
    q, p = root, root
    c = 0
    while p:
        if c >= k:
            q = q.nxt
            p = p.nxt
        else:
            p = p.nxt
        c += 1        
    return q.val

# 查找中间节点 快慢指针，一个一次走一步，一个一次走两步
def find_middle(root:Node):
    if root is None or root.nxt is None:
        return root
    p, q= root, root
    while p and p.nxt:
        p = p.nxt.nxt
        q = q.nxt
    return q.val

def has_cycle(head:Node):
    if head is None:
        return False
    p, q = head, head
    while p and p.nxt:
        p = p.nxt.nxt
        q = q.nxt
        if p == q:
            return True
    return False

def add_last(head:Node, v):
    if head is None:
        head = Node(v, None)
        return head
    p = head
    while p.nxt:
        p = p.nxt
    n = Node(v, None)
    p.nxt = n
    return head

def first_common_node(head1:Node, head2:Node):
    m, n = 0, 0
    p, q = head1, head2
    while p:
        m += 1
        p = p.nxt
    while q:
        n += 1
        q = q.nxt
    t = m - n
    p, q = head1, head2
    if t > 0:
        while t > 0:
            p = p.nxt
            t -= 1
    else:
        t = -t
        while t > 0:
            q = q.nxt
            t -= 1
    while p and q:
        if p is q:
            return p
        p = p.nxt
        q = q.nxt
    return None


if __name__ == "__main__":
    n1 = Node(1, None)
    n2 = Node(2, None)
    n3 = Node(3, None)
    n4 = Node(4, None)
    n1.nxt = n2
    n3.nxt = n1
    n2.nxt = n4
    mm = first_common_node(n1, n3)
    print(mm)