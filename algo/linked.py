import heapq
import random
import math
from typing import List, Optional
import os


def rand(N, a=0):
    return random.randint(a, N)


def rand_list(N, start=1, end=10):
    return [random.randint(start, end) for _ in range(N)]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self)

    def print_list(self):
        p = self
        nodes = []
        while p:
            nodes.append(p.val)
            p = p.next
        print(str(nodes))


class List:
    def __init__(self, v) -> None:
        vals = []
        if isinstance(v, int):
            vals = rand_list(v)
        elif isinstance(v, list):
            vals = v
        self.head = None
        prev = None
        for x in vals:
            if self.head is None:
                self.head = ListNode(x)
                prev = self.head
            else:
                node = ListNode(x)
                prev.next = node
                prev = node

    def __str__(self) -> str:
        p = self.head
        nodes = []
        while p:
            nodes.append(p.val)
            p = p.next
        return str(nodes)


class CycleList:
    def __init__(self, N) -> None:
        cx = rand(N - 1, 1)
        cn = None
        self.head = None
        prev = None
        for x in range(1, N + 1):
            if self.head is None:
                self.head = ListNode(x)
                prev = self.head
            else:
                node = ListNode(x)
                prev.next = node
                prev = node
            if x == cx:
                cn = prev
                print(cx)
        node.next = cn


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # termination.

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid, slow.next = slow.next, None  # save and cut.

        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right

        return res.next

    def inverse(self, head: ListNode) -> ListNode:
        return self._inverse(head)

    def _inverse(self, node: ListNode) -> ListNode:
        if node.next is None:
            return node
        last = self._inverse(node.next)
        node.next.next = node
        node.next = None
        return last

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        _, last = self._reverseN(head, n)
        return last

    def _reverseN(self, node: ListNode, n: int) -> (ListNode, ListNode):  # type: ignore
        if n == 1:
            return node.next, node
        successor, last = self._reverseN(node.next, n - 1)
        node.next.next = node
        node.next = successor
        return successor, last

    def mergeKLists(self, lists) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        a = lists[0]
        for i in range(1, len(lists)):
            b = lists[i]
            a = self.mergeTwo(a, b)
        return a

    def mergeTwo(self, a, b) -> Optional[ListNode]:
        head = p = ListNode(0)
        while a and b:
            if a.val < b.val:
                p.next, a = a, a.next
            else:
                p.next, b = b, b.next
            p = p.next
        p.next = a if a else b
        return head.next

    def detectCycle(self, head):
        if head is None or head.next is None:
            return
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


# y = Solution().maxSlidingWindow(nums = [random.randint(-10, 10) for _ in range(10)], k = 3)
while True:
    os.system("clear")  # ignore_security_alert RCE

    l1 = List([1, 2, 5, 7])
    l2 = List([1, 3, 8])
    l3 = List([4, 5, 6, 7])

    y = Solution().mergeKLists([l1.head, l2.head, l3.head])
    y.print_list()

    input("Press to start")
