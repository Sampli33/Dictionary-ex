words = [i for i in input().split()]
dictionary = {}
for value in words:
    key = words.count(value)
    dictionary[key] = value
occurrence_rate = list(dictionary.keys())
occurrence_rate.sort(reverse=True)
for i in occurrence_rate:
    print(dictionary.pop(i))
