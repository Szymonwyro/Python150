def longestConsecutive(self,nums):
    nums_set = set(nums)

    longest = 0
    
    for i in nums_set:
        if i - 1 not in nums_set:
            seq_start = i
            length = 1
            current = i + 1
            while current in nums_set:
                length += 1
                current += 1

            longest = max(longest, length)

    return longest
            

    
        
    (100,4,200,1,3,2)
        



