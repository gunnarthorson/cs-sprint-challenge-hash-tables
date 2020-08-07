def intersection(arrays):
    """
    YOUR CODE HERE
    """
    List = []
    cache = {}

    for i in arrays:
        for num in i:
            if num not in cache:
                cache[num] = 1
            else:
                List.append(num)
    List = list(dict.fromkeys(List))

    return List


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
