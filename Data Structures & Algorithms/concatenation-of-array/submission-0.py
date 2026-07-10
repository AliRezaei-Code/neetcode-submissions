class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list_out = [] 
        for i in nums*2:
            list_out.append(i)
        return list_out