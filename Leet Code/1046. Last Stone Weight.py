import heapq

class Solution:
    def lastStoneWeight(self, stones):

        # using heapq
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones)!=1:
            m1 = heapq.heappop(stones)
            m2 = heapq.heappop(stones)

            temp = m1-m2
            heapq.heappush(stones,temp)
        return abs(stones[0])

        # recursive Approch
        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]

        if len(stones) >= 2:
            stones.sort()

            Max1 = stones[-1]
            Max2 = stones[-2]

            if Max1 == Max2:
                stones.remove(Max1)
                stones.remove(Max2)

            else:
                temp = Max1 - Max2
                stones.remove(Max1)
                stones.remove(Max2)

                stones.append(temp)

            return self.lastStoneWeight(stones)

        # iterative Approch
        # if len(stones) >= 2:
    #         while True:
    #             stones.sort()
    #             if len(stones) == 1:
    #                 return abs(stones[0])

    #             Max1 = stones[-1]
    #             Max2 = stones[-2]

    #             if Max1 == Max2:
    #                 stones.remove(Max1)
    #                 stones.remove(Max2)

    #             else:
    #                 temp = Max2 - Max1
    #                 stones.remove(Max1)
    #                 stones.remove(Max2)

    #                 stones.append(temp)


arr = [2,1,5,4,7,8,9,63,600,1]
ans = Solution()
print(ans.lastStoneWeight(arr))





