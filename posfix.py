import copy

ope = ["+","-","*","/","^","(",")"]
posfix = []
stack = []
data = "(Q+A/j)*B/(C/D+F)*G^D" #datatest
# data = str(input("Enter Infix"))


for i in data:
    if i in ope:
        stack.append(i)
        while True:
            if i == ")":
                del stack[-1]
                for pushdata in range(1,len(stack)+1):
                    if stack[-1] != "(":
                        posfix.append(copy.deepcopy(stack[-1]))
                        del stack[-1]
                    else:
                        del stack[-1]
                        break
            if len(stack) > 1:
                for count in range(0,6):
                    if stack[-1] in ope[count]:
                        if count == 1 or count == 3:
                            top = count -1
                        else:
                            top = count 
                    if stack[-2] in ope[count]:
                        if count == 1 or count == 3:
                            after = count -1
                        else:
                            after = count 
                if top > after or after == 5:
                        break
                else:
                    posfix.append(copy.deepcopy(stack[-2]))
                    del stack[-2]
            else:
                break
    else:
        posfix.append(i)
        
for i in range(1,len(stack)+1):
    posfix.append(copy.deepcopy(stack[-abs(i)]))
del stack
posfix = ' '.join(map(str, posfix))
print("Infix = " ,data)
print("Posfix = ", posfix)
