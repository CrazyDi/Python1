import sys
num_steps = 5 ##int(sys.argv[1])
step = '#'
space = ' '

for i in range(num_steps):
    print(space * (num_steps - i + 1) + step * (i + 1))