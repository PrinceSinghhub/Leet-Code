class Solution(object):
    def findTheWinner(self, n, k):
        li = [i for i in range(1,n+1)]
        k = k-1
        offset = k
        while len(li) >1:
            li.pop(offset)
            offset = (offset+k) % len(li)
        return li[0]