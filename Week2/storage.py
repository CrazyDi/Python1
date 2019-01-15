import os
import tempfile

import argparse

import json

## разбираемся с аргументами
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="the key")
parser.add_argument("--value", help="the value")
args = parser.parse_args()

## наше хранилищщщщщщщщщщще
keyvalue = dict()

## файл
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if os.path.exists(storage_path):
    ## открываем
    with open(storage_path, 'r') as f:
        ## читаем сразу в строку
        keyvalue = json.load(f)

## если значение не ввели, выводим значение по ключу
if args.value is None:
    print(keyvalue[args.key])
## если ввели, добавляем по ключу
else:
    if args.key in keyvalue:
        keyvalue[args.key] = keyvalue[args.key] + ', ' + args.value
    else:
        keyvalue[args.key] = args.value

    with open(storage_path, 'w') as f:
        json.dump(keyvalue, f)




