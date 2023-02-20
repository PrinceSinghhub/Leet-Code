class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # recursive or linear

        string = "1"

        if n == 1:
            return string

        for i in range(n - 1):

            count = 1
            current = string[0]
            new_string = ''

            for s in string[1:]:
                if s != current:
                    new_string += str(count) + current
                    count = 1
                    current = s
                else:
                    count += 1

            string = new_string + str(count) + current

        return string