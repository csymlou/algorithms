class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node: Node):
        q, p = node.prev, node.next  # q <-> node <-> p
        q.next, p.prev = p, q  # q <-> p

    def remove_last(self) -> Node:
        last = self.tail.prev
        q, p = last.prev, last.next  # q <-> node <-> p
        q.next, p.prev = p, q  # q <-> p
        return last

    def insert_first(self, node: Node):
        s = self.head.next  # head <-> s
        self.head.next, node.prev = node, self.head  # head <-> node <-> s
        node.next, s.prev = s, node

    def __str__(self) -> str:
        p = self.head.next
        vals = []
        while p is not self.tail:
            vals.append(p.val)
            p = p.next
        vals.append("|")
        p = self.tail.prev
        while p is not self.head:
            vals.append(p.val)
            p = p.prev
        return str(vals)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: Node(val)
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.linked_list.remove_node(node)
            self.linked_list.insert_first(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.linked_list.remove_node(node)
            self.linked_list.insert_first(node)
        else:
            # add to cache
            new_node = Node(key, value)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                # remove last
                last = self.linked_list.remove_last()
                del self.cache[last.key]
            # add first
            self.linked_list.insert_first(new_node)

    def __str__(self) -> str:
        return (
            str([(k, v.val) for k, v in self.cache.items()])
            + " "
            + str(self.linked_list)
        )


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(2, 1)
    c.put(2, 2)
    print(c)

    print(c.get(2))
    c.put(1, 1)
    c.put(4, 1)
    print(c.get(2))
    print(c)
