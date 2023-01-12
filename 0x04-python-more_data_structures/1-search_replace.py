#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        new_item = item
        if item == search:
            new_item = replace
        new_list.append(new_item)
    return new_list
