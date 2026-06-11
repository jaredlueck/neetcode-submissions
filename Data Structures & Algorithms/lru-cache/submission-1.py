class ListNode:
    def __init__(self, key = -1, value = -1, prev = None, next = None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.m = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.m.get(key, None)
        if not node: return -1
        # move node to right most side
        # remove from current position in the list
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        # add to right side
        last = self.right.prev
        node.next = self.right
        self.right.prev = node
        last.next = node
        node.prev = last
        return node.value

    def put(self, key: int, value: int) -> None:
        existing = self.m.get(key, None)
        if existing:
            # remove the existing node from the list
            before = existing.prev
            after = existing.next
            before.next = after
            after.prev = before
        elif len(self.m) == self.capacity:
            # the cache is full so evict the lru
            lru = self.left.next
            before = lru.prev
            after = lru.next
            before.next = after
            after.prev = before
            del self.m[lru.key]
        # add the new node to the rightmost side
        new_node = ListNode(key, value)
        last = self.right.prev
        self.right.prev = new_node
        new_node.prev = last
        last.next = new_node
        new_node.next = self.right
        self.m[key] = new_node


