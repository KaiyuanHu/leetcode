// Leetcode 16 3Sum Closest

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if(nums.length == 3) return nums[0]+nums[1]+nums[2];
        Arrays.sort(nums);
        int diff = nums[0]+nums[1]+nums[2]-target;
        for(int idx = 0; idx < nums.length-2; idx++){
            int left = idx+1, right = nums.length-1;
            while(right > left){
                if(nums[idx] + nums[left] + nums[right] == target) return target;
                int temp = (nums[idx] + nums[left] + nums[right]) - target;
                if ( temp < 0){
                    if(Math.abs(diff) > Math.abs(temp)) diff = temp; 
                    left++;
                }
            else{
                    if(Math.abs(diff) > Math.abs(temp)) diff = temp; 
                    right--;
                }
            }
        }
       return target + diff;
    }
}
