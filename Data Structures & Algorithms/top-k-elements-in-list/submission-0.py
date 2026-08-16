class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = set(nums)
        count = {}

        for i in a:
            count[i] = nums.count(i)

        return sorted(count, key=count.get, reverse=True)[:k]