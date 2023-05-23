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
    elif arr[0] >= arr[1]:
        return arr[0]
    elif arr[-1] >= arr[-2]:
        return arr[-1]
    else:
        for i in range(0, length):
            ''' checks if it a peak to its neighbors '''
            element = arr[i]
            if i == 0:
                if element >= arr[i+1]:
                    return element
            elif i == length - 1:
                if element >= arr[i-1]:
                    return element
            elif element >= arr[i-1] and element >= arr[i+1]:
                return element
        
