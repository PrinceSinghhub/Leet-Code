class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        stack = []
        pointer = 0

        for val in range(1, n + 1):
            if pointer == len(target) or val > target[pointer]:
                break

            if val == target[pointer]:
                stack.append('Push')
                pointer += 1
            else:
                stack.extend(["Push", "Pop"])

        return stack
