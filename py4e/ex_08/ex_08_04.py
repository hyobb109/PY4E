fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.strip()
    lst.append(words.split())
lst = sum(lst, [])
lst.sort()
res = []
for value in lst:
    if value not in res:
        res.append(value)
print(res)
