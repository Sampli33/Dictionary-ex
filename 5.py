n = int(input())
tree = {}
for i in range(n):
    p, c = input().split()
    if p not in tree:
        tree[p] = []
    tree[p].append(c)
name = input()
counter = 0
descendant = [name]
while descendant:
    man = descendant.pop()
    if man in tree:
        counter += len(tree.get(man))
        descendant.extend(tree.get(man))
print(counter)
