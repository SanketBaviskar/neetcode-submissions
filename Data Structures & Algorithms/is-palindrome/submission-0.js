class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let cleanedStr = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
        // Reverse the cleaned string
        let reversedStr = cleanedStr.split('').reverse().join('');
        // Check if cleaned string is equal to its reversed version
        return cleanedStr === reversedStr;
    }
}
