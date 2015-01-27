class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False;
        else:
            s = str(x);
        i = 0;
        for c in s[::-1]:
            if c != s[i]:
                return False;
            i += 1;
        return True;