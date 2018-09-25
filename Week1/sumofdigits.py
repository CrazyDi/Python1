import sys

digit_string = sys.argv[1]

digit_sum = 0

for letter in digit_string:
    digit_sum = digit_sum + int(letter)

print(digit_sum)

