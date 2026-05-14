class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortus = 0
        hare = 0
        
        while 1:
            tortus = nums[tortus]
            hare = nums[nums[hare]]
            if hare == tortus:
                break
        
        hare = 0

        while 1:
            hare = nums[hare]
            tortus = nums[tortus]
            if hare == tortus:
                return hare