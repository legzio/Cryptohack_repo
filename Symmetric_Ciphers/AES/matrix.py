from typing import Text


def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
   
    return ''.join(map(chr,(matrix[0]+matrix[1]+matrix[2]+matrix[3])))
   


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

#print(matrix[0]+matrix[1]+matrix[2]+matrix[3])
print(matrix2bytes(matrix))
#print(bytes2matrix('tekst wejsciowy'))

