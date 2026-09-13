class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For optimization list can't be keys of hashmaps but tuples can
        sort_to_word = defaultdict(list)
        for s in strs:
            count = [0] * 26 # will become key with coutns for each letter
            for c in s:
                # for each letter inside letter count array increase by 1 if exist
                count[ord(c) - ord('a')] += 1 
            sort_to_word[tuple(count)].append(s)
        return list(sort_to_word.values())