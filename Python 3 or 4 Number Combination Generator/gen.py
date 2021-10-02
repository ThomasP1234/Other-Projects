choice = int(input("3 or 4"))
if choice == 4:
    num1 = int(input("1st num"))
    num2 = int(input("2nd num"))
    num3 = int(input("3rd num"))
    num4 = int(input("4th num"))

    nums = [num1, num2, num3, num4]

    for i in nums:
        for j in nums:
            if i == j:
                continue
            for k in nums:
                if i == k or j == k:
                    continue
                for l in nums:
                    if i == l or j == l or k == l:
                        continue
                    print(i,j,k,l)

else:
    num1 = int(input("1st num"))
    num2 = int(input("2nd num"))
    num3 = int(input("3rd num"))

    nums = [num1, num2, num3]

    for i in nums:
        for j in nums:
            if i == j:
                continue
            for k in nums:
                if i == k or j == k:
                    continue
                print(i,j,k)