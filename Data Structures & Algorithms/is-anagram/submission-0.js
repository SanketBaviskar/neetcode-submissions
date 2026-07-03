class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let s_arr = s.split("").sort().join("");
        let t_arr = t.split("").sort().join("");

        return s_arr == t_arr

    }
}
