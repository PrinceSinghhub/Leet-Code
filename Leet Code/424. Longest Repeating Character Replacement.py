class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charSet = set(s)
        begin, end, res, mostFrequentCounter = 0, 0, 0, 0
        map = {}
        while end < len(s):
            char = s[end]
            map[char] = map.get(char, 0) + 1
            if mostFrequentCounter < map[char]:
                mostFrequentCounter = map[char]
            end += 1

            while (end - begin > mostFrequentCounter + k):
                char = s[begin]
                map[char] -= 1
                mostFrequentCounter = max(map.values())
                begin += 1

            res = max(end - begin, res)

        return res