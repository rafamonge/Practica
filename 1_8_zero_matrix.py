# %%

import numpy as np


# %%
sample_mat = np.random.randint(-20,20,(5,5))
sample_mat[3,2] = 0
sample_mat[1,1] = 0


def zero_mat(mat):
    pos = []    
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j] == 0:
                pos.append((i,j))
    for (row, col) in pos:
        for j in range(mat.shape[1]):
            mat[row,j] = 0
        for i in range(mat.shape[0]):
            mat[i,col] = 0

def zero_mat_set(mat):
    row_set = set()
    col_set = set()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j] == 0:
                row_set.add(i)
                col_set.add(j)
    for row in row_set:
        for j in range(mat.shape[1]):
            mat[row,j] = 0
    for col in col_set:            
        for i in range(mat.shape[0]):
            mat[i,col] = 0


# %%
# %%
# %%
# %%