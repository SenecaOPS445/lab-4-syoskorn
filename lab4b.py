#!/usr/bin/env python3

def join_lists(l1, l2):
    """Return a list that contains every unique value from both l1 and l2."""
    combined_set = set(l1).union(set(l2))  # Use set to remove duplicates and union to combine
    return list(combined_set)  # Convert the set back to a list

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return list(set(l1).intersection(l2))

def diff_lists(l1, l2):
    """Return a list that contains all different values, which are not shared between the lists."""
    # Convert lists to sets to use symmetric_difference
    set1 = set(l1)
    set2 = set(l2)
    result_set = set1.symmetric_difference(set2)  # Get symmetric difference
    return list(result_set)  # Convert set back to list

if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
