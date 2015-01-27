class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        a = version1.split(".");
        b = version2.split(".");
        #make the rest 0
        if len(a) < len(b):
            for i in range(len(b) - len(a)):
                a.append("0");
        else:
            for i in range(len(a) - len(b)):
                b.append("0");
                
        for i in range(len(a)):
            #a is bigger then b
            v1 = int(a[i]);
            v2 = int(b[i]);
            if v1 > v2: 
                return 1;
            elif v1 < v2: 
                return -1;
            
        return 0;