class Node:
    __slots__ = "prev", "next", "key", "value"

    def __init__(self, key = 0, value = 0) -> None:
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.dic = {}

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.dic:
            return None
        else:
            node = self.dic[key]
            self.remove(node)
            self.push(node)
            return node

    def remove(self, node: Node) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next

    def push(self, node: Node) -> None:
        node.prev = self.dummy
        node.next = self.dummy.next
        node.next.prev = node
        node.prev.next = node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        else:
            self.dic[key] = new_node = Node(key, value)
            self.push(new_node)
            if len(self.dic) > self.capacity:
                del self.dic[self.dummy.prev.key]
                self.remove(self.dummy.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
