    class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):
            new_node = SLNode(val)
            current_head=self.head
            new_node.head = current_head
    class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None

