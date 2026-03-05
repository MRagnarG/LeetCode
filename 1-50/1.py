# 1. Two Sum problem

from typing import List

class Solution: 
    """
    Finds two numbers in a list that add up to a target value.
    This solution uses a brute force approach to find two distinct indices 
    in the input list where the numbers at those indices sum to the target value.
    Args:
        nums (List[int]): A list of integers to search through.
        target (int): The target sum value.
    Returns:
        List[int]: A list containing two indices [i, j] where nums[i] + nums[j] == target.
                Returns an empty list [] if no such pair exists.
    Example:
        >>> solution = Solution()
        >>> solution.twoSum([2, 7, 11, 15], 9)
        [0, 1]
    Note:
        Uses nested loops for comparison. Time Complexity: O(n²), Space Complexity: O(1).
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            first_number = nums[i]
            next = i + 1
            
            for number in nums[next :]:
                if first_number + number == target:
                    j = (nums.index(number) if not nums.index(number) == i 
                        else nums[next :].index(number) + 1)
                    return [i, j]
                    
        return []        

solution = Solution        
print(solution.twoSum(solution, [3,3], 6))    