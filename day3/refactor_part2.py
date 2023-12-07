import os
import math
import re

input_file = os.path.join('day3', 'input.txt')
board = list(open(input_file))


# Make a dict where key value was the index of a gear
# then got the edge indices for each number
# if the edges shared a index with a gear, then add the number to symbol dict

gear_dict = {(row, col): [] for row in range(140) for col in range(140)
                            if board[row][col] == '*'}

for row_index, line in enumerate(board):
    for number_match in re.finditer(r'\d+', line):
        edge_set = {(row_ind, col_ind) for row_ind in (row_index-1, row_index, row_index+1)
                                             for col_ind in range(number_match.start()-1, number_match.end()+1)}

        for edge_set_val in edge_set:
            for gear_dict_key in gear_dict.keys():
                if edge_set_val==gear_dict_key:
                    gear_dict[gear_dict_key].append(int(number_match[0]))

print(sum(math.prod(gear_parts) for gear_parts in gear_dict.values() if len(gear_parts)==2))
