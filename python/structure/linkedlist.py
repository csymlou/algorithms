from commons import Node
from commons import gen_linked_list
from commons import gen_linked_seq

def print_list(head:Node):
    if head is None:
        print('Empty')
        return
    p = head
    while p.nxt:
        print(p.val, end='->')
        p = p.nxt
    print(p.val)


# 反向打印链表，使用递归
def print_reverse(head:Node):
    if head is None:
        return
    print_reverse(head.nxt)
    print(head.val, end='->')


# 将单链表反转 p q r 三个指针
def reverse(head:Node) -> Node:
    if head is None or head.nxt is None:
        return head
    p, q = head, head.nxt
    while q :
        r = q.nxt
        q.nxt = p
        p, q = q, r
    head.nxt = None
    return p


# 求单链表中结点的个数
def count(head:Node):
    cnt = 0
    p = head
    while p:
        cnt += 1
        p = p.nxt
    return cnt


# 查找单链表中的倒数第K个结点（k > 0）
# 快慢指针
def last_k(head:Node, k:int):
    if k <= 0:
        return None
    p, q = head, head
    c = 0
    while p:
        if c >= k:
            p = p.nxt
            q = q.nxt
        else:
            q = q.nxt  # 一个指针走
        c += 1        
    return p.val


# 查找中间节点 快慢指针，一个一次走一步，一个一次走两步
def find_middle(head:Node):
    if head is None or head.nxt is None:
        return head
    p, q= head, head
    while p and p.nxt:
        p = p.nxt.nxt
        q = q.nxt
    return q.val


# 是否有环 快慢指针，一个一次走一步，一个一次走两步
# 如果有环，一定会相交；如果无环，则会走完
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


# 插入最后面 需要遍历到尾部 O(N)
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


# 第一个公共节点
# 先走到离尾部一样距离的位置，然后一起走，看有没有相同的节点
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