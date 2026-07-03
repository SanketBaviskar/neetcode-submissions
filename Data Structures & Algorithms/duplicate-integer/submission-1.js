class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // nums = nums.sort((a,b) => a-b)
        // for(let i = 0 ; i<nums.length ; i++){
        //     if(nums[i] == nums[i+1]) return true
        // }

        let map = new Map();
        for (let i = 0; i < nums.length; i++) {
            if (map.has(nums[i])) {
                return true;
            }
            else {
                map.set(nums[i], 1)
            }

        }
        return false
    }
}
