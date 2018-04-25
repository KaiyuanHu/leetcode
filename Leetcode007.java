// leetcode 07 Reverse Integer

class Solution {
    public int reverse(int x) {
        int res = x;
        if (x < 0) res = -x;
        int result = 0;
        while(res != 0){
            int mod = res%10;
            res = res/10;
            int new_result = result*10 + mod;
            if ((new_result - mod) / 10 != result) { 
                return 0; 
            }
            result = new_result;
        }
        if (x<0) result = -result;
        return result;
    }
}
