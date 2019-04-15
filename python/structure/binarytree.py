from commons import TreeNode

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


#  中序遍历
def in_order(root:TreeNode):
    if root is None:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)


#  后序遍历
def post_order(root:TreeNode):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')


if __name__ == "__main__":
    s = 'ABCDE#G##J#LMN#'
    rt = from_str(s)
    print_tree(rt)
    print_layer_2(rt)
    # pre_order(rt)
    # print()
    # in_order(rt)
    # print()
    # post_order(rt)
    # print()
