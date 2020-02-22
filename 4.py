

def groupNumber(inpt):
    groupNum = ""
    k=0
    for character in inpt:
        
        if character.isdigit():
            k=k+1
            if (k % 3 == 0):
                groupNum += character + "-"
            else:
                groupNum += character

    
    if (k % 3 == 1):
        groupNum = groupNum[:-3]+"-"+groupNum[-3]+groupNum[-1]

    elif (k % 3 == 0):
        groupNum = groupNum[ : -1: ]
        
    return print(groupNum)


inpt = input("Masukkan string : ")

groupNumber(inpt)
    