import random

denoms = list(range(10))
random.shuffle(denoms)

# Debugging Method 1 - print() statements
for i in range(10):
    print(f'i: {i}')
    x = denoms[i]
    print(f'x: {x}')
    result = 100 / x

# Debugging Method 2 - pdb
for i in range(10):
    import pdb; pdb.set_trace()  # pdb = python debugger
    x = denoms[i]
    result = 100 / x

# Debugging Method 3 - 
for i in range(10):
    x = denoms[i]
    try: # try to run below statment
        result = 100 /x  # put the line of code that is failing here        
    except: # if statement in try fails, then drop into debugger
        import pdb; pdb.set_trace()  # debugger goes here

# pdb commands
# l → (list) where in code the debugger is (up to ~11 lines worth)
# ll → lists all source code for current function/frame
# n → runs (next) line
# s → (step) execute current line (differs from next in that it will stop inside a fucnction on the same line)
# c → (continue) on to next instace of debugger
# q → (quit) debugger
