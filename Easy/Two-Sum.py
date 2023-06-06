
class Solution:
    def twoSum(self, nums, target: int):
        for p1, n1 in enumerate(nums):
            # Maybe look directly the difference is in the list or something like that could be faster, not sure
            for p2 in range(p1+1, len(nums)):
                if (n1 + nums[p2]) == target:
                    return [p1, p2]

if __name__=="__main__":
    a = Solution()
    print(a.twoSum([3,3], 6))