#!/usr/bin/python3
'''
function that finds a peak in a list of unsorted integers
'''


def find_peak(arr):
    '''
        find peak in arr
    '''

    length = len(arr)
    if length == 0:
        return None
    elif length == 1:
        return arr[0]
    elif length == 2:
        return arr if arr[0] > arr[1]: arr[0] else arr[1]
    else:
        peak = arr[0]
        for i in range(1, length):
            if peak > arr[i]:
                peak = arr[i]
        return peak
