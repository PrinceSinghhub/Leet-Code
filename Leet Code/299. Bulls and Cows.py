class Solution:

    def getHint(self, secret, guess):

        A = 0
        B = 0
        s_list = ['']*len(secret)
        g_list = ['']*len(guess)


        for i in range(len(secret)):
            s_list[i] = secret[i]
            g_list[i] = guess[i]

        # Check bulls
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
                s_list.remove(secret[i])
                g_list.remove(guess[i])

        # Check cows
        for i in range(len(g_list)):
            if g_list[i] in s_list:
                B += 1
                s_list.remove(g_list[i])


        str_ans = str(A) + "A" + str(B) + "B"

        return str_ans

ans = Solution()
secret = "1807"
guess = "7810"
print(ans.getHint(secret,guess))