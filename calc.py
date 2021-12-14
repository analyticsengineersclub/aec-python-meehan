# calc.py

import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator")

# Add subparser in order to handle differentn commands
subparsers = parser.add_subparsers(help = "sub-command help", dest = "command")

# Add function as a subparser
add = subparsers.add_parser("add", help = "add integers")
# Add argument for add subparser
add.add_argument("ints_to_sum", nargs='*', type=int)

sub = subparsers.add_parser("sub", help = "subtract integers")
sub.add_argument("ints_to_subtract", nargs='+', type=int)

def aec_subtract(ints_to_subtract):
    if len(ints_to_subtract) > 2:
        raise Exception("Too many arguments")

        # Raising an exception propogates out of nested scopes until an exception handler is encountered
        # The default except handling by the interpreter is to print an error message and a tracxeback summary for debugging purposes
        # & exit the code
                
    our_sub = ints_to_subtract[0] - ints_to_subtract[1]
    if our_sub < 0:
        our_sub = 0
    print(f"the difference between values is: {our_sub}")
    return(our_sub)

multiply = subparsers.add_parser("multiply", help = "multiply integers")
multiply.add_argument("ints_to_multiply", nargs='+', type=int)

divide = subparsers.add_parser("divide", help = "divide integers")
divide.add_argument("ints_to_divide", nargs='+', type=int)

def aec_divide(ints_to_divide):
    if len(ints_to_divide) > 2:
        raise Exception("Too many arguments")

    if ints_to_divide[1] == 0:
        our_quotient = 0
    else:
        our_quotient = ints_to_divide[0] / ints_to_divide[1]
    print(f"the quotient of values is: {our_quotient}")
    return(our_quotient) 

# Nesting everyythin under this ensures that this code isn't run during tests
# & instead only runs when called on from the CLI
# Without this, an error would be thrown when tests are run because it would be looking for an argument (ie. add, sub, multiply, divide)
if __name__ == "__main__":
    args = parser.parse_args()

    # Print command output
    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"the sum of values is: {our_sum}")

    if args.command == "sub":
        # our_sub = args.ints_to_subtract[0] - args.ints_to_subtract[1]
        # print(f"the difference between values is: {our_sub}")
        aec_subtract(args.ints_to_subtract)

    if args.command == "multiply":
        our_product = args.ints_to_multiply[0]
        for i in args.ints_to_multiply[1:]:
            our_product *= i
        print(f"the product of the values is: {our_product}")

    if args.command == "divide":
        if args.ints_to_divide[1] == 0:
            print("Cannot divide by 0")
        else:
            # our_quotient = args.ints_to_divide[0] / args.ints_to_divide[1]
            # print(f"the quotient of values is: {our_quotient}")
            aec_divide(args.ints_to_divide)