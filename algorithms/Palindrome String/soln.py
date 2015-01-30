class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == "": return True;
        i = 0;
        j = len(s) - 1;
        while i < len(s):
            while (s[i] < 'A' or s[i] > 'Z') and (s[i] < 'a' or s[i] >'z') and (s[i] < '0' or s[i] > '9'):
                i += 1;
                if i >= j:
                    return True;
            while (s[j] < 'A' or s[j] > 'Z') and (s[j] < 'a' or s[j] >'z') and (s[j] < '0' or s[j] > '9'):
                j -= 1;
                if j <= i:
                    return True;
            if s[i].lower() != s[j].lower():
                return False;
            else:
                i += 1;
                j -= 1;
        
        return True;