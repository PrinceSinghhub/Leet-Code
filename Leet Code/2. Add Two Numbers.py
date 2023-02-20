class Solution:
    def addTwoNumbers(self, l1,l2):
        A = ''
        B = ''

        while l1:
            A += str(l1.val)
            l1 = l1.next

        while l2:
            B += str(l2.val)
            l2 = l2.next

        p3 = int(A[::-1]) + int(B[::-1])
        p3 = str(p3)
        p = ListNode(int(p3[-1]))
        res = p

        for i in range(len(p3) - 2, -1, -1):
            p.next = ListNode(int(p3[i]))
            p = p.next

        return res

