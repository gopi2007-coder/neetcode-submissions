class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=sorted(nums)
        maxx=0
        for i in range(len(a)):
            c=0
            if (a[i]+1 == a[i+1]):
                c+=1
                if c>maxx:
                    maxx=c
        return maxx