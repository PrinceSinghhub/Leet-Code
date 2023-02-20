class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


ans = Solution()
head = [1,2,3,4,5]
print(ans.middleNode(head))