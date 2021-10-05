state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
   
    return ''.join(map(chr,(matrix[0]+matrix[1]+matrix[2]+matrix[3])))

def add_round_key(s, k):
    
    state_res=state
    for i in range(0,4):
        for j in range(0,4):
            state_res[i][j]=state[i][j] ^ round_key[i][j]
            #print(round_key[0][0])
    return state_res


print(matrix2bytes(add_round_key(state, round_key)))

