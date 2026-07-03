class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0
        let left = 0 , right = 0;
        while(right<prices.length){
            if(prices[right] - prices[left] < 0){
                left = right
            }
            maxProfit = Math.max(maxProfit , prices[right] - prices[left])
            right++
        }      
        return maxProfit 
    }
}
