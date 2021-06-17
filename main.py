def insertBefore(self, next, newNode):
    if next is self.head:
        return False
    prev = next.prev
    newNode.next = next
    newNode.prev = prev
    next.prev = newNode
    prev.next = newNode
    self.nodeCount += 1

    return True