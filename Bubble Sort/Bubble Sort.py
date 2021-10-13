array = input('Enter an array of number: num1 num2 num3 etc. ').split(" ")
iteration_max = len(array)
while iteration_max > 0:
    pos, iterations = 0, 1
    while iterations < iteration_max:
        num0, num1 = int(array[pos]), int(array[pos+1])
        if num0 <= num1:
            pass
        else:
            array[pos+1], array[pos] = array[pos], array[pos+1]
        pos, iterations = pos+1, iterations+1
    iteration_max -= 1
print(f"The sorted array is: {array}")