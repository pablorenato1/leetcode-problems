/**
 * @param {string} s
 * @return {string}
 */

var longestPalindrome = function(s) {
    let lengthLongest = 0;
    let strLongest = ""

    var findPalindrome = (left, right) => {
        // l, r = left, i
        while (0 <= left && right <= s.length && s[left] === s[right]) {
            if ((r - l + 1) >lengthLongest) {
                strLongest = s.slice(left, right+1);
                lengthLongest = strLongest.length;
            }
            left--;
            right++;
        }
    }

    for (let i = 0; i < s.length; i++) {
        // Check for odd Palindromes
        findPalindrome(i, i);
        
        // Check for even Palindromes
        findPalindrome(i, i+1);

        // End the loop if it's not possible find longest Palindrome
        if (((s.length - i)* 2) < lengthLongest) {
            break
        }
    }
    return strLongest;
};

console.log(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))