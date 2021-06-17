def popAfter(self, prev):
    curr = prev.next
    if (curr.next is None):
        if (self.nodeCount == 1):
            self.tail = None
            prev.next = None
        else:
            self.tail = prev
            prev.next = None
    else:
        prev.next = curr.next

    self.nodeCount -= 1
    return curr.data


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
    prev = self.getAt(pos - 1)
    return self.popAfter(prev)