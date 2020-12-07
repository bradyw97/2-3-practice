def constrainted_nums(a,b):
    nums = range(a,b)
    filtered_nums = []
    for n in nums:
        if (n % 7 == 0) and (n % 5 != 0):
            print(n)

constrainted_nums(2000,3201)