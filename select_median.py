"""
file: store_location.py
author: Ryan Nowak

purpose: gets file from user and calculates the median, total distance
from median, and time to compute
"""

import tools
import time


def quick_select(lst, k):
    """
    uses the quick select algorithm to find the kth smallest element
    in a list of unsorted numbers

    :param lst: list of unsorted numbers
    :param k: kth smallest element
    :return: returns the value of the kth smallest element
    """
    if not len(lst) == 0:
        pivot = lst[len(lst) // 2]
        smallerList = []
        for i in lst:
            if i < pivot:
                smallerList.append(i)
        largerList = []
        for i in lst:
            if i > pivot:
                largerList.append(i)
        count = 0
        for i in lst:
            if i == pivot:
                count += 1
        m = len(smallerList)

        if m <= k < m + count:
            return pivot
        elif m > k:
            return quick_select(smallerList, k)
        else:
            return quick_select(largerList, k-m-count)


def main():
    """
    Gets file name from user, creates a list of numbers from the file,
    and determines the median from the list. Then prints the median, sum
    of distances from median, and time to compute.
    """
    fileName = input('Enter data file: ')
    lst = tools.read_file(fileName)

    start = time.perf_counter()
    if len(lst)%2 == 0:
        median1 = quick_select(lst, len(lst)//2)
        median2 = quick_select(lst, (len(lst)//2)-1)
        median = (median1 + median2) / 2
    else:
        median = quick_select(lst, len(lst) // 2)
    total_distances = tools.find_distance(lst, median)
    elapsed = time.perf_counter() - start

    print('Optimum new store location: ', median)
    print('Sum of distances to the new store: ', total_distances, '\n')
    print('elapsed time : ', elapsed)


if __name__ == '__main__':
    main()
