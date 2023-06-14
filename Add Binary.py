# Given two binary strings a and b, return their sum as a binary string.

# Input: a = "11", b = "1"
# Output: "100"
# Input: a = "1010", b = "1011"
# Output: "10101"

a = "1010"
b = "1011"

def addBinary(a, b):
    a = list(a)
    b = list(b)
    num = 0

    for i in range (0, len(a)):
        if(a[i]=="1"):
            num = num + (2**(len(a)-1-i))

    for i in range (0, len(b)):
        if(b[i]=="1"):
            num = num + (2**(len(b)-1-i))
    
    return(bin(num)[2:])

print(addBinary(a,b))