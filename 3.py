N = int(input())
dictionary = {}
for i in range(N):
    key, value = input().split()
    dictionary[key] = value
    dictionary[value] = key
word = input()
print(dictionary.get(word, word))
