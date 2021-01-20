#Defining object references
numbers = []
sum = 0
count = 0
lowest = 0
highest = 0
median = 0

#A loop for iterating requests for integer inputs and determining highest/lowest values
while True:
    char = input("Type integers followed by enter, or just enter to finish: ")
    if char:
        try:
            number = int(char)
        except ValueError as err:
            print(err)
            continue
        sum += number
        if count == 0:
            lowest = number
        else:
            if number < lowest:
                lowest = number
        if count == 0:
            highest = number
        else:
            if number > highest:
                highest = number
        numbers.append(number)
        count +=1
    else:
        break

#Only apply the following calculations if valid input has been received
if count:
    #A selection sort applied to the list of inputted numbers to order from lowest to highest
    sorted = []
    while numbers:
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number
        sorted.append(smallest)
        numbers.remove(smallest)

    #A calculation of the median from the sorted number list
    if len(sorted)%2:
        median = sorted[(len(sorted)-1)//2]
    else:
        median = (sorted[(len(sorted)//2)] + sorted[(len(sorted)//2)+1]) / 2
    
    #Output and calculation
    print(" sorted = ", sorted)
    print("count = ", count, " sum = ", sum, "lowest = ", lowest,
        "highest = ", highest, " mean = ", sum/count, " median = ",
        median)