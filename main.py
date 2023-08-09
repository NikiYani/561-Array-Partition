class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        sum = 0
        
        for i in range(0, len(nums), 2) :
            print(nums[i])
            print(nums[i + 1])
            if nums[i] < nums[i + 1] :
                sum += nums[i]
            else : 
                sum += nums[i + 1]
        
        return sum