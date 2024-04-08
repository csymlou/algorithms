from typing import List, Dict


class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.freq = 1
        self.next: Node = None
        self.prev: Node = None

    def access(self) -> None:
        self.freq += 1


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def empty(self) -> bool:
        return self.head.next == self.tail

    def remove_node(self, node: Node):
        a, b = node.prev, node.next
        a.next, b.prev = b, a

    def remove_last(self) -> Node:
        last = self.tail.prev
        self.remove_node(last)
        return last

    def insert_first(self, node: Node):
        s = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, s.prev = s, node

    def __str__(self) -> str:
        p = self.head.next
        vals = []
        while p is not self.tail:
            vals.append(p.key)
            p = p.next
        vals.append("|")
        p = self.tail.prev
        while p is not self.head:
            vals.append(p.key)
            p = p.prev
        return str(vals)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 存储缓存数据, key: Node(val)
        self.freq_list_dict = {} # 存储每个频次对应的键值对, freq: head <-> node2 <-> node1 <-> tail
        self.min_freq = 0  # 记录当前最小频次

    def get_freq_list(self, freq: int) -> LinkedList:
        if freq in self.freq_list_dict:
            return self.freq_list_dict[freq]
        else:
            ll = LinkedList()
            self.freq_list_dict[freq] = ll
            return ll

    def get(self, key) -> Node:
        if key in self.cache:
            ex_node = self.cache[key]
            # freq list: remove ex_node
            freq = ex_node.freq
            self.get_freq_list(freq).remove_node(ex_node)
            # min_freq 正好是 ex_node 所在的频率，且 freq 链表为空了
            if self.min_freq == freq and self.get_freq_list(freq).empty():
                self.min_freq += 1
            # freq+1 list: insert ex_node
            ex_node.access()
            self.get_freq_list(freq + 1).insert_first(ex_node)
            return ex_node.val
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
        else:
            if len(self.cache) == self.capacity:
                last = self.get_freq_list(self.min_freq).remove_last()
                del self.cache[last.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.min_freq = 1
            self.get_freq_list(self.min_freq).insert_first(new_node)

    def __str__(self) -> str:
        return (
            str([(k, v.val, v.freq) for k, v in self.cache.items()])
            + "\t"
            + str([(k, str(v)) for k, v in self.freq_list_dict.items()])
        )


if __name__ == "__main__":
    # nodes = [Node(i, i) for i in range(10)]
    c = LFUCache(3)
    c.put("a", 1)
    c.put("b", 2)
    print(c.get("b"))
    print(c.get("a"))
    c.put("c", 3)
    print(c.get("c"))
    c.put("d", 4)
    print(c)