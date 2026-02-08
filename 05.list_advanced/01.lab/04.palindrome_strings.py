words = input().split()
key_word = input()

filtered_words = [word for word in words if word[::-1] == word]

repetition_count = filtered_words.count(key_word)

print(filtered_words)
print(f"Found palindrome {repetition_count} times")