# print_odd_numbers.py

def odds(lLimit,uLimit):
    for j in range(lLimit,uLimit+1):
        if(j%2!=0):
            print(j)

lLimit=int(input("Enter the lower limit for the range:"))
uLimit=int(input("Enter the upper limit for the range:"))

odds(lLimit,uLimit)

