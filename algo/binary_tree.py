from typing import *
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(tpl: str) -> TreeNode:
    eles = tpl.split()
    print(eles)

    def _build(i) -> TreeNode:
        if i >= len(eles):
            return None
        e = eles[i]
        if e == "#":
            return None
        node = TreeNode(e)
        node.left = _build(2 * i + 1)
        node.right = _build(2 * i + 2)
        return node

    root = _build(0)
    return root


def printTree(root: TreeNode):
    depth = Solution().maxDepth(root)
    i = depth
    q = [root]
    while i > 0:
        s = ""
        t = []
        while q:
            x, q = q[0], q[1:]
            if x is None:
                s += "#"
                t.extend([None, None])
            else:
                s += str(x.val)
                t.extend([x.left, x.right])
        q = t
        i -= 1
        print(s)


class Solution:
    def preorderTraversal(self, root):
        out = []

        def preorder(node: TreeNode):
            if node is None:
                return
            out.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return out

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def inorder(node: TreeNode):
            if node is None:
                return
            inorder(node.left)
            out.append(node.val)
            inorder(node.right)

        inorder(root)
        return out

    def postorderTraversal(self, root):
        out = []

        def postorder(node: TreeNode):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            out.append(node.val)

        postorder(root)
        return out

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)

        return check(root, root)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def travel(node: TreeNode):
            nonlocal max_diameter
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            a = travel(node.left)
            b = travel(node.right)
            # 如果node作为顶点：则直径是 a+b+1
            # node不作为顶点：则node以下到叶子的最长距离为 max(a, b)+1
            if a + b + 1 > max_diameter:
                max_diameter = a + b + 1
            return max(a, b) + 1

        travel(root)
        return max_diameter - 1 if max_diameter > 0 else 0

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = [root]
        while queue:
            s = []
            k = len(queue)
            while k > 0:
                x, queue = queue[0], queue[1:]
                s.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                k -= 1
            out.append(s)
        return out

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def travel(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = travel(left, mid - 1)
            root.right = travel(mid + 1, right)
            return root

        return travel(0, len(nums) - 1)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # @args: node
        # @return: is_valid, min_val, max_val
        def travel(node):
            if node is None:
                return True, float("-inf"), float("inf")
            if node.left is None and node.right is None:
                return True, int(node.val), int(node.val)

            is_left_valid, _, max_left_val = travel(node.left)
            is_right_valid, min_right_val, _ = travel(node.right)

            is_valid = (
                is_left_valid
                and is_right_valid
                and max_left_val < int(node.val) < min_right_val
            )
            return is_valid, max_left_val, min_right_val

        is_valid, _, _ = travel(root)
        return is_valid

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []

        def inorder(node: TreeNode):
            if node is None:
                return
            inorder(node.left)
            out.append(node.val)
            if len(out) >= k:
                return
            inorder(node.right)

        inorder(root)
        print(out)

        return out[k - 1] if len(out) >= k else -1

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_idx_map = {element: i for i, element in enumerate(inorder)}

        def travel(i: int, j: int, a: int, b: int):
            if i > j:
                return None

            # 前序遍历中的第一个节点就是根节点
            x = preorder[i]

            # 在中序遍历中定位根节点
            k = inorder_idx_map[x]

            # 先把根节点建立出来
            root = TreeNode(x)

            # 得到左子树中的节点数目
            left_cnt = k - a

            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = travel(i + 1, i + left_cnt, a, k - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = travel(i + left_cnt + 1, j, k + 1, b)
            return root

        # 构造哈希映射，帮助我们快速定位根节点
        return travel(0, len(preorder) - 1, 0, len(inorder) - 1)


    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        # 从 root 到 node，存在多少条路径和为targetSum
        def travel(node: TreeNode, currSum: int) -> int:
            if not node:
                return 0
            
            path_cnt = 0
            
            # root + ... + node == currSum
            currSum += node.val

            # currSum - targetSum 在 prefix_map 中，说明
            # root + p1 + ... + pi + ... + node == currSum
            # --------------------   ----------
            #  currSum - targetSum    targetSum
            path_cnt += prefix_map[currSum - targetSum]

            # node 作为路径 node-left 或者路径 node-right 的一个节点
            # 所以需要在 prefix_map[currSum] 加1
            prefix_map[currSum] += 1
            path_cnt += travel(node.left, currSum)
            path_cnt += travel(node.right, currSum)
            # 左右子树处理完后 减1
            prefix_map[currSum] -= 1

            return path_cnt

        return travel(root, 0)

if __name__ == "__main__":
    #     tpl = '''
    #                1
    #            2          3
    #         4      #    #    5
    #       #   6  #  #  #  # #  #
    #      # # 7 8
    # '''
    tpl = """
    3
  1   4
 #  2
"""
    root = build(tpl)
    # printTree(root)
    # y = Solution().inorderTraversal(root)
    # print(y)
    # printTree(root=root)
    y = Solution().kthSmallest(root, 1)
    print(y)
    # print(y)
    # printTree(y)
