def is_rotation(list1, list2):
    pointer = 0
    pointer2 = 0

    if len(list1) != len(list2):
        return False

    while pointer2 < len(list2):
        if(list2[pointer2] == list1[pointer]):
            pointer += 1
            pointer2 += 1
            if(pointer >= len(list1)):
                pointer = 0
        else:
            pointer += 1
        if(pointer >= len(list1)):
            return False
    return True
