# A Python module file ‘utils.py’ that defines an average() function
# def average(values):
# # """ Calculates the average of the given list. """
# total = 0
# for n in values: # total the given values
#  total += float(n)
# return total/len(values) # return calculated average
# # initialisation statement
# print("Welcome, utils module has been imported and initialised!")

def average(*values):
    sum=0
    for i in values:
        sum=sum+i
    return sum/len(values)

print("Welcome, utils module has been imported and initialised!")
