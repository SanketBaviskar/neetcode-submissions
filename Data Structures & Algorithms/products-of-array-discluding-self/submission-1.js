class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let answer = new Array(nums.length).fill(1)
    for (let i = 1; i < nums.length; i++) {
        answer[i] = nums[i-1] * answer[i-1];
        }
    let rightProduct = 1;
        for (let i = nums.length-2; i >= 0; i--) {
            rightProduct = rightProduct * nums[i+1];
            answer [i] = answer[i] * rightProduct;
        }
    return answer
    }
}
