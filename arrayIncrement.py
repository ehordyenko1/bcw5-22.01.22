def increment(array):
    new_arr = []

    for i in array:
        new_arr.append(i+1)

    return new_arr



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    arr = increment(arr)

    print(arr)