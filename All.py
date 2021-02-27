import random

def StrToList(str):
    str1 = str
    NewList = [""]
    str1 = str1.replace(", ", "|")
    for i in str1:
        if i == "|":
            NewList.append("")
        else:
            NewList[len(NewList)-1] = NewList[len(NewList)-1] + i
    for i in range(len(NewList)):
        NewList[i] = int(NewList[i])
    return NewList

def BogoSort(List, Loops):
    List1 = List
    while True:
        Break = True
        CMN = -1
        for _ in range(Loops):
            x = random.choice(List1)
            y = random.choice(List1)
            List1[List1.index(y)] = x
            List1[List1.index(x)] = y
        print(List1)
        for i in List1:
            if CMN < i:
                CMN = i
            else:
                Break = False
                break
        if Break:
            break

def RadixSort(List):
    for i in range(len(List)):
        List[i] = str(List[i])
    print(List)

    max_len = -1
    for ele in List: 
        if len(ele) > max_len: 
            max_len = len(ele) 
            res = ele

    for i in range(len(List)):
        List[i] = "0"*(len(res)-len(List[i])) + List[i]


    for k in range(len(res)):
        NewList = []
        for i in range(-9, 10):
            for j in List:
                if j[len(j)-(1+k)] == str(i):
                    NewList.append(j)
        List = NewList
        Show = NewList.copy()
        for i in range(len(Show)):
            while True:
                if Show[i][0] == "0":
                    Show[i] = Show[i][1:]
                else:
                    break
        print(Show)

def InsertSort(List):
    for i in range(1, len(List)):
        if List[i] < List[i-1]:
            for j in range(len(List)):
                if List[0] >= List[i]:
                    NewList = [List[i]]
                    for c in range(1, len(List)):
                        if c != i:
                            NewList.append(List[c])
                    List = NewList
                    print(NewList)
                elif List[j] > List[i]:
                    NewList = List[:j].append(List[i])
                    del List[i]
                    NewList.append(List[i:])
    print(NewList)
InsertSort(StrToList(input()))

# 35, 485, 562, 659, 364, 703, 247, 394, 1423, 9999
