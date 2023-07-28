"""
Solution to detect if a given string is Anagram
"""

def isAnagram(self, s: str, t: str) -> bool:
    # Checking for length of two Strings
    if(len(s) !=len(t)):
      return False

    letters_map = {}
    for letter in s:
        letters_map[letter] = letters_map.get(letter, 0) + 1

    for letter in t:
        val = letters_map.get(letter, 0)
        if(val and val>1):
            letters_map[letter] = val- 1
        elif(val==1):
            del letters_map[letter]
        else:
            # If new letter is introduced, return False
            return False
    
    if(len(letters_map)>0):
        return False
    else:
        return True

    # Can do this too 
    # return sorted(s)== sorted(t)
