#Get the lower limit from user
lower_limit = int(input("Enter Lower limit: "))

#get upper limit from user
Upper_limit = int(input("Enter Upper limit: "))

#initialize submission as zero
sum=0

#iterate from lower to upper limit and add the numbers to sum.
for i in range(lower_limit,Upper_limit+1):
    sum=sum+i

#print sum value
print("Addition of numbers = ",sum)
