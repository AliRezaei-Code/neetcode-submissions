
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mymap = Counter(nums)
        if any(v > 1 for v in mymap.values()):
            return True 
        return False