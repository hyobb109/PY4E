import weakref


fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    # print(line)
    wds = line.split()
    # print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
        # print(w, 'new', di[w])

# print(di)

# now we want to find the most common word
largest = -1
theword = None
for k, v in di.items() :
    print(k,v)
    if v > largest : 
        largest = v
        theword = k #capture/remember the word that was the largest

print(theword, largest)