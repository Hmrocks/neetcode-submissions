class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            if target - v in hashmap:
                return [hashmap[target - v], i]
            hashmap[v] = i
        return []



        # bruteforce loop through elements of array and add to every different pair together until we find target , using 2 nested loops, very inefficient
        # create empty Hashmap and use target - element to see if it's already existing in the created hasmap, repeat same process through all elements until we find a pair 
