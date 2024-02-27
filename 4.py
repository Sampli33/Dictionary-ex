n = int(input())
dictionary = {}
for i in range(n):
    elem = input().split()
    dictionary[elem[0]] = elem[1:]
subject = input()
for i in dictionary:
    if subject in dictionary[i]:
        print(i)
