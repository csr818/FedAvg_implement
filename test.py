import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ints', default=10, type=int, nargs='?')
args = parser.parse_args([])
print(args.ints)
