"""
A solution to group anagrams in the given list of strings

"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map = {}
    for word in strs:
        # sorted word used as key value in the map
        sorted_word = "".join(sorted(word))
        # print(sorted_word)
        curr_ana_group = anagram_map.get(sorted_word, None)
        # print("Current anagram group value: ", curr_ana_group)
        if(curr_ana_group != None):
            # append to existing words
            anagram_map[sorted_word].append(word)
        else:
            # add new word as list
            anagram_map[sorted_word] = [word]
    # Combining and returning the final answer
    final_res = []
    for val in anagram_map.values():
        final_res.append(val)
    return final_res
