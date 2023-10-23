from commons import Node
from commons import gen_linked_list
from commons import gen_linked_seq
from commons import gen_linked_by_list

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


def merge_sorted_list(head1:Node, head2:Node):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    p, q = head1, head2 
    if head1.val <= head2.val: # h 指向头，r 指向尾
        h = head1
        p = p.nxt
    else:
        h = head2
        q = q.nxt
    r = h
    while p and q:  # 从 p和q 里面选出一个放在 r 后面
        if p.val <= q.val:
            r.nxt = p
            p = p.nxt
        else:
            r.nxt = q
            q = q.nxt
        r = r.nxt  # r 在新形成的尾
    if p :
        r.nxt = p
    if q:
        r.nxt = q
    return h


# 合并有序链表 递归方法
def merge_sorted_list_recursive(head1:Node, head2:Node):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.val <= head2.val:
        h = head1
        h.nxt = merge_sorted_list_recursive(head1.nxt, head2)
    else:
        h = head2
        h.nxt = merge_sorted_list_recursive(head1, head2.nxt)
    return h


# 冒泡排序
def bubble_sort(head:Node):
    if head is None or head.nxt is None:
        return head
    p = head
    while p:
        q = p.nxt
        while q:
            if p.val < q.val: #  <则正序  >则倒序
                p.val, q.val = q.val, p.val
            q = q.nxt
        p = p.nxt
    return head




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
            return q # 给下一个找环的入口使用
    return False


# 找出进入环的第一个节点
# 1 判断是否有环
# 2 从环中找一个节点，假设将环断开，行成两个相交链表
# 3 找出两个相交链表的第一个相交节点，即为进入环的首节点
def fine_first_node_in_cycle(head:Node):
    no = has_cycle(head)
    if not no:
        return None
    return first_common_node(no, head)


if __name__ == "__main__":
    h1 = gen_linked_by_list('3572917')
    h = bubble_sort(h1)
    print_list(h)