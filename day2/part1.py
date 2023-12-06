
import os

def main():
    '''Given an input file of games, find out which game is possible
    if the game only contained 12 red, 13 green, 14 blue cubes
    
        For each game
            is game possible?
            for each revealed set in the game
                if the number of red,green,blue exceeds 12,13,14 respectively
                    game is impossible, 
            if game possible
                add game id to total sum
        return total sum
    '''
    
    input_file = os.path.join('day2', 'input.txt')

    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines = f.readlines()
        ret_sum: int = 0
        for line in lines:
            line = line.strip()
            game_str: str = line.split(":")[0]
            game_id = int(game_str.split(" ")[1])
            
            possible_game: bool = True

            # get game in info in a list 
            sets: list(dict) = []
            all_sets_str: str = line.split(":")[1]
            sets_str: list(str) = all_sets_str.split(";")
            for set_info in sets_str:
                set_info = set_info.strip()
                cube_set = {}
                cubes_info: list(str) = set_info.split(",")
                for cube_info in cubes_info:
                    cube_info = cube_info.strip()
                    count, color = int(cube_info.split(" ")[0]),cube_info.split(" ")[1]
                    cube_set[color] = count
                sets.append(cube_set)
                
            for cube_set in sets:
                if 'red' in cube_set and cube_set['red'] > 12:
                    possible_game = False
                elif 'green' in cube_set and cube_set['green'] > 13:
                    possible_game = False
                elif 'blue' in cube_set and cube_set['blue'] > 14:
                    possible_game = False
            
            if possible_game:
                ret_sum += game_id
                
                            
        print(ret_sum)

if __name__ == "__main__":
    main()

