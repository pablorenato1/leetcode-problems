from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for num in nums:
            if nums[index] == num:
                continue
            index += 1
            nums[index] = num
        return index+1