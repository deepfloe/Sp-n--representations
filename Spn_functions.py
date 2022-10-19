from auxiliary_functions import *

def weyl_projection(weight):
    '''Projection of a weight vector into the fundamental Weyl chamber. Returns a sign, which is positive if the number of hyperplane projections was even
    Args:
        weight: list of integers
    Returns:
        list of integers, integer
    '''
    n = len(weight)
    weight, sign1 = abs_signed(weight)
    weight, sign2 = bubble_sort_signed(weight)
    return weight, sign1*sign2

def d(n):
    '''Return the vector d in Salamon's notation. In the case of Sp(n) this is simply (n,..,1)'''
    return [n-i for i in range(n)]


def fund_generators(n):
    '''Given input n, return the list of weight vectors for the basic representation of Sp(n) on C^2n'''
    generators = []
    for i in range(0, n):
        v = n*[0]
        w = n*[0]
        v[i] = 1
        w[i] = -1
        generators.append(v)
        generators.append(w)

    return generators

def in_weyl(weight):
    '''Check whether a weight vector lies in the fundamental Weyl chamber. Returns True if lies in the interior, and 'boundary' if on the boundary.
    Args:
        weight: list of integers
    Returns:
        Boolean or string
    '''
    n=len(weight)
    weight=weight+[0]
    # we avoud weight.append(0) as this manipulates the local variable weight
    #weight=np.append(weight,0)
    boundary = False
    for i in range(0,n):
        if weight[i] < weight[i+1]:
            return False
        if weight[i] == weight[i+1]:
            boundary=True
    if boundary:
        return 'boundary'
    else:
        return True








