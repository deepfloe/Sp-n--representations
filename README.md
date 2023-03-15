# Sp-n--representations
A python programme to compute the weights of the tensor product of two representations V_1,V_2 of the compact group Sp(n).

## Background
The representations V_1 and V_2 can be the k-th symmetric power or the primitve k-forms on C^(2n). The algorithm to achieve that is an implementation of p.83 of Simon Salamon's book "Riemannian Geometry and Holonomy Groups", which he summarised in Fig 6.5:

<img src="https://user-images.githubusercontent.com/53785628/225397576-f8951962-4a1c-4486-9178-4aca73b48c18.png"  width="60%" height="60%">

## How to use
The file `tensor_reps.py` contains the class `Spn_rep`. The attributes are rank, degree, tensor_type. The rank of Sp(n) is n, the degree of the k symmetric power or primitive k forms is k. The tensor type can be 'primitive','antisymmetric' or 'symmetric'. The key function is `tensor_weights(rep1,rep2)`, taking two instances of Spn_rep, the output is a dictionary of the weights of the tensor representation as keys and the multiplicities as values.

## Example 
Compute the weights of the tensor product of the symmetric powers S^2 \otimes S^2 as Sp(2) representations
rep1 = Spn_rep(rank= 2, degree = 2, tensor_type='symmetric')
rep2 = Spn_rep(rank= 2, degree = 2, tensor_type='symmetric')

{(4, 0): 1, (2, 0): 1, (3, 1): 1, (0, 0): 1, (1, 1): 1, (2, 2): 1}
The result agrees with Salamon's computation on p. 84
