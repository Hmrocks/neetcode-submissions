class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Put numbers in buckets by frequency
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Step 4: Collect top k from highest buckets
        result = []
        for i in range(len(buckets) - 1, -1, -1):  # Start from end, go to 0
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]
        
        return result