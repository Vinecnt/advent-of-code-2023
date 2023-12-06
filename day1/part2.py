import os


def main():
    '''
        for each line in the input txt
            replace the string version of numbers to digits
                ***account for insidious behavior twone->21 not twone->tw1 or 2ne
                ***tip from online replace one with one1one to get around words tail end each other
            get only the digits from the line
            get the string consistent of the first and last number from the filtered line
            add to sum
    '''

    input_file = os.path.join('day1', 'input.txt')

    def replace_text_digit(line: str) -> str:
        '''replace numeric text with the numeric version sandwhiched in between'''
        filtered_line = line
        filtered_line = filtered_line.replace("one", "one1one")
        filtered_line = filtered_line.replace("two", "two2two")
        filtered_line = filtered_line.replace("three", "three3three")
        filtered_line = filtered_line.replace("four", "four4four")
        filtered_line = filtered_line.replace("five", "five5five")
        filtered_line = filtered_line.replace("six", "six6six")
        filtered_line = filtered_line.replace("seven", "seven7seven")
        filtered_line = filtered_line.replace("eight", "eight8eight")
        filtered_line = filtered_line.replace("nine", "nine9nine")

        return filtered_line

    with open(input_file, encoding='utf-8',  mode='r') as f:
        lines = f.readlines()
        ret_sum: int = 0
        for line in lines:
            filter_line = replace_text_digit(line.strip())
            filter_line = list(filter(lambda x: x.isdigit(), filter_line))
            if len(filter_line) != 0:
                calibration_value: str = filter_line[0] + filter_line[-1]
                ret_sum += int(calibration_value)
                # print(ret_sum)
        print(ret_sum)


if __name__ == "__main__":
    main()
