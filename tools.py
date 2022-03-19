"""
file: tools.py
author: Ryan Nowak

purpose: contains functions to read data from a file and another
to calculate total distance from median to every other number
"""

def read_file(fileName):
    """
    opens the given file and makes a list of numbers from the data in
    the file

    :param fileName: name of the file to open
    :return: list of unsorted numbers from the file
    """
    lst = []
    for line in open(fileName):
        words = line.split()
        for i in words:
            if i[0].isdigit():
                lst.append(float(i))
    return lst


def find_distance(lst, med):
    """
    takes the median and finds the total distance from the median to
    every other element in the list

    :param lst: unsorted list of numbers
    :param med: median value from the list of numbers
    :return: total distance of median from every other number
    """
    total_dist = 0
    for i in lst:
        total_dist += abs(med - i)
    return total_dist
