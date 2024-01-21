if __name__ == '__main__':
    n = int(input())  
    arr = list(map(int, input().split()))  

    def runner(arr):
        maximum = max(arr)
        second = []
        for i in arr:
            if i < maximum:
                second.append(i)
        print(max(second))

    runner(arr) 