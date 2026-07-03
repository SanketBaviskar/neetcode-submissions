class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map ={};
        for(let num of nums ){
            if(map[num]){
                map[num] +=1;
            }
            else{
                map[num] = 1;
            }
        }
        
        let frequency = Object.keys(map).map(num => [parseInt(num) , map[num]]);
        let sorted_arr = frequency.sort((a,b) => b[1] - a[1]);
        let answer =  sorted_arr.splice(0,k).map(e => e[0]);
        return answer
    }
    
}
