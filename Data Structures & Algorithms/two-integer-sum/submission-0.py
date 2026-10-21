class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}

        for i,num in enumerate(nums) :
            d=target-num
            if d in hmap :
                return [hmap[d],i]
            hmap[num]=i

            
            


