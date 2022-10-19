from Spn_functions import *
class Spn_rep:
    '''A class to represent a representation of the group Sp(n). The representations currently implemented are primitive k-forms and symmetric powers.
    Attributes:
        rank(int) = n: the dimension of the max torus of Sp(n)
        degree(int): degree of the tensor power we consider, ie degree(Sym^k) = k
        tensor_type(str): can be symmetric, antisymmetric or primitive
    '''
    def __init__(self,rank,degree,tensor_type):
        ## check for errors ##
        allowed_types = ['primitive', 'symmetric', 'antisymmetric']
        if tensor_type not in allowed_types:
            raise ValueError('The tensor type must be symmetric, primitve or antisymmetric')

        if degree>rank and tensor_type!='symmetric':
            raise ValueError('The algorithms are only tested if degree<=rank')

        ## assign attributes to newly created object ##
        self.tensor_type = tensor_type
        self.rank = rank
        self.degree = degree

    def highest_weight(self):
        '''Return the highest vector of a representation'''
        n = self.rank
        k = self.degree
        v = n * [0]
        if self.tensor_type == 'primitive':
            for i in range(0, self.degree):
                v[i] = 1
        if self.tensor_type == 'symmetric':
            v[0] = k
        if self.tensor_type == 'antisymmetric':
            print('The antisymmetric representation is not irreducible')
        return v

    def all_weights(self):
        '''Given a representation, return the full list of weight vectors.'''
        # In the end, we are only interested in the primitive, irreducible representation. However it is worthwhile using the whole antisymmetric space for the computation of primitive forms.
        n = self.rank
        k = self.degree
        if k < 0:
            return []
        if k == 0:
            return [n * [0]]
        if self.tensor_type == 'antisymmetric':
            multi_indices = increasing_indices(length=k, start=0, end=2 * n, strictly=True)

        if self.tensor_type == 'primitive':
            rep1 = Spn_rep(n,k,tensor_type='antisymmetric')
            rep2 = Spn_rep(n,k-2,tensor_type='antisymmetric')
            return substract_lists(rep1.all_weights(),rep2.all_weights())

        if self.tensor_type == 'symmetric':
            multi_indices = increasing_indices(length=k, start=0, end=2 * n, strictly=False)
        return [sum_over_indexlist(fund_generators(n), index) for index in multi_indices]

def tensor_weights(rep1,rep2):
    '''Return the weights of the tensor representation of rep1 and rep2
    Args:
        rep1, rep2: objects of type Spn_rep, ie. Sp(n) representations
    Returns:
         list of integer-valued vectors, representing the weights of the tensor product rep
    Errors:
        assertion error if the rank of rep1 and rep2 don't match
    '''

    assert rep1.rank == rep2.rank

    n = rep1.rank
    weights_1 = rep1.all_weights()
    weight_2 = rep2.highest_weight()
    combined_weights = [add_vec(w,weight_2) for w in weights_1]

    final_weights={}
    for w in combined_weights:
        if in_weyl(w):
            add_to_dict(final_weights,w,1)
        else:
            w = add_vec(w,d(n))
            if in_weyl(w) == False:

                w, sign = weyl_projection(w)
                if in_weyl(w) != 'boundary':
                    w=substr_vec(w,d(n))
                    add_to_dict(final_weights, w, sign)
    return final_weights

if __name__ == '__main__':
    rep1 = Spn_rep(degree = 2, rank= 2, tensor_type='symmetric')
    rep2 = Spn_rep(degree = 2, rank= 2, tensor_type='symmetric')
    print(tensor_weights(rep1,rep2))


