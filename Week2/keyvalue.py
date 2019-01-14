import os
import tempfile

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="the key")
parser.add_argument("--value", help="the value")
args = parser.parse_args()

if args.value is None:
    print(1)
else:
    print(2)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f: