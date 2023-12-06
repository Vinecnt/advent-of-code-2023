
import os
import re
def main():
    '''Given a 2D array of numbers and symbols where '.' are spaces
    Find all numbers with adjecent symbols and sum them
    
    For each line
        For each number in the line
            For each index in the number
                Look around up 8 adjecent spaces
                If a symbol is found
                    Include number to added sum
            Add number to sum
    Return sum
    '''
    
    input_file = os.path.join('day3', 'input.txt')
    
    def is_adjacent_symbol(lines: list[str], row_index: int, start_index, end_index) -> bool:
        '''Given a 2D array
        Return true if true to any of the following
            lines[row_index-1][start_index-1] to lines[row_index-1][end_index+1] contains a symbol
            lines[row_index][start_index-1] contains a symbol
            lines[row_index][start_index+1] contains a symbol
            lines[row_index+1][start_index-1] to lines[row_index+1][end_index+1] contains a symbol
        '''
        ret_bool = False
        
        above_line: str = lines[max(row_index-1,0)][max(start_index-1,0):min(end_index+1, len(lines[0])-1)]
        if len(re.sub(r"\d|\.", "",above_line)) > 0:
            ret_bool = True
        
        try:
            side_line_left: str = lines[row_index][start_index-1]
            if len(re.sub(r"\d|\.", "",side_line_left)) > 0:
                ret_bool = True
        except IndexError:
            pass
        
        try:
            side_line_right: str = lines[row_index][end_index]
            if len(re.sub(r"\d|\.", "",side_line_right)) > 0:
                ret_bool = True
        except IndexError:
            pass
        
        below_line: str = lines[min(row_index+1,len(lines)-1)][max(start_index-1,0):min(end_index+1, len(lines[0])-1)]
        if len(re.sub(r"\d|\.", "",below_line)) > 0:
            ret_bool = True
            
        return ret_bool
            

    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines: list[str]= f.readlines()
        lines = [line.strip() for line in lines]
        ret_sum: int = 0
        for row_index, line in enumerate(lines):
            matches = re.finditer("\\d+", line)
            for match in matches:
                num = match[0]
                num_start_index = match.start(0)
                num_end_index = match.end(0)
                if is_adjacent_symbol(lines, row_index, num_start_index, num_end_index):
                    print(num)
                    ret_sum += int(num)
                
        print(ret_sum)

if __name__ == "__main__":
    main()

