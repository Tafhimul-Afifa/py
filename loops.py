num=[1,4,9,16,25,36,49,64,72,81,100]
x=int(input("Enter the value:"))
index=0
while index < len(num):
    if(x==num[index]):
        print("found the number",index)
        break
    else:
        print("not found")

    index+=1
    


