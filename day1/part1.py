# for each line in the input txt
#   get only the digits from the line
#   get the string consistent of the first and last number from the filtered line
#   add to sum
with open('input.txt') as f:
    lines = f.readlines()
    ret_sum: int = 0
    for line in lines:
        filter_line = list(filter(lambda x: x.isdigit(), line))
        if len(filter_line) != 0:
            calibration_value: str = filter_line[0] + filter_line [-1]
            ret_sum += int(calibration_value)
    print(ret_sum)