# calc.py

import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator")

# Add subparser in order to handle differentn commands
subparsers = parser.add_subparsers(help = "sub-command help", dest = "command")

# Add function as a subparser
add = subparsers.add_parser("add", help = "add integers")
# Add argument for add subparser
add.add_argument("ints_to_sum", nargs=2, type=int)

sub = subparsers.add_parser("sub", help = "subtract integers")
sub.add_argument("ints_to_subtract", nargs=2, type=int)

args = parser.parse_args()

# Print command output
if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"the sum of values is: {our_sum}")

if args.command == "sub":
    our_sub = args.ints_to_subtract[0] - args.ints_to_subtract[1]
    print(f"the difference between values is: {our_sub}")