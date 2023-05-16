import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis=0):
    array1 = array1.squeeze()
    array2 = array2.squeeze()
    try:
        array3 = np.append(array1, array2)
        print(array3)
    except:
        raise TypeError("The combination is not possible.")
    return array3


if __name__ == "__main__":
    pass

