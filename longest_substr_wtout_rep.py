def length_of_longest_substring(s: str) -> int:
    seen = {}
    max_length = 0
    left = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length, seen


text = 'sdkjskjsidoiddww'
print(length_of_longest_substring(text))
# print(seen)