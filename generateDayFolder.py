import argparse
import os

def main(day: int):
    folder = f"day{day}"
    if os.path.exists(folder) is False:
        os.mkdir(folder)
        
        input_file = os.path.join(folder, 'input.txt')
        with open(input_file, 'w', encoding='utf-8') as fp:
            pass
        
        boiler_code = f"""
import os

def main():
    ''''''
    
    input_file = os.path.join('day{day}', 'input.txt')

    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines = f.readlines()
        ret_sum: int = 0
        for line in lines:
            pass
        print(ret_sum)

if __name__ == "__main__":
    main()

"""
        with open(os.path.join(folder, 'part1.py'), 'w', encoding='utf-8') as fp:
            fp.write(boiler_code)

        with open(os.path.join(folder, 'part2.py'), 'w', encoding='utf-8') as fp:
            fp.write(boiler_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="create folder ./day\{n\} where n is the day")
    args = parser.parse_args()
    main(args.day)
