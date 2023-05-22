'''So this program is technically designed to get names in a 
list and distribute them to different individuals in another list.
Kind of like 10 names divided by 2 people or 3 etc.'''

# FIRST PART: THE DISTRIBUTED
import random
# Empty list
mynames = []
user_input = int(input("How many names do you have: "))
''' Getting the names from user and adding them to
empty list'''


for num in range(0, user_input):
    names = input("Enter name " + str(num) + " : \n")
    mynames.append(names)
print(mynames)
print('-'*50)
print("\n")

# SECOND PART: THE DISTRIBUTEES
paragons = []
paragon_input = int(input("How many to distribute to: "))

for name in range(0, paragon_input):
    dist_name = input("Enter name " + str(name) + " : \n")
    paragons.append(dist_name)

# THIRD PART: ACTUAL DISTRIBUTION 
random.shuffle(mynames)
''' we need a number for the elements to be displayed
in the slices below at line 34'''
Result = int(len(mynames) / len(paragons))
for i in range(paragon_input):
    # Slices of the mynames list named dist
    dist = mynames[i*Result : (i+1)*Result]
# Empty Dictionary
mapper = {}
# Adding the dist slices into the empty dictionary
for i, item in enumerate(paragons):
    mapper[item] = [dist]
print('-'*50)
print("\n")
print(mapper)