def countB(w):
    count = 0
    for i in range (0, len(w)):
        if w[i] == "b":
            count = count + 1
    return count


def removeLast(w):
    newWord = ""
    for i in range (0, len(w) - 1):
        newWord = newWord + w[i]
    return newWord


def sumBetweenOdd(x, y):
    total = 0
    for i in range (x + 1, y, 2):
        total = total + i
    return total


def firstLast(w):
    if w[0] == w[len(w)-1]:
        return True 
    else:
        return False 




print(countB("baseball"))
print(removeLast("alex"))
print(sumBetweenOdd(4, 13))
print(firstLast("alex"))