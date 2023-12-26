def findRunner():
    arr = [2, 3, 6, 6, 5]
    maximum = max(arr)
    second = []

    for n in arr:
        if n < maximum:
            second.append(n)

   
    second_largest = max(second)
    print(second_largest)

findRunner()


    
