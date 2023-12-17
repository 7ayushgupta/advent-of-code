inputs_dir = '/Users/ayushgupta/Projects/advent-of-code/2023/inputs/'
input_file = 'day1_input.txt'

with open(inputs_dir + input_file) as fh:
    inputs = fh.read()

inputs = inputs.split('\n')
print(len(inputs))

#######

DIGIT_MAPPING = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

###### Part 1

import regex as re

sum_ = 0
for input_ in inputs:
    numbers_ = [x for x in input_ if x.isdigit()]
    number_ = int(numbers_[0] + numbers_[-1])
    sum_ += number_

print(sum_)

###### Part 2

sum_ = 0
numbers_array = []
for input_ in inputs:
    positions_ = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", input_, overlapped=True) # funny that original re library doesn't support overlapped, hence needed to install this else I would have hit my head
    numbers_ = [DIGIT_MAPPING[x] for x in positions_]
    number_ = int(numbers_[0] + numbers_[-1])
    sum_ += number_

print(sum_)