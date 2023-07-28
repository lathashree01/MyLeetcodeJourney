"""
A solution to finding the indexes of two numbers from a given list.
Efficient one pass map based solution

"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    read_numbers = {}
    for idx, item in enumerate(nums):
        sec_num = target-item
        if sec_num in read_numbers:
            return [read_numbers[sec_num], idx]
        read_numbers[item] = idx

    # Return empty list if numbers not found
    return []
