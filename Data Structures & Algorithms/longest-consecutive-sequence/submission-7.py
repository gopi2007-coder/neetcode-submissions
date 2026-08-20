class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a = sorted(set(nums))
        maxx = 1
        c = 1

        for i in range(len(a) - 1):
            if a[i] + 1 == a[i + 1]:
                c += 1
            

            if c > maxx:
                maxx = c

        return maxx