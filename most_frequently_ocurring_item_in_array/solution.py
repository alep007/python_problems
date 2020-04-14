def most_frequent(given_list):
    """given an array of numbers create a function that returns the number that
    is repeated the most

    Arguments:
        given_list {[type]} -- an array of numbers

    Returns:
        int: the number that is the most repeated
    """
    max_item = None
    if len(given_list) == 0:
        return max_item

    max_count = -1
    repeated_items = {}

    for item in given_list:
        if item in repeated_items:
            repeated_items[item] += 1
        else:
            repeated_items[item] = 1

        if repeated_items[item] > max_count:
            max_count = repeated_items[item]
            max_item = item
    print(max_item)
    return max_item
