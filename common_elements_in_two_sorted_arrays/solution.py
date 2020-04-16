
def common_elements(list1, list2):
    """common elements between two sorted arrays

    Arguments:
        list1 sorted array
        list2 sorted array

    Returns:
        array with common elements
    """
    result = []

    visited_elements = []

    for item in list1:
        index = len(visited_elements)
        while index < len(list2):
            if(item >= list2[index]):
                visited_elements.append(list2[index])
            if(item == list2[index]):
                result.append(list2[index])
                break
            index += 1
            pass
        pass

    return result


def common_elements_pro(list1, list2):
    pointer1 = 0
    pointer2 = 0

    result = []

    while pointer1 < len(list1) and pointer2 < len(list2):
        if(list1[pointer1] == list2[pointer2]):
            result.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        if(list1[pointer1] > list2[pointer2]):
            pointer2 += 1
        else:
            pointer1 += 1
    return result
