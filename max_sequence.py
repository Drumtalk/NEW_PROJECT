def max_sequence(arr):
    if arr:
        count = 0
        max = arr[0]
        max_ending = 0
        for i in arr:
            if i < 0: count += 1
            max_ending += i
            if max_ending < 0:
                max_ending = 0
            elif max < max_ending:
                max = max_ending
        if (count == len(arr)): return 0
        else:
            return max
    else:
        return 0


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))