from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):

        deck.sort()
        mydequ = deque([i for i in range(len(deck))])

        index = []

        while len(mydequ) > 0:

            pop = mydequ.popleft()
            index.append(pop)

            if len(mydequ) > 0:
                fs = mydequ.popleft()
                mydequ.append(fs)

        print(index)

        ans = [0] * len(deck)

        ind = 0
        for i in index:
            ans[i] = deck[ind]
            ind += 1

        return ans


ans = Solution()
deck = [17,13,11,2,3,5,7]
print(ans.deckRevealedIncreasing(deck))