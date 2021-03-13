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
    #for i in range(len(NewList)-1):
        # print(NewList)
        # NewList[i] = str(NewList[i])
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
    exlist = List
    for i in range(1, len(exlist)):  
        if exlist[i] < exlist[i-1]:
            if exlist[0] >= exlist[i]:
                    new_exlist = [exlist[i]]
                    for c in range(len(exlist)):
                        if c != i:                        
                            new_exlist.append(exlist[c])
                    exlist = new_exlist
                    print(new_exlist)
            else:
                for j in range(len(exlist)):
                    if exlist[j] <= exlist[i] and exlist[i] < exlist[j+1]:
                        new_exlist = []
                        for c in range(j+1):
                            if c != i:
                                new_exlist.append(exlist[c])
                        new_exlist.append(exlist[i])
                        for c in range(j+1, len(exlist)):
                            if c != i:
                                new_exlist.append(exlist[c])
                        exlist = new_exlist
                        print(exlist)

    
InsertSort(StrToList(input()))

# 35, 485, 562, 659, 364, 703, 247, 394, 1423, 9999
