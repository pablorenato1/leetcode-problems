
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        for _ in range(n):
            if (n % 2) == 0:
                n = n/2
            elif (n % 3) == 0:
                n = n/3
            elif (n % 5) == 0:
                n = n/5
            elif n == 1:
                return True
            else:
                return False
    

if __name__ == "__main__":
    a = Solution()
    print(a.isUgly(21))
# 937351770
# 2147483648