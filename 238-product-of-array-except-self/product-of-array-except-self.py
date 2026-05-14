class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # [1,2,3,4] 
       # [2*3*4, 1 * 3*4, 1*2 * 4, 1*2*3]
        lhs = [1] * (n := len(nums))
        rhs = [1] * len(nums)
        for i in range(1,n):
            lhs[i] = lhs[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            rhs[i] = rhs[i+1]*nums[i+1]
        
        return [x*y for x,y in zip(rhs,lhs)]