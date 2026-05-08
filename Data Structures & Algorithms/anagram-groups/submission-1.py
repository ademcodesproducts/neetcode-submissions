class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store_dict = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            store_dict[sortedS].append(s)
        return list(store_dict.values())
    
                    