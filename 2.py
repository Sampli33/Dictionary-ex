N = int(input())
dictionary = {}
for i in range(N):
    key, value = input().split()
    dictionary[key] = value
sentence = input().split()
for i in sentence:
    print(dictionary.get(i, i), end=' ')
