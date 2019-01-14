import os
import tempfile

import argparse

import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="the key")
parser.add_argument("--value", help="the value")
args = parser.parse_args()

keyvalue = dict()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if os.stat(storage_path).st_size > 0:
    with open(storage_path, 'r') as f:
        keyvalue = json.load(f)

if args.value is None:
    print(keyvalue[args.key])
else:
    if args.key in keyvalue:
        keyvalue[args.key] = keyvalue[args.key] + ', ' + args.value
    else:
        keyvalue[args.key] = args.value

    with open(storage_path, 'w') as f:
        json.dump(keyvalue, f)


