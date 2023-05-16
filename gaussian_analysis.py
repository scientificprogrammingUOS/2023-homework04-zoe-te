import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    #check parameters for int/float
    if all(isinstance(i, (int, float)) for i in [loc, scale, lower_bound, upper_bound]):
        if lower_bound < upper_bound:
            #100 samples of gaussian distribution
            gd = np.random.normal(loc, scale, size=100)
            #setting boundaries
            gd = gd[(gd >= lower_bound) & (gd <= upper_bound)]
            #calculation mean and sample std
            mean=np.mean(gd)
            std=np.std(gd, ddof=1)
            my_tuple = [mean, std]
            return my_tuple
        else:
            print("Your lower bound needs to be smaller than your upper bound")
    else: 
        print("All parameters need to be integers or floats")


if __name__ == "__main__":
    # use this for your own testing!

    pass
