lines = [line.strip().lower() for line in open('/home/gautham/zingarelli2005.txt')]

def signature(wordList):
    anagramDict = {}
    for word in wordList:
        sortedWord = ''.join(sorted(word))
        if sortedWord in anagramDict.keys():
            anagramDict[sortedWord].append(word)
        else:
            anagramDict.update({sortedWord:[word]})
    return anagramDict

print([[v]for k,v in signature(lines).items() if len(v)>1])


