num = int(input("Son kiriting: "))
numbers = [2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9]

def lst(numbers, num):
    a = 0

    for x in numbers:
        if x == num:
            a += 1

    return a


print(lst(numbers, num))
