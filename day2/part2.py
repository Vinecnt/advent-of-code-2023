
import os

def main():
    ''''''
    
    input_file = os.path.join('day2', 'input.txt')

    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines = f.readlines()
        ret_sum: int = 0
        for line in lines:
            game_str: str = line.split(":")[0]
            game_id = int(game_str.split(" ")[1])
           
            
            
        print(ret_sum)

if __name__ == "__main__":
    main()

