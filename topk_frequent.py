
# Problem statement: Given an integer array nums and an integer k, \
# return the k most frequent elements. You may return the answer in any order.

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      result=[]
      count_map = {}
      for i in nums:
          count_map[i] = count_map.get(i,0)+1

      if len(count_map):
          count_list = [(key, val) for key, val in count_map.items()]
          count_list.sort(key=lambda x: x[1], reverse=True)
          result = [num for num, _ in count_list[:k]]
      return result
