import bisect
class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1]:
            return bisect.bisect(nums, target)-1 if nums[bisect.bisect(nums, target)-1] == target else -1

        def helper(left, right):
            mid = (left + right) // 2

            if left > right:
                return -1
            end = nums[right]
            start = nums[left]
            mid_val = nums[mid]

            if target == mid_val:
                return mid
            if (mid_val <= end and start <= mid_val): #we are in a sorted section
                if target == end:
                    return right
                if target == start:
                    return left

                if end < target and target < start:
                    return -1

                if target < end and mid_val < target:
                    return helper(mid+1, right-1)
                else:
                    return helper(left+1, mid-1)
            elif (mid_val < start):# we are crossing the boundary on the left of mid
                if target == end:
                    return right
                if target == start:
                    return left

                if end < target and target < start:
                    return -1
                
                if target > start or target < mid_val:
                    return helper(left+1, mid-1)
                else:
                    return helper(mid+1, right-1)
            else:# we are crossing the boundary on the right of mid
                if target == end:
                    return right
                if target == start:
                    return left

                if end < target and target < start:
                    return -1

                if target < end or target > mid_val:
                    return helper(mid+1, right-1)
                else:
                    return helper(left+1, mid-1)
            

        return helper(0,len(nums)-1)

                