##import os
##import tempfile

##storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
##with open(storage_path, 'w') as f:

import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))