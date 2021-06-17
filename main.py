def popAfter(self, prev):
    if self.head == self.tail:
        return None

    next = prev.next.next
    curr = prev.next
    next.prev = prev
    prev.next = next
    self.nodeCount -= 1
    return curr.data


def popBefore(self, next):
    if self.head == self.tail:
        return None

    prev = next.prev.prev
    curr = next.prev
    next.prev = prev
    prev.next = next
    self.nodeCount -= 1
    return curr.data


def popAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        raise IndexError
    if pos > self.nodeCount // 2:
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)
    else:
        next = self.getAt(pos + 1)
        return self.popBefore(next)