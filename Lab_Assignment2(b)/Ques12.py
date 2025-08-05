from collections import defaultdict

# Sample list of words
words = ['eat', 'ate', 'tea', 'bat', 'tab', 'tan', 'nat', 'hello']

# Dictionary to store grouped anagrams
anagrams = defaultdict(list)

# Group words by sorted characters
for word in words:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word].append(word)

# Print all anagram groups (only if group has more than 1 word)
print("Anagram groups found:")
for group in anagrams.values():
    if len(group) > 1:
        print(group)
