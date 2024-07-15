# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = None
        for i, s in enumerate(strs):
            if i == 0:
                encoded_str = s
            else:
                encoded_str = encoded_str + "/" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        else:
            return s.split("/")
