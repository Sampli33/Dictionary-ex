N = int(input())
dictionary = {}
for i in range(N):
    elem = input().split()
    dictionary[elem[0]] = elem[1:]
subject = input()
for i in dictionary:
    if subject in dictionary.get(i):
        print(i)
