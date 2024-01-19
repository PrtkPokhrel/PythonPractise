# import sys

# def averge(num1,num2,num3):
#     av=(num1+num2+num3)/3
#     return av


# num1=int(sys.argv[1])
# num2=int(sys.argv[2])
# num3=int(sys.argv[3])

# print(averge(num1,num2,num3))


# Example: average.py script
# # A Python script file ‘average.py’ that calculates an average
# import sys
# values = sys.argv[1:] # slice args list to remove the file name
# total = 0;
# for n in values: # total the remaining values
# total += float(n) # convert each string ’n’ to a float
# # calculate and print the average
# print("Average is", total/len(values))


import sys
values=sys.argv[1:]

a=[int(x) for x in values]

sum=0
for i in a  :
    sum+=i

average=len(values)
total=sum/average
print(total)

# import sys

# # Get command-line arguments excluding the script name
# values = sys.argv[1:]

# # Convert the strings to integers
# values = [int(x) for x in values]

# # Calculate the sum
# sum_values = sum(values)

# # Calculate the average
# average = sum_values / len(values)

# print("The average is:", average)
