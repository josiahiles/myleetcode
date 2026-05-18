

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        di = dict()
        N = len(nums)
        for i in range(N):
            if nums[i] in di:
                return [i, di[nums[i]]]
            di[target - nums[i]] = i

        return []




    

