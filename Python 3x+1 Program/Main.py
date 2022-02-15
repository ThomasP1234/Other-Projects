start = 18446744073709551616+2000
tracking = []
while True:
    for i in range(start, start+2000):
        j = i
        print("\nNew i:")
        if j in tracking:
            print(i,'has a loop')
            exit()
        tracking.append(i)
        while j != 1:
            print(j)
            if (j % 2) == 0:
                j = j / 2
            else:
                j = (j*3)+1
        if j == 1:
            print(j)
            print()
    again = input()
    start += 2000