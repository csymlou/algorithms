from commons import TreeNode
from commons import Stack

# 从满二叉树的字符串，创建一个二叉树
def from_str(s:str)->TreeNode:
    root = TreeNode(s[0], None, None)
    from_str_recursive(s, root, 0)
    return root

# s 是字符串序列
# node 是s[i]对应的节点
def from_str_recursive(s, node:TreeNode, i):
    if node is None:
        return None
    lidx = 2 * i + 1
    ridx = 2 * i + 2
    if lidx < len(s) and s[lidx] != '#':
        n = TreeNode(s[lidx], None, None)
        node.left = n
        from_str_recursive(s, n, lidx)
    if ridx < len(s) and s[ridx] != '#':
        n = TreeNode(s[ridx], None, None)
        node.right = n
        from_str_recursive(s, n, ridx)


# 按层打印（打印出层数）
def print_layer(root:TreeNode):
    L = depth(root)
    queue = [root]
    this_cnt, next_cnt = 1, 0
    for k in range(1, L + 1):
        print(k)
        while this_cnt > 0:
            node = queue.pop(0)
            this_cnt -= 1
            if node.left:
                queue.append(node.left)
                next_cnt += 1
            if node.right:
                queue.append(node.right)
                next_cnt += 1
        print(queue)
        this_cnt = next_cnt
        next_cnt = 0


# 按层打印（不打印层数）
def print_layer_2(root:TreeNode):
    rst = []
    queue = [root]
    while queue:
        n = queue.pop(0)
        rst.append(n.val)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    print(rst)


# 打印二叉树
#    A
#  B   C
# D E F G
def print_tree(root:TreeNode):
    L = depth(root)
    queue = [root]
    for k in range(1, L + 1):
        print_one_layer(queue, k, L)
        cc = 1 << (k-1)
        for _ in range(cc):
            node = queue.pop(0)
            queue.append(node.left if node else None)
            queue.append(node.right if node else None) 

SP = ' '
def print_one_layer(nodes, k, L):
    step = (1 << (L - k)) - 1
    print(SP * step, end='')
    print(nodes[0].val if nodes[0] else SP, end='')
    for i in range(1, len(nodes)):
        n = nodes[i]
        print(SP * (2 * step + 1), end='')
        print(n.val if n else SP, end='')
    print()


# 最大高度
def depth(root:TreeNode):
    if root is None:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


#  前序遍历
def pre_order(root:TreeNode):
    if root is None:
        return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)

# 非递归
def pre_order_2(root):
    s = Stack()
    s.push(root)
    while not s.isEmpty() : 
        node = s.pop()
        print(node.val, end=' ')
        if node.right:
            s.push(node.right) # 右节点 入栈
        if node.left : 
            s.push(node.left)  # 左节点 入栈
    print()



#  中序遍历
def in_order(root:TreeNode):
    if root is None:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)

# 中序 非递归
def in_order_2(root:TreeNode):
    s = Stack()
    p = root
    while p or s.isNotEmpty():
        if p.left:
            s.push(p)  # 存在left，根 入栈
            p = p.left
        else:
            print(p.val) # left is None
            p = p.right
            while p is None and s.isNotEmpty():  # right is None
                p = s.pop()
                print(p.val)
                p = p.right

# 中序 非递归
def in_order_3(root:TreeNode):
    s = Stack()
    p = root
    while p or s.isNotEmpty():
        while p :
            s.push(p)
            p = p.left
        if s.isNotEmpty():
            p = s.pop()
            print(p.val)
            p = p.right


#  后序遍历
def post_order(root:TreeNode):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')


def post_order_2(root):
    s = Stack()
    out = Stack() # 输出栈
    p = root
    while p or s.isNotEmpty():
        if p : 
            s.push(p)
            out.push(p)
            p = p.right  # 如果有右节点，一路压栈
        else:
            p = s.pop()  # 如果没有右节点，弹一个出来，走向左边
            p = p.left
    while out.isNotEmpty():
        print(out.pop().val)


def is_leaf(node):
    return node.left is None and node.right is None


def pre_bi_link(root):
    head, tail = to_bi_linklist_post(root)
    head.left, tail.right = None, None
    p = head
    while p:
        print(p.val, end=' ')
        p = p.right
    
    print()
    q = tail
    while q:
        print(q.val, end=' ')
        q = q.left        


# 传入一个node，返回这棵树 按照先序 转化为链表之后的头尾节点
def to_bi_linklist_pre(node):
    if node is None:
        return None, None

    h1, t1 = to_bi_linklist_pre(node.left)  # 左子树转成双链表，返回头尾
    h2, t2 = to_bi_linklist_pre(node.right) # 右子树转成双链表，返回头尾

    node.left = None

    if is_leaf(node): # 叶子是单节点，前后都是None
        node.left = None
        node.right = None
        return node, node

    if h1 is None:
        link(node, h2)
        return node, t2
    
    if h2 is None:
        link(node, h1)
        return node, t1
    
    if h1 and h2:
        link(node, h1)
        link(t1, h2)
        return node, t2

# 传入一个node，返回这棵树 按照中序 转化为链表之后的头尾节点
def to_bi_linklist_in(node):
    if node is None:
        return None, None
    
    h1, t1 = to_bi_linklist_in(node.left)
    h2, t2 = to_bi_linklist_in(node.right)

    node.left = None

    if h1 is None and h2 is None:
        node.left, node.right = None, None
        return node, node
    
    if h1 is None:
        link(node, h2)
        return node, t2
    
    if h2 is None:
        link(t1, node)
        return h1, node
    
    if h1 and h2:
        link(t1, node)
        link(node, h2)
        return h1, t2

# 传入一个node，返回这棵树 按照后序 转化为链表之后的头尾节点
def to_bi_linklist_post(node):
    if node is None:
        return None, None
    
    h1, t1 = to_bi_linklist_post(node.left)
    h2, t2 = to_bi_linklist_post(node.right)

    node.left = None

    if h1 is None and h2 is None:
        node.left, node.right = None, None
        return node, node
    
    if h1 and not h2:
        link(t1, node)
        return h1, node
    
    if h2 and not h1:
        link(t2, node)
        return h2, node
    
    if h1 and h2:
        link(t1, h2)
        link(t2, node)
        return h1, node


def link(n1, n2):
    n1.right, n2.left = n2, n1


if __name__ == "__main__":
    s = 'ABCDE#G##J#LMN#'
    rt = from_str(s)
    print_tree(rt)
    # print_layer_2(rt)
    post_order(rt)
    print()
    # pre_bi_link(rt)
    # in_order_2(rt)
    post_order_2(rt)

