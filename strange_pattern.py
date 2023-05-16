import numpy as np

# implement the function strange pattern

def strange_pattern(n, m):
    base = np.zeros((m * n), dtype=bool)
    base[::3] = 1
    #print(pattern)
    pattern = base[0:m]
    for i in range(n-1):
        i += 1
        helper = base[i:(m+i)]  
        pattern = np.append(pattern,helper)
    pattern = pattern.reshape(n,m)
    return pattern


if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern(7,5))
