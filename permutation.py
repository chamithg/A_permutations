class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results =[]
        temp = nums
        pivot = len(nums)-1
        def run(nums,position):
            i = len(temp)-2
            while nums[i]>= nums[i+ 1]:
                i-=1
            
            if i >= 0: 
                j = nums.length - 1
                while nums[i] >= nums[j]: 
                    j-=1
            
                [nums[i], nums[j]] = [nums[j], nums[i]]
            
            
            left = i + 1
            right = nums.length - 1
            
            

nums = [1,2,3]


obj = Solution()

print(obj.permute(nums))

