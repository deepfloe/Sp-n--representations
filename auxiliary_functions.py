from functools import reduce

def parity(x: int):
    if x % 2 == 0:
        return 1
    else:
        return -1

def substract_lists(a,b):
    ''' a-b: Substract list b from a, keeping in mind multiplicities. Example: substract_lists([0,0],[0]) == [0]'''
    a_copy = [i for i in a]
    for i in b:
        if i in a_copy:
            a_copy.remove(i)
        else:
            raise ValueError('second list is not contained in first list')
    return a_copy


def add_vec(v1,v2):
    ''' Add the components of two vectors, as we're avoiding numpy '''
    l = len(v1)
    assert l == len(v2)

    return [v1[i]+v2[i] for i in range(l)]

def substr_vec(v1,v2):
    l = len(v1)
    assert l == len(v2)
    return [v1[i]-v2[i] for i in range(l)]

def abs_signed(array):
    ''' Returns the absolute value of all elements in a list and the sign, which is the parity of negative entries in the original list'''
    n_swaps = 0
    l = len(array)
    for i in range(l):
        x = array[i]
        if x<0:
            array[i] = -x
            n_swaps += 1
    sign = parity(n_swaps)
    return array, sign


def bubble_sort_signed(array):
    '''Bubble sort for an array, also returns a sign, which counts the parity of the number of swaps'''
# This is taken from https://realpython.com/sorting-algorithms-python/.

    n = len(array)
    n_swaps = 0
    sign = 1
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]
                n_swaps += 1
                # Since you had to swap two elements, set the `already_sorted` flag to `False` so the algorithm doesn't finish prematurely
                already_sorted = False
        if already_sorted:
            break
        sign = parity(n_swaps)
    return array, sign

def sum_over_indexlist(vec_list, indexlist):
    '''Sum a subset of elements of a list of vectors
    Args:
        vec_list: list of vectors (integer valued lists)
        indexlist: list of integers, the indices to be summed over
    Returns:
        vector (integer valued list)
    '''
    sublist = [vec_list[ind] for ind in indexlist]
    return reduce(add_vec,sublist)


def increasing_indices(length,start,end,strictly):
    '''Return all (strictly) increasing sublists of the interval [start, ind].
    Args:
        length (int): the length of the sublist
        start (int): startpoint of the interval
        end (int): endpoint
        strictly: specify whether indices need to be strictly increasing
    Returns:
        list of lists of integers
    '''
    #Example: increasing_indices(length=2,start=0,end=3,strictly=True)=[[0, 1], [0, 2], [1, 2]]
    index_list=[]
    if end-start<length:
        return []
    for i in range(start,end):
        if length == 1:
            index_list.append([i])
        else:
            if strictly:
                new_start = i+1
            else:
                new_start = i
            for x in increasing_indices(length-1,new_start,end,strictly):
                index_list.append([i] + x)
    return index_list


def add_to_dict(dict,weight,multiplicity):
    '''Add (weight:multiplicity) to a dictionary. If weight already exists, add multiplicities.'''
    weight = tuple(weight)
    if weight in dict:
        new_mult = dict[weight] + multiplicity
        if new_mult ==0:
            del dict[weight]
        else:
            dict[weight] = new_mult
    else:
        dict[weight]=multiplicity

    #no return value since dictionaries are mutable, so the input dict is jsut being updated!



