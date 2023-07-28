"""
A solution to detect if a number repeats twice in a given array
"""

def containsDuplicate(self, nums: List[int]) -> bool:
    number_seen = {}
    for ele in nums:
        if(number_seen.get(ele, None)== None):
            number_seen[ele] = 1
        else:
            return True
    return False
