class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
        
        for w in words:
            freq_chars = Counter(chars)
            freq_w = Counter(w)
            stop = False
            for c in w:
                if freq_w[c] > freq_chars[c]:
                    stop = True
                    break
                    
            if stop == False:
                length += len(w)
            
        return length
            