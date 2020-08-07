def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(length):
        cache[weights[i]] = i

    for index, weight in enumerate(weights):
        weight_list = limit - weight

        if weight_list in cache:
            i = cache[weight_list]

            return (index, i) if index > i else (i, index)