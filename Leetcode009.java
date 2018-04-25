// leetcode 09 Palindrome Number

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int old_val = x, new_val = 0;
        while(old_val != 0){
            new_val = new_val*10 + old_val%10;
            old_val = old_val/10;
        }
        return new_val == x;

    }
}
