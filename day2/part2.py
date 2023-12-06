
import os
import re
def main():
    '''Given an input of games
        For each game
            find the fewest number of cubes needed for each color
            Then multiply these fewest number of cubes for each color to form the "power"
        Return the sum of all powers
        
    '''
    
    input_file = os.path.join('day2', 'input.txt')

    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines = f.readlines()
        ret_sum: int = 0
        for line in lines:
            # game_id: int = int(re.findall("(?<=Game )\\d+", line))
            
            all_greens: list[str] = re.findall("\\d+(?= green)", line)
            all_greens: list[int] = [ int(x) for x in all_greens]
            max_green:int = max(all_greens)
            
            all_red: list[str] = re.findall("\\d+(?= red)", line)
            all_red: list[int] = [ int(x) for x in all_red]
            max_red:int = max(all_red)
            
            all_blue: list[str] = re.findall("\\d+(?= blue)", line)
            all_blue: list[int] = [ int(x) for x in all_blue]
            max_blue:int = max(all_blue)
            
            power = max_green * max_red * max_blue
            
            ret_sum += power
            
        print(ret_sum)

if __name__ == "__main__":
    main()

