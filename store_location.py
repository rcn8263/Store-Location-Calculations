"""
file: store_location.py
author: Ryan Nowak

purpose: gets file from user and calculates the median, total distance
from median, and time to compute
"""

import quick_sort
import tools
import time


def find_median(lst):
    """
    sorts the given list using quick sort algorithm then finds the median
    from the list

    :param lst: list of unsorted numbers
    :return: median from sorted list
    """
    lst = quick_sort.quick_sort(lst)
    idx = len(lst) // 2
    median = lst[idx]
    if len(lst) % 2 == 0:
        return (lst[idx] + lst[idx-1]) / 2
    else:
        return median


def main():
    """
    Gets file name from user, creates a list of numbers from the file,
    and determines the median from the list. Then prints the median, sum
    of distances from median, and time to compute.
    """
    fileName = input('Enter data file: ')
    lst = tools.read_file(fileName)

    start = time.perf_counter()
    median = find_median(lst)
    total_distances = tools.find_distance(lst, median)
    elapsed = time.perf_counter() - start

    print('Optimum new store location: ', median)
    print('Sum of distances to the new store: ', total_distances)
    print('elapsed time : ', elapsed)


if __name__ == '__main__':
    main()
