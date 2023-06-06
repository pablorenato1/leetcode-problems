/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var temp = [];
    var subStringLength = 0;

    for (const letter of s) {
        if (temp.includes(letter)) {
            // Save the current progress and restart searching new subString (Save on temp variable)
            if (temp.length > subStringLength) {
                subStringLength = temp.length;
            }
            // Take the previous sequence starting from the repeated letter
            temp = temp.slice(temp.indexOf(letter)+1);
            if (temp.includes(letter)) continue;
            temp.push(letter);
        } else {
            // Add the new letter to a temp variable 
            temp.push(letter);
        }
    }
    if (temp.length > subStringLength) return temp.length
    if (subStringLength == 0 && s.length > 0) return temp.length;
    else return subStringLength;
};

console.log(lengthOfLongestSubstring("anviaj"))
