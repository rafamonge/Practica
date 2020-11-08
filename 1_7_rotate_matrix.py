# Key insighits:
# perform the rotation in concentric squares in order to use O(1) memory
# form a given i, j positoin in the matrix the position to rotate it 90 degress
# is equal to max_mat - j, i
# where max_mat = to the maximum 1 Dimensional  index of the matrix
# note the flipping of i and j
# %%

sample_mat = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"]
    ]

def rotate_90(mat):
    for i in range(int(len(mat[0])/2)):
        swap_concentric(mat, i)
    return mat

def swap_concentric(mat, con):
    for i in range(con, len(mat[0]) - 1- con):
        swap_concentric_pos(mat, con, i)

def swap_concentric_pos(mat, current_i, current_j):
    ((top_i, top_j),
     (left_i, left_j),
     (bottom_i, bottom_j),
     (right_i, right_j),
    ) = get_concentric_pos(mat, current_i, current_j)
    top_v = mat[top_i][top_j]
    mat[top_i][top_j] = mat[left_i][left_j]
    mat[left_i][left_j] = mat[bottom_i][bottom_j]
    mat[bottom_i][bottom_j] = mat[right_i][right_j]
    mat[right_i][right_j] = top_v


def get_concentric_pos(mat, current_i, current_j):
    max_mat = len(mat[0])-1
    current = mat[current_i][current_j]
    (left_i, left_j) = (max_mat- current_j, current_i)
    (bottom_i, bottom_j) = (max_mat- left_j, left_i)
    (right_i, right_j) = (max_mat- bottom_j, bottom_i)
    return (
        (current_i,current_j),
        (left_i,left_j),
        (bottom_i,bottom_j),
        (right_i,right_j)
    )



# %%
