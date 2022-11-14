class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## this solution works, but repeats 
        permutCount = 1
        
        for i in range(1,len(nums)+1):
            permutCount *= i
            
        nums.sort()
        results =[]   
        def run(num,permutCount):
            print(results)
            temp =[]
            for each in num:
                temp.append(each)
            print(temp)
            if permutCount == 0:
                return
            else:
                results.append(temp)
                print(results)
                permutCount -=1
                
            
            i = len(temp)-2
            while temp[i]>= temp[i+ 1] and i > 0:
                i-=1
            
            if i >= 0: 
                j = len(temp)-1
                while temp[i] >= temp[j] and j > i: 
                    j-=1
                [temp[i], temp[j]] = [temp[j], temp[i]]
            
            left = i+1
            right = len(temp)-1
            
            while left < right:
                [temp[left], temp[right]] = [temp[right], temp[left]]
                left+=1
                right-=1
            print(results)
            return run(temp,permutCount)
            
        run(nums,permutCount)
        return results   

nums = [1,2,3,4]
nums1 = [0,2]
nums2 = [0,-1,1]


obj = Solution()

print(obj.permute(nums2))

#[,,,,,[0,1,-1]]
#[,,[-1,0,1],,,]