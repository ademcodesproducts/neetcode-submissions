class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_to_word = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            sort_to_word[sorted_word].append(s)
        return list(sort_to_word.values())