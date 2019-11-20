class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        ans = []
        for i in range(len(nums)):
            dict[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in dict.keys() and dict[target-nums[i]] != i:
                ans.append(i)
                ans.append(dict[target-nums[i]])
                break
        return ans