def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    prev = self.getAt(pos - 1)
    curr = self.getAt(pos)

    if self.nodeCount == 1:
        self.head = None
        self.tail = None
    else:
        if pos == 1:
            self.head = curr.next
        elif pos == self.nodeCount:
            self.tail = prev
            prev.next = None
        else:
            prev.next = curr.next

    self.nodeCount -= 1
    return curr.data