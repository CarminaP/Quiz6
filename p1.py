def superpower(a,b):
    count=0
    answer=1
    while (count < b):
        answer= answer*a
        count+=1
    return answer

x = int(input("Write an integer number: "))
y= int(input("Write the power number you want to rise it up to: "))
print (("The answer is: ")+ str(superpower(x,y)))
