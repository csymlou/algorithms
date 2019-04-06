from commons import TreeNode


def from_str(s:str)->TreeNode:
    root = TreeNode(s[0], None, None)
    from_str_recursive(s, root, 0)
    return root


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


def print_layer(root:TreeNode):
    K = depth(root)
    queue = [root]
    this_cnt, next_cnt = 1, 0
    for k in range(1, K + 1):
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
       

def print_layer2(root:TreeNode):
    K = depth(root)
    queue = [root]
    for k in range(1, K + 1):
        # print(k)
        # print(queue)
        print_one_layer(queue, k, K)
        cc = 1 << (k-1)
        for i in range(cc):
            node = queue.pop(0)
            queue.append(node.left if node else None)
            queue.append(node.right if node else None) 

SP = ' '
def print_one_layer(nodes, k, K):
    step = (1 << (K - k)) - 1
    print(SP * step, end='')
    print(nodes[0].val if nodes[0] else SP, end='')
    for i in range(1, len(nodes)):
        n = nodes[i]
        print(SP * (2 * step + 1), end='')
        print(n.val if n else SP, end='')
    print()


def depth(root:TreeNode):
    if root is None:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


if __name__ == "__main__":
    s = 'ABCDEFG'
    rt = from_str('fceadhg##b###m')
    # print(rt)
    # print(rt.left)
    # print(rt.right)
    # print(depth(rt))
    print_layer2(rt)