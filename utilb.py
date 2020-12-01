import numpy as np

def calculate_covb(x) :
    xcentered = np.mean(x, axis=0)
    lenx = xcentered.shape[0]
    xcentered = x - xcentered
    covX = xcentered.T.dot(xcentered) / lenx
    return covX