# Uses python3
import re,sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    #write your code here
    list1 = re.split('\+|-|\*|/',dataset)
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    M = [[0]*(len(list1)+1) for i in range(len(list1)+1)]
    m = [[0]*(len(list1)+1) for i in range(len(list1)+1)]
    #dict1 = {}
    list2 = [0]*(len(list1))
    j = 1
    for i in range(len(dataset)):
        if dataset[i] in ('+','-','*','/'):
            #dict1.update({i:dataset[i]})
            list2[j] = dataset[i]
            j=j+1
    #print(list2)
    for i in range(len(list1)):
        m[i+1][i+1] = list1[i]
        M[i+1][i+1] = list1[i]
    
    for s in range(1,len(list1)):
        for i in range(1,len(list1)-s+1):
            j = i + s
            #print("Outside... i:",i,"j:",j)
            min1 = sys.maxsize
            max1 = -sys.maxsize-1
            for k in range(i,j):
                #print("i:",i,"j:",j,"k:",k)
                #print("M[i][k]=",M[i][k],list2[k],"M[k+1][j]=",M[k+1][j],"m[i][k]=",m[i][k],list2[k],"m[k+1][j]=",m[k+1][j])
                a1 = evalt(M[i][k],M[k+1][j],list2[k])
                a2 = evalt(M[i][k],m[k+1][j],list2[k])
                a3 = evalt(m[i][k],M[k+1][j],list2[k])
                a4 = evalt(m[i][k],m[k+1][j],list2[k])
                min1 = min([min1,a1,a2,a3,a4])
                max1 = max([max1,a1,a2,a3,a4])
                #print("a1:",a1,"a2:",a2,"a3:",a3,"a4:",a4)
            m[i][j] = min1
            M[i][j] = max1
            #print("Min:",m[i][j])
            #print("Max:",M[i][j])
    #print(m)
    #print(M)
    return M[1][len(list1)]


if __name__ == "__main__":
    print(get_maximum_value(input()))
