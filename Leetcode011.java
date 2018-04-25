// leetcode 11 Container With Most Water

class Solution {
    public int maxArea(int[] height) {
        // this is a two pointer problem
        int left = 0, right = height.length - 1;
        int maxArea = 0;
        while(right > left){
            maxArea = Math.max(maxArea, (right - left)*Math.min(height[left], height[right]));
            if (height[left] < height[right]) left ++;
            else right--;
        }
        return maxArea;


    }
}
