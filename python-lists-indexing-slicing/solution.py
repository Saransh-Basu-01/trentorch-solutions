def replace_middle(lst: list, new_items: list) -> None:
    """
    Mutate `lst` in place so that its first and last elements are
    kept and every element between them is replaced by the
    elements of `new_items` (in order). Use slice assignment.
    If `lst` has fewer than 2 elements, do nothing.
    Return nothing.

    Example: lst = [1, 2, 3, 4]; replace_middle(lst, ["x"])
             -> lst is now [1, "x", 4]
    """
    l=[]
    if len(lst)<2:
        return lst
    else:
        # l.append(lst[0])
        # for i in new_items:
        #     l.append(i)
        # l.append(lst[-1])
        # return lst
        lst[1:-1]=new_items
        return lst
        


def set_every_other(lst: list, value) -> None:
    """
    Mutate `lst` in place so that the elements at positions
    0, 2, 4, ... are all replaced by `value`. Use extended slice
    assignment. Return nothing. An empty list is left empty.

    Example: lst = [1, 2, 3, 4, 5]; set_every_other(lst, 0)
             -> lst is now [0, 2, 0, 4, 0]
    """
    # l=[]
    # for i in range(len(lst)):
    #     if i%2==0:
    #         l.append(value)
    #     else:
    #         l.append(lst[i])
    # return lst
    lst[::2]=[value]*len(lst[::2])
    return lst

def slice_copy(lst: list, start: int, stop: int) -> list:
    """
    Return a NEW list containing the elements of `lst` from
    position `start` up to but not including `stop`. Do not
    modify `lst`.
    """
    l=[]
    l=lst[start:stop]
    return l
