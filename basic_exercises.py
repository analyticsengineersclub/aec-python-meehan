# Write a loop that uses while instead of the built-in looping structure
x = 1
while x < 6:
    print(x)
    x += 1

# Write a loop that loops over the keys in a dictionary and prints the values
co_14ers = {'elbert': 14433, 'antero': 14269, 'la plata': 14336, 'crestone needle': 14197}
for mountain in co_14ers:
    print(mountain + ' = ' + f"{co_14ers[mountain]}" + ' ft')

# Define is_odd & is_even functions
def is_odd(x):
    if x%2 == 1: return True
    else: return False

def is_even(y):
    if y%2 == 0: return True
    else: return False

# Loop over my_first_list
# Print the square of the value if it is a number
# Print the calories of the fruit if it’s a fruit
# (hint: use the dictionary to look up the calories)
my_first_list = ['apple', 1, 'banana', 2]
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for i in my_first_list:
    if type(i) == int or type(i) == float:
        print(i**2)
    elif type(i) == str:
        print(cal_lookup[i])
    else:
        print("the input value is not of type int, float, or string")

# Write a function that:
    # Takes a dictionary as an argument
    # Loops over the keys in the dictionary
    # Prints the square of the value
def sq_dict(**kwargs):
    for key, value in kwargs.items():
        print(key + ' = ' + f"{value**2}")