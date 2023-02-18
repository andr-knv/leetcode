from collections import Counter

def character_replacement(s:str, k:int) -> int:
    left, result, counts = 0, 0, Counter()
    
    for right in range(len(s)):
        counts.update(s[right])
        
        if (right - left + 1) - max(counts.values()) > k:
            counts[s[left]] -= 1
            left += 1 

        result = max(result, right - left + 1)
    return result

