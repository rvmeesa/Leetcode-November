class Solution:
    def findDiagonalOrder(self, nums):
        ans = []
        keyToNums = collections.defaultdict(list)
        maxKey = 0

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                key = i + j
                keyToNums[key].append(nums[i][j])
                maxKey = max(maxKey, key)

        for i in range(maxKey + 1):
            for it in keyToNums[i][::-1]:
                ans.append(it)

        return ans

        