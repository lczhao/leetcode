class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        reList = [];
        print(range(numRows));
        for i in range(numRows):
            curList = [];
			for k in range(i + 1):
                curList.append(int(nCr(i, k)));
            reList.append(curList);
        return reList;
        
def nCr(n, r):
    f = math.factorial;
    if r == 0:
        return 1;
    return (f(n) / f(r) / f(n - r));