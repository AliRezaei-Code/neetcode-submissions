class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list_out = [] 
        list_out.extend(nums)
        list_out.extend(nums)
        return list_out