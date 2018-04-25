class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        if(nums.length < 3) return result;
        if(nums.length == 3){
            if(nums[0] + nums[1] + nums[2] == 0){
                result.add(Arrays.asList(nums[0], nums[1] , nums[2]));
                return result;
            }else{
                return result;
            }
        }

        for(int idx = 0; idx < nums.length-2; idx++){
            if (idx == 0 || (idx > 0 && nums[idx] != nums[idx-1])) {
            int left = idx + 1, right = nums.length -1;
            while(right > left){
                if(nums[idx] + nums[left] + nums[right] == 0) {
                    result.add(Arrays.asList(nums[idx], nums[left] , nums[right]));
                    while(right > left && nums[left] == nums[left+1]) left++;
                    while(right > left && nums[right] == nums[right-1]) right--;
                    left++; right--;
                }
                else if(nums[idx] + nums[left] + nums[right] < 0){
                    left++;
                }else{
                    right--;
                }
            }
        }
        }
        return result;
        
    }
}
