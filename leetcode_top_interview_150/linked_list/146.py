from collections import deque

class LRUCache:
    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys_value = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def remove(self, nodeToDelete):
        prevNode = nodeToDelete.prev
        nextNode = nodeToDelete.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return

    def add(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        return

    def get(self, key: int) -> int:
        if key not in self.keys_value:
            return -1
        
        node = self.keys_value[key]
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys_value:
            node = self.keys_value[key]
            self.remove(node)
            self.add(node)
            node.val = value
            return        
        
        if self.size >= self.capacity:
            last_node = self.tail.prev
            self.remove(last_node)
            self.keys_value.pop(last_node.key)
        
        node = self.Node(key, value)
        self.add(node)
        self.keys_value[key] = node
        self.size += 1
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)