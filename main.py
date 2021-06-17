def reverse(self):
    ans = []
    curr = self.tail
    while (curr.prev.prev):
        curr = curr.prev
        ans.append(curr.data)

    return ans