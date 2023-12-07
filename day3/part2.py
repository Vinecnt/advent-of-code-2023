
import os
import re

def main():
    '''Given a 2D array of numbers and symbols where '.' are spaces
    Find all gears (* symbol) with exactly two adject gear numbers
    Gear ratio is those two numbers multiplied. Sum all gear ratios.
    
    For each line
        For each gear in the line
            Check up it's 8 adjacent cells
            If there are exactly two gear numbers
                Find those two numbers
                Get gear ratio by multiplying those two numbers
                Add gear ratio to sum
    Return sum
    '''
    input_file = os.path.join('day3', 'input.txt')
    
    def find_number(line: str, num_index) -> int:
        '''Given a line, and an index of a number, find the larger number this number is part of'''
        left_splice_index = max(line.rfind("*", 0, num_index),line.rfind(".", 0, num_index))
        
        first_right_gear = line.find("*",num_index)
        first_right_period = line.find(".",num_index)
        
        right_splice_index = None
        if first_right_gear != -1 and first_right_period != -1:
            right_splice_index = min(first_right_gear, first_right_period)
        elif first_right_period != -1:
            right_splice_index = first_right_period
        elif first_right_gear != -1:
            right_splice_index = first_right_gear
        
        num = line[left_splice_index+1:right_splice_index]
        
        return num

    
    def find_parts(lines: list[str], row_index:int, adjacent_cells: str, line_start_index:int, line_end_index:int, cells_side:str) -> (int,list[str]):
        '''Given a 2D lines,
            Find the number of parts 
                If looking at the top and bottom adjacent cells
                    Possible configurations and scores
                        len of 2
                            ".." 0 parts
                            "1." 1 part
                            ".1" 1 part
                            "11" 1 part
                        len of 3
                            "..." 0
                            "1.." 1 part
                            ".1." 1 part
                            "..1" 1 part
                            "11." 1 part
                            ".11" 1 part
                            "1.1" 2 parts
                            "111" 1 part
                If looking at the left and right cells
                    if there is number, then respectively increase count
        '''
        found_parts_count = 0
        found_parts_number= []
        if cells_side == "top" or cells_side == "bottom":
            found_parts = list(re.finditer("\\d+", adjacent_cells))
            found_parts_count += len(found_parts)
            
            for found_part in found_parts:                
                found_parts_number += [find_number(lines[row_index], line_start_index+found_part.start())]
        if cells_side == "left" or cells_side == "right":
            found_parts = list(re.finditer("\\d+", adjacent_cells))
            found_parts_count += len(found_parts)
            
            for found_part in found_parts:                
                found_parts_number += [find_number(lines[row_index], line_start_index+found_part.start())]




            

                
                
                
        return found_parts_count, found_parts_number
    
    def find_gear_ratio(lines: list[str], row_index: int, gear_index: int) -> int:
        '''Given a 2D array 
        Run a total count of adjacent part numbers
        Increment count depending on the up 8 cells around the gear
        If a adjacent part is found, increment counter and record the number
        
            
        If the counter == 2
            multiply the record record numbers and return their product
        else
            return 0
        '''
        adjacent_parts_count: int = 0
        part_numbers = []
        ret_product:int = 0
    
        # top cells
        if row_index-1 >= 0: 
            line_start_index: int = max(gear_index-1,0)
            line_end_index:int = min(gear_index+2, len(lines[0])-1)
            top_adjacent_cells:str = lines[row_index-1][line_start_index:line_end_index]
            found_part_count,found_part_numbers = find_parts(lines, row_index-1,top_adjacent_cells, line_start_index, line_end_index, cells_side="top")
            adjacent_parts_count += found_part_count
            part_numbers += found_part_numbers
            
        # bottom cells
        if row_index+1 <= len(lines[0]):
            line_start_index: int = max(gear_index-1,0)
            line_end_index: min(gear_index+2, len(lines[0])-1)
            bottom_adjacent_cells:str = lines[row_index+1][line_start_index:line_end_index]
            found_part_count,found_part_numbers = find_parts(lines, row_index+1, bottom_adjacent_cells, line_start_index, line_end_index, cells_side="bottom")
            adjacent_parts_count += found_part_count
            part_numbers += found_part_numbers
        
        # left cell
        if gear_index - 1 >= 0:
            line_start_index: int = max(gear_index-1,0)
            line_end_index: int = line_start_index+1
            left_adjacent_cells:str = lines[row_index][line_start_index:line_end_index]
            found_part_count,found_part_numbers = find_parts(lines, row_index, left_adjacent_cells, line_start_index, line_end_index, cells_side="left")
            adjacent_parts_count += found_part_count
            part_numbers += found_part_numbers
            
        # right cell
        if gear_index + 1 <= len(lines[0]):
            line_start_index: int = gear_index+1
            line_end_index:int = line_start_index+1
            right_adjacent_cells:str = lines[row_index][line_start_index:line_end_index]
            found_part_count,found_part_numbers = find_parts(lines, row_index, right_adjacent_cells, line_start_index, line_end_index, cells_side="right")
            adjacent_parts_count += found_part_count
            part_numbers += found_part_numbers
            
        if adjacent_parts_count == 2:
            print(part_numbers)
            ret_product = int(part_numbers[0]) * int(part_numbers[1])
        
        return ret_product
    
    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines: list[str]= f.readlines()
        lines = [line.strip() for line in lines]
        ret_sum: int = 0
        for row_index, line in enumerate(lines):
            matches = re.finditer("\*", line)
            for match in matches:
                gear_index = match.start(0)
                    
                gear_ratio = find_gear_ratio(lines, row_index, gear_index)
                if gear_ratio > 0:
                    ret_sum += gear_ratio
                
        print(ret_sum)

if __name__ == "__main__":
    main()

