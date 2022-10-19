from tensor_reps import *
import matplotlib.pyplot as plt

def zero_weight(dict):
    ''' Counts how often the zero weight occurs'''
    #We first determine the rank, which is just the length of any key in the dictionary
    key_list = list(dict.keys())
    if len(key_list)==0:
        return 0
    rank = len(key_list[0])
    key = tuple([0]*rank)
    if key in dict:
        return dict[key]
    else:
        return 0
#
n = 10
x_nonzero = []
y_nonzero = []
for i in range(0,n+1):
    for j in range(i,n+1):

        rep1 = Spn_rep(rank=n, degree=i, tensor_type='primitive')
        rep2 = Spn_rep(rank=n, degree=j, tensor_type='primitive')
        if zero_weight(tensor_weights(rep1,rep2))>0:
            x_nonzero.append(i)
            y_nonzero.append(j)

plt.scatter(x_nonzero,y_nonzero)
plt.show()