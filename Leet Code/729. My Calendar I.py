class MyCalendar:

    def __init__(self, nums: List[int] = None):
        self.nums = []

    def slotavailable(self, start: int, end: int) -> bool:
        n = len(self.nums)
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if self.nums[mid][0] <= start:
                low = mid + 1
            else:
                high = mid - 1

        if low >= n:
            if self.nums[high][1] <= start:
                self.nums.append([start, end])
                return True
            return False
        elif high < 0:
            if self.nums[low][0] >= end:
                self.nums.insert(0, [start, end])
                return True
            return False
        elif self.nums[low][0] >= end and high >= 0 and self.nums[high][1] <= start:
            self.nums.insert(low, [start, end])
            return True

        return False

    def book(self, start: int, end: int) -> bool:
        if len(self.nums) == 0:
            self.nums.append([start, end])
            return True
        return True if self.slotavailable(start, end) else False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)