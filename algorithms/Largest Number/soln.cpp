class Solution {
public:
    string largestNumber(vector<int> &num) {
        sort(num.begin(), num.end(), comp);
        string reStr;
        if (num[0] == 0) return "0";
        for(int i = 0; i < num.size(); i ++) {
            reStr.append(to_string(num[i]));    
        }
        
        return reStr;
    }
    
    static int comp(int a, int b) {
        string A = to_string(a);
        string B = to_string(b);
        
        return A+B > B+A;
    }
};