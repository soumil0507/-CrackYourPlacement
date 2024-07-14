from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 2 Pointer approach #dutch flag problem
        
        n = len(nums)
        non_zero = -1
        zero = 0

        while zero < n:
            if nums[zero] != 0:
                non_zero+=1
                nums[non_zero], nums[zero] = nums[zero], nums[non_zero]
            zero+=1
        
        