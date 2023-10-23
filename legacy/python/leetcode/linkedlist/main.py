from node import Node
from node import print_list

if __name__ == "__main__":
    a = Node(1)
    b = Node('A')
    a.next = b
    print(a)
    print_list(a)