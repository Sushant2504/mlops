# assignment 1 mlop: # Question no. 1

# Command in terminal
# pip install boto3
# pip install fastAPI

# Question no. 2
#
dict={
    "hello":"World",
    "arr": {
        1:"hi",
        2:"Shir0",
        3:"Ved",
        4:"Varun",
        5:"Sushant"
    }
}
# print("Before Adding Element dict id is:",id(dict))
dict[2]=("hi there!")
print("After Adding Element dict id is :",id(dict))

# Question no. 3
print(100/0)


#  Question no. 4

index=0;
for fruits  in ["apple","banana","blackberry","cherry","orange"]:
    if "orange" in fruits:
        print("YES")
        print(index)
        break
    else :
        print("No")
        index=index+1

# Question no. 5
#
row=int(input("Enter the no. of Rows: "))
col=int(input("Enter the no. of Column: "))

count =col

for i in range(1,row+1):
    for j in range(0, col-i):
        print(" ",end=' ')
    for k in range(i):
        print("*",end=' ')
    print("\n")