# print_odd_numbers.py

def odds(lLimit,uLimit):
    result=0
    for j in range(lLimit,uLimit+1):
        if(j%2!=0):
            result += j
    return result        

lLimit=int(input("Enter the lower limit for the range:"))
uLimit=int(input("Enter the upper limit for the range:"))

print(odds(lLimit,uLimit))

