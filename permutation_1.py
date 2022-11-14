class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        '''
        this is the backtracking solution.
        perms keep the track of the building permutation
        element adding to the perm, removed from the original array.
        when perm completed, it added to the res array.
        nums[:i]+nums[i+1:] this returns everyting in the array without the element in i index.
            nums[:i] --> everything up to i
            nums[i+1:] . --> everything after i+1
        
        '''
        result = []
        
        def run(nums,perm):
            if not nums:
                result.append(perm)
            for i in range(len(nums)):
                run(nums[:i]+nums[i+1:], perm+[nums[i]])
        
        run(nums,[])
        return result
        
nums = [1,2,3,4]
nums1 = [0,2]
nums2 = [0,-1,1]


obj = Solution()

print(obj.permute(nums))

#[,,,,,[0,1,-1]]
#[,,[-1,0,1],,,]