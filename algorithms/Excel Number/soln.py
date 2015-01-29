class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        # prevDigit = 0;
        retDigit = 0;
        i = 0;
        for c in reversed(s):
            currentDigit = ord(c) - ord('A') + 1;
            retDigit += currentDigit * int(math.pow(26, i));
            i += 1;
        return retDigit