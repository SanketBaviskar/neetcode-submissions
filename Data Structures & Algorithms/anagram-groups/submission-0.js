class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = {};

        for(let str of strs){
            let temp = str.split("").sort().join("");
            if(map[temp]){
                map[temp].push(str);
            }
            else{
                map[temp] =  [str];
            }
        }

        return Object.values(map)

        
    }
}
