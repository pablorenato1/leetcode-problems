from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # True index to generate the except list
        for element in nums:
            if element != val: # Verify if current number is different from 'val'
                nums[k] = element
                k +=1
        return k