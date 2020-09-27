import argparse
def say_hello(melfer="World"):
 print("Hello ", melfer, "!")
parser = argparse.ArgumentParser(description='Say hello.')
parser.add_argument('--melfer', type=str, required=False,
 metavar='melfer', help='your melfer', default='World')
args = parser.parse_args()
say_hello(args.melfer)