class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # vortexisalpha
        # [0,0,1,1,1,1,2,3,3]
        #      |
        insertIndex = 1
        count = 0

        for i, num in enumerate(nums[1:], start=1):
            print(count , num)
            if count == 0 and nums[i-1] == nums[i]:
                nums[insertIndex] = nums[i]
                count += 1
                insertIndex += 1
            elif count >= 1 and nums[i-1] == nums[i]:
                continue
            else:
                count = 0
                nums[insertIndex] = nums[i]
                insertIndex += 1

        nums = nums[:insertIndex]
        return insertIndex
