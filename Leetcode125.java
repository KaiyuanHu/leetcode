# Leetcode 125 Valid Palindrome

class Solution {
    public boolean isPalindrome(String s) {
        int lo = 0, hi = s.length()-1;
        if( s == null || lo == hi) return true;
        while(lo <= hi){
            char head = s.charAt(lo), tail = s.charAt(hi);
            if(!Character.isLetterOrDigit(head)){
                lo++;
            }else if(!Character.isLetterOrDigit(tail)){
                hi--;
            }else if(Character.toLowerCase(head) != Character.toLowerCase(tail)){
                return false;
            }else{
                lo++; hi--;
            }
        }
        return true;
    }
}
