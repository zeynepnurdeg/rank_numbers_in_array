def arrayRankTransform(arr):
    temp = sorted(arr)

    ranks_of_nums = {}
    rank = 1

    for num in temp:
        if num not in ranks_of_nums:
            ranks_of_nums[num] = rank
            rank += 1

    return [ranks_of_nums[i] for i in arr]

array = []
while True:
    number = int(input("Enter an integer number (enter a negative number to stop): "))
    if number >= 0:
        array.append(number)
    else:
        break

print(arrayRankTransform(array))