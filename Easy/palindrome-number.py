class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        if len(temp) == 1:
            return True
        if temp == temp[::-1]:
            return True
        else: return False

if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome(2332))
    pass