def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex + 1, endIndex -1)
    else:
        opt1 = findLPS(s, startIndex, endIndex -1)
        opt2 = findLPS(s, startIndex + 1, endIndex)
        return max(opt1, opt2)

print(findLPS('ELRMENMET', 0, 8))