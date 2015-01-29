class Solution:
    # @return a boolean
    def isValid(self, s):
        aCount = 0;
        bCount = 0;
        cCount = 0;
        
        lastOpen = [];
        
        for c in s:
            if c == '(':
                aCount += 1;
                lastOpen.append(c);
            elif c == ')':
                aCount -= 1;
                if (len(lastOpen) < 1) or (lastOpen.pop() != '('):
                    return False;
            elif c == '{':
                bCount += 1;
                lastOpen.append(c);
            elif c == '}':
                bCount -= 1;
                if (len(lastOpen) < 1) or (lastOpen.pop() != '{'):
                    return False;
            elif c == '[':
                cCount += 1;
                lastOpen.append(c);
            elif c == ']':
                cCount -= 1;
                if (len(lastOpen) < 1) or (lastOpen.pop() != '['):
                    return False;
        
        return aCount == 0 and bCount == 0 and cCount == 0;
                