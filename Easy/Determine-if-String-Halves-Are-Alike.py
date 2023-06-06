class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        temp = 0
        length = len(s)
        for letter in range((length//2)):
            if not s[letter] in vowel:
                continue
            temp += 1
        for letter in range((length//2), length):
            if not s[letter] in vowel:
                continue
            temp -= 1
        if temp == 0: return True
        return False

if __name__ == "__main__":
    test = Solution()
    print(test.halvesAreAlike("book"))