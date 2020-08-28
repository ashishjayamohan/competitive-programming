def ex(n1,n2):
    answer = ""
    for i in range(len(n1)):
        if(n1[i] != n2[i]):
            answer += "1"
        else:
            answer += "0"
    return answer

one = input()
two = input()
print(str(ex(one,two)))
