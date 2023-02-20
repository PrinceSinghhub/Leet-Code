import collections


class Solution:
    def countBalls(self, lowLimit, highLimit):
        ballBox = collections.defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            box = sum([int(i) for i in str(i)])
            ballBox[box] += 1

        print(ballBox)

        return max(ballBox.values())




ans = Solution()
lowLimit = 1
highLimit = 10
print(ans.countBalls(lowLimit,highLimit))


print(34%6)
print(34//6)