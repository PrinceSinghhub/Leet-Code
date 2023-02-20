# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:

    def mergeTwoLists(self, list1,list2):

        ans = []
        for i in list1:
            ans.append(i)
        for j in list2:
            ans.append(j)
        return sorted(ans)

ans = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(ans.mergeTwoLists(list1,list2))
'''class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        '''
