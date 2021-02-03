def isogram(word):
    newList = []
    repeatingWords = []
    countList = []
    for i in range(len(word)):
        newList += [word[i]]
    for i in newList:
        if newList.count(i) > 1:
            repeatingWords.append(i)
    for i in repeatingWords:
        countList.append((newList.count(i)))
        while repeatingWords.count(i) > 1:
            repeatingWords.remove(i)
    a=[]
    if countList != a:
        for i in range(len(repeatingWords)):
            print(repeatingWords[i], ":", countList[i])
        return False
    else:
        return True


print(isogram("mose"))