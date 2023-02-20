class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sp  = sentence.split()
        print(sp)
        for i, word in enumerate(sp):
            print(i,word)
            if word[0] == '$' and str.isdigit(word[1:]):
                amount = (100 - discount) * int(word[1:])/ 100
                sp[i] = f'${amount:.2f}'
        return ' '.join(sp)

ans = Solution()
sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
discount = 100
print(ans.discountPrices(sentence,discount))