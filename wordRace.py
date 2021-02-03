def race(words):
    global o, m
    for i in words:
        list1 = i
        newList = []
        for j in range(len(list1)):
            newList += [list1[j]]
        print(newList)
        total = 0
        for k in range(97,123):
            if chr(k) in newList:
                if newList.count(chr(k)) > 1:
                    total += (newList.count(chr(k))-1)*(k-96)
                total += k - 96
        print(total)
        if i is words[0]:
            m = total
        elif i is words[1]:
            o = total
    if m > o:
        print(words[0],"is bigger")
    else:
        print(words[1],"is bigger")
race(["example","work"])