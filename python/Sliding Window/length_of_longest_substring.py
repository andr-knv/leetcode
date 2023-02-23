def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    sum = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        if right - left + 1 > sum:
            sum = right - left + 1
    return sum



