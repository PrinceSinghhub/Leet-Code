import heapq


class SeatManager(object):

    def __init__(self, n):
        self.seat = list(range(1, n + 1))
        """
        :type n: int
        """

    def reserve(self):
        return heapq.heappop(self.seat)
        """
        :rtype: int
        """

    def unreserve(self, seatNumber):
        heapq.heappush(self.seat, seatNumber)
        """
        :type seatNumber: int
        :rtype: None
        """

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)